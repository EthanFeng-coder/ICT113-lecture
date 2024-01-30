import random

def main():
    questions = [
        'What is the biggest island and smallest continent?',
        'What is the Capital of Australia?',
        'What is the capital of NSW?',
        'What is the capital of Victoria?',
        'What is the capital of Tasmania?',
        'What is the capital of South Australia?',
        'What is the capital of Western Australia?',
        'What is the capital of Northern Territory?',
        'What is the capital of Queensland?',
        'What is my name?'
    ]
    
    answers = [
        'australia', 'canberra', 'sydney', 'melbourne',
        'Hobart', 'adelaide', 'perth', 'darwin', 'brisbane', 'ethan'
    ]
    
    points = 0
    question_indices = random.sample(range(len(questions)), 3)  # Ensures unique questions

    for question_index in question_indices:
        question = questions[question_index]
        answer = answers[question_index]
        guess = input(question + " ").strip()
        
        if guess.lower() == answer.lower():
            print('Correct...')
            points += 1
        else:
            print('Sorry...')
    
    print(f'You got {points} out of 3 questions.')

if __name__ == '__main__':
    main()