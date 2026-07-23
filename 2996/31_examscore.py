'''Exam Score'''
STUDENTS = int(input())
i = 1
BEST_SCORE = 0
BEST_STU = 1

while i <= STUDENTS:
    SCORE = int(input())
    if int(SCORE) == int(BEST_SCORE):
        BEST_SCORE = SCORE
        BEST_STU += 1
    if int(SCORE) > int(BEST_SCORE):
        BEST_SCORE = SCORE
        BEST_STU = 1
    i += 1
if not STUDENTS:
    BEST_STU = 0
print(BEST_SCORE)
print(BEST_STU)
