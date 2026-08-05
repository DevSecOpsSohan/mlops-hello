"""
Runner for the MLflow run-function demos.

Each demo lives in its own file (imported below). To study ONE at a time:
run this file, keep exactly ONE demo call uncommented, and comment the rest.

    python run_demos.py

Then view the runs in the UI:
    mlflow ui --backend-store-uri sqlite:///mytracks.db
"""
from demo_start_run import demo_start_run
from demo_end_run import demo_end_run
from demo_active_run import demo_active_run
from demo_last_active_run import demo_last_active_run


if __name__ == "__main__":
    # 👇 Uncomment ONE at a time to see that function in action.
    demo_start_run()
    # demo_end_run()
    # demo_active_run()
    # demo_last_active_run()
