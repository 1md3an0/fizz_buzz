while True:
    try:
        my_input = input("Enter your upper limit: ")
        upperlimit = int(my_input)
        lower_limit = 1
       
        def print_fizz_buzz():
            for i in range(lower_limit,upperlimit+1,1):
                if i % 3 == 0 and i % 5 == 0:
                    print("Fizz Buzz")
                elif i % 5 == 0:
                    print("Buzz")
                elif i % 3 == 0:
                    print("Fizz")
                else:
                    print(i)

        print_fizz_buzz()
        
    except(ValueError):
        print("It's gotta be numerical, dude! Try again!")
        continue
    else:
        break