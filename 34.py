import tkinter as tk
from tkinter import messagebox

DEFAULT_SUBJECTS = ["Mathematics", "Physics", "Chemistry", "English", "Computer Sci", "Social Science"]

def get_grade(p):
    return 'A+' if p >= 90 else 'A' if p >= 80 else 'B' if p >= 70 else 'C' if p >= 60 else 'D' if p >= 50 else 'F'

def generate_card():
    name = ent_name.get().strip() or "Student"
    roll = ent_roll.get().strip() or "N/A"
    
    total = 0
    records = []

    for sub_ent, mark_ent in rows:
        sub = sub_ent.get().strip()
        val = mark_ent.get().strip()

        if not sub or not val:
            messagebox.showerror("Error", "Please fill in all 6 subjects and marks.")
            return

        try:
            m = float(val)
            if not (0 <= m <= 100):
                messagebox.showerror("Range Error", f"Score for '{sub}' must be between 0 and 100.")
                return
            records.append((sub, m, get_grade(m)))
            total += m
        except ValueError:
            messagebox.showerror("Input Error", f"Enter a valid number for '{sub}'.")
            return

    avg = total / 6
    status = "PASSED" if all(m >= 40 for _, m, _ in records) else "FAILED"

    card = (
        f"🎓 OFFICIAL GRADE REPORT\n"
        f"{'═'*38}\n"
        f"Student : {name:<17} Roll: {roll}\n"
        f"{'─'*38}\n"
        f"{'Subject':<18} {'Marks':>6}  {'Grade':>5}\n"
        f"{'─'*38}\n"
    )
    for s, m, g in records:
        card += f"{s[:17]:<18} {m:>6.1f}  {g:>5}\n"

    card += (
        f"{'─'*38}\n"
        f"Total Marks : {total:.1f} / 600\n"
        f"Percentage  : {avg:.2f}%\n"
        f"Final Grade : {get_grade(avg)} ({status})\n"
        f"{'═'*38}"
    )

    txt_out.delete("1.0", tk.END)
    txt_out.insert(tk.END, card)

# Window Setup
root = tk.Tk()
root.title("6-Subject Grade Card Generator")
root.geometry("420x680")
root.resizable(False, False)
root.configure(bg="#f8fafc")

# Student Details
info_frame = tk.Frame(root, bg="#f8fafc")
info_frame.pack(fill="x", padx=16, pady=(12, 6))

tk.Label(info_frame, text="Name:", bg="#f8fafc", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="w")
ent_name = tk.Entry(info_frame, font=("Segoe UI", 9), width=18)
ent_name.grid(row=0, column=1, padx=(4, 10))

tk.Label(info_frame, text="Roll No:", bg="#f8fafc", font=("Segoe UI", 9, "bold")).grid(row=0, column=2, sticky="w")
ent_roll = tk.Entry(info_frame, font=("Segoe UI", 9), width=12)
ent_roll.grid(row=0, column=3, padx=(4, 0))

# 6 Subject Inputs Grid
grid_frame = tk.LabelFrame(root, text=" 6 Subjects & Marks (Max 100) ", font=("Segoe UI", 9, "bold"), bg="#f8fafc", padx=8, pady=6)
grid_frame.pack(fill="x", padx=16, pady=6)

rows = []
for i in range(6):
    s_ent = tk.Entry(grid_frame, font=("Segoe UI", 9), width=22)
    s_ent.insert(0, DEFAULT_SUBJECTS[i])
    s_ent.grid(row=i, column=0, padx=4, pady=3)

    m_ent = tk.Entry(grid_frame, font=("Segoe UI", 9), width=8, justify="center")
    m_ent.grid(row=i, column=1, padx=4, pady=3)
    rows.append((s_ent, m_ent))

# Action Button
tk.Button(
    root, text="Generate Grade Card", font=("Segoe UI", 10, "bold"),
    bg="#2563eb", fg="white", activebackground="#1d4ed8", bd=0, pady=6, cursor="hand2",
    command=generate_card
).pack(fill="x", padx=16, pady=8)

# Output Card Screen
txt_out = tk.Text(root, height=12, font=("Consolas", 9), bg="#0f172a", fg="#38bdf8", bd=0, padx=10, pady=8)
txt_out.pack(fill="both", expand=True, padx=16, pady=(0, 14))

root.mainloop()