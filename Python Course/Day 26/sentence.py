sentence = input("Enter a sentence : ")

result = {word:len(word) for word in sentence.split()}

print(result)