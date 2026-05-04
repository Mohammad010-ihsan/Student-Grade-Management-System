# Student Grade Management System
#### Video Demo: <https://youtu.be/sCaVGtZXKJg?si=Zp9r10ggI_OnFPzH>
#### Description:

This project is a **Student Grade Management System** implemented in Python.  
The purpose of this project is to provide an easy-to-use program for entering student grades, calculating GPAs, classifying student performance, and saving or visualizing the results. It combines **data processing**, **mathematical calculations**, and a **graphical user interface (GUI)** into one package.

---

## Features

1. **Graphical User Interface (GUI):**  
   The project uses the `tkinter` library to create a friendly graphical interface where users can add, edit, and delete student records without needing to work with the terminal.

2. **Grade Management:**  
   - Add new students with their grades.  
   - Edit an existing student’s information (name or grades).  
   - Delete students when no longer needed.  
   - All changes are reflected instantly in the on-screen table.

3. **Automatic GPA Calculation:**  
   - The system calculates the GPA out of **100**.  
   - It also converts this GPA into the **4.0 scale** using a mathematical formula.  
   - Students are classified into categories like *Excellent, Very Good, Good, Pass, or Fail* based on their GPA.

4. **Data Storage:**  
   Grades and student information can be saved to a **CSV file** using the `pandas` library. This ensures that the data is not lost after closing the program and can be loaded later.

5. **Data Visualization:**  
   Using the `matplotlib` library, the program can generate a histogram of all students’ grades. This helps teachers and students see the distribution of scores at a glance.

---

## Libraries Used
- **tkinter** → For the graphical user interface.  
- **pandas** → For handling CSV files (saving and loading data).  
- **matplotlib** → For plotting student grades visually.  

All external dependencies are listed in the `requirements.txt` file. To install them, simply run:

```bash
pip install -r requirements.txt
