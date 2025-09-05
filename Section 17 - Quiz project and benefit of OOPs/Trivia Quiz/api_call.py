import requests

class GenerateQuestions:
    def __init__(self, amount, difficulty) -> None:
        self.api_url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=boolean"
        self.questions = []

    

    def generate_question_bank(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
    # Parse the JSON data
            trivia_data = response.json()
            
            # Convert the data to a list of dictionaries
           
            for question_data in trivia_data['results']:
                question_dict = {
                    'question': question_data['question'],
                    'options': question_data['incorrect_answers'] + [question_data['correct_answer']],
                    'correct_answer': question_data['correct_answer']
                }
                self.questions.append(question_dict)

        return self.questions
