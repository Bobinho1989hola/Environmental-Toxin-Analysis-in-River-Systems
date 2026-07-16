## National River Toxin Analysis
#### Project Description

This project analyzes the National River Toxin Dataset to explore patterns and trends in toxin levels found in river water. The analysis uses Python-based data science and statistical tools to clean, explore, visualize, and analyze the dataset.

#### Tech Stack
Python
pandas
NumPy
Matplotlib
Seaborn
SciPy
Scikit-learn
Statsmodels

#### Project Structure

├── data/
│   └── National_River_Toxin_Dataset_1.csv
├── river_toxin_analysis.py
├── requirements.txt
└── README.md

##### Setup
Clone this repository.
Navigate to the project directory.
Install the required Python dependencies:
pip install -r requirements.txt

##### Running the Analysis

Run the Python script from the project root directory:

python river_toxin_analysis.py

The script loads the dataset from:

data/National_River_Toxin_Dataset_1.csv

and performs the project's data analysis and visualizations.

##### Data

The raw dataset is stored in the data/ directory and is loaded by the analysis script using a relative file path.






#### The below to be deleted if not required#
--

## Environmental-Toxin-Analysis-in-River-Systems
#### An analysis of the different levels of toxins present in river systems throughout the world

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose

%matplotlib inline

#Load the dataset

df = pd.read_csv("C:/df = pd.read_csv("data/National_River_Toxin_Dataset_1.csv")

#Initial data exploration

#df.head()
#print(df.shape)

##df.info()

#df.describe() 

#### Check for missing values

#### print(df.isnull().sum())

#### Fill missing values in numeric column only
numeric_columns = df.select_dtypes(include=[np.number]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

df.dropna(inplace=True)

#### Convert the 'Date' colummn to datetime
df['Date'] = pd.to_datetime(df['Date'])

#### calc avg toxin levels for each river system

average_toxin_levels = df[['Lead', 'Mercury', 'Arsenic']].mean()
#print(f"Average Toxin Levels:\n{average_toxin_levels}")
  
#Top 5 most polluted river systems
top_polluted_rivers = df.groupby('River_System')['Lead'].mean().sort_values(ascending=False)
print(f"Top Polluted Rivers by Lead Levels:\n{top_polluted_rivers.head()}")

#Bar chart for avg lead levels

plt.figure(figsize=(10, 6))
top_polluted_rivers.plot(kind='bar', color='skyblue')
plt.title('Average Lead Levels by River System')
plt.xlabel('River  System')
plt.ylabel('Average Lead Level')
plt.show()

#### line graph for toxin levels over time
plt.figure(figsize=(10, 6))
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Lead', data=df, hue='River_System', errorbar=None)
errorbar=None
plt.title('Lead Levels Over Time')
plt.xlabel('Date')
plt.ylabel('Lead Level')
plt.show()

#Analyse the correlation between pH levels and toxin concentrations
corr_matrix = df[numeric_columns].corr()

#Heatmap for correlation between different parameters
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

#### T-test between two river systems (e.g., Amazon and Nile)
amazon_df = df[df['River_System'] == 'Amazon']['Lead']
nile_df = df[df['River_System'] == 'Nile']['Lead']
t_stat, p_value = stats.ttest_ind(amazon_df, nile_df)

print(f"T-test between Amazon and Nile: T-statistic = {t_stat}, P-value = {p_value}")

#Linear regression analysis for toxin levels and pH
x = df[['pH_Level']]
y = df[['Lead']]
model = LinearRegression()
model.fit(x, y)
print(f"Linear Regression Coefficient: {model.coef_}")
print(f"Linear Regression Intercept: {model.intercept_}")
