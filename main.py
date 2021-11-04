# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import json
from tkinter import messagebox


def find_password():
    web = web_entry.get()
    try:
        with open("data.json","r") as file:
            json_data = json.load(file)
            print(json_data)
    except FileNotFoundError:
        messagebox.showwarning(title="ERROR", message="no details for the website exists")
        web_entry.delete(0, END)
    else:
        try:
            searched_web = json_data[web]["email"]
        except KeyError:
            messagebox.showwarning(title="ERROR", message="No data file found")
            web_entry.delete(0, END)
        else:
            searched_password = json_data[web]["password"]

            messagebox.showinfo(title="wesite has found", message=f"Email: {searched_web}\nPassword: {searched_password}")
            web_entry.delete(0,END)

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list =[]
    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]
    random.shuffle(password_list)
    password = ""
    for char in password_list:
      password += char
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = web_entry.get()
    email = user_entry.get()
    pas = password_entry.get()
    data = {
        web: {
            "email": email,
            "password": pas
        }
    }

    if len(web) == 0 and len(pas) == 0:
        messagebox.showwarning(title="Error", message="Please enter details")
    elif len(pas) < 10:
        messagebox.showwarning(title="Error", message="length of password must be 10 or more")
    else:
        try:
             with open("data.json", "r") as file:
                # file.write(f"{data}\n")
                old_data = json.load(file)

        except FileNotFoundError:
             with open("data.json", "w") as file:
                 json.dump(data, file, indent=4)

        else:
             old_data.update(data)

             with open("data.json", "w") as file:
                 json.dump(old_data, file, indent=4)
        finally:
             web_entry.delete(0, END)
             password_entry.delete(0, END)


            # with open("data.json", "w") as file:
            #     json.dump(data, file, indent=4)
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
# creating window
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20, pady=20)
# creating canvas
canvas = Canvas(width=200, height=200)
# creating img
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
# creating web entry
web_site = Label(text="Website:")
web_site.grid(row=1, column=0)
website_name = StringVar()
web_entry = Entry(width=35, textvariable=website_name)
web_entry.focus()
web_entry.grid(row=1, column=1,  columnspan=2)
search_button = Button(text="Search",width=15, highlightthickness=0, command=find_password)
search_button.grid(row=1, column=3)
# creating user_entry
user_name = Label(text="Email/Username:")
user_name.grid(row=2, column=0)
user = StringVar()
user_entry = Entry(width=35, textvariable=user)
user_entry.insert(0, "example@gamil.com")
user_entry.grid(row=2, column=1,  columnspan=2)
# creating password Entry
password = Label(text="Password:")
password.grid(row=3, column=0)
password = StringVar()
password_entry = Entry(width=21, textvariable=password)
password_entry.grid(row=3,column=1)
# creating password button
button = Button(text="Generate Password", highlightthickness=0, command=generate)
button.grid(row=3, column=3,)
add_button = Button(text="add", width=35, highlightthickness=0, command=save)
add_button.grid( row=4, column=1,columnspan=2)

window.mainloop()