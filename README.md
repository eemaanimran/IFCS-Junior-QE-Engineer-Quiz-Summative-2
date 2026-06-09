# IFCS-Junior-QA-Engineer-Quiz-Summative-2

## Introduction 
As a test Automation Engineer at IBM, I work within a rigorous quality engineering environment, where efficient knowledge about testing practices, and high quality testing processes are vital for producing a successful UI testing outcomes from different environments. New joiners in the Quality Engineering practice should be able to recognise and apply these requirements where necessary to make meaningful contributions whilst adhereing to IBM's value of innovation and trust. However, onboarding of interns, apprentices, and regular employees can be challenging when it comes to understanding each newcomers current knowledge of Quality Engineering. Relying solely on induction sessions and early discussions may not be a consistent approach to understand a candidates knowledge during onboarding.

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

## Development Section 

## Testing Section
