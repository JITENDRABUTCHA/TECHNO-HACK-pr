def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    
    while True:
        choice = input("Enter your choice (1/2): ")
        
        if choice in ('1', '2'):
            temp = float(input("Enter the temperature to convert: "))
            
            if choice == '1':
                converted_temp = celsius_to_fahrenheit(temp)
                print(f"{temp}°C is equal to {converted_temp:.2f}°F")
            elif choice == '2':
                converted_temp = fahrenheit_to_celsius(temp)
                print(f"{temp}°F is equal to {converted_temp:.2f}°C")
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
        next_conversion = input("Do you want to perform another conversion? (yes/no): ")
        if next_conversion.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
