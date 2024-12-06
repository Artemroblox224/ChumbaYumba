import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from pytrends.request import TrendReq


def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(230,100%%, %d%%)" % np.random.randint(49,51))


def cloud_gen(queries, cloud_form):
    stop_words = set(["по", "в", "на", "с", "и", "для"])
    filtered_words = [word for query in queries for word in query.split() if word not in stop_words]
    word_freq = nltk.FreqDist(filtered_words)
    key_words = [word for word, freq in word_freq.most_common(50)]

    mask = np.array(Image.open('yolka3.png'))
    text = ' '.join(key_words)

    wordcloud = WordCloud(width=200,
                          height=150,
                          random_state=1,
                          background_color='white',
                          color_func=lambda *args, **kwargs: 'green',
                          colormap='Set2',
                          collocations=False,
                          stopwords=stop_words,
                          mask=mask).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    wordcloud.recolor(color_func=grey_color_func)
    plt.show()
