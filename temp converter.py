def convert_temperature(value, from_unit, to_unit):
    # Convert from original to Celsius
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5/9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return "Invalid source unit."

    # Convert from Celsius to target unit
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return (celsius * 9/5) + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        return "Invalid target unit."


# MAIN PROGRAM
print("=== Temperature Converter ===")
print("Supported units: C (Celsius), F (Fahrenheit), K (Kelvin)")

try:
    value = float(input("Enter the temperature value: "))
    from_unit = input("Convert from (C/F/K): ").strip().upper()
    to_unit = input("Convert to (C/F/K): ").strip().upper()

    result = convert_temperature(value, from_unit, to_unit)

    if isinstance(result, float):
        print(f"\n✅ Result: {value}°{from_unit} = {result:.2f}°{to_unit}")
    else:
        print(f"\n❌ Error: {result}")

except ValueError:
    print("\n❌ Invalid input! Please enter numeric temperature values.")
