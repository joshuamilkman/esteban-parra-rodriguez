# make DF out of plagiarized/non-plagiarized files
import os

import nltk as nltk
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_predict
from sklearn.svm import LinearSVC
from processing import getVectors


subfolders = [f.path for f in os.scandir("IR-Plag-Dataset\\IR-Plag-Dataset") if f.is_dir()]
dataframe = pd.DataFrame(columns=["Cosine", "isPlagiarized"])
names = []

for folder in subfolders:
    original = folder + "\\original"

    with open(f"{original}\\{os.listdir(original)[0]}") as f:
        originalText = " ".join(f.readlines())

    for (dirpath, dirnames, filenames) in os.walk(folder):
        dirnames[:] = [d for d in dirnames if d not in original]
        for name in filenames:
            path = os.path.join(dirpath, name)
            with open(path) as f:
                text = " ".join(f.readlines())
                group = (text, originalText)
                dataframe.loc[len(dataframe)] = getVectors(group, path)

X = np.array(dataframe["Cosine"]).reshape(-1, 1)
y = dataframe["isPlagiarized"]
predictions = cross_val_predict(LinearSVC(), X, y)
print(predictions)
