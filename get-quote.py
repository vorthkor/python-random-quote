import random


def primary():
    # print("Keep it logically awesome.")

    f = open("quotes.txt", "a")
    quote = input("Add quote:\n")
    f.write(quote+'\n')
    f.close()
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1
    rnd = random.randint(0, last)
    rnd2 = random.randint(0, last)
    print(quotes[rnd], end='')
    print(quotes[rnd2], end='')


if __name__ == "__main__":
    primary()
