# Lucia Kearney
# Summary frame to show all submitted jobs
# Version 1 (Summary frame)
# Version 18 (overall)

from tkinter import *
from tkinter.scrolledtext import *

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
        # summary frame GUI
        self.summary_frame = Frame(parent)

        summary_title_label = Label(self.summary_frame, text="Showing all Jobs")
        summary_title_label.grid(row=0, column=0, pady=5, padx=10)

        self.back_menu_but = Button(self.summary_frame, text="Back")
        self.back_menu_but.grid(row=0, column=1, pady=5, padx=10, sticky=W)

        self.job_display = ScrolledText(self.summary_frame, width=35, height=10, wrap="word")
        self.job_display.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        total_dist_label = Label(self.summary_frame, text="Total distance travelled:")
        total_dist_label.grid(row=2, column=0, pady=5)

        self.total_dist = Label(self.summary_frame, text="TEST")
        self.total_dist.grid(row=2, column=1, pady=5, sticky=W)

        total_charge_label = Label(self.summary_frame, text="Total money charged:")
        total_charge_label.grid(row=3, column=0)

        self.total_charge = Label(self.summary_frame, text="TEST")
        self.total_charge.grid(row=3, column=1, pady=5, sticky=W)

        total_jobs_label = Label(self.summary_frame, text="Total number of jobs:")
        total_jobs_label.grid(row=4, column=0, pady=5)

        self.total_jobs = Label(self.summary_frame, text="TEST")
        self.total_jobs.grid(row=4, column=1, pady=5, sticky=W)

        self.summary_frame.grid(row=0, column=0, pady=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Management Program")
    JobManager = JobManagementGUI(root)
    root.mainloop()
