
def main():
    print("     Calc")
    print("---------------")
    exp = input("")
    
    final = exp.split(" ")

    try:
        if not (final[1] == "+" or final[1] == "-" or final[1] == "/" or final[1] == "\\" or final[1] == "*"):
            print("Please enter it in this format e.g. 1 + 1")
        else:
            print(f"{exp} = {calc(final[1], int(final[0]), int(final[2]))}")

    except:
        print("Please enter it in this format e.g. 1 + 1")




def calc(op, x, y):
    if op == "+":
        return x+y
    elif op == "-":
        return x-y
    elif op == "\\" or op == "/":
        return x/y
    elif op == "*":
        return x*y
    else: return 0

    

if __name__ == "__main__":
    main()