max_temp = 102.5

temperature = float(input("Enter the substance's temperature "))

while temperature > max_temp:
    print("Turn down the thermostat. Wait 5 minutes. Check the temperature again")
    temperature = float(input("Enter the new Celsius temperature "))


print("The temperature is acceptable")
print("Check it again in 15 minutes")
