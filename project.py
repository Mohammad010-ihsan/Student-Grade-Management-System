import tkinter as tk
from   tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt


students = []  # store student records globally


def calculate_gpa_100(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def convert_to_gpa_4(gpa_100):
    return round((gpa_100 / 100) * 4, 2)


def classify_gpa_4(gpa_4):
    if gpa_4 >= 3.7:
        return "Excellent"
    elif gpa_4 >= 3.0:
        return "Very Good"
    elif gpa_4 >= 2.0:
        return "Good"
    elif gpa_4 >= 1.0:
        return "Pass"
    else:
        return "Fail"


def save_students_to_csv(filename="students.csv"):
    if not students:
        messagebox.showwarning("Warning", "No students to save!")
        return
    df = pd.DataFrame(students)
    df.to_csv(filename, index=False)
    messagebox.showinfo("Saved", f"Students saved to {filename}")


def plot_all_grades():
    if not students:
        messagebox.showwarning("Warning", "No students to plot!")
        return

    all_grades = []
    for student in students:
        all_grades.extend(student["Grades"])

    plt.hist(all_grades, bins=10, color="skyblue", edgecolor="black")
    plt.title("All Students Grade Distribution")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.show()


def add_student(name, grades_str, tree):
    try:
        grades = [float(g.strip()) for g in grades_str.split(",") if g.strip()]
    except ValueError:
        messagebox.showerror("Error", "Grades must be numbers separated by commas")
        return

    if not all(0 <= g <= 100 for g in grades):
        messagebox.showerror("Error", "Grades must be between 0 and 100")
        return

    gpa_100 = calculate_gpa_100(grades)
    gpa_4 = convert_to_gpa_4(gpa_100)
    classification = classify_gpa_4(gpa_4)

    student_record = {
        "Name": name,
        "Grades": grades,
        "GPA_100": round(gpa_100, 2),
        "GPA_4": gpa_4,
        "Classification": classification,
    }

    students.append(student_record)

    tree.insert(
        "",
        "end",
        values=(name, ", ".join(map(str, grades)), f"{gpa_100:.2f}", gpa_4, classification),
    )


def delete_student(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a student to delete.")
        return

    item = tree.item(selected_item)
    name = item["values"][0]

    # Remove from list
    global students
    students = [s for s in students if s["Name"] != name]

    # Remove from Treeview
    tree.delete(selected_item)
    messagebox.showinfo("Deleted", f"Student {name} removed.")


def edit_student(name_entry, grades_entry, tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a student to edit.")
        return

    name = name_entry.get()
    grades_str = grades_entry.get()

    try:
        grades = [float(g.strip()) for g in grades_str.split(",") if g.strip()]
    except ValueError:
        messagebox.showerror("Error", "Grades must be numbers separated by commas")
        return

    if not all(0 <= g <= 100 for g in grades):
        messagebox.showerror("Error", "Grades must be between 0 and 100")
        return

    gpa_100 = calculate_gpa_100(grades)
    gpa_4 = convert_to_gpa_4(gpa_100)
    classification = classify_gpa_4(gpa_4)

    # Update in students list
    item = tree.item(selected_item)
    old_name = item["values"][0]

    for student in students:
        if student["Name"] == old_name:
            student["Name"] = name
            student["Grades"] = grades
            student["GPA_100"] = round(gpa_100, 2)
            student["GPA_4"] = gpa_4
            student["Classification"] = classification
            break

    # Update in Treeview
    tree.item(
        selected_item,
        values=(name, ", ".join(map(str, grades)), f"{gpa_100:.2f}", gpa_4, classification),
    )
    messagebox.showinfo("Updated", f"Student {name} updated.")


def main():
    root = tk.Tk()
    root.title("🎓 Student Grade Management System")
    root.geometry("900x550")

    # Frame for input
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Student Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(input_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Grades (comma separated):").grid(row=1, column=0, padx=5, pady=5)
    grades_entry = tk.Entry(input_frame)
    grades_entry.grid(row=1, column=1, padx=5, pady=5)

    # Treeview for displaying data
    columns = ("Name", "Grades", "GPA (100)", "GPA (4.0)", "Classification")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=12)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.pack(pady=10, fill="x")

    # Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    add_button = tk.Button(
        button_frame,
        text="Add Student",
        command=lambda: add_student(name_entry.get(), grades_entry.get(), tree),
    )
    add_button.grid(row=0, column=0, padx=10)

    edit_button = tk.Button(
        button_frame,
        text="Edit Student",
        command=lambda: edit_student(name_entry, grades_entry, tree),
    )
    edit_button.grid(row=0, column=1, padx=10)

    delete_button = tk.Button(
        button_frame,
        text="Delete Student",
        command=lambda: delete_student(tree),
    )
    delete_button.grid(row=0, column=2, padx=10)

    save_button = tk.Button(
        button_frame,
        text="Save to CSV",
        command=save_students_to_csv,
    )
    save_button.grid(row=0, column=3, padx=10)

    plot_button = tk.Button(
        button_frame,
        text="Plot Grades",
        command=plot_all_grades,
    )
    plot_button.grid(row=0, column=4, padx=10)

    root.mainloop()


if __name__ == "__main__":
    main()