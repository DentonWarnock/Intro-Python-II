# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, starting_room):
    self.name = name
    self.current_room = starting_room
    
  def __str__(self):
    return f"{self.name} is in the {self.current_room}"
  
  def move(self, direction):     
    if getattr(self.current_room, f"{direction}_to") is not None:
      self.current_room = getattr(self.current_room, f"{direction}_to")
    else:
      print("\nYou shall not pass, try again!")

