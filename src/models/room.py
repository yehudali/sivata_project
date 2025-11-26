from .soldiers import Soldiers
class Room:
    def __init__(self, room_num:int=0):
        self.room_number = room_num
        self.tenant_list = []

    def add_soldier(self,soldier: Soldiers):
        self.tenant_list.append(soldier)

    def remuve_soldier(self,personal_number:int ):
        for i in self.tenant_list:
            if i.personal_number == personal_number:
                self.tenant_list.remove(i)