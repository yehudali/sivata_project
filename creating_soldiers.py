from .src.models.soldiers import Soldiers


def creat_obj_by_file(row_file)->list[Soldiers]:
    list_Soldier=[]
    for i in range(len(row_file)):
        soldier_obj=Soldiers(row_file[i][0],row_file[i][1],row_file[i][2],row_file[i][3],row_file[i][4],row_file[i][5]):
        list_Soldier.append(soldier_obj)
    return list_Soldier