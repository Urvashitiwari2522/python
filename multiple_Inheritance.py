class Father:
  def skills(self):
     print("Gardening, Programming")
class Mother:
  def hobbies(self):
    print("Cooking, Painting")
class Child(Father, Mother):
  def own_skills(self):
    print("Gaming, Dancing")
c = Child()
c.skills()      # Inherited from Father
c.hobbies()     # Inherited from Mother
c.own_skills()  # Own method