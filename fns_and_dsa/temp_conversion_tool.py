# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius using global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit using global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """Main function to handle user interaction and temperature conversion."""
    print("Temperature Conversion Tool")
    print("=" * 30)
    
    try:
        # Get temperature input
        temperature = float(input("Enter the temperature to convert: "))
        
        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
        
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
            
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
