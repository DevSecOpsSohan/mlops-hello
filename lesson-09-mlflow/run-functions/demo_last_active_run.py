"""
Demo: mlflow.last_active_run() — get the LAST run, even AFTER it ended.

Unlike active_run() (which is None once the run ends), last_active_run() still
returns the run you most recently finished. Great with autolog(), which opens and
closes the run for you — afterwards you use last_active_run() to read its id/status.
"""
import mlflow


def demo_last_active_run():
    mlflow.set_tracking_uri("sqlite:///mytracks.db")
    mlflow.set_experiment("run-functions-demo")

    with mlflow.start_run(run_name="last-active-demo"):
        mlflow.log_metric("score", 0.9)
    # The run has ENDED here. active_run() would be None now...

    last = mlflow.last_active_run()          # ...but this still gives it to us
    print("last_active_run -> id:    ", last.info.run_id)
    print("last_active_run -> name:  ", last.info.run_name)
    print("last_active_run -> status:", last.info.status)   # FINISHED


if __name__ == "__main__":
    demo_last_active_run()
