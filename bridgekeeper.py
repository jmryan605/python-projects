def ask(question):
    answer = input(question)
    answer = answer.lower().strip()
    print("thou hast answered: " + answer)
    return answer

#--------------------------------------------------------------------

print(''' Who would cross the Bridge of
Death must answer me these questions three ...''')

name = input("What is your name?")
quest = input("What is your quest?")


if name.startswith('lancelot'):
    color = ask_color()
elif name.startswith('robin'):
    capital = ask("What is the capital of Assyria?")
elif name.startswith('galihad'):
    color = ask_color()
else:
    print("You arent in the movie. Go jump in the Gorge of Eternal Death")

