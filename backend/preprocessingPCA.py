from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import pickle

df = pd.read_csv("datos/data_vectorh.csv")

posvectors = [str(i) for i in range(1, 129)]
x = df.loc[:, posvectors]
y = df.loc[:, ["path"]]

scaler = StandardScaler()
scalert = scaler.fit_transform(x)

pca = PCA(.95)
pcat = pca.fit_transform(scalert)
dfActual = pd.DataFrame(data=pcat)
dfFinal = pd.concat([df[["path"]], dfActual], axis=1)

dataset = "datos/data_vector_pca.csv"
scalerp = "datos/scaler.dat"
pcap = "datos/pca.dat"
dfFinal.to_csv(dataset, header=None, index=False)
pickle.dump(scaler, open(scalerp, "wb"))
pickle.dump(pca, open(pcap, "wb"))
