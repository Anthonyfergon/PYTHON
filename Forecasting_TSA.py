# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:35:23 2023

@author: AFG
"""

# importing libraries  
import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd  
  
#importing datasets  
data_set= pd.read_csv('C:/Users/Asus VivoBook/Dropbox/My PC (DESKTOP-GN5CQHE)/Desktop/Documentos/The Vault/Python/PYTHON_MACHINE_LEARNING/Forecasting TSA/Position_Salaries.csv')  

# dataset info
data_set.info() 

#Extracting Independent and dependent Variable  
x= data_set.iloc[:, 1:2].values  
y= data_set.iloc[:, 2].values

# Building the Linear regression model:
# Fitting the Linear Regression to the dataset  
from sklearn.linear_model import LinearRegression  
lin_regs= LinearRegression()  
lin_regs.fit(x,y) 

# Building the Polynomial regression model:  
# Fitting the Polynomial regression to the dataset  
from sklearn.preprocessing import PolynomialFeatures  
poly_regs= PolynomialFeatures(degree= 2)  # degree es un parametro que se debe definir
x_poly= poly_regs.fit_transform(x)  
lin_reg_2 =LinearRegression()  
lin_reg_2.fit(x_poly, y)

# Visualizing the result for Linear regression:
#Visulaizing the result for Linear Regression model  
mtp.scatter(x,y,color="blue")  
mtp.plot(x,lin_regs.predict(x), color="red")  
mtp.title("Bluff detection model(Linear Regression)")  
mtp.xlabel("Position Levels")  
mtp.ylabel("Salary")  
mtp.show()

# Visualizing the result for Polynomial Regression
#Visulaizing the result for Polynomial Regression  
mtp.scatter(x,y,color="blue")  
mtp.plot(x, lin_reg_2.predict(poly_regs.fit_transform(x)), color="red")  
mtp.title("Bluff detection model(Polynomial Regression)")  
mtp.xlabel("Position Levels")  
mtp.ylabel("Salary")  
mtp.show() 

# Building a 2nd Polynomial regression model:  
# Fitting the Polynomial regression to the dataset  
from sklearn.preprocessing import PolynomialFeatures  
poly_regs= PolynomialFeatures(degree= 3)  # degree es un parametro que se debe definir
x_poly= poly_regs.fit_transform(x)  
lin_reg_3 =LinearRegression()  
lin_reg_3.fit(x_poly, y)

# Visualizing the result for the 2nd Polynomial Regression
#Visulaizing the result for Polynomial Regression  
mtp.scatter(x,y,color="blue")  
mtp.plot(x, lin_reg_3.predict(poly_regs.fit_transform(x)), color="red")  
mtp.title("Bluff detection model(Polynomial Regression)")  
mtp.xlabel("Position Levels")  
mtp.ylabel("Salary")  
mtp.show() 

# Building a 3rd Polynomial regression model:  
# Fitting the Polynomial regression to the dataset  
from sklearn.preprocessing import PolynomialFeatures  
poly_regs= PolynomialFeatures(degree= 4)  # degree es un parametro que se debe definir
x_poly= poly_regs.fit_transform(x)  
lin_reg_4 =LinearRegression()  
lin_reg_4.fit(x_poly, y)

# Visualizing the result for the 3rd Polynomial Regression
#Visulaizing the result for Polynomial Regression  
mtp.scatter(x,y,color="blue")  
mtp.plot(x, lin_reg_4.predict(poly_regs.fit_transform(x)), color="red")  
mtp.title("Bluff detection model(Polynomial Regression)")  
mtp.xlabel("Position Levels")  
mtp.ylabel("Salary")  
mtp.show() 

# Predicting the final result with the Linear Regression model:
lin_pred = lin_regs.predict([[6.5]])  
print(lin_pred) 

# Predicting the final result with the Polynomial Regression model:
poly_pred = lin_reg_4.predict(poly_regs.fit_transform([[6.5]]))  
print(poly_pred)  






    