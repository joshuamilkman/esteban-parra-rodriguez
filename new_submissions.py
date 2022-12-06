import os
import pandas as pd
from processing import getData

subfolders = [f.path for f in os.scandir("IR-Plag-Dataset\\IR-Plag-Dataset") if f.is_dir()]

print("Please select which assignment this folder is for")
for number, folder in enumerate(subfolders):
    print(number, folder)

assignment = input("Which assignment number?")


names = []

folder = subfolders[int(assignment)]
submissions = folder + "\\submissions"
plagiarized = folder + "\\plagiarized"
ignore = [submissions, plagiarized]


for dirpath, dirnames, filenames in os.walk(submissions):
    for subName in filenames:
        dataframe = pd.DataFrame(columns=["name", "Jaccard", "Tfidf", "Classification"])

        with open(f"{submissions}\\{subName}") as f:
            submissionText = " ".join(f.readlines())

        for (dirpath, dirnames, filenames) in os.walk(folder):
            dirnames[:] = [d for d in dirnames if d not in ignore]
            filenames[:] = [f for f in filenames if f not in [subName]]
            for name in filenames:
                path = os.path.join(dirpath, name)
                with open(path) as f:
                    text = " ".join(f.readlines())
                group = (text, submissionText)
                dataframe.loc[len(dataframe)] = getData(group, path, name)


        print(f"Assignment {subName} is most similar to")
        dataframe = dataframe.sort_values(axis=0, by=["Tfidf", "Jaccard"],ascending=False)
        print(dataframe["name"].head(5))


