import random

# Initializing static dictionaries for each villain's weapon
# Sorted as: energy, damage, resources
gru_weapons = {
    "freeze gun": [50, 11, 100],
    "electric prod": [88, 18, 5],
    "mega magnet": [92, 10, 3],
    "kalman missile": [120, 20, 1]
}
vector_weapons = {
    "laser blaster": [40, 80, 100],
    "plasma grenades": [56, 13, 8],
    "sonic resonance cannon": [100, 22, 3]
}

# Initializing static dictionaries for each villain's shield
# Sorted as: energy, save, resources
gru_shields = {
    "energy projected barrier gun": [20, 0.4, 100],
    "selective permeability": [50, 0.9, 2]
}
vector_shields = {
    "energy net trap": [15, 0.32, 100],
    "quantum deflector": [40, 0.8, 3]
}


# Initialize a class for creating a new gadget for each villain at every round
class RandomGadget():
    def __init__(self, gru_weapon_dic, gru_shield_dic, vector_weapon_dic, vector_shield_dic):
        self.gru_weapon_dic = gru_weapon_dic
        self.gru_shield_dic = gru_shield_dic
        self.vector_weapon_dic = vector_weapon_dic
        self.vector_shield_dic = vector_shield_dic
        
        
        # Creating random weapon and shield
        self.gru_random_weapon = random.choice(list(self.gru_weapon_dic.items())) # type: ignore
        self.gru_random_shield = random.choice(list(self.gru_shield_dic.items())) # type: ignore
        self.vector_random_weapon = random.choice(list(self.vector_weapon_dic.items())) # type: ignore
        self.vector_random_sheild = random.choice(list(self.vector_shield_dic.items())) # type: ignore
        self.gru_weapon_property = self.gru_random_weapon[1]
        self.gru_sheild_property = self.gru_random_shield[1]
        self.vector_weapon_property = self.vector_random_weapon[1]
        self.vector_sheild_property = self.vector_random_sheild[1]
    def __str__(self):
        return f"gru Weapon: {self.gru_random_weapon}, gru Random Shield: {self.gru_random_shield}\n vector weapon: {self.vector_random_weapon}, vector sheild: {self.vector_random_sheild}"



#create a class for each opponent to present his initial values 
class VillianAttributes():
    def __init__(self, villian_weapon_resources = 0, villian_sheild_resources = 0):
        self.villian_weapon_resources = villian_weapon_resources
        self.villian_sheild_resources = villian_sheild_resources
    health = 100
    energy = 500
    winned_rounds = 0

#initialize an object for each opponent
gru_initial_values = VillianAttributes(RandomGadget.gru_weapon_property[2], RandomGadget.gru_sheild_property[2])
vector_initial_values = VillianAttributes(RandomGadget.vector_weapon_property[2], RandomGadget.vector_sheild_property[2])


#create a random choice to choose the starter attacker
starter_attacker = random.choice(["gru", "vector"])
print(f"{starter_attacker} starts attacking")

#creat an attack class that will be used in every attack action
class Battle(RandomGadget):
    def __init__(self, gru_weapon_property, gru_sheild_property, vector_weapon_property, vector_sheild_property):
        super().__init__(gru_weapon_property, gru_sheild_property, vector_weapon_property, vector_sheild_property)
    


        
    #create a function running the whole battle
    def run_battle():
        while not(gru_weapon_property[2] == 0 or vector_weapon_property[2] == 0 or gru_sheild_property[2] == 0 or vector_sheild_property[2] == 0):
            if gru_initial_values.health == 0 or vector_initial_values.health == 0 or gru_initial_values.energy == 0 or vector_initial_values.energy == 0:
                #if the attacker is vector
                if starter_attacker == "vector":
                    print("vector attacks gru")
                    gru_initial_values.health -= self.vector_weapon_property[1] * (1 - gru_sheild_property[1])
                    gru_initial_values.energy -= self.gru_sheild_property[0]
                    vector_initial_values.energy -= self.vector_weapon_property[0]
                    self.vector_weapon_property[2] -= 1
                    self.gru_sheild_property[2] -= 1
        
                #if the attacker is gru
                if starter_attacker == "gru":
                    print("gru attacks vector")
                    vector_initial_values.health -= gru_weapon_property[1] * (1 - vector_sheild_property[1])
                    vector_initial_values.energy -= vector_sheild_property[0]
                    gru_initial_values.energy -= gru_weapon_property[0]
                    gru_weapon_property[2] -= 1
                    vector_sheild_property[2] -= 1
            

            else:
                if gru_initial_values.health == 0 or gru_initial_values.energy == 0:
                    if gru_initial_values.health == 0:
                        print("gru's health is zero, vector wins the round")
                    else:
                        print("gru's energy is zero, vector wins the round")
                    vector_initial_values.winned_rounds += 1
                    if vector_initial_values.winned_rounds == 3:
                        print("gru wins the battle")
                        break
                else:
                    if vector_initial_values.health == 0:
                        print("vector's health is zero, gru wins the round")
                    else:
                        print("vector's energy is zero, gru wins the round")
                    gru_initial_values.winned_rounds += 1
                    if gru_initial_values.winned_rounds == 3:
                        print("vector wins the battle")
                        break
        

        if gru_weapon_property[2] == 0 or gru_sheild_property[2] == 0:
                    if gru_weapon_property[2] == 0:
                        print("the resources of gru's weapons ran out, vector wins the round")
                    else:
                        print("the resources of gru's sheilds ran out, vector wins the round")
                    vector_initial_values.winned_rounds += 1
                    if vector_initial_values.winned_rounds == 3:
                        print("gru wins the battle")
                        break
        else:
                    if vector_weapon_property[2] == 0:
                        print("the resources of vector's weapons ran out, gru wins the round")
                    else:
                        print("the resources of vector's sheilds ran out, gru wins the round")
                    gru_initial_values.winned_rounds += 1
                    if gru_initial_values.winned_rounds == 3:
                        print("vector wins the battle")
                        break



#initialize objects from created classes
random_gadget = RandomGadget(gru_weapons, gru_shields, vector_weapons, vector_shields)
battle = Battle()

#initialize the battle method to simulate the whole battle
battle.run_battle()
