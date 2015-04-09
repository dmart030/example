
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

while i < 8:
    final_grade[i] = 100 * (x[i]/10. + y[i]/10. + z[i]/10.)/3.0
    i += 1
print("Final Grades are:")

for n in final_grade:
    print round(n,2),'%'
j = 0
i = 0
g = 0
while i < 8:
    if final_grade[i] < 60.0:
        j += 1
    if final_grade[i] > 95.5:
        g += 1
    i += 1
w = round(g /10.,2)
print"The number of failed students are: ",j, "\n"
print"The grades of the failed students are: F\n"
print"The number of outstanding students are: ", g, "\n"
print"The fraction of outstanding students is: ",w , "%", "\n"
print"The histogram of the grades is: "


plt.hist(final_grade,bins = 8)
plt.title("histogragh of grades is: ")
plt.xlabel("grades")
plt.ylabel("Frequency")
plt.xlim([40,100])
plt.show()
plt.savefig('Histograph.png')

