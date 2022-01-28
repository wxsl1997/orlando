import random

score = random.randrange(0, 100, 1)

if score >= 90:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "E"

makeUp = False if score >= 60 else True
print("score:%-2d, grade:%s, make up:%-8s " % (score, grade, makeUp))
