def validate_name(name):
    """
    Validates the users name. The name must not be empty, between 2 and 30 characters in length, and only contain alphabetic characters.
    It's parameter is the name entered by the user, and returns either a boolean of True or a string containing an error message.
    """

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
    """
    Validates a manually typed quiz answer, and checks that the answer field is not submitted empty.
    It's parameter is the answer submitted by the user and returns either a boolean of True or a string containing an error message.
    """

    answer = answer.strip()

    if len(answer) == 0:
     return "Answer Field cannot be left empty"
    
    return True

def validate_multiple_choice_answer(answer):
   """
   Validates a multiple choice answer selection, and ensures the user has selected an answer other than the default placeholder value. 
   It passes the answer selected from the dropdown menu and returns either a boolean of True or a string containing an error message.
   """

   if answer == "Select an Answer":
      return "Please Select an Answer"
   
   return True