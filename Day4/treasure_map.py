#write a program that will mark a spot with an X.
#The first digit in the input will specify the column (the position on the horizontal axis).
#The second digit in the input will specify the row number (the position on the vertical axis).

row1 = ["[]","[]","[]"]
row2 = ["[]","[]","[]"]
row3 = ["[]","[]","[]"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? (col no, row no) ")


#Write your code below this row 👇
c,r = int(position[0])-1, int(position[1])
#print(r)
if r == 1:
    row1[c] ="X"
elif r == 2:
    row2[c] ="X"
else:
    row3[c] ="X"

print(f"{row1}\n{row2}\n{row3}")    
