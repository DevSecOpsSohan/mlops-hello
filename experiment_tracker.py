def accuracy_percent(score):
    """"""
    return f"{score * 100:.1f}%"

def best_run(experiments):
    """Return the name of the run with the highest score."""
    best_name = None
    best_score = -1
    for name, score in experiments.items():   # .items() gives BOTH key and value
        if score > best_score:
            best_score = score
            best_name = name
    return best_name
    

def passed_threshold(accuracy):
    """Decide what to do with a model based on its accuracy."""
    if accuracy >= 0.90:
        return "Deploy ✅"
    elif accuracy >= 0.75:
        return "Needs review ⚠️"
    else:
        return "Do not deploy ❌"


def experiment(model_name, experiments):
    """Print a experiment report for a model given a list of accuracy scores."""
    scores = experiments.values()
    print(scores)

    best = max(scores)
    average = sum(scores) / len(scores)

    print(f"Avg:   {accuracy_percent(average)}")
    print(f"Best:  {best_run(experiments)}")
    print(f"Decision: {passed_threshold(best)}")

if __name__ == "__main__":
    experiments = {"run1": 0.88, "run2": 0.94, "run3": 0.91}
    experiment("experiment", experiments)
