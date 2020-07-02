import tkinter
from tkinter import *
root = Tk()
root.title("Pandemic Analytics Engine")


label_1 = Label(root,font=("helvetica", 22, "bold"), text="Pandemic Analytics Engine")
label_1.grid(row=1,columnspan = 1)

label_2 = Label(root, text="Enter State ")
label_2.grid(row=2)
entry_1 = Entry(root)
entry_1.grid(row=2, column=2)

label_3 = Label(root, text="Total number of ppl")
label_3.grid(row=3)
entry_2 = Entry(root)
entry_2.grid(row=3, column=2)

label_4 = Label(root, text="Infected")
label_4.grid(row=4)
entry_3 = Entry(root)
entry_3.grid(row=4, column=2)

label_5 = Label(root, text="Deceased")
label_5.grid(row=5)
entry_4 = Entry(root)
entry_4.grid(row=5, column=2)



def calculation():

    total_ppl = entry_2.get()
    int_total_ppl = int(total_ppl)

    infected = entry_3.get()
    int_infected = int(infected)

    deceased = entry_4.get()
    int_deceased = int(deceased)

    ifr = (int_deceased / int_infected) * 100
    cmr = (int_deceased / int_total_ppl)

    root = Tk()
    root.title("Report")

    label_1 = Label(root, font=("helvetica", 22, "bold"), text="Result")
    label_1.grid(row=1, columnspan=1)

    label_2 = Label(root, font=("courier", 12, "bold"), text="IFR : ")
    label_2.grid(row=2, column=1, padx=10, pady=10)
    label_3 = Label(root, text=ifr)
    label_3.grid(row=2, column=2)

    label_4 = Label(root, font=("courier", 12, "bold"), text="CMR : ")
    label_4.grid(row=3, column=1, padx=10, pady=10)
    label_5 = Label(root, text=cmr)
    label_5.grid(row=3, column=2)

button1 = Button(root, text="Calculate IFR & CMR ",command=calculation)
button1.grid(column=2)
root.mainloop()