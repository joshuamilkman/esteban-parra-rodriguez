# make DF out of plagiarized/non-plagiarized files
import os
import pandas as pd


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

X = np.array(dataframe["Cosine"]).reshape(-1, 1)
y = dataframe["isPlagiarized"]
predictions = cross_val_predict(LinearSVC(), X, y)
print(predictions)

# filter out files from "original" <3
# Add one more vector
# Get those vectors from the file in "original"
# Compare vectors by cosine distance
