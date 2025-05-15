import unittest
from infrastructure.in_memory_fish_repo import InMemoryFishRepository
from entities.fish import Fish

class TestInMemoryFishRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryFishRepository()
        self.fish1 = Fish("Ikan Koi", "Hias", "Air Tawar")
        self.fish2 = Fish("Ikan Cupang", "Hias", "Air Tawar")
        self.repo.add(self.fish1)
        self.repo.add(self.fish2)

    def test_get_all(self):
        fishes = self.repo.get_all()
        self.assertEqual(len(fishes), 2)

    def test_add_duplicate(self):
        result = self.repo.add(Fish("Ikan Koi", "Hias", "Air Tawar"))
        self.assertFalse(result)

    def test_delete(self):
        self.assertTrue(self.repo.delete(1))
        self.assertFalse(self.repo.delete(10))

    def test_update(self):
        new_fish = Fish("Ikan Mas", "Konsumsi", "Air Tawar")
        self.assertTrue(self.repo.update(0, new_fish))
        self.assertEqual(self.repo.get(0).name, "Ikan Mas")
        self.assertFalse(self.repo.update(10, new_fish))

    def test_get(self):
        self.assertEqual(self.repo.get(0).name, "Ikan Koi")
        self.assertIsNone(self.repo.get(99))