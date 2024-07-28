from flask import Blueprint, render_template, request, redirect, url_for, session
from .forms import AnswerForm
from .utils.question_loader import get_random_question, load_questions

app = Blueprint('app', __name__)

@app.route('/')
def home():
    interview_tip_data = get_random_question('interview_tips')
    interview_tip = interview_tip_data['question'] if interview_tip_data else "No tips available."
    return render_template('home.html', interview_tip=interview_tip)

@app.route('/question', methods=['GET', 'POST'])
def question():
    category = request.args.get('category', 'general_questions')
    form = AnswerForm()

    if 'question' not in session or session.get('category') != category:
        question_data = get_random_question(category)
        session['question'] = question_data['question'] if question_data else "No question available."
        session['category'] = category

    question = session['question']

    if form.validate_on_submit():
        user_answer = form.answer.data
        return redirect(url_for('app.result', answer=user_answer))

    return render_template('question.html', form=form, question=question)

@app.route('/result')
def result():
    answer = request.args.get('answer')
    question = session.get('question')
    category = session.get('category', 'general_questions')
    questions = load_questions()

    # Ensure questions[category] is a list of dictionaries
    if category in questions:
        correct_answer = next((q['answer'] for q in questions[category] if q['question'] == question), "No answer found.")
    else:
        correct_answer = "No questions found for this category."

    evaluation = f"Question: {question}<br>Your answer: {answer}<br>Correct answer: {correct_answer}"
    return render_template('result.html', evaluation=evaluation)
