# program for Collatz Sequence

def collatz(number):
    if(number % 2 == 0):
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
def main():
    n = int(input("Enter a number: "))
    n = collatz(n)
    while(n != 1):
        n = collatz(n)
main()
