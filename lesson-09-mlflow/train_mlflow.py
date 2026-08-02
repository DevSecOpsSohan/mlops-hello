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

    # -------------------------------------------------------------------------
    # WHERE does MLflow store tracking data?  ->  set_tracking_uri()
    #
    # If we DON'T set this, MLflow defaults to auto-creating an `mlruns/` folder
    # in the current working directory (on Windows that lands on the C: drive,
    # right next to the code — easy to lose track of).
    #
    # BEST PRACTICE: always set your own explicit path so you control where data
    # lives. The URI can be LOCAL or REMOTE:
    #   local  DB     -> "sqlite:///mlflow.db"          (default DB)
    #   custom DB     -> "sqlite:///mytracks.db"        (custom-named DB — this)
    #   remote server -> "http://mlflow-server:5000"    (shared team server)
    #
    # NOTE (MLflow 3.x): a bare FOLDER path like "./mytracks" is the old *file
    # store* and is now DEPRECATED — MLflow raises an error and tells you to use
    # a database backend. So for a custom name, use a SQLite DB (sqlite:///NAME.db),
    # not a folder.
    # -------------------------------------------------------------------------
    mlflow.set_tracking_uri("sqlite:///mytracks.db")   # <- custom-named SQLite DB

    # get_tracking_uri() READS back where MLflow is currently pointing.
    # Great for debugging "where did my runs actually go?"
    print("Tracking data is going to:", mlflow.get_tracking_uri())

    # -------------------------------------------------------------------------
    # EXPERIMENTS = named groups of related runs (keeps projects separate).
    #
    # create_experiment(name, artifact_location=None, tags=None):
    #   Creates a BRAND-NEW experiment. Errors if it already exists. Lets you set
    #   a custom artifact location + tags. Returns the new experiment's ID.
    #   -> We guard it with get_experiment_by_name so re-runs don't crash.
    #
    # set_experiment(name):
    #   Activates the experiment for the runs that follow (creates it if missing).
    #   This is the everyday function you'll almost always use.
    # -------------------------------------------------------------------------
    experiment_name = "iris-classifier"

    if mlflow.get_experiment_by_name(experiment_name) is None:
        mlflow.create_experiment(
            name=experiment_name,
            tags={"project": "iris", "team": "mlops-learning"},
        )

    mlflow.set_experiment(experiment_name)   # activate it for the run below

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
