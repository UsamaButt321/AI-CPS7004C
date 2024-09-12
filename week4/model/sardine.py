from week4.model.agent import Agent
from week4.controller.config import MAX_SARDINE_ENERGY


class Sardine(Agent):

    def __init__(self, location):
        super().__init__(location, MAX_SARDINE_ENERGY)

    def act(self, environment):
        pass