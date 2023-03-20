"""
This is an abstract class for car engines
"""

from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self):
        return

    @abstractmethod
    def needs_service(self):
        pass
