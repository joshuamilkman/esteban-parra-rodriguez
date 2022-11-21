from sklearn.feature_extraction.text import TfidfVectorizer

def getData(text, path):
    tfidf = TfidfVectorizer()
    x = tfidf.fit_transform(text)
    print(x)
    return [x, int(path.__contains__("non-plagiarized"))]

