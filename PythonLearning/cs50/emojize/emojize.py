import emoji

emj = input("Input: ")
output = emoji.emojize(emj, language='alias')
print(output)
