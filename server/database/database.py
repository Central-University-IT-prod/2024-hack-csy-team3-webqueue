import sqlite3 as sql
from interface import DatabaseTableInterface
from typing import Any

class DatabaseTable(DatabaseTableInterface):
    __database: sql.Connection
    __table: str

    def __init__(self, filePath: str, tableName: str):
        """
        Реализация sql в интерфейсном формате.
        """
        self.__database = sql.connect(filePath)
        self.__databaseEditor = self.__database.cursor()
        self.__table = tableName

    def create(self, tableProperties: str):
        self.__databaseEditor.execute(f"CREATE TABLE IF NOT EXISTS {self.__table} ({tableProperties})")
        self.__database.commit()

    def insert(self, properties: 'tuple[str]', values: 'tuple[Any]'):
        strProperties = ""
        flagQuestions = "("
        for prop in properties:
            strProperties = strProperties + prop + ", "
            flagQuestions = flagQuestions + "?, "

        strProperties = strProperties[:len(strProperties)-2]
        flagQuestions = flagQuestions[:len(flagQuestions)-2] + ")"

        self.__databaseEditor.execute(f"INSERT INTO {self.__table} ({strProperties}) VALUES {flagQuestions}", values)
        self.__database.commit()

    def get(self, propertiesToGet: 'tuple[str]', condition: str = "", conditionData: 'tuple[Any]' = ()):
        strProperties = ""
        for prop in propertiesToGet:
            strProperties = strProperties + prop + ","

        strProperties = strProperties[:len(strProperties)-1]
        if(condition != ""):
            self.__databaseEditor.execute(f"SELECT {strProperties} FROM {self.__table} WHERE {condition}", conditionData)
        else:
            self.__databaseEditor.execute(f"SELECT {strProperties} FROM {self.__table}")

        information = self.__databaseEditor.fetchall()
        return information

    def update(self, propertyToSet: str, pointer: str, propertyValues: 'tuple[Any]'):
        self.__databaseEditor.execute(f"UPDATE {self.__table} SET {propertyToSet} = ? WHERE {pointer} = ?", propertyValues)
        self.__database.commit()

    def delete(self, property: str, value: Any):
        self.__databaseEditor.execute(f"DELETE FROM {self.__table} WHERE {property} = ?", (value, ))
        self.__database.commit()

    def endWork(self):
        self.__database.close()
