import os

from tkinter import *
from tkinter import messagebox
import lottery

root = Tk()
root.title("Lottery")
root.geometry("400x300")


listbox = Listbox(root, height=4, width=30, bg="gray", activestyle="dotbox", font="Helvetica", fg="blue")
lottery = lottery.Lottery()

Label_amount = Label(root, text="amount of tickets, max 3: ")
Label_amount.grid(row=0, column=0, sticky=E, padx=5, pady=5)

textbox_amount = Entry(root, width=2)
textbox_amount. grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_amount.focus_set()


def update_listbox(amount_tickets):
    listbox.delete(0, END)
    listbox.insert(1, "Congrats! You won")

    try:
        int_amount_tickets = int(amount_tickets)
    
    except ValueError:
        messagebox.showinfo("Only numbers!")
        i = 0

        if (int_amount_tickets < 4):
            while i < int_amount_tickets:
                reward = lottery.get_reward()
                listbox.insert(i + 2, reward)
                i = i + 1
        else:
            messagebox.showinfo("Too many tickets! ")


def clickRandom():
    amount_ticket = textbox_amount.get()
    textbox_amount.delete(0, END)
    textbox_amount.focus_set()

    update_listbox(amount_ticket)


Button_random = Button(text="Try your best!", command=clickRandom)
Button_random.grid(row=1, column=0, columnspan=2, padx=15, pady=15)

listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)













root.mainloop()