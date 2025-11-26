from .room import Room

class House:
    def __init__(self,house_num:int=0,num_rooms:int=0 ):
        self.house_num=house_num
        self.room_list=[]
        
        for room in range(1,num_rooms+1):
            room_obj = Room(room)
            self.add_room(room_obj)

    def add_room(self,room: Room):
        self.room_list.append(room)

    def remuve_room(self,room_number:int ):
        for i in self.room_list:
            if i.room_number == room_number:
                self.room_list.remove(i)


            