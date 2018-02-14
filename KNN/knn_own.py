import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from collections import Counter
style.use('fivethirtyeight')


dataset =  {'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
new = [4,3]

def knn(data,predict,k=3):

    if(len(data)>k):
        warnings.warn('K is set to value less than voting groups')
    distances = []

    for group in data :
        for featu in data[group]:
            euclid_dist = np.linalg.norm(np.array(featu)-np.array(predict))
            distances.append([euclid_dist,group])


    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]

    return vote_result

result = knn(dataset,new,k=3)
print(result)

[[plt.scatter(ii[0],ii[1],s=100,color=i ) for ii in dataset[i]] for i in dataset]
plt.scatter(new[0],new[1],s=100,color=result)
#plt.show()