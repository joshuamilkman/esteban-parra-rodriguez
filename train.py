# make DF out of plagiarized/non-plagiarized files
import os
import pandas as pd

from processing import getData

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

def compare_homework(dataframe1, dataframe2): 
    plagarism_counter
    count = 0
    width = len(dataframe1.columns)
    height = len(dataframe1)
    total_cells = width * height
    for (i in len(dataframe1)):
        for (f in len(dataframe1.columns)):
            for (j in len(dataframe2.columns):
                if (dataframe1[i,f] == dataframe2[i,j]):
                    count = count + 1 
    if (float(count) > float(total_cells * 0.8)):
        return "plagarized"
    else:
        return "clean"
              
            
                
        
        

# filter out files from "original" <3
# Add one more vector
# Get those vectors from the file in "original"
# Compare vectors by cosine distance
