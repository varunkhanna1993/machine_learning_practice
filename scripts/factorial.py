# this is an example of recursion 

def factorial(n):
    if n< 1:
        return 1
    else:
        return n* factorial(n-1)

if __name__ == "__main__":
    user_input = int(input("Enter a number to return its factorial:"))
    print(factorial(user_input))
