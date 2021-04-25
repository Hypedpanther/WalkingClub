import csv


class member():
    def __init__(self,firstname,surname,distance):
        self.firstname = firstname
        self.surname = surname
        self.distance = distance

class cars():
    def __init__(self,make,year,transmission,fuel):
        self.make = make
        self.year. 
        # etc

class guns_simple():
    def __init__(self,
    stock,muzzle,foregrip,trigger,
    number_bullets,accuracy,fire_rate,recoil
    ):
        self.stock = stock
        self.muzzle = muzzle
        self.foregrip = foregrip
        self.trigger = trigger
        self.number_bullets = number_bullets
        self.accuracy = accuracy
        self.fire_rate = fire_rate
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil
        self.recoil = recoil

class physical_props():
    def __init__(self,stock,muzzle,foregrip,trigger):
        self.stock = stock
        self.muzzle = muzzle
        self.foregrip = foregrip
        self.trigger = trigger

class gun_stats():
    def __init__(self,number_bullets,accuracy,fire_rate,recoil):
        self.number_bullets = number_bullets
        self.accuracy = accuracy
        self.fire_rate = fire_rate
        self.recoil = recoil

class gun_stats_with_attachments(gun_stats):
    def __init__(self,number_bullets,accuracy,fire_rate,recoil,attachments):
        super.__init__(number_bullets,accuracy,fire_rate,recoil)
        self.attachments = attachments

class guns():
    def __init__(self,physical_props,gun_stats):
        self.physical_props = physical_props
        self.gun_stats = gun_stats






members = []


def get_data():
    input_file = open("members-walk.txt", "r")
    data = csv.reader(input_file)

    for line in data:
        members.append(member(line[0], line[1],float(line[2])))
    input_file.close()
    return members

def find_furthest(members):
    furthest_distance = members[0].distance
    for x in range(len(members)):
        if members[x].distance > furthest_distance:
            furthest_distance = members[x].distance
    print("The Furthest Distance walked:",furthest_distance,"miles")
    return furthest_distance

def find_winners(members, furthest_distance):
    print("\t\tWalked 70% of the furthest distance")
    for index in range (len(members)):
        if members[index].distance > 0.7*furthest_distance:
            print(members[index].firstname ,members[index].surname)
            output_file = open("winners.txt", "a")
            output_file.writelines(members[index].firstname + " " + members[index].surname + "\n")


OOP
    


members = get_data()
furthest_distance = find_furthest(members)
find_winners(members, furthest_distance)