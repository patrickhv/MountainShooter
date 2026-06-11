from abc import ABC, abstractmethod

# Mocks para não quebrar a tipagem do Pygame
class Surface: pass
class Rect: pass

class Entity(ABC):
    def __init__(self, name: str, surf: Surface, rect: Rect):
        self.name: str = name
        self.surf: Surface = surf
        self.rect: Rect = rect

    @abstractmethod
    def move(self) -> None:
        pass