from toolkit import errors
def convert(exp): 
    
    value = float(exp[1])
    unit_one = (exp[3]).lower()
    unit_two = (exp[5]).lower()
    dist_units = ["mm",'cm','m','km']
    weight_units =[ "kg",'g']
    temperature_units = ['k','f','c']
    
    if (unit_two in dist_units and unit_one in dist_units) or (unit_two in weight_units and unit_one in weight_units) or (unit_two in temperature_units and unit_one in temperature_units):
        pass
    else:
        errors.conversion_of_different_groups()
    
    uni_metrics = {
        "mm" :  0.001,
        "cm" : 0.01,
        "m" : 1 ,
        "km":1000,
        'g':1,
        'kg':1000


    }
    if unit_one not in temperature_units and unit_two not in temperature_units:

        print((float(uni_metrics[unit_one] )* value)/float(uni_metrics[unit_two]))
    else:
        
        if unit_one == 'c':
            if value < -273.15:
                errors.below_zero()
            uni_for_c = {
                'c':0,
                'k':273.15
                
            }
            if unit_two != 'f':
                res = uni_for_c[unit_two] + value 
               
            else: 
                print((value * (9/5))+32)
        if unit_one == 'k':
            if value < 0 :
                errors.below_zero()
            uni_for_k = {
                'c':-273.15,
                'k':0
            }
            if unit_two != 'f':
                print(uni_for_k[unit_two] + value)
            else: 
                print(((value -273.15)* (9/5))+32)
        if unit_one == 'f':
            
            pre_result  =  ( value  -32 ) * 5/9
            result_for_c = pre_result
            result_for_k = pre_result + 273.15
            if result_for_k < 0 :
                errors.below_zero()
                
            
            if unit_two == 'k':
                print(result_for_k)
            if unit_two == 'c':
                print(result_for_c)





            
            
    
