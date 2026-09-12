from study_plan import generate_study_plan

topics = [
    {
        "name": "Arrays",
        "frequency": 12,
        "weakness": 0.8
    },
    {
        "name": "Trees",
        "frequency": 10,
        "weakness": 0.7
    },
    {
        "name": "Stacks",
        "frequency": 5,
        "weakness": 0.3
    }
]

plan = generate_study_plan(topics)

assert len(plan) == 7
assert "Day 1" in plan
assert "Day 7" in plan

print("Study plan test passed successfully!")
print(plan)