def forward_chaining(rules, facts, goal):
    """
    Forward Chaining Algorithm

    :param rules: List of rules in form (conditions, conclusion)
                  Example: [(["A", "B"], "C"), (["C"], "D")]
    :param facts: Initial set of known facts
                  Example: {"A", "B"}
    :param goal: The fact we want to derive
    :return: True if goal is reached, False otherwise
    """
    inferred = set(facts)  # copy initial facts
    applied_rules = set()  # rules already used

    while True:
        new_fact_added = False

        for i, (conditions, conclusion) in enumerate(rules):
            if i not in applied_rules and all(cond in inferred for cond in conditions):
                # Rule is applicable
                inferred.add(conclusion)
                applied_rules.add(i)
                new_fact_added = True
                print(f"Applied Rule {i+1}: {conditions} -> {conclusion}")
                print(f"Current Facts: {inferred}")

                if conclusion == goal:
                    print(" Goal reached!")
                    return True

        if not new_fact_added:
            break

    print(" Goal not reached.")
    return False


# Example Knowledge Base
rules = [
    (["A", "B"], "C"),  # Rule1: If A and B then C
    (["C"], "D"),       # Rule2: If C then D
    (["D"], "E")        # Rule3: If D then E
]

facts = {"A", "B"}  # Initial facts
goal = "E"          # Goal to prove

# Run Forward Chaining
result = forward_chaining(rules, facts, goal)
print("Result:", result)