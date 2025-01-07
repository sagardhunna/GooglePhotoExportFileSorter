word = "helloworld.JSON"

print(word[:-5])

if word[-5:].lower() == '.json':
    print("LAST 5 LETTERS ARE .JSON")
else:
    print("last 5 letters are not .JSON")