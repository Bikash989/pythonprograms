
students = [('Timmy', 95, 'Will pass'), ('Martha', 70), ('Betty', 82, 'Will pass'), ('Stewart', 50, 'Will not pass'), ('Ashley', 68), ('Natalie', 99, 'Will pass'), ('Archie', 71), ('Carl', 45, 'Will not pass')]

passing = {'Will pass': 0, 'Will not pass': 0}
not_processed = 0
for tup in students:
    try:
        if tup[2] == 'Will pass':
            passing['Will pass'] += 1
        elif tup[2] == 'Will not pass':
            passing['Will not pass'] += 1
    except Exception:
        not_processed += 1
print('''With the help of exception those student whose values is not provided
whether they will pass or not, will be ignored or else
the program would crash''')
print("Total student ",len(students))
print("Student not taken in consideration: ",not_processed)
print("Will pass: ",passing['Will pass'])
print("Will not pass: ",passing['Will not pass'])
