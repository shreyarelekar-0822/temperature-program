import sys

# Check if the user provided a temperature argument
if len(sys.argv) < 2:
    print("Usage: python temp_check.py <temperature>")
    sys.exit(1)

# Read temperature from command line argument
try:
    temperature = float(sys.argv[1])
except ValueError:
    print("Please enter a valid number for temperature.")
    sys.exit(1)

# Check temperature range
if temperature < 15:
    print("Cold")
elif 15 <= temperature <= 30:
    print("Normal")
else:
    print("Hot")
