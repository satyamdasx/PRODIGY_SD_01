def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67
def main():
    temperature = float(input("Enter the Temperature value: "))
    unit = input("Enter the unit of measurement (celsius, fahrenheit, kelvin): ").lower()
    if unit == "celsius":
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature} Degrees Celsius is equal to {fahrenheit} Degrees Fahrenheit and {kelvin} Kelvin.")
    elif unit == "fahrenheit":
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature} Degrees Fahrenheit is equal to {celsius} Degrees Celsius and {kelvin} Kelvin.")
    elif unit == "kelvin":
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"{temperature} Kelvin is equal to {celsius} Degrees Celsius and {fahrenheit} Degrees Fahrenheit.")
    else:
        print("Invalid Input!!!")
main()
