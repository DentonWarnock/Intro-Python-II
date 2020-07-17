# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, starting_room, items = []):
    self.name = name
    self.current_room = starting_room
    self.items = items
    
  def __str__(self):
    return f"{self.name} is in the {self.current_room}"
  
  def move(self, direction):     
    if getattr(self.current_room, f"{direction}_to") is not None:
      self.current_room = getattr(self.current_room, f"{direction}_to")
      print(self.current_room)
    else:
      print("\nYou shall not pass, try again!")
  
  def print_inventory(self):
    return_string = ""
    if len(self.items) > 0:
      print("You are holding: ")    
      for item in self.items:      
        return_string += f"\n{item.name}"
    else:
      return_string = "You're not carrying any items."
    return return_string
    
  def item_names(self):
    names = [item.name for item in self.items]
    return names
        
  def take_item(self, item_name):
    for index, i in enumerate(self.current_room.item_names()):
      if i == item_name:
        print(f"You have picked up the {item_name}!")
        item = self.current_room.items[index]
        self.items.append(item)
        self.current_room.take_item(item)     
    
    
  def drop_item(self, item_name):
    for index, i in enumerate(self.item_names()):      
      if i == item_name:
        print(f"You have dropped the {item_name}!")
        item = self.items[index]
        self.items.remove(item)
        self.current_room.drop_item(item)   
        
  def has_item(self, item_name):
    for i in self.item_names():
      if i == item_name:
        return True
      else:
        return False

