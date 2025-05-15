# entities/fish.py
from dataclasses import dataclass

@dataclass
class Fish:
    name: str
    jenis: str
    perairan: str
