cont = 1
a = []
b = []
c = []
for i in range(100):

    if(cont % 3 == 0 and cont % 5 == 0):
        a.append(cont)
        #FIZZBUZZ
    elif(cont % 3 == 0):
        b.append(cont)
        #FIZZ
    elif(cont % 5 == 0):
        c.append(cont)
        #BUZZ
    cont += 1
print("FizzBuzz")
print(a)
print("Fizz")
print(b)
print("Buzz")
print(c)
print("Hola")
