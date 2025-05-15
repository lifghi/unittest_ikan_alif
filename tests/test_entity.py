import unittest
from entities.fish import Fish

class TestFishEntity(unittest.TestCase):
    def test_create_fish(self):
        fish = Fish(name="Ikan Koi", jenis="Hias", perairan="Air Tawar")
        self.assertEqual(fish.name, "Ikan Koi")
        self.assertEqual(fish.jenis, "Hias")
        self.assertEqual(fish.perairan, "Air Tawar")

    def test_fish_equality(self):
        fish1 = Fish(name="Ikan Koi", jenis="Hias", perairan="Air Tawar")
        fish2 = Fish(name="Ikan Koi", jenis="Hias", perairan="Air Tawar")
        self.assertEqual(fish1, fish2)

    def test_fish_repr(self):
        fish = Fish(name="Ikan Lele", jenis="Konsumsi", perairan="Air Tawar")
        self.assertIn("Ikan Lele", repr(fish))