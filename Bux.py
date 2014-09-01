
rewards = [
   {
       'name': "Regular Attendance",
       'desc': "One regular class (90-120 min)",
       'min': 40,
       'max': 40,
   },
   {
       'name': "GitHub Green Dot",
       'desc': "Get a green dot from committing something new",
       'min': 10,
       'max': 40,
   }
]

items = [
    {
        'name': "Tee Shirt (Basic)",
        'desc': "The basic SkilStak logo on a Tee Shirt (whatever size)",
        'cost': 600
    },
    {
        'name': "Saturday Minecraft Camp",
        'desc': "Regular 2-hour Minecrafrt camp held Saturday (usually 3-5)",
        'cost': 400
    },
    {
        'name': "Water Bottle",
        'desc': "One of our regular water bottles with SkilStak logo",
        'cost': 150
    }
]


for reward in rewards:
    if reward['min'] == reward['max']:
        print("{name},{desc}: {min}-{max}".format(**reward))
    else:
        print("{name},{desc}: {min}-{max}".format(**reward))

for item in items:
    print("{name},{desc}: {cost}".format(**item))
