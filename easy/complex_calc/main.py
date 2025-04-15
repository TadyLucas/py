
def main():
    print("     Calc")
    print("---------------")
    exp = input("")
    
    tokens = exp.strip().split(" ")

    if len(tokens) < 3 or len(tokens) % 2 == 0:
        print("Please enter in format like: 4 + 2 * 3 (with spaces)")
        return
    
    try:
        x = int(tokens[0])
        i = 1
        while i < len(tokens):
            op = tokens[i]
            num = int(tokens[i+1])

            x = calc(op,x, num)
            
            i+=2
        print("-----------")
        print("Result:", x)
    except ValueError:
        print("Please use valid numbers and operators (e.g. 1 + 2 * 3)")
    except ZeroDivisionError:
        print("Division by zero? C’mon now.")
    except Exception as e:
        print("Something went wrong:", e)



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