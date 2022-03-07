from abc import ABC, abstractmethod
from dataclasses import dataclass

import random

from backrooms.utils.randomizers import chance


@dataclass
class AGenerator(ABC):
    weights: dict[float, int]
    resolution: tuple[int, int]

    @abstractmethod
    def to_matrix(self) -> list:
        ...

    @abstractmethod
    @property
    def weight(self) -> list[int, float]:
        ...

    @abstractmethod
    @property
    def row(self) -> list:
        ...


@dataclass
class Generator(AGenerator):
    def to_matrix(self) -> list:
        matrix = [[self.row] * self.resolution[0]]

        return matrix

    @property
    def row(self) -> list:
        row = []

        for x in range(self.resolution[1]):
            row.append(self.weight)

        return row

    @property
    def weight(self):
        wt = 0
        for index, weight in enumerate(self.weights):
            key, value = weight

            if chance(key):
                wt = value

        return wt






