#- Read numbers from a file and handle errors gracefully
# Step 1: File name
file_name = "numbers.txt"

# Step 2: Try to open and read the file
try:
    # Open the file in read mode
    file = open(file_name, "r")

    # Read all lines into a list
    lines = file.readlines()

    print("Reading and processing numbers from the file:\n")

    # Step 3: Loop through each line
    for line in lines:
        line = line.strip()  # Remove extra whitespace or newlines

        try:
            # Convert the line to a number
            number = float(line)

            # Perform division
            result = 100 / number
            print("100 divided by", number, "is", result)

        except ValueError:
            # Handle non-numeric input
            print("Invalid input:", line, "is not a number.")

        except ZeroDivisionError:
            # Handle division by zero
            print("Cannot divide by zero. Skipping:", line)

    # Close the file after reading
    file.close()

except FileNotFoundError:
    print("File", file_name, "not found. Please check the file name or path.")

finally:
    print("\nDone processing the file.")
