"""Train the Iris model AND track the run with MLflow — Lesson 09."""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn


def load_data():
    data = load_iris()
    return data.data, data.target


def main():
    # --- settings we chose (these are PARAMETERS) ---
    max_iter = 200
    test_size = 0.2

    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    # Name the group of runs
    mlflow.set_experiment("iris-classifier")

    # Start recording ONE run
    with mlflow.start_run():
        # 1. Log the input settings (parameters)
        mlflow.log_param("max_iter", max_iter)
        mlflow.log_param("test_size", test_size)

        # 2. Train
        model = LogisticRegression(max_iter=max_iter)
        model.fit(X_train, y_train)

        # 3. Evaluate and log the result (metric)
        acc = accuracy_score(y_test, model.predict(X_test))
        mlflow.log_metric("accuracy", acc)

        # 4. Log the trained model itself (artifact)
        mlflow.sklearn.log_model(model, name="model")

        print(f"Logged run — accuracy: {acc * 100:.1f}%")


if __name__ == "__main__":
    main()
