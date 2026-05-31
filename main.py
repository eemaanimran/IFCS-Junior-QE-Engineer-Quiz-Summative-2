import tkinter as tk 

class QEQuizApp:
 
  def __init__(self):
   self.root = tk.Tk()
   self.root.title("Quality Engineering Quiz")
   self.root.geometry("800x600")

  def home_page(self):
   title = tk.Label (
       self.root,
       text ="Quality Engineering Quiz",
       font=("Arial", 40, "bold")
   )
   title.pack(pady=20)

   sub_title = tk.Label (
     self.root,
       text ="Junior Automation Test Engineer",
       font=("Arial", 26, "bold")
   )
   sub_title.pack()

   name_indicator = tk.Label(
    self.root,
    text="Enter your name:",
    font=("Arial", 20)
   )
   name_indicator.pack()

   self.name_input = tk.Entry(self.root)
   self.name_input.pack(pady=10)

   submit_button = tk.Button(
     self.root,
     text="Submit Name",
     font=("Arial", 18),
     command=self.submit_name
   )
  
  def submit_name(self):
   print("name submitted")

   start_button = tk.Button(
    self.root,
    text="Start Quiz!",
    font=("Arial", 20),
    command=self.start_quiz
   )
   start_button.pack(pady=10)

  def start_quiz(self):
    pass


if __name__ == "__main__":
  app = QEQuizApp()
  app.home_page()
  app.root.mainloop()
