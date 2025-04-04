from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from src.support.entities.base_class import BaseClass

@dataclass
class IBaseRepository (ABC):

    @abstractmethod
    def get(self, id: int) -> BaseClass:
        raise NotImplementedError()

    @abstractmethod
    def get_all(self) -> List[BaseClass]:
        raise NotImplementedError()

    @abstractmethod
    def exists(self, id: int, only_active: bool = False) -> bool:
        raise NotImplementedError()