# from data import question_data
from question_model import QuestionModel
from  quiz_brain import QuizBrain
from api_call import GenerateQuestions
# make a list on Question objects
num_ques = int(input("Input the number of question: "))
level = input("Choose the difficulty level (easy/medium/hard): ").lower()

gq = GenerateQuestions(num_ques,level)
question_data = gq.generate_question_bank()
question_bank = []

for question in question_data:
    question_bank.append(QuestionModel(question["question"],question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
