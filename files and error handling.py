def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content written to {output_filename}")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except IOError:
        print("Error: Could not read/write the file.")

input_file = input("Enter the filename to read from: ")
output_file = input("Enter the filename to write to: ")

modify_file(input_file, output_file)
