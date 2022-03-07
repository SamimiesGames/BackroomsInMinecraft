from abc import ABC, abstractmethod
from dataclasses import dataclass

from backrooms.utils.randomizers import chance


@dataclass
class AGenerator(ABC):
    weights: dict[float, int]
    resolution: tuple[int, int]

    @abstractmethod
    def to_matrix(self) -> list:
        ...

    @property
    @abstractmethod
    def weight(self) -> list[int, float]:
        ...

    @property
    @abstractmethod
    def row(self) -> list:
        ...


@dataclass
class Generator(AGenerator):
    def to_matrix(self) -> list:
        matrix = []

        for y in range(self.resolution[1]):
            matrix.append(self.row)

        return matrix

    @property
    def row(self) -> list:
        row = []

        for x in range(self.resolution[0]):
            row.append(self.weight)

        return row

    @property
    def weight(self):
        wt = 0
        for likelyhood, value in self.weights.items():
            if chance(likelyhood):
                wt = value
                break

        return wt






