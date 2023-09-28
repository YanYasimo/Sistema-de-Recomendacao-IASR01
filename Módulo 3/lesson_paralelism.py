import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from concurrent.futures import ThreadPoolExecutor

#Gerar dados sintéticos
X, y = make_regression(n_samples=10000, n_features=20, noise=0.1)

# Funções de treinamento 
def train_linear(data):
    X, y = data
    model = LinearRegression()
    model.fit(X, y)
    return model.coef_

def train_ridge(data):
    X, y = data
    model = Ridge()
    model.fit(X, y)
    return model.coef_

def train_lasso(data):
    X, y = data
    model = Lasso()
    model.fit(X, y)
    return model.coef_

def train_model(func_data):
    func, data = func_data
    return func(data)

def main():
    functions = [train_linear, train_ridge, train_lasso]
    tasks = [(func, (X, y)) for func in functions]

    with ThreadPoolExecutor(max_workers=3) as executor:
        print("Iniciando treinamento")
        results = list(executor.map(train_model, tasks))

    model_names = ["Linear Regression", "Ridge", "Lasso"]

    for name, coef in zip(model_names, results):
        print(f"Modelo: {name} Coeficientes: {coef[:2]}...")

if __name__ == "__main__":
    main()