# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items = []):
    self.name = name 
    self.description = description    
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None   
    self.items = items 
    
  def __str__(self):
    return_string = (f"\n{self.name}")
    return_string += f"\n- - - - - - - - - - - - - - - - -"
    return_string += f"\n{self.description}"
    return_string += f"\nIn this room you see: {self.print_room_items()}"
    return_string += "\nPlease choose a direction to travel: "
    return_string += f"\nAvailable Paths: {self.get_exits_string()}"    
    return return_string
  
  def get_exits_string(self):
    exits = []
    if self.n_to is not None:
      exits.append("n - north")
    if self.s_to is not None:
      exits.append("s - south")
    if self.e_to is not None:
      exits.append("e - east")
    if self.w_to is not None:
      exits.append("w - west")
    return exits
  
  def item_names(self):
    names = [item.name for item in self.items]
    return names
 
  def drop_item(self, item_name):
    self.items.append(item_name)
   
  def take_item(self, item):    
    self.items.remove(item)
   
  def print_room_items(self): 
    return_string = ""
    if len(self.items) > 0:  
      for i in self.items:
        return_string += (f"\n{i}")
    else:
      return_string = "no items to pickup..."
    return return_string
    
  def has_item(self, item_name):    
    for i in self.item_names():
      if i == item_name:
        return True
      else:
        return False
      
      
  