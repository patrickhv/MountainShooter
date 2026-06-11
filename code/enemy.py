from entity import Entity, Surface, Rect

class Enemy(Entity):
    def __init__(self, name: str, surf: Surface, rect: Rect):
        super().__init__(name, surf, rect)

    def move(self) -> None:
        pass