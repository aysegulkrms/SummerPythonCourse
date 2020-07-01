print("   KPH     MPH")
print("------------------")
for i in range(60, 131, 10):
    print("{:>3} KPH = {:0.1f} MPH".format(i, i * 0.6214))

# Nested LOOPS
for seconds in range(60):
    print(seconds)

for minutes in range(60):
    for seconds in range(60):
        print(minutes, ":", seconds)

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ":", minutes, ":", seconds)

