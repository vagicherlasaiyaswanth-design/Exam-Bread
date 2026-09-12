def generate_study_plan(topics):
    """
    topics should be a list of dictionaries:
    {
        "name": "Arrays",
        "frequency": 12,
        "weakness": 0.8
    }
    """

    # Calculate priority
    for topic in topics:
        topic["priority"] = topic["frequency"] * topic["weakness"]

    # Sort topics from highest priority to lowest
    topics.sort(key=lambda x: x["priority"], reverse=True)

    plan = {}

    for day in range(1, 8):
        plan[f"Day {day}"] = []

    # Assign important topics across 7 days
    for index, topic in enumerate(topics):
        day = (index % 5) + 1

        plan[f"Day {day}"].append({
            "topic": topic["name"],
            "activity": "Study and solve previous-year questions",
            "priority": round(topic["priority"], 2)
        })

    # Add revision and mock test
    plan["Day 6"].append({
        "topic": "Revision",
        "activity": "Revise important and weak topics"
    })

    plan["Day 7"].append({
        "topic": "Mock Test",
        "activity": "Attempt a timed PYQ mock test and analyze mistakes"
    })

    return plan


if __name__ == "__main__":
    sample_topics = [
        {
            "name": "Arrays",
            "frequency": 12,
            "weakness": 0.8
        },
        {
            "name": "Linked Lists",
            "frequency": 8,
            "weakness": 0.6
        },
        {
            "name": "Stacks",
            "frequency": 5,
            "weakness": 0.3
        },
        {
            "name": "Trees",
            "frequency": 10,
            "weakness": 0.7
        }
    ]

    study_plan = generate_study_plan(sample_topics)

    for day, tasks in study_plan.items():
        print(f"\n{day}:")
        for task in tasks:
            print(task)