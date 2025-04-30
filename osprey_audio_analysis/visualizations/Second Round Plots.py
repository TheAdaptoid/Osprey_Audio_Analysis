import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('updated_dataset.csv', usecols=lambda column: column != 'Unnamed: 0')

# Set seaborn theme
sns.set_theme(style='whitegrid', palette='pastel', font_scale=1)

print("Generating second round plots")

# Identify numerical and categorical features
numerical_features = df.select_dtypes(include=['number']).columns
categorical_features = df.select_dtypes(include=['object', 'category']).columns

#this is optional can change if needed
target_variable = 'target'

#Pairplot
if len(numerical_features) > 1:
    print("Creating pairplot for numerical features")

    sample_df = df[numerical_features].dropna()
    if len(sample_df) > 2000:
        sample_df = sample_df.sample(1000, random_state=42)

    sns.pairplot(sample_df, corner=True, diag_kind='kde', plot_kws={'alpha': 0.5})
    plt.suptitle('Pairplot of Numerical Features', y=.95)
    plt.tight_layout()
    plt.show()

#Violin plots
for cat_col in categorical_features:
    unique_vals = df[cat_col].nunique()

    if unique_vals <= 5:
        for num_col in numerical_features:
            print(f"Creating violin plot: {num_col} vs {cat_col}")
            plt.figure(figsize=(10, 5))
            sns.violinplot(x=cat_col, y=num_col, data=df, inner='quartile')
            plt.title(f'{num_col} distribution by {cat_col}')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

#target-variable analysis
if target_variable in df.columns:
    print(f"Analyzing features with target: {target_variable}")

    if df[target_variable].nunique() <= 10:
        #If the target is categorical
        for num_col in numerical_features:
            if num_col != target_variable:
                plt.figure(figsize=(10, 5))
                sns.boxplot(x=target_variable, y=num_col, data=df)
                plt.title(f'{num_col} by {target_variable}')
                plt.tight_layout()
                plt.show()
    else:
        #If the target is continuous
        for num_col in numerical_features:
            if num_col != target_variable:
                plt.figure(figsize=(10, 5))
                sns.scatterplot(x=num_col, y=target_variable, data=df, alpha=0.5)
                plt.title(f'{num_col} vs {target_variable}')
                plt.tight_layout()
                plt.show()

#Swarm plots for outliers
for cat_col in categorical_features:
    unique_vals = df[cat_col].nunique()

    if unique_vals <= 5:
        for num_col in numerical_features:
            print(f"Creating swarm plot: {num_col} vs {cat_col}")
            plt.figure(figsize=(10, 5))
            sns.swarmplot(x=cat_col, y=num_col, data=df, size=3)
            plt.title(f'Swarm plot of {num_col} by {cat_col}')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()


