import random

answers = ['yes','no',
           'go sit in a corner and think about your life',
           'hopefully']

while True:
    print('TELL ME YOUR QUESTION OR YOU TOTES ARE LAME')
    question = input('> ').lower().strip()
    if 'die' in question or 'death' in question or 'love' in question or 'live' in question:
        print('i dont like tat question bi')
    elif 'j' in question:
        print('dont ask questions with a j in it')
        answers.append('do not ask a question wif j in it')
    else:    
        answer = random.choice(answers)  
        print (answer)
