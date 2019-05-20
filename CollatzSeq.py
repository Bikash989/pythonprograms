# program for Collatz Sequence

def collatz(number):
    if(number % 2 == 0):
        print(number // 2, end=" ")
        return number // 2
    else:
        print(3 * number + 1, end=" ")
        return 3 * number + 1
def main():
    try:
        n = int(input("Enter a number: "))
        assert(n>1)
        n = collatz(n)
        while(n != 1):
            n = collatz(n)
        print("\nDone")
    except Exception as e:
        print("Error: You must enter a valid integer and should be greater than 1")

if __name__ == "__main__": main()
