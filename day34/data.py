import requests

def generate_questions():
    token = requests.get('https://opentdb.com/api_token.php?command=request')
    token.raise_for_status()
    tk = token.json()

    parameters = {
        'amount':10,
        'type':'boolean',
        'token':tk['token']
    }

    questions = requests.get("https://opentdb.com/api.php",params=parameters)
    questions.raise_for_status()
    requests.get(f'https://opentdb.com/api_token.php?command=reset&token={tk["token"]}')
    new_questions = questions.json()
    
    return new_questions['results']



question_data = generate_questions()
