# Lucia Kearney
# Combining both job display frame and job entry frame in one program (no switching between frames yet)
# version 8

from tkinter import *

# setting constants for calculating the job cost
VIRUS_RATE = 0.8
WOF_RATE = 100
DIST_BASE_RATE = 10
DIST_RATE = 0.5
DIST_BASE_MIN = 5


# support class for individual jobs
class Job:
    def __init__(self, num, name, dist, virus, wof, minutes, charge):
        self.num = num
        self.name = name
        self.dist = dist
        self.virus = virus
        self.wof = wof
        self.minutes = minutes
        self.charge = charge


# a class containing all the GUI
class JobManagementGUI:
    def __init__(self, parent):
        # a list that keeps track of the Job objects
        self.job_list = []

        # example jobs for testing
        self.job_list.append(Job(1, "Bindi", 20, True, True, 38, 147.9))
        self.job_list.append(Job(2, "Dash", 46, False, True, 0, 130.5))
        self.job_list.append(Job(3, "Hippo", 1, True, True, 50, 150))
        self.job_list.append(Job(4, "Honey", 4, True, False, 7, 15.6))
        self.logo_img = PhotoImage(file="logo.gif")

        # variables for the entry frame
        self.next_id = len(self.job_list) + 1
        self.customer_name = StringVar()
        self.distance = IntVar()
        self.virus = IntVar()
        self.wof = IntVar()
        self.minutes = StringVar()
        self.minutes.set("0")

        # variable for the display frame
        self.position = 0

        # display frame GUI
        self.display_frame = Frame(parent)

        self.display_label = Label(self.display_frame,
                                   text="Displaying Job: {}/{}".format(self.position + 1, len(self.job_list)))
        self.display_label.grid(row=0, column=0, pady=10)

        self.add_but = Button(self.display_frame, text="New Job")
        self.add_but.grid(row=0, column=1)

        disp_num_desc_label = Label(self.display_frame, text="Job number:")
        disp_num_desc_label.grid(row=1, column=0, sticky=E, padx=10)

        self.job_num_label = Label(self.display_frame, text=self.job_list[self.position].num)
        self.job_num_label.grid(row=1, column=1, sticky=W, padx=10)

        disp_name_desc_label = Label(self.display_frame, text="Customer name:")
        disp_name_desc_label.grid(row=2, column=0, sticky=E, padx=10)

        self.name_label = Label(self.display_frame, text=self.job_list[self.position].name)
        self.name_label.grid(row=2, column=1, sticky=W, padx=10)

        disp_charge_desc_label = Label(self.display_frame, text="Job charge:")
        disp_charge_desc_label.grid(row=3, column=0, sticky=E, padx=10)

        self.charge_label = Label(self.display_frame, text="${:.2f}".format(self.job_list[self.position].charge))
        self.charge_label.grid(row=3, column=1, sticky=W, padx=10)

        self.back_but = Button(self.display_frame, text="Back", command=self.back, state=DISABLED)
        self.back_but.grid(row=4, column=0, pady=10, sticky=W, padx=25)

        self.next_but = Button(self.display_frame, text="Next", command=self.next)
        self.next_but.grid(row=4, column=1, pady=10, sticky=E, padx=25)

        logo = Label(self.display_frame, image=self.logo_img)
        logo.grid(row=5, column=0, columnspan=2)

        self.display_frame.grid(row=0, column=0, padx=5, pady=5)

        # entry frame GUI

        self.entry_frame = Frame(parent)

        title_label = Label(self.entry_frame, text="Enter Job Details:")
        title_label.grid(row=0, column=0, columnspan=2, pady=5)

        num_desc_label = Label(self.entry_frame, text="Job number:")
        num_desc_label.grid(row=1, column=0, pady=5)

        self.num_label = Label(self.entry_frame, text=self.next_id)
        self.num_label.grid(row=1, column=1)

        name_desc_label = Label(self.entry_frame, text="Customer name:")
        name_desc_label.grid(row=2, column=0)

        self.name_entry = Entry(self.entry_frame, textvariable=self.customer_name)
        self.name_entry.grid(row=2, column=1)

        dist_desc_label = Label(self.entry_frame, text="Distance travelled (in km):")
        dist_desc_label.grid(row=3, column=0)

        self.dist_slider = Scale(self.entry_frame, orient=HORIZONTAL, variable=self.distance, sliderlength="15px")
        self.dist_slider.grid(row=3, column=1, pady=10, sticky=N)

        self.virus_check = Checkbutton(self.entry_frame, text="Virus Protection", variable=self.virus, onvalue=1,
                                       offvalue=0, command=self.toggle_min)
        self.virus_check.grid(row=4, column=0, pady=10)

        self.wof_check = Checkbutton(self.entry_frame, text="WOF and tune", variable=self.wof, onvalue=1, offvalue=0)
        self.wof_check.grid(row=4, column=1, pady=10)

        self.min_desc_label = Label(self.entry_frame, text="Minutes spent:", fg="#949494")
        self.min_desc_label.grid(row=5, column=0)

        self.min_entry = Entry(self.entry_frame, textvariable=self.minutes, state=DISABLED, width=5)
        self.min_entry.grid(row=6, column=0, pady=5)

        self.cancel_but = Button(self.entry_frame, text="Cancel")
        self.cancel_but.grid(row=7, column=0, pady=10)

        self.submit_but = Button(self.entry_frame, text="Submit", command=self.printjob)
        self.submit_but.grid(row=7, column=1, pady=10)

    def printjob(self):
        min_number = int(self.minutes.get())
        if self.virus.get() == 1:
            virus_selected = True
        else:
            virus_selected = False
            min_number = 0
        if self.wof.get() == 1:
            wof_selected = True
        else:
            wof_selected = False

        charge = self.calc_charge(min_number, virus_selected, wof_selected, self.distance.get())

        self.job_list.append(
            Job(self.next_id, self.customer_name.get(), self.distance.get(), virus_selected, wof_selected, min_number,
                charge))

        print(self.job_list[-1].num)
        print(self.job_list[-1].name)
        print(self.job_list[-1].dist)
        print(self.job_list[-1].virus)
        print(self.job_list[-1].wof)
        print(self.job_list[-1].minutes)
        print(self.job_list[-1].charge)
        print()

        self.next_id = len(self.job_list) + 1
        self.num_label.configure(text=self.next_id)

    def toggle_min(self):
        if self.virus.get() == 1:
            self.min_entry.configure(state=NORMAL)
            self.min_desc_label.configure(fg="black")
        else:
            self.min_entry.configure(state=DISABLED)
            self.min_desc_label.configure(fg="#949494")
            self.minutes.set("0")

    def calc_charge(self, minutes, virus, wof, dist):
        charge = 0
        if virus == True:
            charge += VIRUS_RATE * minutes
        if wof == True:
            charge += WOF_RATE

        charge += DIST_BASE_RATE
        if dist > DIST_BASE_MIN:
            dist -= DIST_BASE_MIN
            charge += DIST_RATE * dist

        return charge

    def next(self):
        self.position += 1
        self.check_pos_update()

    def back(self):
        self.position -= 1
        self.check_pos_update()

    def check_pos_update(self):
        if self.position == len(self.job_list) - 1:
            self.next_but.configure(state=DISABLED)
        else:
            self.next_but.configure(state=NORMAL)

        if self.position == 0:
            self.back_but.configure(state=DISABLED)
        else:
            self.back_but.configure(state=NORMAL)

        self.display_label.configure(text="Displaying Job: {}/{}".format(self.position + 1, len(self.job_list)))
        self.job_num_label.configure(text=self.job_list[self.position].num)
        self.name_label.configure(text=self.job_list[self.position].name)
        self.charge_label.configure(text="${:.2f}".format(self.job_list[self.position].charge))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Management Program")
    JobManager = JobManagementGUI(root)
    root.mainloop()
