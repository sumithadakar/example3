import sys

if len(sys.argv) != 2:
    print("Usage: <TEMP>")
    sys.exit(1)

temp = float(sys.argv[1])

print("Temperature:", temp)

if temp < 15:
    status = "Cold"
elif 15 <= temp <= 30:
    status = "Normal"
else:
    status = "Hot"

print("Temperature Status:", status)
