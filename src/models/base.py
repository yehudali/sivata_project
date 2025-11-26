from models.house import House

class Base:
    def __init__(self, base_name: str):
        self.base_name=base_name
        self.houses=[]

    def add_house(self,house: House):
        self.houses.append(house)

    def remuve_house(self,house_num:int ):
        for i in self.houses:
            if i.house_num == house_num:
                self.houses.remove(i)
    

# class Base:
#     def __init__(self, base_name: str):
#         self.base_name=base_name
#         self.houses=list[hash]
#         self.rooms=list[Room]