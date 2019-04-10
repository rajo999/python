while True:
    x = int(input("select a number between 1 and 100: "))
    for y in range(1, x+1):
        if y%3==0 and y%5== 0:
            print("buzzfizz")
        elif y%3==0:
            print("fizz")
        elif y%5==0:
            print("buzz")
        else:
            print(y)
    i= input("do you want another guess? y/n: ")
    if g.lower()[0] !="y":
        print("ciao!")
        break

