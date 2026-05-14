import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv("sales.csv")

def analyze(df):
    print("Total Sales:", df["revenue"].sum())

    print("\nSales by Product:")
    print(df.groupby("product")["revenue"].sum())

def visualize(df):
    df.groupby("product")["revenue"].sum().plot(kind="bar")
    plt.title("Revenue by Product")
    plt.show()

def main():
    df = load_data()
    analyze(df)
    visualize(df)

if __name__ == "__main__":
    main()
