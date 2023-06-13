#função que calcula media
def media(num1, num2):
    return (num1 + num2)/2

try:
    num1 = float(input("primeiro numero: "))
    num2 = float(input("segundo numero: "))
except:
    print("Insira apenas numeros, pfv")

print(media(num1, num2))