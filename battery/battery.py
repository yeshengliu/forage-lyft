"""
This is an interface for batteries
"""

from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass
