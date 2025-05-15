# interface/fish_repository.py
from abc import ABC, abstractmethod
from entities.fish import Fish
from typing import List, Optional

class FishRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Fish]:
        pass

    @abstractmethod
    def get(self, index: int) -> Optional[Fish]:
        pass

    @abstractmethod
    def add(self, fish: Fish) -> bool:
        pass

    @abstractmethod
    def update(self, index: int, fish: Fish) -> bool:
        pass

    @abstractmethod
    def delete(self, index: int) -> bool:
        pass
