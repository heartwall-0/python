'''
Author: your name
Date: 2021-02-17 17:24:20
LastEditTime: 2021-02-17 17:43:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\lanauge_survey.py
'''
from test_class import AnonymousSurvey

question = "What lanauge did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Lanauge: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()