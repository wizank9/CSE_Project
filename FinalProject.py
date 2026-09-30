subjects = {}
tasks = []
exams = []


def add_subject():
    print("\n========== ADD SUBJECT ==========")

    name = input("Enter subject name: ")
    chapters = int(input("Enter number of chapters: "))

    print("\nDifficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    difficulty_choice = input("Enter choice: ")

    if difficulty_choice == "1":
        difficulty = "Easy"
        points = 1
    elif difficulty_choice == "2":
        difficulty = "Medium"
        points = 2
    elif difficulty_choice == "3":
        difficulty = "Hard"
        points = 3
    else:
        print("Invalid choice.")
        return

    print("\nPriority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input("Enter choice: ")

    if priority_choice == "1":
        priority = "Low"
    elif priority_choice == "2":
        priority = "Medium"
    elif priority_choice == "3":
        priority = "High"
    else:
        print("Invalid choice.")
        return

    subjects[name] = {
        "chapters": chapters,
        "completed": 0,
        "difficulty": difficulty,
        "points": points,
        "priority": priority
    }

    print("\nSubject added successfully!")


def view_subjects():
    print("\n========== YOUR SUBJECTS ==========")

    if len(subjects) == 0:
        print("No subjects added yet.")
        return

    for name, data in subjects.items():

        if data["chapters"] > 0:
            progress = (data["completed"] / data["chapters"]) * 100
        else:
            progress = 0

        print("\nSubject:", name)
        print("Chapters:", data["chapters"])
        print("Completed:", data["completed"])
        print("Difficulty:", data["difficulty"])
        print("Priority:", data["priority"])
        print("Progress:", round(progress, 1), "%")


def add_exam():
    print("\n========== ADD EXAM ==========")

    if len(subjects) == 0:
        print("Please add subjects first.")
        return

    subject = input("Enter subject name: ")

    if subject not in subjects:
        print("Subject not found.")
        return

    exam_name = input("Enter exam name: ")
    exam_date = input("Enter exam date: ")

    exams.append({
        "name": exam_name,
        "subject": subject,
        "date": exam_date
    })

    print("\nExam added successfully!")


def view_exams():
    print("\n========== UPCOMING EXAMS ==========")

    if len(exams) == 0:
        print("No exams added.")
        return

    for exam in exams:
        print("\nExam:", exam["name"])
        print("Subject:", exam["subject"])
        print("Date:", exam["date"])


def create_study_plan():
    print("\n========== CREATE STUDY PLAN ==========")

    if len(subjects) == 0:
        print("Please add subjects first.")
        return

    hours = float(input("Enter available study hours today: "))

    total_points = 0

    for name in subjects:
        total_points += subjects[name]["points"]

    print("\n========== TODAY'S STUDY PLAN ==========")

    total_time = 0

    for name, data in subjects.items():

        if total_points > 0:
            study_time = (data["points"] / total_points) * hours
        else:
            study_time = 0

        print("\nSubject:", name)
        print("Difficulty:", data["difficulty"])
        print("Priority:", data["priority"])
        print("Recommended Time:", round(study_time, 2), "hours")

        total_time += study_time

    print("\nTotal Study Time:", round(total_time, 2), "hours")


def add_task():
    print("\n========== ADD TASK ==========")

    task = input("Enter study task: ")
    subject = input("Enter subject: ")

    tasks.append({
        "task": task,
        "subject": subject,
        "completed": False
    })

    print("Task added successfully!")


def view_tasks():
    print("\n========== STUDY TASKS ==========")

    if len(tasks) == 0:
        print("No tasks added.")
        return

    for i, task in enumerate(tasks, 1):

        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(i, ".", task["task"])
        print("   Subject:", task["subject"])
        print("   Status:", status)


def complete_task():
    print("\n========== COMPLETE TASK ==========")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    number = int(input("\nEnter task number to mark as completed: "))

    if number >= 1 and number <= len(tasks):
        tasks[number - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


def update_progress():
    print("\n========== UPDATE PROGRESS ==========")

    if len(subjects) == 0:
        print("No subjects available.")
        return

    subject = input("Enter subject name: ")

    if subject not in subjects:
        print("Subject not found.")
        return

    completed = int(input("Enter number of completed chapters: "))

    if completed < 0 or completed > subjects[subject]["chapters"]:
        print("Invalid number of chapters.")
        return

    subjects[subject]["completed"] = completed

    print("Progress updated successfully!")


def recommendations():
    print("\n========== STUDY RECOMMENDATIONS ==========")

    if len(subjects) == 0:
        print("Add subjects first.")
        return

    found = False

    for name, data in subjects.items():

        remaining = data["chapters"] - data["completed"]

        if data["priority"] == "High" and remaining > 0:
            print("\nFocus on:", name)
            print("Reason: High priority and chapters are remaining.")
            found = True

        elif data["difficulty"] == "Hard" and remaining > 0:
            print("\nFocus on:", name)
            print("Reason: This subject has a higher difficulty.")
            found = True

    if found == False:
        print("Your current subjects are under control!")
        print("Continue revising and completing your pending tasks.")


def dashboard():
    print("\n========== STUDY DASHBOARD ==========")

    total_chapters = 0
    completed_chapters = 0

    for name, data in subjects.items():
        total_chapters += data["chapters"]
        completed_chapters += data["completed"]

    if total_chapters > 0:
        overall_progress = (completed_chapters / total_chapters) * 100
    else:
        overall_progress = 0

    completed_tasks = 0

    for task in tasks:
        if task["completed"]:
            completed_tasks += 1

    print("Total Subjects:", len(subjects))
    print("Total Exams:", len(exams))
    print("Total Tasks:", len(tasks))
    print("Completed Tasks:", completed_tasks)
    print("Overall Progress:", round(overall_progress, 1), "%")

    print("\nKeep studying and stay consistent!")


def main():

    while True:

        print("\n")
        print("========================================")
        print("          SMART STUDY PLANNER")
        print("========================================")

        print("1. Add Subject")
        print("2. View Subjects")
        print("3. Add Exam")
        print("4. View Upcoming Exams")
        print("5. Create Study Plan")
        print("6. Add Study Task")
        print("7. View Study Tasks")
        print("8. Complete Task")
        print("9. Update Subject Progress")
        print("10. Study Recommendations")
        print("11. View Dashboard")
        print("12. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_subject()

        elif choice == "2":
            view_subjects()

        elif choice == "3":
            add_exam()

        elif choice == "4":
            view_exams()

        elif choice == "5":
            create_study_plan()

        elif choice == "6":
            add_task()

        elif choice == "7":
            view_tasks()

        elif choice == "8":
            complete_task()

        elif choice == "9":
            update_progress()

        elif choice == "10":
            recommendations()

        elif choice == "11":
            dashboard()

        elif choice == "12":
            print("\nThank you for using Smart Study Planner!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()