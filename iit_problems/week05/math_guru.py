import sys
import random
import operator
from datetime import datetime
import asyncio

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

operators_list = ['+','-','*','/']
answers = []
actual_answers = []

def questions():
    try:
        while True:
            rand_one = random.randint(1,9)
            rand_two = random.randint(1,9)
            rand_operator = random.choice(operators_list)

            op = operators[rand_operator]
            actual_answer = op(rand_one, rand_two)
            if actual_answer != int(actual_answer):
                continue
            actual_answers.append(actual_answer)
            while True:
                try:
                    answer = int(input(f'What is {rand_one} {rand_operator} {rand_two}: '))
                    answers.append((f'What is {rand_one} {rand_operator} {rand_two}', answer))
                    break
                except ValueError:
                    print('Enter a valid answer in numeric format')
                    # continue
    except Exception as e:
        pass

async def main():
    loop = asyncio.get_event_loop()
    try:
        await asyncio.wait_for(loop.run_in_executor(None, questions), timeout=10)
    except asyncio.TimeoutError:
        print("\n--- Time's up! ---")
        # print("Your answers:", answers)
        # print("Actual answers:", actual_answers)
        i = 0
        for item in answers:
            # print(answer[0])
            print(f"{i+1} Question {i+1}: {item[0]}\nAnswer {item[1]}\nCorrect answer: {actual_answers[i]}")
            i += 1
    

asyncio.run(main())