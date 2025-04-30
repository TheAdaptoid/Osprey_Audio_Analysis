import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset and remove the first column if needed
df = pd.read_csv('updated_dataset.csv')
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])


# Set seaborn theme
sns.set_theme(style='whitegrid', palette='pastel', font_scale=1.2)

print("Generating second round plots")

# Identify numerical and categorical features
numerical_features = df.select_dtypes(include=['number']).columns
numerical_features = [col for col in numerical_features if "Unnamed" not in col]  # Filter unnamed columns
categorical_features = df.select_dtypes(include=['object', 'category']).columns

# Pairplot
if len(numerical_features) > 1:
    print("Creating pairplot for numerical features")

    sample_df = df[numerical_features].dropna()
    if len(sample_df) > 2000:
        sample_df = sample_df.sample(1000, random_state=42)

    # Temporarily set smaller font context
    with sns.plotting_context("notebook", font_scale=0.4):
        g = sns.pairplot(sample_df, corner=True, diag_kind='kde', plot_kws={'alpha': 0.5}, height=2.0)
        g.fig.suptitle('Pairplot of Numerical Features', y=.95)
        plt.tight_layout(pad=3.0)
        plt.show()


# Swarm Plots for Outliers
for cat_col in categorical_features:
    unique_vals = df[cat_col].nunique()

    if unique_vals <= 100:
        for num_col in numerical_features:
            print(f"Creating swarm plot: {num_col} vs {cat_col}")
            plt.figure(figsize=(10, 5))
            sns.swarmplot(x=cat_col, y=num_col, data=df, size=3)
            plt.title(f'Swarm plot of {num_col} by {cat_col}')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout(pad=3.0)
            plt.show()
