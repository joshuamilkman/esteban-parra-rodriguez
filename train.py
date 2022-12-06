# make DF out of plagiarized/non-plagiarized files
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import cross_val_predict, StratifiedKFold, cross_validate
from sklearn.preprocessing import OrdinalEncoder
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from processing import getData

subfolders = [f.path for f in os.scandir("IR-Plag-Dataset\\IR-Plag-Dataset") if f.is_dir()]
dataframe = pd.DataFrame(columns=["name", "Jaccard", "Tfidf", "Classification"])
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
            dataframe.loc[len(dataframe)] = getData(group, path, name)

X, y = dataframe.iloc[:, 1:-1], dataframe.iloc[:, -1]

oe = OrdinalEncoder()
y_encoded = oe.fit_transform(np.array(y).reshape(-1, 1))

decision_tree = cross_val_predict(DecisionTreeClassifier(), X, y, cv=10)
decision_tree_scores = cross_validate(DecisionTreeClassifier(), X, y_encoded, cv=10, scoring=["accuracy", "precision",
                                                                                              "f1", "recall"])
print(decision_tree_scores)
scores = pd.DataFrame()
scores["Accuracy"] = decision_tree_scores["test_accuracy"]
scores["Precision"] = decision_tree_scores["test_precision"]
scores["f1"] = decision_tree_scores["test_f1"]
scores["Recall"] = decision_tree_scores["test_recall"]

scores.plot.bar(rot=0)
plt.show()


# random_forest = cross_val_predict(RandomForestClassifier(), X, y, cv=10)
sv_machine = cross_val_predict(LinearSVC(), X, y, cv=StratifiedKFold(10))

ConfusionMatrixDisplay.from_predictions(y, decision_tree)
plt.show()
