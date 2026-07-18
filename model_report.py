"""A tiny model-evaluation report — Lesson 03 practice."""


def accuracy_percent(score):
    """Convert a 0-1 score into a readable percentage string."""
    return f"{score * 100:.1f}%"


def is_improving(scores):
    """Return True if the last score is higher than the first."""
    return scores[-1] > scores[0]


def deployment_decision(accuracy):
    """Decide what to do with a model based on its accuracy."""
    if accuracy >= 0.90:
        return "Deploy ✅"
    elif accuracy >= 0.75:
        return "Needs review ⚠️"
    else:
        return "Do not deploy ❌"


def report(model_name, scores):
    """Print a small report for a model given a list of accuracy scores."""
    best = max(scores)
    average = sum(scores) / len(scores)
    worst = min(scores)

    print(f"Model: {model_name}")
    print(f"Runs:  {len(scores)}")
    print(f"Best:  {accuracy_percent(best)}")
    print(f"Avg:   {accuracy_percent(average)}")
    print(f"Worst: {accuracy_percent(worst)}")
    print(f"Improving: {is_improving(scores)}")
    print(f"Decision: {deployment_decision(best)}")


if __name__ == "__main__":
    experiment_scores = [0.88, 0.91, 0.94, 0.89]
    report("fraud-detector", experiment_scores)
