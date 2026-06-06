import tkinter as tk 
from validation import validate_name, validate_answer, validate_multiple_choice_answer
import csv
from questions import section_one, section_two

class QEQuizApp:
 
  def __init__(self):
   self.root = tk.Tk()
   self.root.title("Quality Engineering Quiz")
   self.root.geometry("800x600")
   self.name = None
   self.quiz_frame = tk.Frame(self.root)
   self.question_index = 0
   self.current_section = section_one

  def home_page(self):
   self.title = tk.Label (
       self.root,
       text ="Quality Engineering Quiz",
       font=("Arial", 40, "bold")
   )
   self.title.pack(pady=20)

   self.sub_title = tk.Label (
     self.root,
       text ="Junior Automation Test Engineer",
       font=("Arial", 26, "bold")
   )
   self.sub_title.pack()
   self.home_frame = tk.Frame(self.root)
   self.home_frame.pack()

   self.name_indicator = tk.Label(
    self.home_frame,
    text="Enter your name:",
    font=("Arial", 20)
   )
   self.name_indicator.pack()

   self.name_input = tk.Entry(self.home_frame, width="50")
   self.name_input.pack(pady=10)

   self.submit_button = tk.Button(
     self.home_frame,
     text="Submit Name",
     font=("Arial", 18),
      command=self.submit_name
   )
   self.submit_button.pack()

   self.error_message = tk.Label(
     self.home_frame,
     text="",
     font=("Arial", 15),
     fg = "red"
    )
   self.error_message.pack()

   self.name_isvalid = tk.Label(
     self.home_frame,
     text="",
     font=("Arial", 15),
     fg = "green"
   )
   self.name_isvalid.pack()
  

   self.start_button = tk.Button(
    self.home_frame,
    text="Start Quiz!",
    font=("Arial", 20),
    command=self.start_quiz
   )
   self.start_button.pack(pady=10)

  def quiz_complete(self):
    for widget in self.quiz_frame.winfo_children():
      widget.destroy()

    complete_message = tk.Label(
      self.quiz_frame,
      text=f"Thank you for completing the quiz {self.name}!",
      font=("Arial", 28)
    )
    complete_message.pack(pady=40)
    answers_recorded_message = tk.Label(
      self.quiz_frame,
      text="Your answers have been recorded and will be reviewed by someone from our team shortly!",
      font=("Arial", 28)
    )
    answers_recorded_message.pack(pady=10)

    contact_message = tk.Label(
      self.quiz_frame,
      text="We will be in touch soon regarding your results and feedback!",
      font=("Arial", 28)
    )
    contact_message.pack(pady=10)



  def submit_name(self):
   name_entered = self.name_input.get()
   validation_outcome = validate_name(name_entered)
   if validation_outcome == True:
     self.name = name_entered
     self.name_isvalid.config(text="Name Successfully submitted!")
     self.error_message.config(text="")

   else:
     self.error_message.config(text=validation_outcome)

  def next_question(self):
    question = self.current_section[self.question_index]
    self.error_message= tk.Label(
    self.quiz_frame,
    text="",
    fg="red",
    font=("Arial", 14)
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
          return

    self.question_index += 1
      
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
        font=("Arial", 25) 
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
          font=("Arial", 25) 
         )
          self.section_label.pack(pady=10)
          self.quiz_questions() 
        else:
          self.quiz_complete()


  


  def quiz_questions(self):
    self.quiz_frame.pack()
    question = self.current_section[self.question_index]

    self.question_message = tk.Label(
      self.quiz_frame,
      text = question["question"],
      font=("Arial", 22) 
    )
    
    self.question_message.pack(pady=20)
    if question["type"] == "manual_answer":
      self.user_answer = tk.Entry (
        self.quiz_frame,
        width=50
      )
      self.user_answer.pack(pady=20)
      self.submit_button = tk.Button(
        self.quiz_frame,
        text="Next Question",
        font=("Arial", 20),
        command=self.next_question
      )

      self.submit_button.pack()
    elif question["type"] == "multiple_choice":
      self.selected_option = tk.StringVar()
      self.selected_option.set("Select an Answer")
      answer_selection = tk.OptionMenu(
        self.quiz_frame,
        self.selected_option,
        *question["options"]
      )
      answer_selection.config(font=("Arial", 14))
      answer_selection.pack(pady=20)
      self.submit_button = tk.Button(
        self.quiz_frame,
        text="Next Question",
        command=self.next_question
      )
      self.submit_button.pack()

  
  def start_quiz(self):
    if self.name == None:
      self.error_message.config(text="Please submit your name first")
      return
    
    self.home_frame.destroy()

    self.quiz_frame = tk.Frame(self.root)  
    self.quiz_frame.pack()

    self.section_label = tk.Label(
    self.quiz_frame,
    text="Section 1: Testing Fundamentals",
    font=("Arial", 25) 
    )
    self.section_label.pack(pady=10)
    self.quiz_questions()


if __name__ == "__main__":
  app = QEQuizApp()
  app.home_page()
  app.root.mainloop()
