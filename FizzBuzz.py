cont = 1
for i in range(100):

    if(cont % 3 == 0 and cont % 5 == 0):
        print("FizzBuzz")
    elif(cont % 3 == 0):
        print("Fizz")
    elif(cont % 5 == 0):
        print("Buzz")
    else:
        print(cont)

    cont += 1
