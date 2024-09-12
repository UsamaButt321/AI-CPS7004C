from abc import ABC, abstractmethod


class Environment(ABC):

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_agent(self, location):
        pass

    @abstractmethod
    def set_agent(self, agent, location):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_width(self):
        pass
