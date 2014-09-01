print('Welcome to Buy With SkilBux')
number = input('Please tell me how many SkilBux you have')

if number == 'fifteen' or number == '15':
    print("you have enough to get a water bottle")
elif number == 'fourty' or number == '40':
    print("you have enough to get a Minecraft camp or water bottle")
elif number == 'sixty' or number == '60':
    print("You have enough to get a T-Shirt, Minecraft camp or water bottle")
else:
    print("I will only respond to 15, 40, or 60")
