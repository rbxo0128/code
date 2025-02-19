import sys

grades = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
    "P" : 0.0
}


# n = int(sys.stdin.readline())

score = 0
average = 0

for i in range(20):
    no, num, grade = sys.stdin.readline().split()
    if grade == "P":
        continue
    score += grades[grade] * float(num)
    average += float(num)

print(score/average)