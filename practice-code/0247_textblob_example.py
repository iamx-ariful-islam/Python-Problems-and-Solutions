from textblob import TextBlob


blob = TextBlob("Python is amazing!")
print(blob.sentiment)  # outputs sentiment of the text



'''output:

Sentiment(polarity=0.7500000000000001, subjectivity=0.9)
'''