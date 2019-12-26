import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import openpyxl 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split

df=pd.read_csv("dataset_test.csv")
#sns.pairplot(df)
print("1")
df.drop(['Maximum EVI','Latest EVI value','Last year Average EVI','Maximum NDWI','Latest NDWI value','Last year Average NDWI','Maximum MSAVI','Latest MSAVI value','Last year Average MSAVI','vegetation'], axis = 1, inplace = True)
#sns.pairplot(df)

print("2")
#calculate distortion for a range of number of cluster
distortions = []
for i in range(1, 5):
    km = KMeans(
        n_clusters=i, init='random',
        n_init=10, max_iter=300,
        tol=1e-04, random_state=0
    )
    km.fit(df)
    distortions.append(km.inertia_)

#plot
plt.plot(range(1, 5), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

X = np.array(df).astype(float)

kmeans = KMeans(n_clusters=3) 
kmeans.fit(X)
a = kmeans.predict(X)

df['Drought_Severity'] = a
df.to_csv('Clustering_done1.csv')

plt.scatter(df['Average Rainfall'],a)

plt.scatter(df['Average EVI'],a)

plt.scatter(df['Average NDWI'],a)

plt.scatter(df['Average MSAVI'],a)

#plt.scatter(df['vegetation'],a)

df=pd.read_csv('Clustering_done1.csv')
X=df[['Average EVI','Average NDWI','Average MSAVI','Average Rainfall']]
y=df['Drought_Severity']
C = 1.0              #gamma : varied c:bias
svc = svm.SVC(kernel='linear', C=C).fit(X, y)
print("4")
test_size=0.4

X_train, X_test, y_train, y_test = train_test_split(X, y) 

svc.fit(X_train,y_train)

prediction = svc.predict(X_test)
print("5")
from sklearn.metrics import classification_report

print(classification_report(y_test, prediction))

import sklearn
print("The accuracy of the model is",(sklearn.metrics.accuracy_score(y_test, prediction))*100,"%")   #converting accuracy score to %

svc.probability=True

svc.fit(X_train,y_train)

prediction = svc.predict_proba(X_test)

print(prediction)

import pickle
filename = 'finalized_kmeans_model.sav'
pickle.dump(svc, open(filename, 'wb'))


