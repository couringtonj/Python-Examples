def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    should_accumulate=True
    num1=float(input("What is the first number?: "))
    while should_accumulate:
    
        for symbol in operations.keys():
            print(symbol)
        operation_symbol=input("Pick an operation: ")
        num2=float(input("What is the next number?: "))
        ans=operations[operation_symbol](num1,num2)
        print(f"Your answer is {num1} {operation_symbol} {num2} = {ans}")

        choice=input(f"Type 'y' to continue calculating with {ans} or type 'n' for a new calculation: ").lower()
        if choice=="y":
            num1=ans
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()
            
            for symbol in operations.keys():
                print(symbol)
            operation_symbol=input("Pick an operation: ")
            num2=float(input("What is the next number?: "))
            ans=operations[operation_symbol](num1,num2)
            print(f"Your answer is {num1} {operation_symbol} {num2} = {ans}")    


calculator()