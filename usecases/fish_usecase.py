# usecases/fish_usecase.py
from interface.fish_repository import FishRepository
from entities.fish import Fish
from typing import List, Optional

class FishUseCase:
    def __init__(self, repo: FishRepository):
        self.repo = repo

    def browse_fishes(self) -> List[Fish]:
        return self.repo.get_all()

    def read_fish(self, index: int) -> Optional[Fish]:
        return self.repo.get(index)

    def add_fish(self, name: str, jenis: str, perairan: str) -> bool:
        return self.repo.add(Fish(name=name, jenis=jenis, perairan=perairan))

    def edit_fish(self, index: int, name: str, jenis: str, perairan: str) -> bool:
        old_fish = self.repo.get(index)
        if not old_fish:
            return False
        # Jika input kosong, pakai data lama
        new_fish = Fish(
            name=name if name else old_fish.name,
            jenis=jenis if jenis else old_fish.jenis,
            perairan=perairan if perairan else old_fish.perairan
        )
        return self.repo.update(index, new_fish)

    def delete_fish(self, index: int) -> bool:
        return self.repo.delete(index)
