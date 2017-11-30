#Jonathan Geller
#Minesweeper in 150 lines or less. November 16th, 2017 
import random, math
alpha='abcdefghijklmnopqrstuvwxyz' #used to change numbers to letters and vice versa
def click(a,b,x,y,auto): #function used for clicking a square, 
    if b[x][y]=='⚑' and not auto:
        print('You have flagged this space')
    elif b[x][y]!='█' and not auto:
        print('You have already discovered this space')
    elif a[x][y]=='⚑':
        print('You lose :(')
        return 2 #returns if clicked square is a bomb
    else:
        b[x][y]=a[x][y]
        if b[x][y]==0:
            for c in range(x-1,x+2):
                for d in range(y-1,y+2):
                    if c>=0 and c<len(b) and d>=0 and d<len(b[0]):
                        if a[c][d]!=b[c][d]:
                            click(a,b,c,d,True) #reexecutes function around any zeroes, on an automatic mode that doesn't print to terminal
    if not auto:
        pr(b)
def pr(a): #a way of printing the board that doesn't look completely awful
    print(' ', end=' ')
    for x in range(len(a[0])):
        print(str(x+1), end='')
        if len(str(x+1))==1:
            print('', end=' ')
    print()
    for x in range(len(a)):
        print(alpha[x], end=' ')
        for y in range(len(a[0])):
            print(str(a[x][y]), end=' ')
        print()  
    print()        
playing=True
while playing:        
    a=[]
    b=[]
    w=0
    h=0
    p=0
    while w==0:
        wInput=input('How wide should the board be? ')
        if wInput.isnumeric():
            w=int(wInput)
        else:
            print('Please enter a number')
    while h==0:
        hInput=input('How tall should the board be? ') #technically the board can be a maximum of 26 rows tall but if you try more and the code gives you an error, that's really just to keep you safe from a miserable game of minesweeper
        if hInput.isnumeric() and int(hInput)*w>10:
            h=int(hInput)
        else:
            print('Please enter a number above '+str(math.ceil(10/w))) #board needs to be at least 10 squares or it won't be able to place mines
    while p==0:
        pInput=input('How many mines should there be? ')
        if pInput.isnumeric() and int(pInput)<h*w-9:
            p=int(pInput)
        else:
            print('Please enter a number below '+str(h*w-10)) #if there are too many mines, then there will be no way to make the first square clicked a '0'
    for x in range(h):
        row=[]
        for y in range(w):
            row.append('█')
        b.append(row)
    pr(b) #kind of a trick the real board doesn't exist yet, there are no mines because otherwise there is a chance of the user clicking on a mine first try, which isn't fair
    q=True
    while q: #loop inputs until they work
        guess=input('First Guess? ')
        if len(guess)>1 and guess[0].isalpha() and alpha.find(guess[0])<h and guess[1:].isnumeric() and int(guess[1:])<=w:
            c1=alpha.find(guess[0].lower())
            c2=int(guess[1:])-1
            q=False
        else:
            print('Please enter a square with the letter first, then the number, like \'B4\'')
    for x in range(h):
        row=[]
        for y in range(w):
            row.append(0)
        a.append(row)
    for x in range(p):
        q=True
        while q:
            x1=random.randint(0,h-1)
            x2=random.randint(0,w-1)
            if a[x1][x2]!='⚑' and (abs(x1-c1)>1 or abs(x2-c2)>1):
                a[x1][x2]='⚑'
                q=False
    for x in range(h):
        for y in range(w):
            if a[x][y]!='⚑':
                z=0
                for g in range(-1,2):
                    for j in range(-1,2):
                        if x+g>=0 and x+g<h and y+j<w and y+j>=0:
                            if a[x+g][y+j]=='⚑':
                                z+=1
                a[x][y]=z
    click(a,b,c1,c2,False) #first click executes after board is generated
    op='click mode'
    while q!=2:
        print('Please enter a square to '+op[0:5])
        if op=='click mode':
            print('Type \'flag\' to switch modes')
        if op=='flag mode':
            print('Type \'click\' to switch modes')
        square=input()
        if square.isalpha() and square.lower()=='flag': #allow user to switch modes
            op='flag mode'
        elif square.isalpha() and square.lower()=='click':
            op='click mode'
        elif square.isalpha() and square.lower()=='quit': #just for testing, but i just left it in because it wasn't hurting anything 
            quit()
        elif len(square)>1 and square[0].isalpha() and alpha.find(square[0])<h and square[1:].isnumeric() and int(square[1:])<=w:
            x=alpha.find(square[0].lower())
            y=int(square[1:])-1
            if b[x][y]=='█': #perform operation on square
                if op=='flag mode':
                    b[x][y]='⚑'
                if op=='click mode':
                    q=click(a,b,x,y,False)
            elif b[x][y]=='⚑':
                if op=='flag mode':
                    b[x][y]='█'
                if op=='click mode':
                    print('This square is flagged, unflag it by selecting it in flag mode to click it.')
            else:
                print('That square is already uncovered. ')
        else:
            print('Sorry, print your response with the letter first, then the number, like \'A1\'')
        z=0
        for x in range(h): #checks if player won
            for y in range(w):
                if not(b[x][y]==a[x][y] or (a[x][y]=='⚑' and b[x][y]=='█')):
                    z=1
        if z==0:
            print('You win!')
            q=2
        elif q==2:
            b=a
        pr(b)
    print('Play again?')
    if input()[0].lower()=='y':
        playing=True
    else:
        playing=False