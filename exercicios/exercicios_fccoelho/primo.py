num = int(input("numero: "))

"""
if num != 2 and num != 3 and num != 5 and num != 7:
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print("não é primo")
    else: 
        print("é primo")
else:
    print("é primo") 
"""
for i in range((num - 1), 0, -1):
    if num % i == 0:
        primo = False
        break
    else:
        primo = True

if primo:
    print("é primo")
else:
    print("nao é primo")
