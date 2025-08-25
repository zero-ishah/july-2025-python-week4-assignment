# Error Handling Lab
# This program asks for a filename and handles errors if it does not exist or can't be read.

def error_handling():
    try:
        filename = input("Enter a file name to open: ")

        # Attempt to open and read the file
        with open(filename, "r") as file:
            print("File opened successfully!")
            print("Content:")
            print(file.read())

    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except PermissionError:
        print("Error: You don't have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
error_handling()
