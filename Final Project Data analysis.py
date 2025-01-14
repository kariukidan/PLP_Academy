from pandas import *
import matplotlib.pyplot as plt
import seaborn as sns

# read csv file
file_name = "/content/diabetes.csv"
df = read_csv(file_name)

df.head()

#get a summary of the data
df.info()

#check for missing values
df.isna()

#find total missing values for each column
df.isna().sum()

# Calculate basic statistics (minimum, maximum, mean, variance, quantiles) for all columns.

#check for maximum value per column
df.max()

#check for minimum value in each column
df.min()

df.describe()

#How many women over 50 years have diabetes?
women_over_50_with_diabetes = df[(df['Age'] > 50) & (df['Outcome'] == 1)].shape[0]
print (women_over_50_with_diabetes)

#diabetic women under 30 years
women_under_50_with_diabetes = df[(df['Age'] < 30) & (df['Outcome'] == 1)].shape[0]
print (women_under_50_with_diabetes)

#top 5 women with most pregnancies
top_five_pregnancies = df.nlargest(5, 'Pregnancies')
print (top_five_pregnancies)

#women aged between 30 and 40 who gave birth to 3 or more children?
women_30_to_40_with_3_or_more_kids = df[(df['Age'] >= 30) & (df['Age'] <= 40) & (df['Pregnancies'] >= 3)].shape[0]
print(women_30_to_40_with_3_or_more_kids)

#considering BMI >= 30 is a sign of obesity.
#calculate number of women with signs of obesity and have high blood pressure
obese_women_with_high_bp = df[(df['BMI'] >= 30) & (df['BloodPressure'] > 89)].shape[0]
print (obese_women_with_high_bp)

#Comparison of mean values for Glucose, BloodPressure and Insulin among those with and without diabetes.
mean_values_with_without_diabetes = df.groupby('Outcome')[['Glucose', 'BloodPressure', 'Insulin']].mean()
print(mean_values_with_without_diabetes)

#women who have been pregnant and are diabetic
pregnant_diabetic = df[(df['Pregnancies'] > 0) & (df['Outcome'] == 1)].shape[0]
print(pregnant_diabetic)

#add new column

# Define the function to categorize BMI
def bmi_category(BMI):
    if BMI < 18.5:
        return 'Underweight'
    elif 18.5 <= BMI <= 24.9:
        return 'Normal weight'
    elif 25 <= BMI <= 29.9:
        return 'Overweight'
    else:  # BMI 30 or greater
        return 'Obesity'

# Apply the function to create the 'bodyType' column
df['bodyType'] = df['BMI'].apply(bmi_category)

# Display the first few rows to check the result
print(df[['BMI', 'bodyType']].head())

# VISUALIZATION

#histogram to show pregnancy distribution

plt.figure(figsize=(8, 6))
sns.histplot(df['Pregnancies'], kde=True)
plt.title('Pregnancy Distribution')
plt.xlabel('Pregnancy')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of Glucose vs BMI with Outcome as hue
sns.scatterplot(data=df, x="Glucose", y="BMI", hue="Outcome")

plt.title('Scatter Plot of Glucose vs BMI by Diabetes Outcome')
plt.xlabel('Glucose')
plt.ylabel('BMI')
plt.show()

# Bar plot for Outcome distribution
plt.figure(figsize=(6, 6))
sns.countplot(x='Outcome', data=df)
plt.title('Diabetes Outcome Distribution')
plt.xlabel('Outcome (0: No, 1: Yes)')
plt.ylabel('Count')
plt.show()

# Bar plot of Pregnancies vs Age with Outcome as hue
sns.barplot(data=df, x="Pregnancies", y="Age", hue="Outcome")

# Adding titles and labels
plt.title('Bar Plot of Pregnancies vs Age by Diabetes Outcome')
plt.xlabel('Number of Pregnancies')
plt.ylabel('Age')

# Show the plot
plt.show()

# Violin plot for Glucose levels by Outcome
plt.figure(figsize=(8, 6))
sns.violinplot(x='Outcome', y='Glucose', data=df)
plt.title('Glucose Distribution by Diabetes Outcome')
plt.show()

# Density plot for Age
plt.figure(figsize=(8, 6))
sns.kdeplot(df['Age'], fill=True)
plt.title('Age Distribution (Density Plot)')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Pairplot shows the relationships between multiple variables
sns.pairplot(df, hue='Outcome', diag_kind='kde')
plt.show()