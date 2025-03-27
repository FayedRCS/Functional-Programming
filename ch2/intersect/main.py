def get_common_formats(formats1, formats2):
  
  #function takes in a list if integers, that needs to be converted to sets
  ## .intersection() method returns a new set containing only elements that are in both

  return set(formats1).intersection(set(formats2)) 