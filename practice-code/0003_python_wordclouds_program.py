# pip install wordcloud
# pip install matplotlib

from wordcloud import WordCloud
import matplotlib.pyplot as plt


# defalut some text
txt = 'Python, Django, ReactJs, Datascience, Machine learning, IoT, Deep learning, Artificial intelligence'
wordcloud = WordCloud().generate(txt)

# display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()