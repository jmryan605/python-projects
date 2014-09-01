import random

answers = ['no',
           'yes',
           'I hope you live',
           'no can win',
           'please ask again',]

while True:
    print("please tell me your question")
    question = input('> ').lower().strip()
    if 'taco' in question:
        print('Mr.Rob should buy you tacos')
        answers.append('remember to show Mr.Rob the taco question')
    else:
        answer = random.choice(answers)
        print (answer)
