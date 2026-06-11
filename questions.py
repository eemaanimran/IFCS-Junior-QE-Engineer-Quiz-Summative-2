"""
Stores question data for the quiz application. 
The questions are organised into sections using lists and dictionaries, so they can be dynamically loaded.
Each question has the question text, question type, and multiple choice options where necessary.
"""
section_one = [
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
section_two = [
    {
        "type":"manual_answer",
        "question":"Describe when API Testing should be used"
    },
    {
        "type":"manual_answer",
        "question":"What is a locator and how is it used for automation testing?"
    }
]