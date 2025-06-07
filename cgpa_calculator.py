import tkinter as tk
from tkinter import ttk, messagebox

class CGPACalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CGPA Calculator")
        self.root.geometry("400x500")

        self.subject_entries = []

        # Title
        ttk.Label(root, text="CGPA Calculator", font=("Arial", 16)).pack(pady=10)

        # Number of subjects input
        self.num_subjects_var = tk.IntVar()
        ttk.Label(root, text="Enter number of subjects:").pack()
        self.num_subjects_entry = ttk.Entry(root, textvariable=self.num_subjects_var)
        self.num_subjects_entry.pack(pady=5)

        # Button to generate input fields
        ttk.Button(root, text="Generate Fields", command=self.generate_fields).pack(pady=5)

        # Frame to hold dynamic subject fields
        self.fields_frame = ttk.Frame(root)
        self.fields_frame.pack(pady=10)

        # Button to calculate CGPA
        ttk.Button(root, text="Calculate CGPA", command=self.calculate_cgpa).pack(pady=10)

        # Label to display result
        self.result_label = ttk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack()

    def generate_fields(self):
        # Clear previous entries
        for widget in self.fields_frame.winfo_children():
            widget.destroy()
        self.subject_entries.clear()

        try:
            num_subjects = self.num_subjects_var.get()
            if num_subjects <= 0:
                raise ValueError

            # Create fields for grade and credit
            for i in range(1, num_subjects + 1):
                ttk.Label(self.fields_frame, text=f"Subject {i} Grade Point:").grid(row=i*2-2, column=0, padx=5, pady=2, sticky="w")
                grade_entry = ttk.Entry(self.fields_frame)
                grade_entry.grid(row=i*2-2, column=1, padx=5, pady=2)

                ttk.Label(self.fields_frame, text=f"Subject {i} Credit Hours:").grid(row=i*2-1, column=0, padx=5, pady=2, sticky="w")
                credit_entry = ttk.Entry(self.fields_frame)
                credit_entry.grid(row=i*2-1, column=1, padx=5, pady=2)

                self.subject_entries.append((grade_entry, credit_entry))
        except:
            messagebox.showerror("Input Error", "Please enter a valid number of subjects.")

    def calculate_cgpa(self):
        try:
            total_points = 0
            total_credits = 0

            for grade_entry, credit_entry in self.subject_entries:
                grade = float(grade_entry.get())
                credit = float(credit_entry.get())
                total_points += grade * credit
                total_credits += credit

            if total_credits == 0:
                raise ZeroDivisionError

            cgpa = total_points / total_credits
            self.result_label.config(text=f"Your CGPA is: {cgpa:.2f}", foreground="green")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Total credit hours cannot be zero.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CGPACalculatorApp(root)
    root.mainloop()