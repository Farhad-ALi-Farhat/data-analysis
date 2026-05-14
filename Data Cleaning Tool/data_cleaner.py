import pandas as pd

def clean_data(file):
    df = pd.read_csv(file)

    print("Before cleaning:")
    print(df.isnull().sum())

    df = df.dropna()

    df = df.drop_duplicates()

    print("\nAfter cleaning:")
    print(df.isnull().sum())

    df.to_csv("cleaned_data.csv", index=False)
    print("Cleaned data saved!")

if __name__ == "__main__":
    file = input("Enter CSV file path: ")
    clean_data(file)
