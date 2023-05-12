#write a program that calculates the highest score from a List of scores.
#Important you are not allowed to use the max or min functions.

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
max_score = 0
for s in student_scores:
    if s > max_score:
        max_score = s

print("The highest score in the class is: {}".format(max_score))        

