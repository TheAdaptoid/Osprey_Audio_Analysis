import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df = pd.read_csv('updated_dataset.csv')
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])


#try:
 #   df = pd.read_csv(dataset)
#except FileNotFoundError:
#    print("Error: 'updated_dataset.csv' was not found.")

#    exit()



#set the style for seaborn
sns.set_theme(style='whitegrid', palette='muted', font_scale=1.1)

print("Generating first round plots")



#plotting numerical features
numerical_features = df.select_dtypes(include=['number']).columns
for col in numerical_features:
    print(f"Plotting numerical feature: {col}")
    plt.figure(figsize=(10, 4))

    #histogram
    plt.subplot(1, 2, 1)
    sns.histplot(df[col], bins=50, kde=False)
    plt.title(f'Histogram of {col}')

    #boxplot
    plt.subplot(1, 2, 2)

    if len(df) > 5000:
        sns.boxplot(y=df[col].sample(1000, random_state=1))
    else:
        sns.boxplot(y=df[col])
    plt.title(f'Boxplot of {col}')

    plt.tight_layout()
    plt.show()



#plotting categorical features
#will probably need to edit
categorical_features = df.select_dtypes(include=['object', 'category']).columns

for col in categorical_features:
    unique_vals = df[col].nunique()
    print(f"Plotting categorical feature: {col} ({unique_vals} unique values)")

    if unique_vals <= 20:
        plt.figure(figsize=(10, 4))
        sns.countplot(x=df[col], order=df[col].value_counts().index)
        plt.title(f'Countplot of {col}')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print(f"Skipping {col}: too many unique categories")



#heat map for number features
if len(numerical_features) > 1:
    correlation_matrix = df[numerical_features].corr()

    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

    plt.title('Correlation Matrix Heatmap')
    plt.tight_layout()
    plt.show()


# dont really need this and will not include this graphs with the submited final
#scatter plot for important relationships this only shows 2 features will probably need to add more
if 'popularity' in df.columns and 'energy' in df.columns:
    print("Plotting scatter plot for feature1 vs feature2")

    plt.figure(figsize=(6, 6))
    sample_df = df[['popularity', 'energy']].dropna()

    if len(sample_df) > 5000:
        sample_df = sample_df.sample(1000, random_state=1)
    sns.scatterplot(x='popularity', y='energy', data=sample_df, alpha=0.5)


    plt.title('Scatter Plot of Feature1 vs. Feature2')
    plt.tight_layout()
    plt.show()

print("First Round Plots completed.")
