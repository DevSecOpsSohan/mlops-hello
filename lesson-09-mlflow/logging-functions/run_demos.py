"""
Runner for the MLflow logging-function demos.

Each group lives in its own file (imported below). To study ONE at a time:
run this file with exactly ONE demo call uncommented, comment the rest.

    python run_demos.py

Then view what got logged in the UI:
    mlflow ui --backend-store-uri sqlite:///mytracks.db
"""
from demo_params import demo_params
from demo_metrics import demo_metrics
from demo_artifacts import demo_artifacts
from demo_tags import demo_tags


if __name__ == "__main__":
    # 👇 Uncomment ONE at a time.
    demo_params()
    # demo_metrics()
    # demo_artifacts()
    # demo_tags()
