import numpy as np

def zahlenraten(max=100, tries=5):
    SECRET_NUM = np.random.randint(max)
    isSolved = False
    numTry = 0

    print('Please guess a number between 0 and ' + str(max))

    while (isSolved == False) and (numTry < tries):
        guess = input('Your guess: ')
        try:
            guess = int(guess)
            numTry += 1
            if guess == SECRET_NUM:
                isSolved = True
            elif guess < SECRET_NUM:
                print('Try again with a larger number\n')
            else:
                print('Try again with a smaller number\n')
        except:
            print('Please enter a number')

    if isSolved == True:
        print('Congrats, you win!')
    else:
        print('You loose :-(')


if __name__ == '__main__':
    zahlenraten(50)
