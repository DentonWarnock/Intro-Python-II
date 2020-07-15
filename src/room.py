# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items = []):
    self.name = name 
    self.description = description
    self.items = items
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None
    
    
  def __str__(self):
    return_string = (f"\n{self.name}")
    return_string += f"\n- - - - - - - - - - - - - - - - -"
    return_string += f"\n{self.description}"
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
      
      
  