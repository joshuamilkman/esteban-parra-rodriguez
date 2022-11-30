from sklearn.feature_extraction.text import TfidfVectorizer

def getData(text, path):
    tfidf = TfidfVectorizer()
    x = tfidf.fit_transform(text)
    return [x, int(path[40] == "p")]
