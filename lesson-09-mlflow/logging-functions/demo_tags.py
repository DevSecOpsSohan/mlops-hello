"""
Demo: TAG logging — set_tag() and set_tags().

  set_tag(key, value)   -> set ONE tag on the current run.   Returns None.
  set_tags({...})       -> set MANY tags (dict) on the run.  Returns None.

A TAG is a LABEL (key=value string) you attach to a run so you can organize and
later SEARCH/FILTER runs by it (e.g. stage="production", author="sohan").

Limits:
  key   = string, up to 250 characters
  value = string, up to 5000 characters

⚠️ set_tag / set_tags tag the RUN (call them inside an active run). To tag the
   EXPERIMENT itself, use create_experiment(tags={...}) or
   mlflow.set_experiment_tag(key, value).
"""
import mlflow


def demo_tags():
    mlflow.set_tracking_uri("sqlite:///mytracks.db")
    mlflow.set_experiment("logging-demo")

    with mlflow.start_run(run_name="tags-demo"):
        mlflow.set_tag("stage", "experiment")          # ONE tag  -> None
        mlflow.set_tags({                               # MANY tags (dict) -> None
            "author": "sohan",
            "model_type": "logistic-regression",
            "release": "v1",
        })
        print("Tags set on the run.")

    # 🔎 Tags are SEARCHABLE — filter runs by a tag value (UI or API).
    # Query syntax:  tags.<key> = '<value>'
    results = mlflow.search_runs(
        experiment_names=["logging-demo"],
        filter_string="tags.author = 'sohan'",
    )
    print(f"search_runs found {len(results)} run(s) with tag author='sohan'.")


if __name__ == "__main__":
    demo_tags()
