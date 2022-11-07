import random, pyperclip
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = [char.upper() for char in lower_letters]
symbols = [symbol for symbol in "!#$()*+-<=>?[\]_" ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

all_chars = lower_letters+upper_letters+symbols+numbers

def generate():
    pwd = random.choice(lower_letters)
    password_input.delete(0, 'end')

    for i in range(12):
        pwd += random.choice(all_chars)
    
    password_input.insert(END, string=pwd)
    pyperclip.copy(pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():

    em = email_input.get()
    web = website_input.get()
    p = password_input.get()

    if len(em) <1 or len(web) <1 or len(p) < 1:
        messagebox.showwarning(title="Oops", message="You left some fields empty")
    else:
        is_ok = messagebox.askokcancel(title="save", message=f"These are the credentials, do you wanna continue?\nEmail: {em}\nWebsite: {web}\nPassword: {p}")

        if is_ok:
            with open('passwords.txt', 'a') as f:
                f.write(web + "  |  " + em + "  |  " + p + "\n")

            password_input.delete(0, 'end')
            website_input.delete(0, 'end')
            email_input.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# logo image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
 
# website label and entry
website = Label(text="Website: ")
website.grid(row=1, column=0)
website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# email label and entry
email = Label(text="Email/Username: ")
email.grid(row=2, column=0)
email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)
# email_input.focus()

# password label and entry
password = Label(text="Password: ")
password.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)
# password_input.focus()
# generate password
generate = Button(text="Generate Password", command=generate)
generate.grid(row=3, column=2)


# Add button
add = Button(text="Add", width=36, command=add_password)
add.grid(row=4, column=1, columnspan=2)




window.mainloop()