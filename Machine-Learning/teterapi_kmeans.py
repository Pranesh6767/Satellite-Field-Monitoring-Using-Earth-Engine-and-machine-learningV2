import pickle
filename = 'finalized_kmeans_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


Xnew = [[0.100814774,-0.09354851,0.182100458,0.599136986]]
# make a prediction
ynew = loaded_model.predict_proba(Xnew)
print(ynew)
cluster1 = ynew[0,0]
cluster2 = ynew[0,1]
cluster3 = ynew[0,2]
cluster4 = ynew[0,3]
	
arr = [cluster1,cluster2,cluster3,cluster4]
maximum = max(arr)
index = arr.index(maximum)

percentage_prediction = maximum*100

print("element is in  cluster :",index+1)
print("Probability : ",percentage_prediction," %")

