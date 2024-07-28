import json
import os
import random

def load_questions():
    questions_file = os.path.join(os.path.dirname(__file__), '../questions.json')
    with open(questions_file, 'r') as file:
        questions = json.load(file)
    return questions

def get_random_question(category):
    questions = load_questions().get(category, [])
    if questions:
        return random.choice(questions)
    return None
