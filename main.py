import random, pyperclip, json
from tkinter import *
from tkinter import messagebox

# ---------------------------- SEARCH ENTRIES ------------------------------- #
def search():
    web = website_input.get()
    e = "email"
    p = "password"
    try:
        with open('passwords.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("You have to add a website first!")
    else:
        if data.get(web):
            messagebox.showinfo(title=web, message=f"Email: {data[web][e]}\nPassword: {data[web][p]}\n")
        else:
            messagebox.showinfo(title=web, message="Website not found")
        

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

    data_dict = { web: {"email":em,"password":p} }

    if len(em) <1 or len(web) <1 or len(p) < 1:
        messagebox.showwarning(title="Oops", message="You left some fields empty")
    else:
        is_ok = messagebox.askokcancel(title="save", message=f"These are the credentials, do you wanna continue?\nEmail: {em}\nWebsite: {web}\nPassword: {p}")

        if is_ok:

            try:
                with open('passwords.json', 'r') as f:
                        data = json.load(f)
                        
            except FileNotFoundError:
                with(open('passwords.json', 'w')) as f:
                    json.dump(data_dict, f, indent=4)
            else:
                data.update(data_dict)

                with open('passwords.json', 'w') as f:
                    json.dump(data, f, indent=4)   
            finally:           
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
website_input = Entry(width=20)
website_input.grid(row=1, column=1, columnspan=1)
website_input.focus()
# search button
search = Button(text="Search", width=15, command=search)
search.grid(row=1, column=2, columnspan=2)

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