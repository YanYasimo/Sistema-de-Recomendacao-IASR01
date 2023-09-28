import multiprocessing
import numpy as np
from sklearn.linear_model import LinearRegression
import time

def generate_data(n_samples=100):
    # Generate random data
    X = np.random.rand(n_samples, 1)
    y = 2.5 * X + np.random.rand(n_samples, 1)
    return X, y

def train_model(i):
    # Train model
    X, y = generate_data()
    model = LinearRegression()
    model.fit(X, y)
    time.sleep(5)
    print(f"Process {i} finished training")

if __name__ == "__main__":
    processes = []
    for i in range(50):
        process = multiprocessing.Process(target=train_model, args=(i,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("Done!")
