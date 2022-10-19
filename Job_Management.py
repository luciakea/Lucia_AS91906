# Lucia Kearney
# Prints job details entered to shell
# Version 2
from tkinter import *


class JobManagementGUI:
    def __init__(self, parent):
        self.entry_frame = Frame(parent)

        self.customer_name = StringVar()
        self.distance = IntVar()
        self.virus = IntVar()
        self.wof = IntVar()
        self.minutes = StringVar()

        self.entry_frame = Frame(parent)

        title_label = Label(self.entry_frame, text="Enter Job Details:")

        name_desc_label = Label(self.entry_frame, text="Customer name:")
        name_desc_label.grid(row=2, column=0)

        self.name_entry = Entry(self.entry_frame)
        self.name_entry = Entry(self.entry_frame, textvariable=self.customer_name)
        self.name_entry.grid(row=2, column=1)

        dist_desc_label = Label(self.entry_frame, text="Distance travelled:")
        dist_desc_label = Label(self.entry_frame, text="Distance travelled (in km):")
        dist_desc_label.grid(row=3, column=0)

        self.dist_slider = Scale(self.entry_frame, orient=HORIZONTAL)
        self.dist_slider = Scale(self.entry_frame, orient=HORIZONTAL, variable=self.distance, sliderlength="15px")
        self.dist_slider.grid(row=3, column=1)

        self.virus_check = Checkbutton(self.entry_frame, text="Virus Protection")
        self.virus_check = Checkbutton(self.entry_frame, text="Virus Protection", variable=self.virus, onvalue=1,
                                       offvalue=0, command=self.toggle_min)
        self.virus_check.grid(row=4, column=0)

        self.wof_check = Checkbutton(self.entry_frame, text="WOF and tune")
        self.wof_check = Checkbutton(self.entry_frame, text="WOF and tune", variable=self.wof, onvalue=1, offvalue=0)
        self.wof_check.grid(row=4, column=1)

        self.min_desc_label = Label(self.entry_frame, text="Minutes spent:")
        self.min_desc_label.grid(row=5, column=0)

        self.min_entry = Entry(self.entry_frame)
        self.min_entry = Entry(self.entry_frame, textvariable=self.minutes, state=DISABLED)
        self.min_entry.grid(row=6, column=0)

        self.cancel_but = Button(self.entry_frame, text="Cancel")
        self.cancel_but.grid(row=7, column=0)

        self.submit_but = Button(self.entry_frame, text="Submit")
        self.submit_but = Button(self.entry_frame, text="Submit", command=self.printjob)
        self.submit_but.grid(row=7, column=1)

        self.entry_frame.grid(row=0, column=0)

    def printjob(self):
        print(self.customer_name.get())
        print(self.distance.get())
        if self.virus.get() == 1:
            print("Virus protection")
        if self.wof.get() == 1:
            print("WOF and tune")
        print(self.minutes.get())
        print("----------")

    def toggle_min(self):
        if self.virus.get() == 1:
            self.min_entry.configure(state=NORMAL)
        else:
            self.min_entry.configure(state=DISABLED)
            self.minutes.set("")

    # main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Management Program")
    JobManager = JobManagementGUI(root)
    root.mainloop()
