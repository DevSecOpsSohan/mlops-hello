"""
Demo: mlflow.active_run() — get the run that is active RIGHT NOW.

Returns the current Run object, or None if no run is active.
Common use: grab the current run's id -> mlflow.active_run().info.run_id
"""
import mlflow


def demo_active_run():
    mlflow.set_tracking_uri("sqlite:///mytracks.db")
    mlflow.set_experiment("run-functions-demo")

    print("Before starting a run:", mlflow.active_run())   # -> None

    with mlflow.start_run(run_name="active-run-demo"):
        run = mlflow.active_run()                           # a Run object now
        print("During the run -> id:  ", run.info.run_id)
        print("During the run -> name:", run.info.run_name)

    print("After the run:", mlflow.active_run())            # -> None again


if __name__ == "__main__":
    demo_active_run()
