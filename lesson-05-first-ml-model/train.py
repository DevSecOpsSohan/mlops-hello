"""Train a first ML model on the Iris dataset — Lesson 05."""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib


def load_data():
    """Load the Iris dataset. Returns features (X) and labels (y)."""
    data = load_iris()
    return data.data, data.target


def train_model(X_train, y_train):
    """Train a Logistic Regression classifier and return it."""
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)          # <- this is where learning happens
    return model


def evaluate(model, X_test, y_test):
    """Return the model's accuracy on unseen test data."""
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)


def main():
    # 1. Load data
    X, y = load_data()

    # 2. Split into train (80%) and test (20%)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Train
    model = train_model(X_train, y_train)

    # 4. Evaluate on unseen data
    acc = evaluate(model, X_test, y_test)
    print(f"Test accuracy: {acc * 100:.1f}%")

    # 5. Save the trained model to a file
    joblib.dump(model, "lesson-05-first-ml-model/model.joblib")
    print("Model saved to model.joblib")


if __name__ == "__main__":
    main()