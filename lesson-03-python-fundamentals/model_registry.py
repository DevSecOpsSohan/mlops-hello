"""Model registry — Lesson 03 Part A (v2)."""


def count_deployable(models, threshold=0.90):
    """Return how many models have accuracy >= threshold."""
    count = 0
    for name, score in models.items():
        if score >= threshold:
            count += 1
    return count


def deployable_names(models, threshold=0.90):
    """Return a list of model names that pass the threshold."""
    names = []
    for name, score in models.items():
        if score >= threshold:
            names.append(name)
    return names


def worst_model(models):
    """Return the name of the lowest-scoring model."""
    worst_name = None
    worst_score = 2.0
    for name, score in models.items():
        if score < worst_score:
            worst_score = score
            worst_name = name
    return worst_name


def registry_report(models):
    """Print a summary report of the model registry."""
    worst = worst_model(models)
    print(f"Total models:       {len(models)}")
    print(f"Deployable (>=90%): {count_deployable(models)}")
    print(f"Deployable names:   {deployable_names(models)}")
    print(f"Worst model:        {worst} ({models[worst] * 100:.1f}%)")


if __name__ == "__main__":
    models = {
        "logreg": 0.86,
        "random_forest": 0.93,
        "xgboost": 0.95,
        "neural_net": 0.71,
    }
    registry_report(models)
