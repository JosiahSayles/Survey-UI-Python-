import tkinter
from tkinter import ttk
from tkinter import messagebox


window = tkinter.Tk()
window.title("Survey form")

frame = tkinter.Frame(window)
frame.pack()

#Survey User Info 

survey_user_info_frame = tkinter.LabelFrame(frame, text="Survey User Information")
survey_user_info_frame.grid(row=0, column=0, padx=10, pady=5)

user_name_label = tkinter.Label(survey_user_info_frame, text="Full Name")
user_name_label.grid(row=0, column=0)
user_email_lable = tkinter.Label(survey_user_info_frame, text="Email")
user_email_lable.grid(row=0, column=1)
user_phone_number_label = tkinter.Label(survey_user_info_frame, text="Phone number")
user_phone_number_label.grid(row=0, column=2)
user_zipcode_label = tkinter.Label(survey_user_info_frame, text="Zipcode")
user_zipcode_label.grid(row=0, column=3)

user_name_input = tkinter.Entry(survey_user_info_frame)
user_email_input = tkinter.Entry(survey_user_info_frame)
user_phone_number_input = tkinter.Entry(survey_user_info_frame)
user_zipcode_input = tkinter.Entry(survey_user_info_frame)
user_name_input.grid(row=1, column=0)
user_email_input.grid(row=1, column=1)
user_phone_number_input.grid(row=1, column=2)
user_zipcode_input.grid(row=1,column=3)

for widget in survey_user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)


#Survey questions 



window.mainloop()