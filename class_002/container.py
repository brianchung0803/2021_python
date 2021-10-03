def CountNames(givenarray):
    print(f"there are {len(givenarray)} names in the list.")

def ListNames(givenarray):
    # num = 0
    # for name in givenarray:
    #     num+=1
    #     print(f"{num}, {name}")
    # for num in range(len(givenarray)):
    #     print(f"{num+1}, {givenarray[num]}")

    for num, name in enumerate(givenarray):
        print(f"{num+1}, {name}")


####### list
list1 = ["brian","erik","calvin"]
# len() 有多少elements 
# CountNames(list1)
# ListNames(list1)

#append() 加一個element到最後
list1.append("tiff")
# CountNames(list1)
# ListNames(list1)

# list1.pop(0)
# print("\n")
# ListNames(list1)

list2 = ["dog","cat"]

# extend
list1.extend(list2)
# ListNames(list1)


#tuple
tuple1 = (1,2,3,4)
# CountNames(tuple1)
# ListNames(tuple1)

# tuple是唯讀

list1[0] = "BRIAN"
# ListNames(list1)


# tuple1[0] = 6 # forbidden
# ListNames(tuple1)

#dictionary
# key, value pair
# dict1 = {}
# dict1["brian"] = ["male", 178, 75, "MS"]
# dict1["erik"] = ["male", 182,76,"BC"]
# dict1["calvin"] = ["male", 186,76,"BC"]

# print(dict1["calvin"])

def AssignPower(dict1,hero_name,atk, mana, defend, health):
    dict1[hero_name]["ATK"] = atk
    dict1[hero_name]["MANA"] = mana
    dict1[hero_name]["DEF"] = defend
    dict1[hero_name]["HEALTH"] = health

def BuyItem(item):
    if(item=="sword"):
        return "ATK", 10
    elif(item == "blue crystal"):
        return "MANA", 20
    elif(item=="shield"):
        return "DEF", 15
    elif(item=="red crystal"):
        return "HEALTH", 30
    else:
        return None, None
    

# Heros ={}
# Heros["Garen"] = {}
# AssignPower(Heros, "Garen", 50, 0 , 200, 300)
# Heros["Darius"] = {}
# AssignPower(Heros, "Darius", 120, 150 , 130, 200)

# print(Heros["Garen"])
# power, add_ = BuyItem("red crystal")
# Heros["Garen"][power] += add_
# print(Heros["Garen"])

# set 不能有重複的element

# tuple2 = (1,1,1,1,1,1,2,2,2,2,3,4,5,6,7,8)
# print(tuple2)
# set1 = set(tuple2)
# print(set1)

# set1 = set()
# set1.add(1)
# set1.add(1)
# set1.add(1)

# set1.add(2)
# set1.add(2)

# set1.add(3)
# print(set1)

list1 = [1,1,1,1,1,2,2,2,2,3,4,5,6]
set1 = set(list1)
list1.append(3)
print(set1)


