def fatorial(number):
    if number > 1:
        return number * fatorial(number - 1)
    else:
        return 1

if __name__ == "__main__":
    print(fatorial(5))