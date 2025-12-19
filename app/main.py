from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health: int = health
        self.name: str = name
        self.hidden: bool = hidden
        Animal.alive.append(self) if self.health > 0 else None

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Carnivore):
            return
        if not target.hidden:
            target.health -= 50
            if target.health <= 0:
                Animal.alive.remove(target)
