import math  

def main():
    inputa = int(input("Please enter your first number: "))

    inputb = int(input("Please enter your second number: "))
    
    print("The hypotenuse of this triangle is: " + str(pythag(inputa, inputb)))

def pythag(A,B):
    output = math.sqrt(((A ** 2) + (B ** 2)))
    return output

main()
