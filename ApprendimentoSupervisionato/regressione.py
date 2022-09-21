import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split



boston = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data", sep='\s+', usecols=[5,13], names=["RM", "MEDV"])

boston.head()

X = boston.drop("MEDV", axis=1).values

# oppure 
# X = boston["RM"].values

Y = boston["MEDV"].values

#divido dataset per fare un test 


X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)


from sklearn.linear_model import LinearRegression

ll = LinearRegression()
ll.fit(X_train, Y_train)
Y_pred = ll.predict(X_test)

from sklearn.metrics import mean_squared_error

mean_squared_error(Y_test, Y_pred)

from sklearn.metrics import r2_score

r2_score(Y_test, Y_pred)

import matplotlib.pyplot as plt
%matplotlib inline

print("Peso di RM: "+ str(ll.coef_[0]))
print("Bias: "+str(ll.intercept_))


plt.scatter(X_train, Y_train, c="green",  edgecolor='white', label="Train set")
plt.scatter(X_test, Y_test, c="blue",  edgecolor='white', label="Test set")

plt.xlabel('Numero medio di stanze [RM]')
plt.ylabel('Valore in $1000 [MEDV]')

plt.legend(loc='upper left')

plt.plot(X_test, Y_pred, color='red', linewidth=3)
    