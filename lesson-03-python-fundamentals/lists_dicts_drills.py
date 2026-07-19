"""Lists & dicts drills — professional version (return, not print)."""

# ---------- functions: they COMPUTE and RETURN ----------

def first_and_last(nums):
    """Return a tuple of the first and last items."""
    return nums[0], nums[-1]

def count_good(scores, threshold=0.80):
    """Return how many scores meet the threshold."""
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count

def good_scores(scores, threshold=0.80):
    """Return a list of scores that meet the threshold."""
    result = []                       # not 'list' — that's a built-in
    for score in scores:
        if score >= threshold:
            result.append(score)
    return result

def best(models):
    """Return the NAME of the highest-scoring model."""
    best_name = None
    best_score = -1
    for name, score in models.items():
        if score > best_score:
            best_score = score
            best_name = name
    return best_name

def worst(models):
    """Return the NAME of the lowest-scoring model."""
    worst_name = None
    worst_score = 2.0
    for name, score in models.items():
        if score < worst_score:
            worst_score = score
            worst_name = name
    return worst_name                 # NAME, not score (D5 fix)

# ---------- main block: it PRINTS ----------

if __name__ == "__main__":
    nums = [4, 8, 15, 16, 23, 42]
    scores = [0.7, 0.95, 0.88, 0.6]
    models = {"a": 0.81, "b": 0.77, "c": 0.90}

    low, high = first_and_last(nums)
    print(f"First: {low}, Last: {high}")
    print(f"Good count: {count_good(scores)}")
    print(f"Good scores: {good_scores(scores)}")
    print(f"Best model: {best(models)}")
    print(f"Worst model: {worst(models)}")

    # D6 — loop and format
    for name, score in models.items():
        print(f"{name} scored {score * 100:.1f}%")

    # D7 — add a key
    config = {"epochs": 10, "lr": 0.001}
    config["batch_size"] = 32
    print(config)
