"""
Demo: mlflow.end_run() — how to END a run MANUALLY (without `with`).

Use this when you start a run WITHOUT the `with` block. If you use
`with mlflow.start_run():`, MLflow calls end_run() for you automatically.

end_run(status="FINISHED")  -> status can be "FINISHED", "FAILED", or "KILLED".
"""
import mlflow


def demo_end_run():
    mlflow.set_tracking_uri("sqlite:///mytracks.db")
    mlflow.set_experiment("run-functions-demo")

    # Start WITHOUT `with` -> we are now responsible for ending it.
    mlflow.start_run(run_name="manual-end-demo")
    mlflow.log_param("y", 2)
    print("Active run id (running):", mlflow.active_run().info.run_id)

    # We MUST end it ourselves, or it stays open.
    mlflow.end_run()   # status defaults to "FINISHED"
    print("After end_run(), active run is:", mlflow.active_run())   # -> None


if __name__ == "__main__":
    demo_end_run()
