def validate_name(name):

    name = name.strip()

    if len(name) == 0:
     return "Name Field cannot be left empty"
    
    if len(name) < 2 or len(name) > 30:
       return "Name must be between 2 and 30 characters"
    
    for character in name:
       if (not character.isalpha() or character == " "):
          return "Name must only contain letters"
    
    return True

def validate_answer(answer):

    answer = answer.strip()

    if len(answer) == 0:
     return "Answer Field cannot be left empty"
    
    return True

def validate_multiple_choice_answer(answser):
   return True