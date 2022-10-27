# programa para receber 5 produtos em variaveis e realizar todas operações matemáticas
# incluindo resto da divisão e potência.

iphone = 2980
Sansung = 2540
ps5 = 2100
tablet = 1950
notebook = 2350

total = "qntiphone iphone" * iphone , "qntSansung Sansung" * Sansung , "qntps5 ps5" * ps5 ,"qnttablet tablet" * tablet , "qntnotebook notebook" * notebook

qntiphone = int(input ("Quantos iphones voce deseja?" ))
int(inputi ("quantos iphones voce deseja?" , qntSansung))
int(input ("quantos iphones voce deseja?" , qntps5))
int(input ("quantos iphones voce deseja?", qntTablet))
int(input ("quantos iphones voce deseja?" , qntnotebook))

total = (qntiphone * iphone)+ (qntSansung * Sansung)+(qntps5 * ps5)+(qnttablet * tablet)+(qntnotebook * notebook)

print("valor parcelado de 3 vezes é:", total/3)
print("valor parcelado de 6 vezes é:", (total*1.05)/6)
print("valor com desconto a vista é:", total-(total*0.10) )