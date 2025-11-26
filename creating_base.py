from src.models.base import Base
from src.models.house import House
from src.models.room import Room


def creating_base_homes_and_rooms(name:str,num_house:int, num_rooms:int):
    for i in range(1,num_rooms+1):
        house=House(i,num_rooms)
        base=Base(name,house)
    return base






# def Creating_homes_base(base:Base, num_house:int):
#     for house in range(1,num_house+1):
#         house = House(house)
#         base.add_house(house)
#     return base


# def reating_rooms_in_base_home(base:Base, num_room:int):
#     for  in range(1,num_room+1):
#             m_room=Room(room)
#             m_house.add_room(m_room)
#     return 

