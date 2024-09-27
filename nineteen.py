class WorkStudyPosition:
    def __init__(self, job_id, title, description):
        self.job_id = job_id
        self.title = title
        self.description = description


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.assigned_jobs = []
        self.performance = {}


class WorkStudySystem:
    def __init__(self):
        self.jobs = {}
        self.students = {}

    def create_job(self, job_id, title, description):
        if job_id not in self.jobs:
            self.jobs[job_id] = WorkStudyPosition(job_id, title, description)
            print(f"Job '{title}' created.")
        else:
            print("Job ID already exists.")

    def read_job(self, job_id):
        job = self.jobs.get(job_id)
        return job.__dict__ if job else "Job not found."

    def delete_job(self, job_id):
        if job_id in self.jobs:
            del self.jobs[job_id]
            print("Job deleted.")
        else:
            print("Job not found.")

    def assign_work_study_jobs(self, student_id, job_id):
        if student_id not in self.students:
            print("Student not found.")
            return
        if job_id not in self.jobs:
            print("Job not found.")
            return

        student = self.students[student_id]
        student.assigned_jobs.append(job_id)
        print(f"Student {student.name} assigned to job '{self.jobs[job_id].title}'.")

    def track_job_performance(self, student_id, performance_id, feedback):
        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]
        student.performance[performance_id] = feedback
        print(f"Performance for student {student.name} recorded.")

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added.")
        else:
            print("Student ID already exists.")


system = WorkStudySystem()
system.create_job(1, "Library Assistant", "Assist with book sorting and shelving.")
system.create_job(2, "IT Support", "Provide tech support to students.")
system.add_student(101, "Alice Smith")
system.add_student(102, "Bob Johnson")

system.assign_work_study_jobs(101, 1)
system.track_job_performance(101, 1, "Excellent performance, very helpful.")
print(system.read_job(1))
print(system.students[101].__dict__)
