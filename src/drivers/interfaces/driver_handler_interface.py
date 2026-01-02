from abc import ABC, abstractmethod

class IDriverHandler(ABC):
    @abstractmethod
    def standard_derivation(self, numbers: list[float]) -> float:
        ...
        
    @abstractmethod
    def variance(self, numbers: list[float]) -> float:
        ...