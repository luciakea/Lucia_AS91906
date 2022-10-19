# Lucia Kearney
# Display frame GUI setup
# version 5 (overall)
# (version 1 of display frame development)
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
        self.job_list.append(JOB)
        self.logo_img = PhotoImage(file="logo.gif")

        self.display_frame = Frame(parent)

        self.display_label = Label(self.display_frame, text="Displaying Job: {}/{}".format(JOB.num, len(self.job_list)))
        self.display_label.grid(row=0, column=0, pady=10)

        self.add_but = Button(self.display_frame, text="New Job")
        self.add_but.grid(row=0, column=1)

        disp_num_desc_label = Label(self.display_frame, text="Job number:")
        disp_num_desc_label.grid(row=1, column=0, sticky=E, padx=10)

        self.job_num_label = Label(self.display_frame, text=JOB.num)
        self.job_num_label.grid(row=1, column=1, sticky=W, padx=10)

        disp_name_desc_label = Label(self.display_frame, text="Customer name:")
        disp_name_desc_label.grid(row=2, column=0, sticky=E, padx=10)

        self.name_label = Label(self.display_frame, text=JOB.name)
        self.name_label.grid(row=2, column=1, sticky=W, padx=10)

        disp_charge_desc_label = Label(self.display_frame, text="Job charge:")
        disp_charge_desc_label.grid(row=3, column=0, sticky=E, padx=10)

        self.charge_label = Label(self.display_frame, text="${:.2f}".format(JOB.charge))
        self.charge_label.grid(row=3, column=1, sticky=W, padx=10)

        back_but = Button(self.display_frame, text="Back")
        back_but.grid(row=4, column=0, pady=10, sticky=W, padx=25)

        next_but = Button(self.display_frame, text="Next")
        next_but.grid(row=4, column=1, pady=10, sticky=E, padx=25)

        logo = Label(self.display_frame, image=self.logo_img)
        logo.grid(row=5, column=0, columnspan=2)

        self.display_frame.grid(row=0, column=0, padx=5, pady=5)


# main routine
if __name__ == "__main__":
    # hard coded job for testing
    JOB = Job(1, "Bindi", 20, True, True, 38, 147.9)

    root = Tk()
    root.title("Job Management Program")
    JobManager = JobManagementGUI(root)
    root.mainloop()
