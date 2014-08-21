import time

yes = ('yes','yep','yeah','yup','obviously','absouloutly','definitley','sure')

waffles = input("Do you like waffles?")

if waffles.startswith(yes):
    print("yeah we like waffles!")
    pancakes = input("do you like pancakes?")
    if pancakes.startswith(yes):
        print("yeah we like waffles!")
        french_toast = input("do you like french toast?")
        if french_toast.startswith(yes):
            print("yeah we like french toast")
            print("doo doo doo dooo can't wait to get a mouthful!")
            time.sleep(1)
            print("WAFFLES!")
            time.sleep(3)
            print("WAFFLES!")
            time.sleep(3)
            print("WAFFLES!")
            time.sleep(2)

waffles = input("Do you like waffles?")
if waffles.startswith(yes):
    print("yeah we like waffles!")
    pancakes = input("do you like pancakes?")
    if pancakes.startswith(yes):
        print("yeah we like waffles!")
        french_toast = input("do you like french toast?")
        if french_toast.startswith(yes):
            print("yeah we like french toast")
            print("doo doo doo dooo can't wait to get a mouthful!")
