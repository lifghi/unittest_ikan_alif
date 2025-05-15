# infrastructure/in_memory_fish_repo.py
from interface.fish_repository import FishRepository
from entities.fish import Fish
from typing import List, Optional

class InMemoryFishRepository(FishRepository):
    def __init__(self):
        self.fishes: List[Fish] = []

    def get_all(self) -> List[Fish]:
        return self.fishes

    def get(self, index: int) -> Optional[Fish]:
        if 0 <= index < len(self.fishes):
            return self.fishes[index]
        return None

    def add(self, fish: Fish) -> bool:
        if fish.name not in [f.name for f in self.fishes]:
            self.fishes.append(fish)
            return True
        return False

    def update(self, index: int, fish: Fish) -> bool:
        if 0 <= index < len(self.fishes):
            self.fishes[index] = fish
            return True
        return False

    def delete(self, index: int) -> bool:
        if 0 <= index < len(self.fishes):
            del self.fishes[index]
            return True
        return False
