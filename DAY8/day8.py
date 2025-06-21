def calculator():
    print("welcome to simple calculator")
    
    num1 = float(input("Enter the first Number"))
    num2 = float(input("Enter the second Number"))
    
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    
    choice = input("Enter choice (1/2/3/4): ")
     
    if choice=='1':
        result = num1 + num2
        print(f"\n{num1} +{num2} = {result}")
        
    elif choice=='2':
        result = num1 -num2
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"\n{num1} * {num2} = {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"\n{num1} / {num2} = {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid input. Please select a valid operation.")
        
        
calculator()
        
        
    
        