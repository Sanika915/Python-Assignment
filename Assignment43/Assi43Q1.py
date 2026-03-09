# Design machine learning application which follows below step as 
# Step 1 :
# Get Data : Load data from MarvellousInfosystems_PlayPredictor.csv file into python application.
# Step 2 :
# Clean,Prepare and Manipulate data: As we want to use the above data into machine learning application we have prepare that 
# in the format which is accepted by the algorithms.
# As our dataset contains two features as Wether and Temperature. We have to replace each sttring filed into numeric constants by using 
# LableEncoder from processing module of sklearn.
# Step 3 :
# Train Data : Now we want to train our data for that we have to select the Machine learning algorithm. For that we select K Nearest Neighnour algorithm.
# use fit method for training purpose. For training use whole dataset.
# Step 4 :
# Test Data : After successful training now we can test our trained data by passing some value of whether and temperature.
# As we are using KNN algorithm use value of K as 3.
# After providing the values check the result and display on screen.
# Result may be Yes or No.
# Step 5:
# Calculate Accuracy : Write one function as CheckAccuracy() which calculate the accuracy of our algorithm. For calculating the accuracy divide the dataset into two equal parts as Training data and Testing data.
# Calculate Accuracy by changing value of K.

# ------------------------------------------------------------
# Marvelous Infosystems - Play Predictor using KNN
# ------------------------------------------------------------

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def MarvellousPlayPredictor(Datapath):

    Border = "-" * 40

    #-----------------------------------------------
    # Step 1 : Load Dataset
    #-----------------------------------------------
    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)

    df = pd.read_csv(Datapath)

    print("First few records of dataset :")
    print(df.head())

    #-----------------------------------------------
    # Step 2 : Check Missing Values
    #-----------------------------------------------
    print(Border)
    print("Step 2 : Check Missing Values")
    print(Border)

    print(df.isnull().sum())

    #-----------------------------------------------
    # Step 3 : Data Preparation (Label Encoding)
    #-----------------------------------------------
    print(Border)
    print("Step 3 : Data Preparation")
    print(Border)

    le_weather = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    df['Whether'] = le_weather.fit_transform(df['Whether'])
    df['Temperature'] = le_temp.fit_transform(df['Temperature'])
    df['Play'] = le_play.fit_transform(df['Play'])

    print("Encoded Dataset :")
    print(df.head())

    #-----------------------------------------------
    # Step 4 : Split Dataset into X and Y
    #-----------------------------------------------
    print(Border)
    print("Step 4 : Split Dataset into Independent and Dependent Variables")
    print(Border)

    X = df[['Whether','Temperature']]
    Y = df['Play']

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)

    #-----------------------------------------------
    # Step 5 : Train Test Split
    #-----------------------------------------------
    print(Border)
    print("Step 5 : Train Test Split")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Shape of X_train :",X_train.shape)
    print("Shape of X_test :",X_test.shape)

    #-----------------------------------------------
    # Step 6 : Create and Train Model
    #-----------------------------------------------
    print(Border)
    print("Step 6 : Create and Train Decision Tree Model")
    print(Border)

    model = DecisionTreeClassifier()

    model.fit(X_train,Y_train)

    #-----------------------------------------------
    # Step 7 : Test Model
    #-----------------------------------------------
    print(Border)
    print("Step 7 : Test Model")
    print(Border)

    y_pred = model.predict(X_test)

    print("Predictions :",y_pred)

    #-----------------------------------------------
    # Step 8 : Calculate Accuracy
    #-----------------------------------------------
    print(Border)
    print("Step 8 : Model Accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test,y_pred)

    print("Accuracy :",accuracy*100,"%")

    #-----------------------------------------------
    # Step 9 : Compare Actual and Predicted
    #-----------------------------------------------
    print(Border)
    print("Step 9 : Actual vs Predicted")
    print(Border)

    Result = pd.DataFrame({'Actual':Y_test.values,
                           'Predicted':y_pred})

    print(Result.head())

    #-----------------------------------------------
    # Step 10 : Manual Prediction
    #-----------------------------------------------
    print(Border)
    print("Step 10 : Manual Prediction")
    print(Border)

    sample = [[le_weather.transform(['Sunny'])[0],
               le_temp.transform(['Cool'])[0]]]

    result = model.predict(sample)

    print("Prediction for Sunny & Cool :",le_play.inverse_transform(result))

def main():

    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()
    