'''
Author: 零到正无穷
Date: 2021-02-17 17:13:26
LastEditTime: 2021-02-17 17:41:52
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\test_class.py
'''
class AnonymousSurvey:

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")

    def check_duplicate(self):
        for response in self.responses:
            break