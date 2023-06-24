class Table:
    
    def __init__(self, column: int):
        self.id_counter = 0
        self.rows = dict() # id -> Row (List[str])
        
        
    def insert(self, row: List[str]) -> None:
        self.id_counter += 1
        self.rows[self.id_counter] = row
        
        
    def delete(self, rowId: int) -> None:
        if rowId in self.rows:
            del self.rows[rowId]
    
    
    def select(self, rowId: int, columnId: int) -> str:
        if rowId in self.rows:
            return self.rows[rowId][columnId - 1]
        return None
    
        
class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = dict()
        for name, column in zip(names, columns):
            self.tables[name] = Table(column)

            
    def insertRow(self, name: str, row: List[str]) -> None:
        self.tables[name].insert(row)

        
    def deleteRow(self, name: str, rowId: int) -> None:
        self.tables[name].delete(rowId)
        

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name].select(rowId, columnId)
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)