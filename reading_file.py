def count_characters(text):
    words = text.split()
    sentences = text.split('.')
    upper_count = 0
    lower_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    special_count = len(text) - (upper_count + lower_count + text.count(' ') + text.count('.') + text.count('\n'))
    return len(words), len(sentences), upper_count, lower_count, special_count



file_name = input("Enter the name of the file: ")
try:
    with open(file_name, 'r') as file:
        text = file.read()
        word_count, sentence_count, upper_count, lower_count, special_count = count_characters(text)
        print("Number of words:", word_count)
        print("Number of sentences:", sentence_count)
        print("Number of uppercase letters:", upper_count)
        print("Number of lowercase letters:", lower_count)
        print("Number of special symbols:", special_count)
except FileNotFoundError:
    print("File not found.")



