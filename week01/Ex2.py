
'''
Dominic Martinez-Ta
Physics 177
Laboratory 1
'''

import matplotlib.pyplot as plt


print("Dominic Martinez-Ta, Physics 177, lab 1")
print("2) Student's final grades")
x = Homework = [10,10,8,9,9.5,3,9,0,6]
y = Mid_term = [10,10,10,10,8,5,10,7]
z = Final_project= [9,10,10,6,10,6,8,9]
final_grade = [0,0,0,0,0,0,0,0]

i = 0
failed_grades = []
while i < 8:
    final_grade[i] =(x[i]*0.4 + y[i]*0.2 + z[i]*0.4)
    if final_grade[i] < 6.5:
        failed_grades.append(final_grade[i])
    i += 1
print("Final Grades are:")

for n in final_grade:
    print round(n,2)
j = 0
i = 0
g = 0
while i < 8:
    if final_grade[i] < 6.0:
        j += 1
    if final_grade[i] > 9.5:
        g += 1
    i += 1
w = round(g/8.,2)
print"The number of failed students are: ",j, "\n"
print"The grades of the failed students are:", failed_grades, "\n"

print"The number of outstanding students are: ", g, "\n"
print"The fraction of outstanding students is: ",w , "%", "\n"
print"The histogram of the grades is: "


plt.hist(final_grade,bins = 8)
plt.title("histogragh of grades is: ")
plt.xlabel("grades")
plt.ylabel("Frequency")
plt.xlim(0,10)
plt.show()
plt.savefig('Histograph.png')

