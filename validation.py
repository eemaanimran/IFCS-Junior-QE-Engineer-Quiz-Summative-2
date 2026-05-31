def validate_name(name):
    if len(name) == 0:
     return "Name Field cannot be left empty"
    
    if len(name) < 2 or len(name) > 30:
       return "Name must be between 2 and 30 characters"
    
    for character in name:
       if not character.isalpha():
          return "Name must only contain letters"
    
    return True