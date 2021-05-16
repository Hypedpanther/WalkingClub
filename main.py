import csv

class member():
    def __init__(self,firstname,surname,distance):
        self.firstname = firstname
        self.surname = surname
        self.distance = distance

def get_data():
    members = []
    with  open("members-walk.txt", "r") as file:
        for line in csv.reader(file):
            members.append(member(line[0], line[1],float(line[2])))
    
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
            with open("winners.txt", "a") as f:
                f.writelines(members[index].firstname + " " + members[index].surname + "\n")




def main():
    members = get_data()
    furthest_distance = find_furthest(members)
    find_winners(members, furthest_distance)
if __name__ == "__main__":
    main()