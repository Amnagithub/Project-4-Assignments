def main ():
    print("*** This program is to convert the Fahrenheit to Celsius.*** \n")
    fahrenheit = float(input("\033[1;3mEnter the temperature in Fahrenheit: \033[0m "))
    celsius = (fahrenheit - 32) * 5.0/9.0
    
    print(f"\033[1;3m{fahrenheit}°F is equal to {celsius}°C\033[0m")
    
if __name__ == "__main__":
    main()
    
