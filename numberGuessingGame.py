import random

def main():
        correctAnswer = random.randint(1, 100)
        userAnswer = (int)(input('Enter a number between 1 and 100: '))

        #Create a for loop instead of what is down below
        while userAnswer != correctAnswer:
                if userAnswer > correctAnswer:
                        userAnswer = (int)(input('Your answer is too high. Try again: '))
                elif userAnswer < correctAnswer:
                        userAnswer = (int)(input('Your answer is too low. Try again: '))
                

        print('You Win!')

if __name__ == '__main__':
        main()