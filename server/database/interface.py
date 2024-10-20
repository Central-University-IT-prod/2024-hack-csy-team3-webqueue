from abc import ABC
from abc import abstractmethod
from typing import Any

class DatabaseTableInterface(ABC):
    def __init__(self, filePath: str, tableName: str):
        pass

    @abstractmethod
    def create(self, tableProperties: str):
        pass

    @abstractmethod
    def insert(self, properties: 'tuple[str]', values: 'tuple[str]'):
        pass

    @abstractmethod
    def get(self, propertiesToGet: 'tuple[str]', condition: str, conditionData: 'tuple[str]'):
        pass

    @abstractmethod
    def update(self, propertyToSet: str, pointer: str, propertyValues: 'tuple[str]'):
        pass

    @abstractmethod
    def delete(self, property: str, value: str):
        pass

    @abstractmethod
    def endWork(self):
        pass
