"""
This is an interface for car tires
"""
from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass
