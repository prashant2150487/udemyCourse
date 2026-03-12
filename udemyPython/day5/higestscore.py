scores = [12, 13, 14, 1, 15, 151, 51, 4413, 12, 3, 124, 5, 45, 4, 6, 6, 7, 7]
# total_exam_score = sum(scores)
# print(total_exam_score)

max_score = 0
for score in scores:
    if score > max_score:
        max_score = score


print(max_score)