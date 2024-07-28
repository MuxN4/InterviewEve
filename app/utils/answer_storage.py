import os

def store_answer(question, answer, category):
    answers_file = os.path.join(os.path.dirname(__file__), '../answers.txt')
    with open(answers_file, 'a') as file:
        file.write(f"Category: {category}\nQuestion: {question}\nAnswer: {answer}\n\n")
