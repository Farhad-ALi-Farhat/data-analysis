import numpy as np

def main():
    arr = np.array([1, 2, 3, 4, 5])

    print("Array:", arr)
    print("Mean:", np.mean(arr))
    print("Standard Deviation:", np.std(arr))

    matrix = np.array([[1, 2], [3, 4]])
    print("\nMatrix:\n", matrix)

    print("Transpose:\n", matrix.T)

if __name__ == "__main__":
    main()
