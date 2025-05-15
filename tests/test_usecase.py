# Sudah sesuai, tidak perlu diubah banyak
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from usecases.fish_usecase import FishUseCase
from infrastructure.in_memory_fish_repo import InMemoryFishRepository

class TestFishUseCase(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryFishRepository()
        self.usecase = FishUseCase(self.repo)
        self.usecase.add_fish("Ikan Koi", "Hias", "Air Tawar")
        self.usecase.add_fish("Ikan Cupang", "Hias", "Air Tawar")

    def test_browse(self):
        result = self.usecase.browse_fishes()
        self.assertEqual(len(result), 2)

    def test_add(self):
        self.assertTrue(self.usecase.add_fish("Ikan Lele", "Konsumsi", "Air Tawar"))
        self.assertFalse(self.usecase.add_fish("Ikan Koi", "Hias", "Air Tawar"))

    def test_read(self):
        self.assertEqual(self.usecase.read_fish(0).name, "Ikan Koi")
        self.assertIsNone(self.usecase.read_fish(99))

    def test_edit(self):
        self.assertTrue(self.usecase.edit_fish(0, "Ikan Mas", "Konsumsi", "Air Tawar"))
        fish = self.usecase.read_fish(0)
        self.assertEqual(fish.name, "Ikan Mas")
        self.assertEqual(fish.jenis, "Konsumsi")
        self.assertEqual(fish.perairan, "Air Tawar")
        self.assertFalse(self.usecase.edit_fish(10, "Ikan Gurame", "Konsumsi", "Air Tawar"))

    def test_delete(self):
        self.assertTrue(self.usecase.delete_fish(1))
        self.assertFalse(self.usecase.delete_fish(10))