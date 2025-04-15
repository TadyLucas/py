import re

def main():
    print("     Calc")
    print("---------------")
    exp = input("")
    

    final = re.split(r'[+\-\\*]', exp)

    for part in final:
        part.strip()
        
    print(final)

if __name__ == "__main__":
    main()