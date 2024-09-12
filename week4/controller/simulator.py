import time
import random

from week4.controller.config import (OCEAN_WIDTH,
                                     OCEAN_HEIGHT,
                                     SHARK_CREATION_PROBABILITY,
                                     SARDINE_CREATION_PROBABILITY)
from week4.model.location import Location
from week4.model.ocean import Ocean
from week4.model.sardine import Sardine
from week4.model.shark import Shark
from week4.view.tui import Tui


class Simulator:

    def __init__(self):
        self.__ocean = Ocean(OCEAN_WIDTH, OCEAN_HEIGHT)
        self.__tui = Tui()
        self.__agents = []
        self.__populate()

        shark_location = Location(5, 5)
        shark = Shark(shark_location)
        self.__ocean.set_agent(shark, shark_location)
        self.__agents.append(shark)

        sardine_location = Location(6, 6)
        sardine = Sardine(sardine_location)
        self.__ocean.set_agent(sardine, sardine_location)
        self.__agents.append(sardine)

    def __populate(self):
        for row in range(OCEAN_HEIGHT):
            for col in range(OCEAN_WIDTH):
                probability = random.random()
                if probability <= SHARK_CREATION_PROBABILITY:
                    agent_location = Location(col, row)
                    agent = Shark(agent_location)
                    self.__ocean.set_agent(agent, agent_location)
                    self.__agents.append(agent)
                elif probability <= SARDINE_CREATION_PROBABILITY:
                    agent_location = Location(col, row)
                    agent = Sardine(agent_location)
                    self.__ocean.set_agent(agent, agent_location)
                    self.__agents.append(agent)

    def run(self):
        self.__tui.display_environment(self.__ocean)

        while True:
            # make all the agents act
            for agent in self.__agents:
                potential_baby = agent.act(self.__ocean)
                if potential_baby:
                    self.__agents.append(potential_baby)

                agent.act(self.__ocean)

            # display updated environment
            self.__tui.display_environment(self.__ocean)

            # remove dead agents
            dead_agents = []
            for agent in self.__agents:
                if agent.get_energy() == 0:
                    dead_agents.append(agent)

            self.__agents = [agent for agent in self.__agents if agent not in dead_agents]

            # sleep for a short while
            time.sleep(1)


if __name__ == "__main__":
    sim = Simulator()
    sim.run()