unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * 10) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}ºF")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius is: {temp}ºC")
else:
    print(f"{unit} is am invalid unit of measurement")