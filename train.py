# make DF out of plagarized/nonplagarized files
import os
import pandas as pd

from processing import getData

subfolders = [f.path for f in os.scandir("IR-Plag-Dataset\\IR-Plag-Dataset") if f.is_dir()]
dataframes = []

for folder in subfolders:
    df = pd.DataFrame(columns=["TFIDF", "isPlagiarized"])
    for (dirpath, dirnames, filenames) in os.walk(folder):
        for name in filenames:
            path = os.path.join(dirpath, name)
            #   if path[44:].__contains__("plagiarized"):
            with open(path) as f:
                text = f.readlines()
                df.loc[len(df)] = getData(text, path)
    print(df)
