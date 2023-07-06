#write a program that calculates the average student height from a List of heights.
#You should not use the sum() or len() functions in your answer.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
h_sum,s_sum =0,0
for height in student_heights:
    h_sum += height
    s_sum+=1
avg_height = round(h_sum/s_sum)    
print("Average height is :{}".format(avg_height))
