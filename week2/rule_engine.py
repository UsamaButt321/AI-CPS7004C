class RuleEngine():
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rules(self, input_value):
        for condition, result in self.rules:
            if condition(input_value):
                return result
        return "Default"

engine = RuleEngine()
engine.add_rule(lambda x: x < 5, "Very Low")
engine.add_rule(lambda x: 5 <= x < 10, "Low")
engine.add_rule(lambda x: 10 <= x < 20, "Medium")

result = engine.apply_rules(15)
print(result)  # Output: Medium