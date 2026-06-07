import os
import seaborn as sns
import matplotlib.pyplot as plt

from model_training.data_prep import prepare_features

PLOT_DIR = "logs"


def run_eda(df):
    os.makedirs(PLOT_DIR, exist_ok=True)

    df_features = prepare_features(df)
    df_features["price"] = df["price"].values

    print("EDA: feature distribution and correlation summary")
    print(df_features.describe(include="all"))

    plt.figure(figsize=(10, 8))
    sns.heatmap(df_features.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    correlation_path = os.path.join(PLOT_DIR, "correlation_matrix.png")
    plt.title("Feature Correlation Matrix")
    plt.savefig(correlation_path, bbox_inches="tight")
    plt.close()

    plot_path = os.path.join(PLOT_DIR, "pairplot.png")
    sns.pairplot(df_features, corner=True)
    plt.savefig(plot_path, bbox_inches="tight")
    plt.close()

    print(f"Saved correlation matrix at {correlation_path}")
    print(f"Saved pair plot at {plot_path}")
