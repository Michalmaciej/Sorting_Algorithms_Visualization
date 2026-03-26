from abc import ABC, abstractmethod

class BaseSort(ABC):
    def __init__(self, numbers):
        self.numbers = numbers.copy()
        self.elapsed = None
    
    @abstractmethod
    def sort(self):
        #sorting and returning sorted list measuring time
        pass

    @abstractmethod    
    def sort_gen(self):
        #generating yield for animation
        pass

    @property
    def name(self) -> str:
        return self.__class__.__name__
    
    @property
    @abstractmethod
    def time_complexity(self) -> str:
        pass

    @property
    @abstractmethod
    def space_complexity(self) -> str:
        pass

