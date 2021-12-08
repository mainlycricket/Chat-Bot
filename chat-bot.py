# functions with definitions:

# 1. wishes and tells its development year

def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')

# 2. asks the user his name

def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')

# 3. guesses the age of the user by a trick:

def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")

# 4. prints positive whole numbers as per the user input

def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1

# 5. Plays a quiz - runs until the user answers correctly

def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("Why do we use methods?")

    answers = ['To repeat a statement multiple times.',
               'To decompose a program into several small subroutines.',
               'To determine the execution time of a program.',
               'To interrupt the execution of a program.']

    correct_answer = 2
    selected = 0

    for answer in answers:
        i = 1
        print(str(i) + '. ' + answer)

    while selected != correct_answer:
        selected = int(input())

    print('Completed, have a nice day!')

# 6. says Bye

def end():
    print('Congratulations, have a nice day!')


# calling functions:

greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()