import sys

results = []
subjects = []
grade = ''
total = 0

def get_grade(score):
    if score >= 75:
        return 'A'
    elif 75 > score >= 50:
        return 'B'
    elif 50 > score >= 30:
        return 'C'
    elif 30 > score >= 20:
        return 'D'
    elif 20 > score:
        return 'F'

while True:
    try:
        subject = input('What is the subject? ')
        while True:
            try:
                marks = int(input('What is the score? '))
                results.append({subject: marks})
                break
            except ValueError:
                print('Please enter the correct subject score in numbers')
                continue
        subjects.append(subject)
    except EOFError:
        print('===========================')
        print('Here are your exam results')
        print('===========================')
        i=0
        for result in results:
            # print(result)
            # print(result[subjects[i]])
            grade = get_grade(result[subjects[i]])
            print(f"You have got {grade} for the subject - {subjects[i]}")
            total += result[subjects[i]]
            i += 1
        final_grade = get_grade(total/i)
        print(f"You have got {final_grade} as the final grade for the exam for scoring {total/i} on average for the above {i} subjects")
        sys.exit()
    except ValueError:
        print('Enter valid numeric value')

