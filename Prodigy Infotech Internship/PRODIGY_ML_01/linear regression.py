import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

housing = pd.read_csv('train.csv')
#housing = pd.DataFrame(pd.read_csv("train.csv"))
housing.info()

house=pd.DataFrame().assign(Price=housing['price'], Area=housing['area'], Bedrooms=housing['bedrooms'], Bathrooms=housing['bathrooms'])

# Data Cleaning - Check for null values
print(house.isnull().sum())

x=house.drop(columns='Price')
y=house['Price']

# Outlier Analysis
fig, axs = plt.subplots(2,2, figsize = (10,5))
plt1 = sns.boxplot(house['Price'], ax = axs[0,0])
plt2 = sns.boxplot(house['Area'], ax = axs[0,1])
plt1 = sns.boxplot(house['Bedrooms'], ax = axs[1,0])
plt2 = sns.boxplot(house['Bathrooms'], ax = axs[1,1])

plt.tight_layout()
plt.show()

# Outlier treatment for price
plt.boxplot(house.Price)
Q1 = house.Price.quantile(0.25)
Q3 = house.Price.quantile(0.75)
IQR = Q3 - Q1
house = house[(house.Price >= Q1 - 1.5*IQR) & (house.Price <= Q3 + 1.5*IQR)]

# Outlier treatment for area
plt.boxplot(house.Area)
Q1 = house.Area.quantile(0.25)
Q3 = house.Area.quantile(0.75)
IQR = Q3 - Q1
house = house[(house.Area >= Q1 - 1.5*IQR) & (house.Area <= Q3 + 1.5*IQR)]

# Performing outlier analysis again
fig, axs = plt.subplots(2,2, figsize = (10,5))
plt1 = sns.boxplot(house['Price'], ax = axs[0,0])
plt2 = sns.boxplot(house['Area'], ax = axs[0,1])
plt1 = sns.boxplot(house['Bedrooms'], ax = axs[1,0])
plt2 = sns.boxplot(house['Bathrooms'], ax = axs[1,1])

plt.tight_layout()
plt.show()

# Splitting the data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)    

# Machine Learning Model
from sklearn.linear_model import LinearRegression
lr=LinearRegression()

# Fitting
lr.fit(x_train, y_train)


c=lr.intercept_
print("Intercepts: ",c)

m=lr.coef_
print("Coefficients: ",m)

#Predicting
y_pred_train=lr.predict(x_train)
#Visualization
plt.scatter(y_train, y_pred_train)
plt.xlabel("Real Price")
plt.ylabel("Predicted Price")
plt.show()

from sklearn.metrics import r2_score
print(r2_score(y_train, y_pred_train))


