student_names = ('Juan', 'Maria', 'Joseph')
student_scores = (70, 90, 81)

high_score_name = student_names[0]
high_score = student_scores[0]

for name, score in zip(student_names, student_scores):
    print(f"Student: {name} scored {score} in the exam")
    if score > high_score:
        high_score_name = name
        high_score = score
print(f"Highest Score: ", high_score_name)