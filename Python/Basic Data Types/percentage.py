n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    score = sum(scores) / 3
    student_marks[name] = score
query_name = input()
print("{0:.2f}".format(student_marks[query_name]))
