while True:
    def calculator():
        print("Welcome to the Simple Calculator!")
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Choose an operation (1/2/3/4):")
            choice = input("Enter your choice: ")

            if choice == '1':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
            else:
                print("Invalid choice. Please restart and choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            
    calculator()