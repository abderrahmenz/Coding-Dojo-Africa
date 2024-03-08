class user:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    def display_info(self):
        print(f"first_name:{self.first_name}\n last_name:{self.last_name}")
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200   
    def spend_points(self, amount) :
        if amount<self.gold_card_points:
            self.gold_card_points = self.gold_card_points-amount




man =  user("jack", "smaith","jack@gmail.com", 23)
man.display_info()
man.enroll()
print(man.gold_card_points)
player_1 = user("messi","andres","messi@gmail.com",37)
player_2 = user("cristiano","ronaldo","cristiano@gmail.com",39)
man.spend_points(50)
player_1.enroll()
player_2.enroll()
player_1.spend_points(80)
man.display_info()
player_1.display_info()
player_2.display_info()