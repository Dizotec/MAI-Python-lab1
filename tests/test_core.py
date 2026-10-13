import os
import sys

import pytest

# Автоматически добавил src в пути
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from toolkit import converter, expression, validation


def run_valid(args):
    if len(args) >= 2:
        expression.args = args[1]  
    return validation.valid(args)


# Позитивные тесты калькулятора
def test_calc_modulo():
    assert run_valid(["calc", "10%3"]) == "10%3=1.00"


def test_calc_priority():
    assert run_valid(["calc", "2+3*4"]) == "2+3*4=14.00"

def test_calc_division():
    assert run_valid(["calc", "10/4"]) == "10/4=2.50"

def test_calc_unary_minus():
    assert run_valid(["calc", "2*-3"]) == "2*-3=-6.00"

def test_calc_unary_combo():
    assert run_valid(["calc", "1+-2"]) == "1+-2=-1.00"

def test_calc_brackets():
    assert run_valid(["calc", "(2+3)*4"]) == "(2+3)*4=20.00"

def test_calc_spaces():
    assert run_valid(["calc", "  2.5  +  1.5  "]) == "  2.5  +  1.5  =4.00"

# Негативные тесты калькулятора
def test_calc_error_empty():
    with pytest.raises(SystemExit) as exc:
        run_valid(["calc"])
    assert exc.value.code == 2

def test_calc_error_invalid_symbol():
    with pytest.raises(SystemExit) as exc:
        run_valid(["calc", "2+a"])
    assert exc.value.code == 2

def test_calc_error_div_by_zero():
    with pytest.raises(SystemExit) as exc:
        run_valid(["calc", "1/0"])
    assert exc.value.code == 2

def test_calc_error_double_operators():
    with pytest.raises(SystemExit) as exc:
        run_valid(["calc", "2/*3"])
    assert exc.value.code == 2

def test_calc_error_missed_operand():
    with pytest.raises(SystemExit) as exc:
        run_valid(["calc", "2+"])
    assert exc.value.code == 2

# Тесты конвертера величин 
def test_converter_distance():
    assert pytest.approx(converter.convert(["convert", "1000", "", "mm", "", "m"])) == 1.0

def test_converter_mass():
    assert pytest.approx(converter.convert(["convert", "1.5", "", "kg", "", "g"])) == 1500.0

def test_converter_temperature():
    assert pytest.approx(converter.convert(["convert", "0", "", "c", "", "f"])) == 32.0

def test_converter_temp_k_to_c():
    assert pytest.approx(converter.convert(["convert", "0", "", "k", "", "c"])) == -273.15

def test_converter_temp_f_to_c():
    assert pytest.approx(converter.convert(["convert", "32", "", "f", "", "c"])) == 0.0

# Тесты ошибок конвертера и абсолютного нуля
def test_converter_absolute_zero_error():
    with pytest.raises(SystemExit) as exc:
        converter.convert(["convert", "-300", "", "c", "", "k"])
    assert exc.value.code == 2

def test_converter_absolute_zero_k_error():
    with pytest.raises(SystemExit) as exc:
        converter.convert(["convert", "-5", "", "k", "", "c"])
    assert exc.value.code == 2

def test_converter_absolute_zero_f_error():
    with pytest.raises(SystemExit) as exc:
        converter.convert(["convert", "-500", "", "f", "", "k"])
    assert exc.value.code == 2

def test_converter_undefined_group():
    with pytest.raises(SystemExit) as exc:
        converter.convert(["convert", "10", "", "xyz", "", "m"])
    assert exc.value.code == 2

# Тесты CLI интерфейса
def test_cli_help():
    from toolkit.__main__ import main
    sys.argv = ["__main__.py", "--help"]
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 0

def test_cli_error_output_stream(capsys):
    from toolkit.__main__ import main
    sys.argv = ["__main__.py", "calc", "1/0"]
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 2
    captured = capsys.readouterr()
    assert len(captured.err) > 0

def test_cli_incompatible_units_error():
    from toolkit.__main__ import main
    sys.argv = ["__main__.py", "convert", "10", "", "kg", "", "m"]
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 2

# Тесты на изоляцию данных и окружение
def test_isolation_json_history():
    log_file = 'results.json'
    initial_count = 0
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as f:
            initial_count = len(f.readlines())
            
    run_valid(["calc", "1+1"])
    
    with open(log_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        assert len(lines) == initial_count + 1
        assert "1+1=" in lines[-1]

def test_isolation_clean_state():
    res_first = run_valid(["calc", "5-3"])
    res_second = run_valid(["calc", "10-2"])
    assert "5-3=2.00" in res_first
    assert "10-2=8.00" in res_second

def test_isolation_config_load_integrity():
    res1 = converter.convert(["convert", "1", "", "m", "", "cm"])
    res2 = converter.convert(["convert", "1", "", "m", "", "cm"])
    assert res1 == res2 == 100.0
