# Open the file with the assumed incorrect encoding and read the contents
with open('output.txt', 'r', encoding='windows-1252') as file:
    text = file.read()

# Write the contents back with the correct UTF-8 encoding
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text)
