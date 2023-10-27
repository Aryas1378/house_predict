from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error

class Predict:
    def __init__(self, model):
        self.__model = model

    def train(self, dataset):
        self.__dataset = dataset
        X = self.__dataset.drop(['price'], axis=1)
        y = self.__dataset['price']

        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
        trained_data = X_train.join(y_train)

        return trained_data
    
    def read_data(self):
        client = MongoClient("localhost", 27017)
        my_db = client['house']

        collec = my_db['houses']
        cursor = collec.find()
        df = pd.DataFrame(list(cursor))

        return df
    
    def predict_decision_tree(self, df):
        
        feature_columns = ['sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement']
        df = df.drop('_id', axis=1)
        X = df[feature_columns]
        y = df['price']
        y = np.log1p(df['price'])

        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        decision_tree = DecisionTreeRegressor(max_depth=5)
        decision_tree = decision_tree.fit(X_train, y_train)
        y_predicted = decision_tree.predict(X_test)
        
        #Mean Squered Error
        mse = mean_squared_error(y_test, y_predicted)
       
        plt.figure(figsize=(10, 6))
        plot_tree(decision_tree, feature_names=feature_columns, filled=True, rounded=True)
        plt.text(0.5, -0.1, f'MSE: {mse:.2f}', fontsize=12, ha='center', transform=plt.gca().transAxes)
        plt.show()

    
    def predict_linear_regression(self, df):
        feature_columns = ['sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement']
        df = df.drop('_id', axis=1)
        X = df[feature_columns]
        y = df['price']
        y = np.log1p(df['price'])
        

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        linear_reg = LinearRegression()
        linear_reg = linear_reg.fit(X_train, y_train)
        y_predicted = linear_reg.predict(X_test)

        mse = mean_squared_error(y_test, y_predicted)

        plt.figure(figsize=(10, 6))
        plt.scatter(y_test, y_predicted)
        plt.xlabel("Actual Price (Log)")
        plt.ylabel("Predicted Price (Log)")
        plt.title("Linear Regression Prediction")
        plt.text(0.5, -0.1, f'MSE (Linear Regression): {mse:.2f}', fontsize=12, ha='center', transform=plt.gca().transAxes)
        plt.show()

    
    def my_predict_price(self, user_df):
        feature_columns = ['sqft_living', 'sqft_above', 'sqft_basement']
        
        user_df = pd.DataFrame([user_df], columns=feature_columns)
        df = self.read_data()
        df = df.drop('_id', axis=1)
        X = df[feature_columns]
        y = df['price']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = DecisionTreeRegressor()
        model = model.fit(X_train, y_train)
        
        return model.predict(user_df)
        
    
    
    # def predict_price(self, user_df):        
    #     user_df = pd.DataFrame([user_df])
    #     predicted_price = self.my_predict_price(user_df)