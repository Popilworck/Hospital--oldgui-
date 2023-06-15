#do appointments if you can\
import tkinter as tk
import modules,tkintermods as k
import csv
ii='Invalid input, Please re-enter'
post=1
chimp = k.lors()[0]
if chimp == 2:
    pass
elif chimp == 1:
    k.inputsignup()
else:
    k.inputlogin()
k.menu()
# while True:
#     if post ==1 :
#         print("""Enter:
#         1 to add a doctor
#         2 to remove a doctor
#         3 to display all doctors
#         4 to update a doctor information
#         5 to display all patients assigned to a doctor
#         6 to assign a new patient to a doctor
#         7 to update patients assigned to a doctor""")
#         opt1 = eval(input())
#         if opt1 == 4:
#             while True:
#                 choice1 = eval(input("Enter 1 to change name and 2 to change id:\t"))
#                 if  type(choice1)== int:
#                     doci = input("Enter data to update:\t")
#                     modules.updoc(doci,choice1)
#                     break
#                 else:
#                     print(ii)
#         elif opt1==5:
#             modules.sdp(input("Enter doctors name"))
#         elif opt1 == 6:
#             modules.addpat(input('Enter Doctors name:\t'))
#         elif opt1 == 7:
#             print("""Enter:
#                   1 to remove all patients assigned to this doctor
#                   2 to remove one patient assigned to this doctor
#                   3 to update a patiets name""")
#             modules.uppat(eval(input()),input("Enter doctors name:\t"))
#         else:
#             print(ii)
#     else:
#       pass