# File Read & Write Challenge
# This program reads content from a file, modifies it, and writes it to a new file.

def file_read_and_write():
    try:
        # Ask user for the input file name
        input_file = input("Enter the name of the file to read: ")

        # Read the file content
        with open(input_file, "r") as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"Modified content saved in '{output_file}'")

    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
file_read_and_write()
