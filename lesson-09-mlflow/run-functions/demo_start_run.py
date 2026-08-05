"""
Demo: mlflow.start_run() — how to START a run and use its options.

start_run(run_id, experiment_id, run_name, nested, tags, description)
  - run_id       : resume an EXISTING run (then you CAN'T set run_name/experiment_id)
  - experiment_id: which experiment a NEW run goes to (only if run_id not set)
  - run_name     : friendly name for a NEW run (auto-random if not given)
  - nested       : True = a run INSIDE another run
  - tags         : labels for the run (new or resumed)
  - description  : free-text notes for a NEW run
Returns an ActiveRun object -> works as a context manager (`with`).
"""
import mlflow


def demo_start_run():
    mlflow.set_tracking_uri("sqlite:///mytracks.db")
    mlflow.set_experiment("run-functions-demo")

    # A NEW run with a custom name, tags, and description.
    # Using `with` means the run auto-ends when the block finishes.
    with mlflow.start_run(
        run_name="start-run-demo",
        tags={"stage": "demo", "author": "sohan"},
        description="A demo run created with start_run().",
    ) as run:
        mlflow.log_param("x", 1)
        mlflow.log_metric("score", 0.95)
        print("Inside the run — run_id:", run.info.run_id)
        print("Inside the run — run_name:", run.info.run_name)

    print("Block finished -> run auto-ended (thanks to `with`).")

    # 🔁 To RESUME this run later, you'd reopen it by id (no run_name allowed):
    #   with mlflow.start_run(run_id="<that id>"):
    #       mlflow.log_metric("score2", 0.97)


if __name__ == "__main__":
    demo_start_run()
