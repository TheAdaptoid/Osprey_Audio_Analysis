import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset and remove the first column if needed
df = pd.read_csv('cleaned_dataset.csv')
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])


#set theme
sns.set_theme(style='whitegrid', palette='pastel', font_scale=1.2)

print("Generating second round plots")

#identify numerical and categorical features
numerical_features = df.select_dtypes(include=['number']).columns
numerical_features = [col for col in numerical_features if "Unnamed" not in col]  # Filter unnamed columns
categorical_features = df.select_dtypes(include=['object', 'category']).columns

#Pairplot
if len(numerical_features) > 1:
    print("Creating pairplot for numerical features")

    sample_df = df[numerical_features].dropna()
    if len(sample_df) > 2000:
        sample_df = sample_df.sample(1000, random_state=42)

    #had to set font smaller because it was impossible to read .4-.5 siz3e
    #after rotating the text this is no longer an issue but i will keep it
    with sns.plotting_context("notebook", font_scale=0.8):
        g = sns.pairplot(sample_df, corner=True, diag_kind='kde', plot_kws={'alpha': 0.5}, height=2.0)
        g.fig.suptitle('Pairplot of Numerical Features', y=.95)
        plt.tight_layout(pad=3.0)

        #rotate the labels on the left so that they are not overlapping
        for ax in g.axes.flatten():
            if ax is not None:  # Some grids might be empty
                ax.yaxis.label.set_rotation(0)   # 0 degrees -> horizontal
                ax.yaxis.label.set_ha('right')   # Right-align labels
                ax.yaxis.label.set_va('center')  # Vertical align to center

        plt.show()


