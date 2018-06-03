import math
import collections
import string
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import Word
import matplotlib.pyplot as plt
from wordcloud import WordCloud

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')


def canonize_text(messages):
    processed_text = []
    stop = set(stopwords.words('russian'))
    punct = set(string.punctuation)
    for message in messages:
         words = [i for i in word_tokenize(message.lower()) if i not in stop and i not in punct]
         base_verb_words = [Word(word).lemmatize("v") for word in words]
         base_noun_words = [Word(word).lemmatize() for word in base_verb_words]
         processed_text.append(base_noun_words)
    return [' '.join(word for word in sentences) for sentences in processed_text]


def createDTM(messages):
    tfid_vectorizer = TfidfVectorizer()
    dtm = tfid_vectorizer.fit_transform(messages)
    print(pd.DataFrame(dtm.toarray(), columns=tfid_vectorizer.get_feature_names()))
    return dtm

def clusterize_message(data, matrix, k=2):
    kmeans = KMeans(n_clusters=k, random_state=0, n_jobs=-2)
    kmeans.fit(matrix)
    clustering = collections.defaultdict(list)
    for idx, label in enumerate(kmeans.labels_):
        clustering[label].append(data[idx])

    return clustering
    # return kmeans.predict(matrix)


def generate_cloud(data):
    vectorizer_data = createDTM(data)
    clustering = clusterize_message(data, vectorizer_data)
    print(clustering)
    # wc = WordCloud()
    # wc.generate(' '.join(clustering))
    # plt.imshow(wc, interpolation="bilinear")
    # plt.axis("off")
    # plt.figure()
    for ind in range(clustering.__len__()):
        wc = WordCloud(
            width=200,
            height=200,
            relative_scaling=1,
            normalize_plurals=False,
            max_words=2000,
            background_color="white")
        wc.generate(' '.join(clustering[ind]))
        # create coloring from image
        # wc.to_file("image%s.png" % ind)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.figure()
    plt.show()

# if __name__ == "__main__":
#     # m  = ['red! sdfsdfsdf, * am  ru %32321 34 going to ', ', % blue cars went, what do! you hjhjh think mama', 'greens found']
#     canonized_text = canonize_text(m)
#     print(canonized_text)
#     dtm = createDTM(canonized_text)
#     print(dtm)
#     clusters = clusterize_message(dtm)

    
