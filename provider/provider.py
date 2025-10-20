from abc import ABC, abstractmethod

class Provider(ABC):

    @abstractmethod
    def fetch_data():
        """Get maket data"""
        pass