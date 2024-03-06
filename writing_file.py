def remove_special_characters(text):
    # Define special characters
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # Remove special characters from the text
    cleaned_text = ''.join(char for char in text if char not in special_chars)

    return cleaned_text



# Get input and output file names from the user
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

try:
    # Read text from the input file
    with open(input_file, 'r') as file:
        text = file.read()

    # Remove special characters
    cleaned_text = remove_special_characters(text)

    # Write cleaned text to the output file
    with open(output_file, 'w') as file:
        file.write(cleaned_text)

    print("Special characters removed and result saved to", output_file)
except FileNotFoundError:
    print("File not found.")



