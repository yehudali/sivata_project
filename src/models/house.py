from models.room import Room
class House:
    def __init__(self,house_num:int=0):
        self.house_num
        self.room_list=[]
    def add_room(self,room: Room):
        self.room.append(room)

    def remuve_room(self,room_number:int ):
        for i in self.room_list:
            if i.room_number == room_number:
                self.room.remove(i)


            