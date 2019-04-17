
# Action Plan for Evidence Delivery of Machine Learning

Competences target:
1. Theory and Conceptual:    Level 2-3
2. Implementatino of ML:     Level 3
3. Deep Learning Frameworks: Level 2-3


## 1 Theory and Conceptual
Concepts Remaining:
- Learning Rate
- Classification
- Activation Funct  2.a) in NeuralNetwork we use the def sigmoid(x) implementatino as actfun
- 1 hot encoding    2.c) in data_utils generated for titanic problem. Function 1hot-encoding
- batch             2.a) in MiniGD uses batches to proceed
- kernel
- networks          2.a) has a complete structure of a nn of 'n' layers each with 'm' parameters
- learning          2.a) Learning Diagrams of Minimizing Error
- train set         2.a) NeuralNet.train recieves both training set and validation set for testing
- valid set         2.a) ^^
- test  set
- confusion mat     2.a)/2.c) Confunsion Matrix Generated after MiniBGD for Validation Data
- variance
- Accuracy 		    2.a) Accuracy for training and validation is calculated in MiniGD and BGD
- cross-validation
- linearity non lin 

## 2 Implementing Models

a) Neural Network Arquitecture
Simple General Purpose Neural Net that can be loaded saved and visualized results
It does each epoch an accuracy and error check
#! TODO: Implement a confusion matrix report
#! TODO: Calculate Precision Besides Error
#! TODO: Implement Dynamic Learning Rate


#! Implement Strategy Trainer With Stats Concepts applicable to any classification model


#! b) Implement RandomForest and Simple Logistic Regression
Simple Logistics Regression Implemented for Titanic Problem and with 1500 number of epochs got 0.47 error while neural net got 0.14

#! c) Resolve (Titanic) with NN & RandomForset & Logistic and compare results (Conf Matrix, Time, Etc)
- Gives full evidence for competence 2.

* Problems:
1. Titanic Problem ()
Preprocess:
I, we obtain a good test_data csv by joining gender_submission.csv and test.csv: "join -t, gender_submission.csv test.csv > test_data.csv"




2. Heart Disease UCI (https://www.kaggle.com/ronitf/heart-disease-uci)


## 3 Deep Learning Frameworks

#! a) Stock Bot Trader

#! b) 
