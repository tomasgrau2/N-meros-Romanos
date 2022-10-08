def decimal_to_roman(x):
    decimal = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    i = len(decimal) - 1
    roman_number = ""
    while x != 0:
        if decimal[i] <= x: 
            roman_number += roman[i]
            x = x - decimal[i]
        else:
            i -= 1
    return roman_number



    





            






   