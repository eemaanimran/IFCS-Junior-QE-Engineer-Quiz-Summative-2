import tkinter as tk 
from validation import validate_name
import csv

class QEQuizApp:
 
  def __init__(self):
   self.root = tk.Tk()
   self.root.title("Quality Engineering Quiz")
   self.root.geometry("800x600")
   self.name = None

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

   name_indicator = tk.Label(
    self.root,
    text="Enter your name:",
    font=("Arial", 20)
   )
   name_indicator.pack()

   self.name_input = tk.Entry(self.root, width="50")
   self.name_input.pack(pady=10)

   submit_button = tk.Button(
     self.root,
     text="Submit Name",
     font=("Arial", 18),
      command=self.submit_name
   )
   submit_button.pack()

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
  

   start_button = tk.Button(
    self.root,
    text="Start Quiz!",
    font=("Arial", 20),
    command=self.start_quiz
   )
   start_button.pack(pady=10)

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
      text="Section 1: Testing Fundamentals"
    )

    
    return
  
  def start_quiz(self):
    if self.name == None:
      self.error_message.config(text="Please Enter your name first")
      return 
    for widget in self.root.winfo_children():
      widget.destroy

      




if __name__ == "__main__":
  app = QEQuizApp()
  app.home_page()
  app.root.mainloop()
