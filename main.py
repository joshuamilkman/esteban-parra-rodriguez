from train import *
import os
import pandas as pd
from processing import getData

# make DF out of plagiarized/non-plagiarized files
subfolders = [f.path for f in os.scandir("IR-Plag-Dataset\\IR-Plag-Dataset") if f.is_dir()]
dataframes = []

for folder in subfolders:
    df = pd.DataFrame(columns=["TFIDF", "isPlagiarized"])
    original = folder + "\\original"
    for (dirpath, dirnames, filenames) in os.walk(folder):
        dirnames[:] = [d for d in dirnames if d not in original]
        for name in filenames:
            path = os.path.join(dirpath, name)
            with open(path) as f:
                text = f.readlines()
                df.loc[len(df)] = getData(text, path)
                
    with open(original) as f:
        text = f.readlines()
        originalVectors = getData(text, original)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hello, welcome to the best plagarism checker")
    
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
