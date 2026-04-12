# A Basic Calculator

while True:
    prompt = input("Enter an operation (+,-,*,/,^,%,√): ")
 
    proper_operation = prompt.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ").replace("^", " ^ ").replace("%", " % ").replace("√", " √ ")
    element = proper_operation.split()

    result = int(element[0])

    for i in range(1, len(element), 2):
        operation = element[i]
        nextnumber = int(element[i + 1])

        if operation == "+":
            result += nextnumber
        elif operation == "-":
            result -= nextnumber
        elif operation == "*":
            result *= nextnumber
        elif operation == "/":
            result /= nextnumber
        elif operation == "^":
            result **= nextnumber
        elif operation == "%":
            result = (result * nextnumber) // 100
        elif operation == "√": # I couldn't find a way to make it work with more than one number, so I just made it work with the first number and ignore the rest :(
            result **= 0.5 # It won't work without the second number despite it will be ignored.
    
    print(result)


