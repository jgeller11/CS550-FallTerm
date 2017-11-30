import math
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print('It\'s September 21st, you\'re sitting in programming class with no creativity.')
print('Suddenly, a big monster emerges from the Science Center pond, and breaks through the window of your classroom.')
a = input('Do you Run or Fight? ')
print()
if a == 'Fight':
    b = input('Are you sure? This is a really big monster. ')
    if b == 'Y' or b == 'Yes':
        print()
        print('The monster eats you. That was dumb, why did you do that?')
        quit()
print('As you run away, the monster is momentarily distracted by your slower-thinking peers.')
c = input('Do you run to Hill House, the Cafe, or the WJAC? ')
if c == 'Cafe':
    print()
    print('Your severe caffiene addiction is your downfall, and the monster catches you before your latte is ready.')
elif c == 'WJAC':
    print()
    print('There is an emergency meeting at the WJAC, and the sheer boredom and inefficiency causes you to drop dead.')
elif c == 'Hill House':
    print()
    print('You make it to Hill House, and have about a minute of time to prepare for the monster\'s arrival.')
    print()
d = input('Do you go to the Tuck Shop, the Library, or stay in the Hill House Commons? ')
print()
if d[0] == 'T':
    print('There\'s no one there, why\'d you think this would work?')
    e = input('Do you go the the Library or back to Hill House Commons')
    print()
    if e[0] == 'H':
        print('You wasted so much time trying to get a f\'real that the monster has reached Hill House and it eats you.')
elif d[0] == 'H':
    print('You wait in the commons, and when the monster arrives, you have only an apple you were saving for lunch to defend yourself.')
    print('The monster stands 60 meters away from you on even ground, and is 15 meters tall.')
    print('You are capable of throwing the apple at 30m/s. Air resistance is negligible.')
    print()
    f = float(input('What angle do you throw the apple at relative to the horizontal (in radians)? '))
    g = (60 / (30 * math.cos(f))) * math.sin(f) - 4.9 * ((60 / (30 * math.cos(f))) ** 2)
    if g >= 0 and g <= 15:
    #if (((60 / (14 * math.cos(f))) * math.sin(f) - 4.9 * ((60 / (14 * math.cos(f))) ** 2)) >= 0) and (((60/(14*math.cos(f)))*math.sin(f)-4.9*(60/(14*math.cos(f)))**2) <= 3) :
        r = input('The apple hits the monster, and bounces off. Why did you do that? ')
        print()
        print('That was a rhetorical question. The monster comes and eats you.')
        quit()
    else:
        print('You miss, the monster eats you.')
if e[0] == 'L' or d[0] == 'L':
    print('You wait out in the John F. Kennedy reading room.')
    print('Community Safety takes down the monster, and you survive. Good job.')