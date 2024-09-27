class Familly:
    def __init__(self,add) -> None:
        self.add=add
class School:
    def __init__(self,id,level) -> None:
        self.id=id
        self.level = level

class Sports:
    def __init__(self,game) -> None:
        self.game=game

class Student(Familly,School,Sports):
    def __init__(self, add,id,level,game) -> None:
        School.__init__(self,id, level)
        Sports.__init__(self,game)
        super().__init__(add)