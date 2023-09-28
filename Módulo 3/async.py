import asyncio
import numpy as np
import time
from sklearn.linear_model import LinearRegression

def generate_data(n_samples = 100):
    # Generate random data
    X = np.random.rand(n_samples, 1)
    y = 2.5 * X + np.random.rand(n_samples, 1)
    return X, y

async def fetch_data(delay = 2):
    # Generate data
    await asyncio.sleep(delay) # Simulate network delay
    data = generate_data()
    return data

async def train_model_async(delay = 3):
    # Train model
    print(f"Training model...")
    X, y = await fetch_data() # Wait for data to be fetched
    await asyncio.sleep(delay) # Simulate training time
    model = LinearRegression()
    model.fit(X, y)
    print(f"Model trained!")

async def main():
    print("Starting async tasks...")
    # Different delays for each task
    tasks = [
        train_model_async(i) for i in [2, 3, 4]
    ]

    # Wait for all tasks to finish
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Create an event loop and run the main() function
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()