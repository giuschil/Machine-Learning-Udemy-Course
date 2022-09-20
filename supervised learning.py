import pandas as pd
import numpy as np


boston = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data", sep='\s+', usecols=[5,13], names=["RM", "MEDV"])

boston.head()

X = boston.drop("MEDV", axis=1).values

# oppure 
# X = boston["RM"].values

Y = boston["MEDV"].values

#divido dataset per fare un test 

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)

count = np.count_nonzero(X_train)


conta = 0
for i in X_train:
    conta +=1

print(conta)


def count_np(array):
    element = 0
    for i in array:
        element +=1
        
    return element


print(count_np(X_train))

    