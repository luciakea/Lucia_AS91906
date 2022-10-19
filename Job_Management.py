# Lucia Kearney
# Entry frame gui setup
# Version 1
from tkinter import *


class JobManagementGUI:
    def __init__(self, parent):
        self.entry_frame = Frame(parent)

        title_label = Label(self.entry_frame, text="Enter Job Details:")
        title_label.grid(row=0, column=0, columnspan=2)

        num_desc_label = Label(self.entry_frame, text="Job number:")
        num_desc_label.grid(row=1, column=0)

        self.num_label = Label(self.entry_frame, text="[]")
        self.num_label.grid(row=1, column=1)

        name_desc_label = Label(self.entry_frame, text="Customer name:")
        name_desc_label.grid(row=2, column=0)

        self.name_entry = Entry(self.entry_frame)
        self.name_entry.grid(row=2, column=1)

        dist_desc_label = Label(self.entry_frame, text="Distance travelled:")
        dist_desc_label.grid(row=3, column=0)

        self.dist_slider = Scale(self.entry_frame, orient=HORIZONTAL)
        self.dist_slider.grid(row=3, column=1)

        self.virus_check = Checkbutton(self.entry_frame, text="Virus Protection")
        self.virus_check.grid(row=4, column=0)

        self.wof_check = Checkbutton(self.entry_frame, text="WOF and tune")
        self.wof_check.grid(row=4, column=1)

        self.min_desc_label = Label(self.entry_frame, text="Minutes spent:")
        self.min_desc_label.grid(row=5, column=0)

        self.min_entry = Entry(self.entry_frame)
        self.min_entry.grid(row=6, column=0)

        self.cancel_but = Button(self.entry_frame, text="Cancel")
        self.cancel_but.grid(row=7, column=0)

        self.submit_but = Button(self.entry_frame, text="Submit")
        self.submit_but.grid(row=7, column=1)

        self.entry_frame.grid(row=0, column=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Management Program")
    JobManager = JobManagementGUI(root)
    root.mainloop()
