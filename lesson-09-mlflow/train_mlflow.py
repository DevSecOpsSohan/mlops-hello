"""Train the Iris model AND track the run with MLflow — Lesson 09."""

from pathlib import Path
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
    # WHEN TO USE WHICH:
    #
    # create_experiment(name, artifact_location=None, tags=None)
    #   USE FOR: a BRAND-NEW experiment you're about to start.
    #   - Errors if an experiment with that name ALREADY EXISTS.
    #   - Only place you can set a custom ARTIFACT LOCATION + tags (set ONCE,
    #     at creation — cannot be changed later).
    #   - Returns the new experiment's ID.
    #
    # set_experiment(name)
    #   USE FOR: pointing at an EXISTING experiment by name to keep logging to it.
    #   - If NO experiment with that name exists yet, it CREATES one automatically.
    #   - Always ACTIVATES it (all runs after this line are filed under it).
    #   - RETURNS the Experiment object (so we can read/print its details).
    #   -> This is the everyday function. Safe to call on every run.
    #
    # THE PATTERN BELOW: use create_experiment ONLY the first time (to set the
    # custom artifact location + tags), guarded so re-runs don't crash; then
    # set_experiment every time to activate it.
    # -------------------------------------------------------------------------
    experiment_name = "iris-experiment"

    # A CUSTOM artifact location for THIS experiment (its own separate folder).
    # Could also be a cloud bucket: "s3://my-bucket/iris" or "gs://my-bucket/iris".
    artifact_uri = Path("iris_artifacts").absolute().as_uri()   # -> file:///.../iris_artifacts

    if mlflow.get_experiment_by_name(experiment_name) is None:
        mlflow.create_experiment(
            name=experiment_name,
            artifact_location=artifact_uri,                       # custom artifact path
            tags={"project": "iris", "team": "mlops-learning"},   # metadata tags
        )

    # set_experiment activates it AND returns the Experiment object.
    experiment = mlflow.set_experiment(experiment_name)

    # Print the experiment's details (get_experiment_by_name / get_experiment
    # return the same object if you fetch it separately).
    print("--- experiment details ---")
    print("name:             ", experiment.name)
    print("experiment_id:    ", experiment.experiment_id)
    print("artifact_location:", experiment.artifact_location)   # the artifact URL
    print("tags:             ", experiment.tags)
    print("lifecycle_stage:  ", experiment.lifecycle_stage)
    print("--------------------------")

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
