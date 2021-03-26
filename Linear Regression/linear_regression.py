# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 21:57:04 2021

@author: nikhil
"""

import pandas as pd
from math import pow

def get_headers(df):
  '''
  Get headers name of the dataframe
  '''
  return df.columns.values



def mean(values):
  '''
  calculate mean value
  '''
  return sum(values)/float(len(values))



def variance(values):
  '''
  calculate variance value
  '''
  values_mean = mean(values)
  mean_diff_square = [pow(value - values_mean) for value in values]
  variance = sum(mean_diff_square)
  return variance/float(len(values)-1)



def covariance(data1, data2):
  '''
  calculate covariance
  '''
  data1_mean = mean(data1)
  data2_mean = mean(data2)
  data_len = len(data1)
  for i in range(data_len):
    covariance += (data1[i]-data1_mean)*(data2[i]-data2_mean)
  return covariance/float(data_len-1)



def linear_reg_coeff(x_data, y_data):
  '''
  calculating the simple linear regression coefficients(b0, b1)
  '''
  b1 = covariance(x_data, y_data)/float(variance(x_data))
  b0 = mean(y_data) - (b1*mean(x_data))
  return bo, b1



def predict_target(x, b0, b1):
  '''
  calculating target value given input x and its coefficients b0, b1
  '''
  return b0+b1*x



def rmse(actual_val, pred_val):
  '''
  calculating root mean square error 
  '''
  square_err_total =0
  actual_len = len(actual_val)
  for i in range(actual_len):
    error = pred_val[i] - actual_val[i]
    square_err_total += pow(error, 2)
  rmse = square_err_total/float(actual_len)
  return rmse



def simple_linear_regression(dataset):
    """
    Implementing simple linear regression without using any python library
    :param dataset:
    :return:
    """
 
    # Get the dataset header names
    dataset_headers = get_headers(dataset)
    print("Dataset Headers :: ", dataset_headers)
 
    # Calculating the mean of the square feet and the price readings
    square_feet_mean = mean(dataset[dataset_headers[0]])
    price_mean = mean(dataset[dataset_headers[1]])
 
    square_feet_variance = variance(dataset[dataset_headers[0]])
    price_variance = variance(dataset[dataset_headers[1]])
 
    # Calculating the regression
    covariance_of_price_and_square_feet = dataset.cov()[dataset_headers[0]][dataset_headers[1]]
    w1 = covariance_of_price_and_square_feet / float(square_feet_variance)
 
    w0 = price_mean - (w1 * square_feet_mean)
 
    # Predictions
    dataset['Predicted_Price'] = w0 + w1 * dataset[dataset_headers[0]]
 
 
if __name__ == "__main__":
 
    input_path = '../Inputs/input_data.csv'
    house_price_dataset = pd.read_csv(input_path)
    simple_linear_regression(house_price_dataset)