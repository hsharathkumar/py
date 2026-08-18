# py
 print(eval(input("Calc: "), {"__builtins__":None}, {})) 

 Explaination:
 Alright, let's go *line by line / block by block* 👇
This is a full *Tkinter Grade Card Generator App*

---

### *1. IMPORTS + DATA*
import tkinter as tk
from tkinter import messagebox
DEFAULT_SUBJECTS = ["Mathematics", "Physics", "Chemistry", "English", "Computer Sci", "Social Science"]
*`import tkinter as tk`* : Import the GUI library. `tk` is just a shortcut name
*`messagebox`* : For error popups like "Please fill all fields"
*`DEFAULT_SUBJECTS`* : List of 6 subjects. This auto-fills the subject boxes so user doesn't type everything

---

### *2. HELPER FUNCTION: GRADING*
def get_grade(p):
    return 'A+' if p >= 90 else 'A' if p >= 80 else 'B' if p >= 70 else 'C' if p >= 60 else 'D' if p >= 50 else 'F'
This is a "ternary chain". It checks marks and returns a grade.
`90+ = A+`, `80+ = A`, `70+ = B`... `<50 = F`

---

### *3. MAIN FUNCTION: `generate_card()`*
This runs when you click the "Generate Grade Card" button

#### *Step 1: Get Student Info*
name = ent_name.get().strip() or "Student"
roll = ent_roll.get().strip() or "N/A"
`.get()` = read text from entry box
`.strip()` = remove extra spaces
`or "Student"` = if box is empty, use default value

#### *Step 2: Loop Through 6 Subjects*
total = 0
records = []
for sub_ent, mark_ent in rows:
`rows` is a list containing all 6 pairs of `[subject_box, marks_box]`
We loop each one

#### *Step 3: Validation*
sub = sub_ent.get().strip()
val = mark_ent.get().strip()

if not sub or not val:
    messagebox.showerror("Error", "Please fill in all 6 subjects and marks.")
    return
1. *Empty check*: If subject or marks is blank → show error popup and stop
try:
    m = float(val)
    if not (0 <= m <= 100):
        messagebox.showerror("Range Error", f"Score for '{sub}' must be between 0 and 100.")
        return
2. *Number check*: `float(val)` converts to number. If user types "abc" → goes to `except`
3. *Range check*: Marks must be 0 to 100
records.append((sub, m, get_grade(m)))
    total += m
except ValueError:
    messagebox.showerror("Input Error", f"Enter a valid number for '{sub}'.")
    return
If all good: save `(subject, marks, grade)` to `records` list and add to `total`
If not number: show error

#### *Step 4: Calculate Result*
avg = total / 6
status = "PASSED" if all(m >= 40 for _, m, _ in records) else "FAILED"
`avg` = percentage out of 100
`status` = PASSED only if ALL subjects have >= 40 marks. `all()` checks this

#### *Step 5: Build The Card String*
card = f"🎓 OFFICIAL GRADE REPORT\n..."
Uses f-strings to format text.
`{name:<17}` = left align name in 17 spaces
`{m:>6.1f}` = right align marks in 6 spaces with 1 decimal
`{'═'*38}` = prints ════ 38 times for a line

Then loop `records` to add each subject line

#### *Step 6: Show Output*
txt_out.delete("1.0", tk.END)
txt_out.insert(tk.END, card)
`"1.0"` = line 1, column 0. Delete everything in text box
`insert(tk.END, card)` = put the new card at the end

---

### *4. GUI SETUP: BUILDING THE WINDOW*

#### *A. Main Window*
root = tk.Tk()
root.title("6-Subject Grade Card Generator")
root.geometry("420x680")
root.resizable(False, False)
root.configure(bg="#f8fafc")
Creates 420x680 window, title, light gray background, can't resize

#### *B. Student Info Section*
info_frame = tk.Frame(root, bg="#f8fafc")
info_frame.pack(fill="x", padx=16, pady=(12, 6))
`Frame` = container. `pack(fill="x")` = stretch full width
Inside it we use `grid` to place 4 widgets: Label Name, Entry Name, Label Roll, Entry Roll

#### *C. 6 Subject Grid*
grid_frame = tk.LabelFrame(root, text=" 6 Subjects & Marks (Max 100) ",...)
grid_frame.pack(fill="x", padx=16, pady=6)

rows = []
for i in range(6):
    s_ent = tk.Entry(grid_frame,...)
    s_ent.insert(0, DEFAULT_SUBJECTS[i])
    m_ent = tk.Entry(grid_frame,...)
    rows.append((s_ent, m_ent))
`LabelFrame` = box with a title border
Loop 6 times: Create 1 subject entry + 1 marks entry per row
`insert(0,...)` = pre-fill subject name
Save both entries in `rows` list so `generate_card()` can read them later

#### *D. Button*
tk.Button(root, text="Generate Grade Card",..., command=generate_card)
Blue button. `command=generate_card` means "run this function when clicked"

#### *E. Output Text Box*
txt_out = tk.Text(root, height=12, font=("Consolas", 9), bg="#0f172a", fg="#38bdf8")
txt_out.pack(fill="both", expand=True, padx=16, pady=(0, 14))
Dark blue terminal-style box. `expand=True` = takes all remaining space
This is where the final grade card is printed

#### *F. Start The App*
root.mainloop()
Keeps the window open and waits for clicks/typing

---

### *5. Summary Flow*
`User fills form` → `Click Button` → `generate_card() runs` → `Validate` → `Calculate` → `Format String` → `Show in Text Box`

Want me to add *2 upgrades* to this code now:
1. *Save http://to.txt file button*
2. *"Clear All" button*

Which one do you want first?
