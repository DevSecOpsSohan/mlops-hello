"""
Demo: PARAM logging — log_param() and log_params().

  log_param(key, value)   -> log ONE param.  RETURNS the value.
  log_params({...})       -> log MANY params from a dict.  Returns None.

A PARAM is an INPUT you chose (e.g. max_iter=200). Logged once, never changes.
"""
import mlflow


def demo_params():
    mlflow.set_tracking_uri("sqlite:///mytracks.db")
    mlflow.set_experiment("logging-demo")

    with mlflow.start_run(run_name="params-demo"):
        returned = mlflow.log_param("max_iter", 200)              # ONE -> returns value
        print("log_param returned:", returned)                   # -> 200
        mlflow.log_params({"test_size": 0.2, "solver": "lbfgs"})  # MANY (dict) -> None
        print("Logged 1 single param + 2 params from a dict.")


if __name__ == "__main__":
    demo_params()
