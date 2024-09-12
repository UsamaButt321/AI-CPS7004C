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
            'very cold': lambda temp: max(0, 1 - abs((temp - 0)/ 10)),
            'cold': lambda temp: max(0, 1 - abs((temp - 10)/ 10)),
            'warm': lambda temp: max(0, 1 - abs((temp - 20)/ 10)),
            'very warm': lambda temp: max(0, 1 - abs((temp - 30)/ 10)),
            'hot': lambda temp: max(0, 1 - abs((temp - 440)/ 10)),
        }

    def __fuzzify(self, temp):
        return {
            'very cold': self.memberships['very cold'](temp),
            'cold': self.memberships['cold'](temp),
            'warm': self.memberships['warm'](temp),
            'very warm': self.memberships['very warm'](temp),
            'hot': self.memberships['hot'](temp),
        }

    def __infer(self, antecedents):
        # Rule Evaluation: Apply rules to determine the consequent
        # TODO: write code here

    def __defuzzify(self, consequent):
        # Defuzzification: Choose the consequent with the highest aggregated degree of membership
        # TODO: write code here

    def evaluate(self, temperature):
        # Fuzzification for input temperature
        # TODO: write code here

        # Inference: Apply rules to determine the consequent
        # TODO: write code here

        # Defuzzification: Choose the final fan operation
        # TODO: write code here
