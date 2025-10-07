def backward_chaining(rules, facts, goal, depth=0):
    """
    Backward Chaining Algorithm

    :param rules: List of rules in form (conditions, conclusion)
                  Example: [(["A", "B"], "C"), (["C"], "D")]
    :param facts: Initial set of known facts
                  Example: {"A", "B"}
    :param goal: The fact we want to prove
    :param depth: For tracing recursion levels
    :return: True if goal is proven, False otherwise
    """
    indent = "  " * depth
    print(f"{indent}Trying to prove: {goal}")

    # If goal is already known
    if goal in facts:
        print(f"{indent} {goal} is a known fact.")
        return True

    # Check rules that conclude this goal
    applicable_rules = [rule for rule in rules if rule[1] == goal]

    if not applicable_rules:
        print(f"{indent} No rules to prove {goal}. Fails.")
        return False

    # Try each rule
    for conditions, conclusion in applicable_rules:
        print(f"{indent}Checking rule: {conditions} -> {conclusion}")

        # Assume this rule is true, now prove all its conditions
        success = True
        for condition in conditions:
            if not backward_chaining(rules, facts, condition, depth + 1):
                success = False
                break

        if success:
            print(f"{indent} Rule succeeded: {conditions} -> {goal}")
            return True

    print(f"{indent} Could not prove {goal}.")
    return False


# Example Knowledge Base
rules = [
    (["A", "B"], "C"),  # Rule1: If A and B then C
    (["C"], "D"),       # Rule2: If C then D
    (["D"], "E")        # Rule3: If D then E
]

facts = {"A", "B"}  # Initial known facts
goal = "E"          # Goal to prove

# Run Backward Chaining
result = backward_chaining(rules, facts, goal)
print("\nFinal Result:", result)