from entity import Entity, Surface, Rect
from player import Player
from enemy import Enemy
from background import Background

class EntityFactory:
    def get_entity(self, entity_type: str) -> Entity:
        if entity_type.lower() == "player":
            return Player(name="Player", surf=Surface(), rect=Rect())
        elif entity_type.lower() == "enemy":
            return Enemy(name="Enemy", surf=Surface(), rect=Rect())
        elif entity_type.lower() == "background":
            return Background(name="Background", surf=Surface(), rect=Rect())
        else:
            raise ValueError(f"Tipo de entidade desconhecido: {entity_type}")