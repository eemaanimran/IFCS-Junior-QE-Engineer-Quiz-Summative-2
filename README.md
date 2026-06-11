# IFCS-Junior-QA-Engineer-Quiz-Summative-2

## Introduction 
As a test Automation Engineer at IBM, I work within a rigorous quality engineering environment, where efficient knowledge about testing practices, and high quality testing processes are vital for producing a successful UI testing outcomes from different environments. New joiners in the Quality Engineering practice should be able to recognise and apply these requirements where necessary to make meaningful contributions whilst adhering  to IBM's value of innovation and trust. However, onboarding of interns, apprentices, and regular employees can be challenging when it comes to understanding each newcomers current knowledge of Quality Engineering. Relying solely on induction sessions and early discussions may not be a consistent approach to understand a candidates knowledge during onboarding.

To understand each candidates initial understanding and knowledge of Quality Engineering, this Junior Quality Engineer Quiz provides a structured and consistent approach to assess foundational knowledge about Quality Engineering, with a focus towards newcomers of Automation Testing. This desktop application has been developed using Python and Tkinter, allowing recruiters to test candidates through multiple questions about Automation Testing and key testing concepts, which can be used during an application process or after onboarding to check understanding. 

This proposed Minimum Viable Product (MVP) has been designed to follow a professional Software Development process, including modular Python code, object-orientated programming principles and others. The application also implements CSV data storage to record the candidates name and answers, with no scoring system to allow assessors to analyse open ended answers when determining knowledge and understanding, creating a more subjective approach. Input validation has been implemented throughout the quiz as well, to ensure valid information is provided.

Overall, this quiz application supports IBM by improving visibility into candidate knowledge, allowing for more informed decisions during recruitment and onboarding of Automation Testers. 

## Design Section 
### GUI Design
The GUI for this proposed quiz was initially designed using Figma before starting development. This [designed prototype](https://www.figma.com/design/YEnZW1DAnGG0WgBUDgGgDz/Summative-2-Quiz-Prototype?node-id=0-1&p=f&t=TOqvNqTx2kkMrGuW-0) was done to visualise the user journey from start till end, and its navigation flow. This prototype has minimal graphical elements to soley focus on user navigation, and maintain simplicity as this quiz will be used in a professional environment. The main planned user journey consists of the home page, quiz questions, and the finishing page. This final prototype is shown in the screenshot below.  

<img width="1112" height="656" alt="image" src="https://github.com/user-attachments/assets/110013c1-a360-4f23-846c-2806c844aaf5" />

### Functional and Non-functional requirements
Below are tables listing each type of requirements for this Quiz App.
#### Functional Requirements
| ID  | Requirement |
|-----|-------------|
| FR1 | The quiz must validate that an answer has been submitted before moving onto the next question. |
| FR2 | The quiz must display one question at a time in a specificed order (e.g., Section 1, Section 2). |
| FR3 | The quiz must provide navigation buttons to move between pages. |
| FR4 | The system should record input data, including the users name, and answers in a csv file that can be accessed later on. |
#### Non-Functional Requirements
| ID  | Requirement |
|-----|-------------|
| NFR1 | The application should have clearly labelled input fields and buttons to support users with less technical expertise. |
| NFR2 |  |
| NFR3 |  |
| NFR4 |  |

### Tech Stack outline
Below are the features that were used to create this Quiz Application.
- [Python](https://www.python.org/) — Main programming language
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — Python library used to create the desktop GUI
- [csv](https://docs.python.org/3/library/csv.html) — Used for CSV data storage, and storing quiz responses
- [unittest](https://docs.python.org/3/library/unittest.html) — Used for automated unit testing for validation functions

### UML diagram
This class diagram displays the structure of the Quiz Application. The ```QEQuizApp``` class manages the user interface, question navigation, and recording results. This class is dependant on ```validation.py``` to validate user input and uses the question data stored in ```question.py``` for the quiz content.

## Development Section 
Following the completion of the initial prototype design and establishing technical requirements, the development of the quiz application became more manageable. This development process follows an organised design approach, involving the Codes structure, object-oriented design, GUI implementation, alongside input validation and logic for navigating questions. This section outlines the key features of the quiz application, including how different classes and functions work to ensure functionality.
### Code Structure
The application was designed using a modular, object‑oriented approach to improve code readability and separate different areas of functionality. For example, the quiz application has been separated into four different Python files.
<img width="307" height="63" alt="image" src="https://github.com/user-attachments/assets/35e2cf82-754e-4d4c-8027-73d4c55b7656" />
<img width="319" height="20" alt="image" src="https://github.com/user-attachments/assets/45b60d2b-24af-417a-a8e1-f1f8ae5a30a4" />
<img width="233" height="54" alt="image" src="https://github.com/user-attachments/assets/68ae824a-718e-4a4c-8b40-e951ef915c2a" />
#### main.py
<img width="961" height="596" alt="image" src="https://github.com/user-attachments/assets/4ba7afff-b056-435f-9b6b-cf19b1fde2df" />

The ```main.py``` module contains the primary application logic and GUI functionality using Tkinter. It's main class ```QEQuizApp``` contains the overall quiz navigation, including user interaction, switching questions, and transiting to different sections. This class also contains the creation of Tkinter widgets, including labels, buttons, frames, and drop down menus.

Object-oriented programming principles were also applied in this class including attributes like quiz frames (e.g, ```self.home_frame```) and Tkinter widgets (e.g., ```self.title```). This class also contains various methods, which will be discussed in more detail below. 

#### validation.py
<img width="1041" height="584" alt="image" src="https://github.com/user-attachments/assets/a6ac8c49-e5d6-45aa-816d-810c35e9f4ac" />

The validation.py file contains a set of validation functions for checking user input throughout the quiz. These functions ensure that all required fields are correctly completed before allowing the user to proceed to the next question or frame. Separating this logic from the main module not only improves modularity but also allows the functions to be tested independently through automated unit tests. The file contains three key validation functions. 

```
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
```

The ```validate_name``` function checks that the user's name contains only alphabetic characters and meets a minimum length of two to prevent invalid inputs such as numbers of empty values. 

```
def validate_answer(answer):

    answer = answer.strip()

    if len(answer) == 0:
     return "Answer Field cannot be left empty"
    
    return True
```

The ```validate_answer``` function ensures that manually typed answers aren't left blank by checking if the users input only has whitespaces.

```
def validate_multiple_choice_answer(answer):

   if answer == "Select an Answer":
      return "Please Select an Answer"
   
   return True
```

Lastly, the ```validate_multiple_choice_answer``` function verifies that a selection has been made by checking if the user has changed the default selected value. 

If any validation doesn't return True then the application will display an error message prompting the user to submit in answer correctly. This ensures that all data is collected appropriately.

#### question.py
The questions.py module was created to separate quiz content from the main application module. The quiz questions were stored using Python lists and dictionaries. Each section of the quiz was stored in a list, such as ```section_one``` and ```section_two```. Within each list, individual questions were stored as dictionaries with key-value pairs. Each question dictionary contains ```question``` representing the text displayed to the user, ```type``` which determines whether the questions were multiple choice or manually typed, and ```options``` stores multiple choice answers if applicable. An example of this is shown below with section one.
```section_one = [
    {
      "type": "manual_answer",
      "question": "What is the difference between functional and non-function testing in your own words?" 
    },
    {
        "type": "multiple_choice",
        "question": "What are test planning deliverables based off?",
        "options": [
            "Test Strategy",
            "Contract",
            "Exit Gates"
        ],
        "answer": "Test Strategy"
    },
    {
        "type": "multiple_choice",
        "question": "What does UAT stand for?",
        "options": [
            "User Access Testing",
            "User Acceptance Testing",
            "Unified Application Testing",
            "Utility Assessment Technology"
        ],
        "answer": "User Acceptance Testing"
    }
]
```
The reason for storing quiz questions separate from the main module is to ensure that questions were loaded dynamically into the GUI using ```question_index``` attribute. The ```type``` key pair is also essential, as it controls the type of Tkinter widget displayed for each question. For example, manually typed questions generated an Entry widget, whereas multiple choice questions would  load an Option Menu.

Storing questions separate also allows flexibility within the application's design. Questions can be updated easily without making any major changes to the application logic. If this were hardcoded into the main module, updates would take longer, as the corresponding  Tkinter widgets would also need to be adjusted. 

#### GUI Implementation
The GUI was developed using Tkinter. This quiz application consists of multiple frames that represent different stages of the user journey. This quiz contains the following frames: ```home_frame```, ```quiz_frame```. At the start, users are presented with the home page in ```home_frame``` where they enter their name before starting the quiz. After a valid name has been submitted, the home frame is destroyed in the method ```start_quiz()```and then replaced with the ```quiz_frame```. Using different frames helps present the user's journey as they navigate through each section of the quiz. 
Tkinter widgets are also widely used throughout the quiz. This involves labels, entry fields, buttons etc as shown in the examples below. 
```
def home_page(self):
   self.title = tk.Label (
       self.root,
       text ="Quality Engineering Quiz",
       font=("Arial", 40, "bold"),
       bg="#8ac5d4"
   )
   self.title.pack(pady=20)
```
```
self.name_input = tk.Entry(self.home_frame, width="50")
   self.name_input.pack(pady=10)
```
```
  def start_quiz(self):
    if self.name == None:
      self.error_message.config(text="Please submit your name first")
      return
    
    self.home_frame.destroy()
 
    self.quiz_frame.pack()
```
Using the ```questions.py``` module, Tkinter widgets are displayed based on the type of question defined in the dictionary using ```if``` statements. For example, manually entered answers create an Entry widget whereas multiple-choice questions will generate an Option Menu.

```
self.question_message.pack(pady=20)
    if question["type"] == "manual_answer":
      self.user_answer = tk.Entry (
        self.quiz_frame,
        width=50
      )
```
```
   elif question["type"] == "multiple_choice":
      self.selected_option = tk.StringVar()
      self.selected_option.set("Select an Answer")
      answer_selection = tk.OptionMenu(
        self.quiz_frame,
        self.selected_option,
        *question["options"]
```

As mentioned above, the use of dynamic widgets and Tkinter frames helps to improve the flexibility of the application, as new questions or changes to the GUI can be implemented with minimal impact to existing code.

#### Question Navigation Logic
The navigation of questions is controlled primarily through the ```next_question()``` method and the ```question_index``` attribute. This attribute tracks the current position of the user within the quiz section and is incremented after a valid answer is submitted.
```self.question_index += 1```

Before moving to the next question, the application validates the user’s response using the corresponding validation function. This process occurs in the ```next_question()``` method as shown below.
```
 def next_question(self):
    question = self.current_section[self.question_index]
    self.error_message= tk.Label(
    self.quiz_frame,
    text="",
    fg="red",
    font=("Arial", 14),
    bg="#8ac5d4"
    )
    if question["type"] == "manual_answer":
      answer = self.user_answer.get()
      validation = validate_answer(answer)
      if validation != True:
        self.error_message.config(text=validation)
        self.error_message.pack()
        return
    elif question["type"] == "multiple_choice":
        answer = self.selected_option.get()
        validation = validate_multiple_choice_answer(answer)
        if validation != True:
          self.error_message.config(text=validation)
          self.error_message.pack()
```
After completing the final question, the application switches from ```section_one``` to ```section_two``` by updating the ```current_section``` attribute and resetting the index to zero. This method allows the same logic to be reused for multiple sections without repeating code. As each button widget has the ```next_question()``` method defined through its command attribute, so the user can navigate to the next part.
```
 if self.question_index < len(self.current_section):
        for widget in self.quiz_frame.winfo_children():
          widget.destroy()
        if self.current_section == section_one:
          section_title = "Section 1: Testing Fundamentals"
        else:
          section_title = "Section 2: Automation Knowledge"
        self.section_label = tk.Label(
        self.quiz_frame,
        text=section_title,
        font=("Arial", 25),
        bg="#8ac5d4"
        )
        self.section_label.pack(pady=10)
        self.quiz_questions()
    else:
        if self.current_section == section_one:
          self.current_section = section_two
          self.question_index = 0
          for widget in self.quiz_frame.winfo_children():
            widget.destroy()
          self.section_label = tk.Label(
          self.quiz_frame,
          text="Section 2: Automation Knowledge",
          font=("Arial", 25),
          bg="#8ac5d4"
         )
          self.section_label.pack(pady=10)
          self.quiz_questions() 
        else:
          self.quiz_complete()
```
#### CSV Writing
To ensure persistent data storage in the quiz application, quiz responses are stored in a CSV file. When a user submits an answer, the application appends a new row to the CSV file containing the users name, the question presented, and the user the user has given. This ensures that responses are saved after closing the application and answers can be reviewed by recruiters or assessors.

```
    try: 
      with open("quiz_results.csv", "a", newline="") as file:
       writer = csv.writer(file)
       writer.writerow([self.name, question["question"], answer])
    except Exception as error:
       self.error_message.config(text=f"An error occurred while saving data: {error}")
       self.error_message.pack()
       print(error)
```

## Testing Section
