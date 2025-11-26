from models.soldiers import Soldiers


def bubblesort(soldiers:list[Soldiers]):
     "Sorts lst in place and returns it."
     for passesLeft in range(len(soldiers)-1, 0, -1): #run from the end to the start
         for index in range(passesLeft):
             if soldiers[5][index] > soldiers[5][index + 1]:
                soldiers[5][index], soldiers[5][index + 1] = soldiers[5][index + 1], soldiers[5][index]
     return soldiers

# def order_soldiers_by-(soldiers:list[Soldiers])->list[Soldiers]:
#     for i in range(len(soldiers)):