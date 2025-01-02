from abc import ABC, abstractmethod

"""Abstract class to enforce handlers to implement  load and save methods."""

class StorageInterface(ABC):
    @abstractmethod
    def load(self):
        """Load data from the source."""
        pass

    @abstractmethod
    def save(self, tasks):
        """Save tasks to the destination."""
        pass
