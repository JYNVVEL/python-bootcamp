from statistics import mean

student_scores = [98, 75, 100, 86, 100, 3]

average_score = mean(student_scores)
print(average_score)
rankings = (sorted(student_scores, reverse=True))
print(rankings)

for rank in sorted(rankings, reverse=True):
    print(rank)

