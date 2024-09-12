class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if rule["condition"] in text.lower():
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."


# Example usage
rule_engine = RuleEngine()

# Add rules
rule_engine.add_rule("hello", "Hi there!")
rule_engine.add_rule("\bhow are you?\b", "I'm good thank you!")
rule_engine.add_rule("what's up?", "Just here to help you!")
rule_engine.add_rule("goodbye", "Goodbye!")

# Have conversation
while True:
    user_input = input("You: ")
    response = rule_engine.apply_rules(user_input)
    print(response)

    if user_input.lower() == "goodbye":
        break