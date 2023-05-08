def fibonacci(n):

   temp1, temp2 = 0, 1

   total = 0

   while total < n:

       yield temp1

       temp3 = temp1 + temp2

       temp1 = temp2

       temp2 = temp3

       total += 1

fib_object = fibonacci(20)

for i in fib_object:
    print(i)

print(list(fib_object))

dictionary = {key:values for key,values in zip(range(9), 'guilherme')}
print(dictionary)
print(dictionary.keys())