import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv("students.csv")

def analyze(df):
    print("\n--- Basic Info ---")
    print(df.info())

    print("\n--- Average Scores ---")
    print(df.mean(numeric_only=True))

    print("\n--- Top Students ---")
    print(df.sort_values(by="math_score", ascending=False).head())

def visualize(df):
    df["math_score"].hist()
    plt.title("Math Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()

def main():
    df = load_data()
    analyze(df)
    visualize(df)

if __name__ == "__main__":
    main()
