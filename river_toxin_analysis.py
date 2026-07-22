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

df = pd.read_csv("C:/Users/David Holliday/OneDrive/Documents/Rob Python Project/Project 2 Environmental Toxin Analysis in River Systems/National_River_Toxin_Dataset_1.csv")

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

#### Graphs and charts

![ENVIRONMENTAL-TOXIN-ANALYSIS-IN-RIVER-SYSTEMS](Images/ENVIRONMENTAL-TOXIN-ANALYSIS-IN-RIVER-SYSTEMS.png)
![ENVIRONMENTAL-TOXIN-ANALYSIS-IN-RIVER-SYSTEMS](Images/LinegraphLeadLevels.png)
![ENVIRONMENTAL-TOXIN-ANALYSIS-IN-RIVER-SYSTEMS](Images/River-System-Barchart.png)
