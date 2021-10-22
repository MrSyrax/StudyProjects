from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q['question'], q['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

u_score = quiz.score
q_number = quiz.question_number
print(f"you've completed the quiz\nYour final socre was:{u_score}/{q_number}") 