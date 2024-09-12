class FuzzySystem:
    def __init__(self):
        # Rules list
        self.rules = {
            'very cold': 'heat',
            'cold': 'heat',
            'warm': 'nothing',
            'very warm': 'cool',
            'hot': 'cool'
        }

        # Linguistic terms and membership functions
        self.memberships = {
            'very cold': lambda temp: max(0, 1 - abs((temp - 0) / 10)),
            'cold': lambda temp: max(0, 1 - abs((temp - 10) / 10)),
            'warm': lambda temp: max(0, 1 - abs((temp - 20) / 10)),
            'very warm': lambda temp: max(0, 1 - abs((temp - 30) / 10)),
            'hot': lambda temp: max(0, 1 - abs((temp - 40) / 10)),  # Fixed typo (440 -> 40)
        }

    def __fuzzify(self, temp):
        # Fuzzify the input temperature
        return {
            'very cold': self.memberships['very cold'](temp),
            'cold': self.memberships['cold'](temp),
            'warm': self.memberships['warm'](temp),
            'very warm': self.memberships['very warm'](temp),
            'hot': self.memberships['hot'](temp),
        }

    def __infer(self, antecedents):
        # Rule Evaluation: Find the rule with the highest membership degree
        # Apply the rule that has the highest membership degree in fuzzification
        max_membership = 0
        selected_rule = None
        for term, value in antecedents.items():
            if value > max_membership:
                max_membership = value
                selected_rule = self.rules[term]
        return selected_rule

    def __defuzzify(self, consequent):
        # In this case, defuzzification is simply returning the consequent from inference
        return consequent

    def evaluate(self, temperature):
        # Step 1: Fuzzification for input temperature
        fuzzy_values = self.__fuzzify(temperature)

        # Step 2: Inference - Apply rules to determine the consequent
        consequent = self.__infer(fuzzy_values)

        # Step 3: Defuzzification - Choose the final operation
        result = self.__defuzzify(consequent)

        return result


# Example usage
fuzzy_system = FuzzySystem()
temperature = 25  # Example input temperature
action = fuzzy_system.evaluate(temperature)
print(f"For a temperature of {temperature}°C, the system suggests to: {action}")
