from typing import List
from entity import Surface
from menu import Menu
from level import Level

class Game:
    def __init__(self, window: Surface):
        self.window: Surface = window
        self.menu: Menu = Menu(window=self.window)
        self.levels: List[Level] = [Level(window=self.window, name="Level 1")]

    def run(self) -> None:
        pass