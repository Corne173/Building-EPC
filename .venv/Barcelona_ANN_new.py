import pandas as pd
#from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neural_network import MLPClassifier  # Import the MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from imblearn.over_sampling import SMOTE

# SHAP and LIME library for explanability of the EPC label classifications
import shap
import lime
import lime.lime_tabular


import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import re  # regular expressions


import seaborn as sns

# for deep explainer NN
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical
from sklearn.tree import DecisionTreeClassifier
from tensorflow.keras.layers import Dense, Input, Flatten, Reshape
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.optimizers import Adam

# Load the data from the CSV excel file
file_path = 'Barcelona.csv'
df = pd.read_csv(file_path)

 # allow pandas to display all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 30)


# Display the first few rows of the Data Frame to understand the structure for data manipulation
print('columns',len(df.columns))
print('test')
print("First few rows of the data:")
print(df.head())
