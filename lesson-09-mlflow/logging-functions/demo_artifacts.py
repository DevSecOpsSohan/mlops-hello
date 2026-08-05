"""
Demo: ARTIFACT logging — log_artifact() and log_artifacts().

  log_artifact(local_path, artifact_path=None)  -> log ONE file.
  log_artifacts(local_dir, artifact_path=None)  -> log ALL files in a FOLDER.

An ARTIFACT is any FILE a run produces (model, plot, report, config...).
`artifact_path` is an optional SUBFOLDER inside the run's artifact store to
organize where the file(s) land.
"""
import os
import mlflow


def demo_artifacts():
    mlflow.set_tracking_uri("sqlite:///mytracks.db")
    mlflow.set_experiment("logging-demo")

    with mlflow.start_run(run_name="artifacts-demo"):
        # (a) ONE file -> stored under artifacts/notes/
        with open("notes.txt", "w") as f:
            f.write("Run used LogisticRegression, max_iter=200.\n")
        mlflow.log_artifact("notes.txt", artifact_path="notes")

        # (b) a whole FOLDER of files -> stored under artifacts/reports/
        os.makedirs("reports", exist_ok=True)
        with open("reports/summary.txt", "w") as f:
            f.write("accuracy=0.97\n")
        with open("reports/config.txt", "w") as f:
            f.write("solver=lbfgs\n")
        mlflow.log_artifacts("reports", artifact_path="reports")

        print("Logged one file (notes/) + a folder of files (reports/).")


if __name__ == "__main__":
    demo_artifacts()
