# Importing Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# NLP Packages
import nltk 
from nltk.corpus import stopwords
from textblob import TextBlob 
from textblob import Word
import re
import string
from sklearn.feature_extraction.text import CountVectorizer

# WordCloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Sklearn Packages
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, plot_confusion_matrix, roc_curve, auc, classification_report


# Evaluation function

def evaluation(y_true, y_pred):

    '''
    Shows Accuracy, Precision, Recall, and F1-Score evaluation metrics
    '''

    print('Evaluation Metrics:')
    print('Accuracy: ' + str(metrics.accuracy_score(y_true, y_pred)))
    print('Precision: ' + str(metrics.precision_score(y_true, y_pred)))
    print('Recall: ' + str(metrics.recall_score(y_true, y_pred)))
    print('F1 Score: ' + str(metrics.f1_score(y_true, y_pred)))
    
# Print Confusion Matrix
    print('\nConfusion Matrix:')
    print(' TN,  FP, FN, TP')
    print(confusion_matrix(y_true, y_pred).ravel())
    
    
# Confusion Matrix    
def confusion_matrix(clf, X_test, y_test):
	plot_confusion_matrix(knn, X_test, y_test,  annot=True,cmap="OrRd")
	plt.show()  


# Cross-validation evaluation

def cross_validation(model, X_train, y_train, x):
    '''
    Prints cross-validation metrics for evaluation
    '''

    scores = cross_val_score(model, X_train, y_train, cv=x)
    print('Cross-Validation Accuracy Scores:', scores)    
    print('\nMin: ', round(scores.min(), 6))
    print('Max: ', round(scores.max(), 6))
    print('Mean: ', round(scores.mean(), 6)) 
    print('Range: ', round(scores.max() - scores.min(), 6))
    
# Creating dictionary with all metrics
def evaluation_dict(accuracy, precision, recall, f1, y_test, y_pred, model_name):

    '''
    This function adds the results to a dictionary so that we can create a DataFrame with the results
    '''
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    
    metric_dict[model_name] = {
                                                    'Accuracy': accuracy,
                                                    'Precision': precision,
                                                    'Recall': recall,
                                                    'F1 Score': f1 }


# This function lowercase all the review words, removes punctuation and numbers
def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)

    return text
round1 = lambda x: clean_text_round1(x)


# Create a function to get subjectivity
def getSubjectivity(text):
	'''
	This function tests the subjetivity of the reviews
	'''
	return TextBlob(text).sentiment.subjectivity

# Create a function to get polarity with tweets
def getPolarity(text):
    '''
    Checks review polarity
    '''
    return TextBlob(text).sentiment.polarity
    
# Print Confusion Matrix
    print('\nConfusion Matrix:')
    print(' TN,  FP, FN, TP')
    print(confusion_matrix(y_true, y_pred).ravel())
    
# Function Prints best parameters for GridSearchCV
def print_results(results):
    print('Best Parameters: {}\n'.format(results.best_params_))   