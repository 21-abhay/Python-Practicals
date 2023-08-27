def digits(n):
    l = set({})
    for x in n:
        l.add(int(x))
    return l

if __name__ == "__main__":
    n = input("Enter a number :")
    print("Digits are :",digits(n))