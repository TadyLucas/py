import random
def main():
    start = 1
    end = 20
    rnd_num = random.randint(start, end)
    heards = 4
    print("Guess The Number and win Jackpot!!!")
    print(rnd_num)
    print(f"Guess number between {start} and {end}\n")
    while True:
        if heards <= 0:
            print("GAME OVER!")
            break
        g = input("Guess number: ")
        try:
            if rnd_num == int(g):
                print("\nYou win!!")
                break
            else:
                heards -= 1
                print(f"You lose, Try again! Tries left: {heards}")
                print("------------------------")
        except:
            print("Plese enter number")

if __name__ == "__main__":
    main()