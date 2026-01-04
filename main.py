import tkinter 




window = tkinter.Tk()
window.title("Survey form")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

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

survey_questions_frame = tkinter.LabelFrame(frame)
survey_questions_frame.grid(row=1,column=0, sticky= "news", padx=10, pady=25)

question_1_label = tkinter.Label(survey_questions_frame, text="Question 1. Please let us know how your experience was with our company?")
question_1_label.grid(row=0, column=0)
question_1_input = tkinter.Text(survey_questions_frame, height=5, width=30, bd=2)
question_1_input.grid(row=1,column=0, sticky="news")

question_2_label = tkinter.Label(survey_questions_frame, text="Question 2. What could we have changed to make your experience better?")
question_2_label.grid(row=2,column=0)
question_2_input = tkinter.Text(survey_questions_frame, height=5, width=30, bd=2)
question_2_input.grid(row=3, column=0, sticky="news" )

question_3_label = tkinter.Label(survey_questions_frame, text="Question 3. What additional or  general comments would you like to add?")
question_3_label.grid(row=4, column=0)
question_3_input = tkinter.Text(survey_questions_frame, height=5, width=30, bd=2)
question_3_input.grid(row=5, column=0, sticky="news") 

question_4_label = tkinter.Label(survey_questions_frame, text="Question 4. On a Scale of 1 to 5 how would you rate your overall service? ")
question_4_label.grid(row=6, column=0)
# question_4_star_rating 
for widget in survey_questions_frame.winfo_children():
    widget.grid_configure(padx=20, pady=10)

window.mainloop()