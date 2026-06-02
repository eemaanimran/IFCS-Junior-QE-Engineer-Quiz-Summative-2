import tkinter as tk 
from validation import validate_name, validate_answer
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

   self.name_indicator = tk.Label(
    self.root,
    text="Enter your name:",
    font=("Arial", 20)
   )
   self.name_indicator.pack()

   self.name_input = tk.Entry(self.root, width="50")
   self.name_input.pack(pady=10)

   self.submit_button = tk.Button(
     self.root,
     text="Submit Name",
     font=("Arial", 18),
      command=self.submit_name
   )
   self.submit_button.pack()

   self.error_message = tk.Label(
     self.root,
     text="",
     font=("Arial", 15),
     fg = "red"
    )
   self.error_message.pack()

   self.name_isvalid = tk.Label(
     self.root,
     text="",
     font=("Arial", 15),
     fg = "green"
   )
   self.name_isvalid.pack()
  

   self.start_button = tk.Button(
    self.root,
    text="Start Quiz!",
    font=("Arial", 20),
    command=self.start_quiz
   )
   self.start_button.pack(pady=10)

  def submit_name(self):
   name_entered = self.name_input.get()
   validation_outcome = validate_name(name_entered)
   if validation_outcome == True:
     self.name = name_entered
     self.name_isvalid.config(text="Name Successfully submitted!")
     self.error_message.config(text="")
     #with open("quiz_data.csv", "a", newline="") as file:
      # writer = csv.writer(file)
       #writer.writerow(["Name", self.name]) 
   else:
     self.error_message.config(text=validation_outcome)


  def quiz_questions(self):
    self.title.pack(pady=20)
    self.sub_title.pack()

    self.section_one = tk.Label(
      self.root,
      text="Section 1: Testing Fundamentals",
      font=("Arial", 25) 
    )
    self.section_one.pack()
    question = section_one[self.question_index]

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
        command=self.next_question
      )

      self.submit_button.pack()
    elif question["type"] == "multiple_choice":
      self.select_option = tk.StringVar()
      self.selected_option.set("Select an Answer")
      answer_selection = tk.OptionMenu(
        self.quiz_frame,
        self.selected_option,
        *question["options"]
      )
      answer_selection.config(font=("Arial", 14))
      answer_selection.pack(pady=20)
      self.submit_button.pack()

  
  def start_quiz(self):
    if self.name == None:
      self.error_message.config(text="Please Enter your name first")
      return 
    for widget in self.root.winfo_children():
      self.name_input.destroy()
      self.error_message.destroy()
      self.name_isvalid.destroy()
      self.name_indicator.destroy()
      self.submit_button.destroy()
      self.start_button.destroy()

    self.quiz_frame = tk.Frame(self.root)  
    self.quiz_frame.pack()
    self.quiz_questions()




      




if __name__ == "__main__":
  app = QEQuizApp()
  app.home_page()
  app.root.mainloop()
