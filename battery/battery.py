"""
This is an abstract class for all batteries
"""

from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self):
        return

    @abstractmethod
    def needs_service(self):
        pass
