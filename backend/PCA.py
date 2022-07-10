from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import pickle

df = pd.read_csv("data_vector.csv")

features = [str(i) for i in range(1, 129)]
x = df.loc[:, features]
y = df.loc[:, ["path"]]

scaler = StandardScaler()
scalert = scaler.fit_transform(x)

pca = PCA(.95)
pcat = pca.fit_transform(scalert)
principalDf = pd.DataFrame(data=pcat)
finalDf = pd.concat([principalDf, df[["path"]]], axis=1)

dataset = "dataset.csv"
scalerp = "scaler.dat"
pcap = "pca.dat"
finalDf.to_csv(dataset, index=False)
pickle.dump(scaler, open(scalerp, "wb"))
pickle.dump(pca, open(pcap, "wb"))
