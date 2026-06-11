from typing import List
from entity import Entity, Surface
from entity_factory import EntityFactory

class Level:
    def __init__(self, window: Surface, name: str):
        self.window: Surface = window
        self.name: str = name
        self.entity_list: List[Entity] = []

    def run(self) -> None:
        factory = EntityFactory()
        pass