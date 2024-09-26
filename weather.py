
# Task 2: Temperature Conversion 
    # Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

def temp_conversion():
    while True:
        try:
            # Task 1: Start 
            # Begin by asking the user to enter the temperature in Fahrenheit.
            temp = int(input('''
            Welcome to my weather forecast app!
            ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️
            Enter degrees in Fahrenheit: 
            '''))

            celsius = ((temp-32)*5/9)

        except ValueError:
            print ("=" * 25)
            print("Temperature must be a number!")
            continue
            
            # Task 3: User Experience 
            # Implement an else block that prints the converted temperature in a user-friendly format. 
        else:   
            print (f'''
                {temp} degrees Fahrenheit converted to Celsius is:
                {celsius} degrees 🌡️
            ''')

            # Task 4: Finally 
            # Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
        finally:
            print("Thanks for using my weather forecast application!")
            break                

temp_conversion()

