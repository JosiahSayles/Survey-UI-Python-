import tkinter 
from tkinter import messagebox

def survey_data(): 
    username = user_name_input.get()
    email = user_email_input.get()
    if username and email: 
        question1 = question_1_input.get("1.0", "end")
        question2 = question_2_input.get("1.0", "end")
        question3 = question_3_input.get("1.0", "end")
        starrating = rating_label.cget("text")

        print("User name: ", username, "Email: ", email)
        print("Question 1: ", question1)
        print("Question 2: ", question2)
        print("Question 3: ", question3)
        print("Rating: ", starrating)
        print("-------------------------------------------")
    else: 
        tkinter.messagebox.showwarning(title="Error", message="User name and email are required")   



def set_rating(rating):
    for i in range(1,6):
        if i <= rating: 
            star_buttons[i-1].config(text="★", fg="#FFD700")
        else: 
            star_buttons[i-1].config(text="☆", fg="black")   
    rating_label.config(text=f"Rating: {rating}/5") 

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


for widget in survey_questions_frame.winfo_children():
    widget.grid_configure(padx=20, pady=10)


Rating_label = tkinter.Label(window, text="Please rate your experience from 1-5.")
Rating_label.pack()

star_frame = tkinter.Frame(window)

star_frame.pack()

star_buttons =[]
for i in range(1,6):
    btn = tkinter.Button(star_frame, text="☆", fg="black", cursor="hand2",  command=lambda r=i: set_rating(r))
    btn.pack(side="left")
    star_buttons.append(btn)

rating_label= tkinter.Label(star_frame, text="Rating:0/5")
rating_label.pack(pady=30)   


button_frame= tkinter.Frame(window)
button_frame.pack()

button = tkinter.Button(button_frame, text="Submit", command= survey_data)
button.pack(pady=10 )


window.mainloop()