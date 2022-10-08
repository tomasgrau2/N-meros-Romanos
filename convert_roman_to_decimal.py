

def roman_to_decimal(x):
    roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
    resultado = 0
    decimal_l = []
    for letter in x:
        decimal_l.append(roman[letter])
     
    if "IV" in x:
        resultado = resultado + 4 - 6

    if "IX" in x:
        resultado = resultado + 9 - 11

    if "XL" in x:
        resultado = resultado + 40 - 60

    if "XC" in x:
        resultado = resultado + 90 - 110

    if "CD" in x:
        resultado = resultado + 400 - 600

    if "CM" in x:
        resultado = resultado + 900 - 1100     

    suma = sum(decimal_l)

    return(suma+ resultado)    

      

print(roman_to_decimal("CV"))






