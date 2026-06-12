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
| NFR1 | The application should write responses to the CSV file within 2 seconds after submission |
| NFR2 | The application should load and display each question within a few milliseconds of user interaction. |
| NFR3 | The application should provide clear error messages where necessary |
| NFR4 | The application should provide a consistent layout and font style acrosss every section |

### Tech Stack outline
Below are the features that were used to create this Quiz Application.
- [Python](https://www.python.org/) — Main programming language
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — Python library used to create the desktop GUI
- [csv](https://docs.python.org/3/library/csv.html) — Used for CSV data storage, and storing quiz responses
- [unittest](https://docs.python.org/3/library/unittest.html) — Used for automated unit testing for validation functions

### UML diagram
This diagram displays the structure of the Quiz Application. The ```QEQuizApp``` class manages the user interface, question navigation, and recording results. This class is dependant on ```validation.py``` to validate user input and uses the question data stored in ```question.py``` for the quiz content.
<img width="795" height="628" alt="Screenshot 2026-06-11 121828" src="https://github.com/user-attachments/assets/4700691d-d1c1-440c-871e-e518bbf2b27a" />


## Development Section 
Following the completion of the initial prototype design and establishing technical requirements, the development of the quiz application became more manageable. This development process follows an organised design approach, involving the Codes structure, object-oriented design, GUI implementation, alongside input validation and logic for navigating questions. This section outlines the key features of the quiz application, including how different classes and functions work to ensure functionality.
### Code Structure
The application was designed using a modular, object‑oriented approach to improve code readability and separate different areas of functionality. For example, the quiz application has been separated into four different Python modules.
<img width="307" height="63" alt="image" src="https://github.com/user-attachments/assets/35e2cf82-754e-4d4c-8027-73d4c55b7656" />
<img width="319" height="20" alt="image" src="https://github.com/user-attachments/assets/45b60d2b-24af-417a-a8e1-f1f8ae5a30a4" />
<img width="233" height="54" alt="image" src="https://github.com/user-attachments/assets/68ae824a-718e-4a4c-8b40-e951ef915c2a" />
#### main.py

The ```main.py``` module contains the primary application logic and GUI functionality using Tkinter. It's main class ```QEQuizApp``` contains the overall quiz navigation, including user interaction, switching questions, and transiting to different sections. This class also contains the creation of Tkinter widgets, including labels, buttons, frames, and drop down menus.

Object-oriented programming principles were also applied in this class including attributes like quiz frames (e.g, ```self.home_frame```) and Tkinter widgets (e.g., ```self.title```). This class also contains various methods, which will be discussed in more detail below. 

#### validation.py

The validation.py module contains a set of validation functions for checking user input throughout the quiz. These functions ensure that all required fields are correctly completed before allowing the user to proceed to the next question or frame. Separating this logic from the main module not only improves modularity but also allows the functions to be tested independently through automated unit tests. The module contains three key validation functions. 

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

If any validation doesn't return True then the application will display an error message prompting the user to submit an answer correctly. This ensures that all data is collected appropriately.

#### question.py
The questions.py module was created to separate quiz content from the main application module. The quiz questions are stored using Python lists and dictionaries. Each section of the quiz are stored in a list, including ```section_one``` and ```section_two```. Within each list, individual questions are stored as dictionaries with key-value pairs. Each question dictionary contains ```question``` representing the text displayed to the user, ```type``` which determines whether the questions were multiple choice or manually typed, and ```options``` stores multiple choice answers if applicable. An example of this is shown below with section one.
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
The reason for storing quiz questions separate from the main module is to ensure that questions were loaded dynamically into the GUI using ```question_index``` attribute. The ```type``` key pair is also essential, as it controls the type of Tkinter widget displayed for each question. For example, manually typed questions generated an Entry widget, whereas multiple choice questions would load an Option Menu.

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
Both manual testing and automated unit testing were used throughout the development of the quiz application. These testing approaches help verify that the validation logic and user focused actions are successfully functioning as intended. 
Manual testing was done during development to verify that users can navigate between quiz sections, submit answers, and complete the quiz successfully. This type of testing was particularly useful for identifying issues related to the GUI, widget logic for question types, and question navigation, so if any errors are detected, it's easier to focus on those specific areas rather than searching through the entire codebase. The table below shows actions performed for manual testing and their results.

### Manual Testing Table of results

| Test ID | Test Description | Expected Result | Actual Result | Pass/Fail |
|----------|---------------|----------------|---------------|---------|
| 1 | Submit empty name | Error message ```Name Field cannot be left empty``` is displayed | Successfully displayed error message | Pass |
| 2 | Submit numbers as a name | Error message ``Name must only contain letters`` is displayed | Successfully displayed error message | Pass |
| 3 | Submit name with only one character | Error message ``Name must be between 2 and 30 characters`` is displayed | Successfully displayed error message | Pass |
| 4 | Submit valid name | Validation message ```Name Successfully submitted!``` appears | Validation message appeared successfully | Pass |
| 5 | Start the quiz | User switches to the first question after clicking ```Start Quiz!``` | Successfully switched to Section 1 question 1 | Pass |
| 6 | Submit empty manual answer | Error message ```Answer Field cannot be left empty``` is displayed | Error message displayed correctly. | Pass |
| 7 | Leave multiple choice question on default answer | Error message ```Please Select an Answer``` is displayed | Successfully displayed error message | Pass |
| 8 | Submit valid manual answer | User progresses to the next question | Next question displayed successfully | Pass |
| 9 | Submit valid multiple choice answer | User progresses to the next question | Next question displayed successfully | Pass|
| 10 | Successfully complete all section 1 questions | Section 2 is displayed | Section 2 displayed successfully | Pass |
| 11 | Successfully complete all section 2 questions | Quiz completion screen is displayed | Completion screen displayed successfully | Pass |
| 12 | Submit quiz response | Name, question, and answer written to CSV file | Data written successfully to ```quiz_results.csv``` file | Pass |

Overall, these manual testing results confirm that the quiz application functions as intended, with all features working correctly and validation rules effectively prevent invalid input.

### Unit Testing 
Automated unit testing was implemented using Python's built in ```unittest``` framework. These unit tests focused on input validation functions that can be tested separately from the GUI, this ensures high consistency of these validation functions. 
```
 def test_valid_name(self):
        result = validate_name("John")
        self.assertEqual(result, True)

    def test_empty_name(self):
        result = validate_name("")
        self.assertEqual(result, "Name Field cannot be left empty")

    def test_valid_manual_answer(self):
        result = validate_answer("API Testing")
        self.assertEqual(result, True)

    def test_empty_manual_answer(self):
        result = validate_answer("")
        self.assertEqual(result, "Answer Field cannot be left empty")

    def test_valid_multiple_choice_answer(self):
        result = validate_multiple_choice_answer("User Acceptance Testing")
        self.assertEqual(result, True)

    def test_empty_multiple_choice_answer(self):
        result = validate_multiple_choice_answer("Select an Answer")
        self.assertEqual(result, "Please Select an Answer")


if __name__ == "__main__":
     unittest.main()
```
As shown in the code above, several areas were tested including:
* Valid user names
* Empty user name submitted
* Valid manually entered answer
* Empty manually entered answer
* Valid multiple choice answer
* Empty multiple choice answer

#### Unit Testing Outcomes
All tests passed successfully, demonstrating that the validation functions behaved as expected for both valid and invalid inputs. A screenshot of these unit tests passing in the terminal is shown below
<img width="911" height="127" alt="image" src="https://github.com/user-attachments/assets/715cdbd6-89b6-42c4-bb8a-b4d7683ff951" />
#####  Continuous Integration 
Continuous Integration (CI) was also implemented as part of the testing process for this Quiz application using GitHub Actions to automate execution of unit tests when changes were pushed to the repository. This approach can help identify any errors during early development, ensuring that validation works correctly even after pushing new code. The screenshot below shows CI passing for this GitHub repository, ensuring that validation is consistently working as intended.
<img width="1358" height="342" alt="image" src="https://github.com/user-attachments/assets/e87c7569-d84c-4581-99df-a794e8ceb8c6" />

## User Documentation
This Quality Engineering quiz has been designed for potential candidates or onboarded early professionals joining Automation Testing to gain an insight into their current knowledge about the practice in general and their automation testing knowledge. The quiz is intended for use for both recruiters to analyse the quiz results and candidates. Below are the steps candidates can take to interact with the quiz. 
### 1. Launch the application
To run the application, execute the code from ```main.py```. After launching, the home screen should be displayed. 
<img width="1145" height="820" alt="image" src="https://github.com/user-attachments/assets/5a1f9ceb-d177-409e-a359-2547e18a858e" />
### 2. Enter your name
Enter your name into the input field and press ```Submit name```. A message will then appear to show whether or not your name has been successfully submitted.
<img width="1035" height="706" alt="image" src="https://github.com/user-attachments/assets/1a32101f-389b-4724-864b-04f496f00cdc" />
### 3. Start the Quiz
Select ```Start Quiz``` to begin the quiz. This should then display Section 1 Question 1.
### 4. Answer Questions
Questions will be shown as either manually written responses, where your answer should be typed out, or multiple choice, where you should select an option from a list of options in the drop down menu. Ensure that no questions are left blank otherwise you cannot progress to the next question.
<img width="1839" height="631" alt="image" src="https://github.com/user-attachments/assets/54ee52ef-81a8-47f8-ac13-e3526d84443d" />
<img width="968" height="310" alt="image" src="https://github.com/user-attachments/assets/ccfb8990-084f-4ac5-a166-3720f10361e9" />
### 5. Quiz Complete!
Once you've gone through both sections, a completion screen will be displayed confirming that you've successfully finished the quiz.
<img width="1690" height="833" alt="image" src="https://github.com/user-attachments/assets/313f37d4-ec58-4772-b555-fbaf5d09b582" />

After a candidate has completed the quiz, recruiters or assessors can access this CSV file to review answers and reach a solid conclusion about a potential candidate or early professional about their current knowledge of Automation Testing. An example of this CSV file is shown below, opened in Microsoft Excel.
<img width="881" height="213" alt="image" src="https://github.com/user-attachments/assets/869ee28d-487a-41a9-ba91-945aa153dcbc" />


## Technical Documentation

### Libraries and programming language used
This quiz was developed using Python 3.13 and uses the following libraries:
* Tkinter
* csv
* unittest
### Cloning the repository
To create a local version of this project, copy the repository URl and clone it in a terminal using ```git clone``` in a terminal. An example is shown below using the web URL
```bash
git clone https://github.com/eemaanimran/IFCS-Junior-QE-Engineer-Quiz-Summative-2.git
```
In the terminal you can now change directory using the repository name to move inside the folder using the ```cd``` command. 
```bash
cd IFCS-Junior-QE-Engineer-Quiz-Summative-2
```
You can now open this folder in a suitable code editor, like Visual Studio code to view and modify any code or modules if necessary. This can be done with the command below if you wish to open it in Visual Studio code.
```bash
code .
```
### Quiz Structure
This quiz project has been organised into multiple python modules to separate different functionality of the quiz.
```main.py``` - Contains the main GUI and quiz functionality
```validation.py``` - Contains validation functions used throughout the application
```questions.py``` - Stores quiz questions and the type of question, alongside answer options for multiple choice and the correct answer.
```test_validation.py``` - Contains automated unit tests for validation functions. 
```quiz_results.csv``` - Stores user responses to the quiz. 

### Running the application
To run the Tkinter application, run the code from ```main.py``` which should launch the Tkinter GUI and display the home screen.
```bash
python main.py
```
To run the automated unit tests, run the ```test_validation.py``` module.
```bash
python test_validation.py
```

## Evaluation
Overall, the development of this Quality Engineering Quiz was successful, all the main requirements outlined during the design phase were implemented. The application provides a fully functional GUI, CSV data storage, input validation, automated and manual testing, and the use of CI through GitHub Actions for any new code pushed to the repository. 

### What went well

One area which was the most successful was the modular design of the application. Separating functionality into individual modules dramatically helped to improve code by separating different functionality areas of the Quiz for better organisation. This is useful because any future improvements or error handling can be added more easily, making it simpler to navigate the code and locate the relevant areas. 

Another successful feature that I particularly enjoyed creating was the implementation of dynamically loaded questions. By storing questions in lists and dictionaries in a separate module will allow new questions to be modified and added without changing any GUI code logic, especially for individuals with limited programming experience.

This feature also fits the main purpose of this quiz quite well. Recruiters can tailor questions based on the individual taking the assessment. For example, candidates applying for Junior roles such as internships or apprenticeships may be presented with more foundational questions. However, someone with more industry experience could be given more advanced questions to showcase their knowledge and skillset, which makes results easier to analyse.

### Improvements

Although the quiz is fully functional, there are a few areas that could be improved. For example, the visual design of the user interface could be improved, whilst the app does have sufficient functionality that makes it simple to use, a more visually appealing interface could improve user engagement. 

The validation functions could also be expanded. This is because the multiple choice validation only checks whether the user has selected an option other than the default value in the drop down. However, a future implementation could have better validation rules tailored to specific multiple choice options, to ensure a valid option has been selected. Though this may reduce its dynamic advantage, it may be valuable consideration for future development.

Another potential improvement could be having a scoring system. The current application records answers for review but doesn’t automatically calculate the user’s performance. Having a scoring system, specifically for checking correct multiple choice answers could make the assessment process more efficient. 

