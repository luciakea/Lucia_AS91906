# Lucia Kearney
# Setting up back button and disabling appropriate buttons when at the start or end of job list
# version 7 (overall)
# (version 3 of display frame development)
from tkinter import *

VIRUS_RATE = 0.8
WOF_RATE = 100
DIST_BASE_RATE = 10
DIST_RATE = 0.5
DIST_BASE_MIN = 5


class Job:
    def __init__(self, num, name, dist, virus, wof, minutes, charge):
        self.num = num
        self.name = name
        self.dist = dist
        self.virus = virus
        self.wof = wof
        self.minutes = minutes
        self.charge = charge


class JobManagementGUI:
    def __init__(self, parent):
        self.job_list = []
        self.job_list.append(Job(1, "Bindi", 20, True, True, 38, 147.9))
        self.job_list.append(Job(2, "Dash", 46, False, True, 0, 130.5))
        self.job_list.append(Job(3, "Hippo", 1, True, True, 50, 150))
        self.job_list.append(Job(4, "Honey", 4, True, False, 7, 15.6))
        self.logo_img = PhotoImage(file="logo.gif")
        self.position = 0
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
