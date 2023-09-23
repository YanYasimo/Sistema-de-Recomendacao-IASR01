import threading
import numpy as np

from sklearn.linear_model import LinearRegression
import time

def generate_data(n_samples = 100):
    # Generate random data
    X = np.random.rand(n_samples, 1)
    y = 2.5 * X + np.random.rand(n_samples, 1)
    return X, y

def train_model(thread_id, X, y):
    # Train model
    print(f"Thread {thread_id} training model...")
    model = LinearRegression()
    model.fit(X, y)
    time.sleep(5)
    print(f"Thread {thread_id} model trained!")

def main():
    # Generate data

    # Create threads
    threads = []
    for i in range(4):
        X, y = generate_data()
        thread = threading.Thread(target=train_model, args=(i, X, y))
        threads.append(thread)
        thread.start()

    # Wait for threads to finish
    for thread in threads:
        thread.join()

    print("All threads finished!")