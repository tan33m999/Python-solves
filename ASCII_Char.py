def ASCII_Char():
    x = input("Input a number ,range eg.'5-10' or a english character: ")
    if "-" in x:
        start, end = map(int, x.split("-"))
        for i in range(start, end + 1):
            print(f"{i} {chr(i)}")
    elif x.isdigit() == True:
            print(f"Serial: {x} || Chr: {chr(int(x))}")
    elif x.isdigit() == False:
            y = []
            for i in x:
                print(f"Chr: {i} || Serial: {ord(i)}")   
                y.append(ord(i))
            for i in y:
                print(i, end=" ")
        
     


def ASCII():
    x = input()
    num_set = []
    if " " in x:
        num_set.append(map(int, x.split(" ")))
        for i in num_set:
            print(i)

ASCII()

