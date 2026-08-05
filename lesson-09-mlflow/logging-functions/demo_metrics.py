"""
Demo: METRIC logging — log_metric() and log_metrics().

  log_metric(key, value, step=None)   -> log ONE metric.  Returns None.
  log_metrics({...}, step=None)        -> log MANY metrics from a dict.  Returns None.

A METRIC is a RESULT you measured (e.g. accuracy=0.97). With `step` you can log the
same metric repeatedly (once per epoch) to form a CURVE over time.
"""
import mlflow


def demo_metrics():
    mlflow.set_tracking_uri("sqlite:///mytracks.db")
    mlflow.set_experiment("logging-demo")

    with mlflow.start_run(run_name="metrics-demo"):
        mlflow.log_metric("accuracy", 0.97)                       # ONE metric
        mlflow.log_metrics({"precision": 0.95, "recall": 0.93})   # MANY (dict)

        # `step` lets one metric be logged over time -> a curve in the UI
        for epoch in range(5):
            mlflow.log_metric("loss", 1.0 / (epoch + 1), step=epoch)

        print("Logged 1 metric + 2 metrics + a 5-step loss curve.")


if __name__ == "__main__":
    demo_metrics()
