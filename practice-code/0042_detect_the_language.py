# pip install langdetect


from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

input_lang  = input("Enter a language: ")
# detected the language
output_lang = detect(input_lang)

print(f"The detected language is: {output_lang}")


'''output:

Enter a language: this is a book
The detected language is: en
'''