'''import tkinter as tk

def on_click(char):
    current = display_var.get()
    
    if char == "C":
        display_var.set("")
    elif char == "=":
        try:
            # Evaluate expression and format result
            result = eval(current)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            display_var.set(str(result))
        except Exception:
            display_var.set("Error")
    else:
        if current == "Error":
            display_var.set(char)
        else:
            display_var.set(current + char)

# Window Setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x380")
root.resizable(False, False)
root.configure(bg="#f4f4f5")

display_var = tk.StringVar()

# Display Screen
screen = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 20),
    bd=0,
    justify="right",
    bg="#e4e4e7",
    fg="#18181b"
)
screen.grid(row=0, column=0, columnspan=4, padx=12, pady=16, ipady=10, sticky="nsew")

# Button Layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and Grid Buttons
for text, row, col in buttons:
    # Stylize operator and action buttons
    if text in ['/', '*', '-', '+', '=']:
        bg_color, fg_color = "#3b82f6", "#ffffff"
    elif text == 'C':
        bg_color, fg_color = "#ef4444", "#ffffff"
    else:
        bg_color, fg_color = "#ffffff", "#18181b"

    btn = tk.Button(
        root,
        text=text,
        font=("Arial", 13, "bold"),
        bg=bg_color,
        fg=fg_color,
        activebackground="#cbd5e1",
        bd=0,
        width=5,
        height=2,
        command=lambda t=text: on_click(t)
    )
    btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

# Configure grid weights for uniform spacing
for i in range(5):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

root.mainloop()
import tkinter as tk

state = {"new_input": False}

def on_click(char):
    current = display_var.get()
    
    if char == "AC":
        display_var.set("0")
        state["new_input"] = True
    elif char == "C":
        if len(current) > 1 and current not in ("ERROR", "DIV BY 0"):
            display_var.set(current[:-1])
        else:
            display_var.set("0")
    elif char == "=":
        try:
            calc_str = current.replace('×', '*').replace('÷', '/')
            result = eval(calc_str, {"__builtins__": None}, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            elif isinstance(result, float):
                result = round(result, 6)
            display_var.set(str(result))
            state["new_input"] = True
        except ZeroDivisionError:
            display_var.set("DIV BY 0")
            state["new_input"] = True
        except Exception:
            display_var.set("ERROR")
            state["new_input"] = True
    else:
        if current in ("0", "ERROR", "DIV BY 0") or state["new_input"]:
            if char in ("+", "-", "×", "÷"):
                display_var.set((current if current not in ("ERROR", "DIV BY 0") else "0") + char)
            else:
                display_var.set(char)
            state["new_input"] = False
        else:
            display_var.set(current + char)

def toggle_sign():
    val = display_var.get()
    if val not in ("0", "ERROR", "DIV BY 0"):
        if val.startswith('-'):
            display_var.set(val[1:])
        else:
            display_var.set('-' + val)

# Window Setup
root = tk.Tk()
root.title("Skeuomorphic Pocket Calculator")
root.geometry("340x520")
root.resizable(False, False)
root.configure(bg="#121316")

# Outer Heavy Chassis (Beveled Plastic Casing)
casing = tk.Frame(root, bg="#2e3238", bd=8, relief=tk.RAISED)
casing.pack(fill="both", expand=True, padx=8, pady=8)

# Inner Recessed Metal Plate
inner_frame = tk.Frame(casing, bg="#1c1e22", bd=4, relief=tk.SUNKEN)
inner_frame.pack(fill="both", expand=True, padx=4, pady=4)

# Top Section: Brand Badge and Realistic Solar Strip
top_bar = tk.Frame(inner_frame, bg="#1c1e22")
top_bar.pack(fill="x", padx=10, pady=(10, 4))

brand_label = tk.Label(
    top_bar, 
    text="RETRO•CALC  FX-80", 
    font=("Helvetica", 9, "bold"), 
    bg="#1c1e22", 
    fg="#8a94a6"
)
brand_label.pack(side="left")

# Simulated Glass Solar Cell
solar_cell = tk.Frame(top_bar, bg="#332415", bd=2, relief=tk.SUNKEN, width=76, height=22)
solar_cell.pack(side="right")
solar_cell.pack_propagate(False)

for _ in range(4):
    strip = tk.Frame(solar_cell, bg="#4a341e", bd=1, relief=tk.RAISED, width=15, height=16)
    strip.pack(side="left", padx=1, pady=1)

# Inset LCD Screen Well
lcd_border = tk.Frame(inner_frame, bg="#0d0e10", bd=5, relief=tk.SUNKEN)
lcd_border.pack(fill="x", padx=10, pady=10)

display_var = tk.StringVar(value="0")

lcd_screen = tk.Label(
    lcd_border,
    textvariable=display_var,
    font=("Consolas", 26, "bold"),
    bg="#8ea380",
    fg="#192414",
    anchor="e",
    padx=12,
    pady=10
)
lcd_screen.pack(fill="both")

# Tactile Keypad Section
keypad = tk.Frame(inner_frame, bg="#1c1e22")
keypad.pack(fill="both", expand=True, padx=8, pady=(4, 10))

buttons = [
    [('AC', '#b83228', '#ffffff'), ('C', '#c4512b', '#ffffff'), ('%', '#3d444d', '#dbe2eb'), ('÷', '#3d444d', '#dbe2eb')],
    [('7', '#2e333a', '#f8fafc'), ('8', '#2e333a', '#f8fafc'), ('9', '#2e333a', '#f8fafc'), ('×', '#3d444d', '#dbe2eb')],
    [('4', '#2e333a', '#f8fafc'), ('5', '#2e333a', '#f8fafc'), ('6', '#2e333a', '#f8fafc'), ('-', '#3d444d', '#dbe2eb')],
    [('1', '#2e333a', '#f8fafc'), ('2', '#2e333a', '#f8fafc'), ('3', '#2e333a', '#f8fafc'), ('+', '#3d444d', '#dbe2eb')],
    [('0', '#2e333a', '#f8fafc'), ('.', '#2e333a', '#f8fafc'), ('±', '#2e333a', '#f8fafc'), ('=', '#d97706', '#ffffff')],
]

for r_idx, row in enumerate(buttons):
    keypad.rowconfigure(r_idx, weight=1)
    for c_idx, (text, bg_col, fg_col) in enumerate(row):
        keypad.columnconfigure(c_idx, weight=1)

        action = toggle_sign if text == '±' else (lambda t=text: on_click(t))

        btn = tk.Button(
            keypad,
            text=text,
            font=("Arial", 13, "bold"),
            bg=bg_col,
            fg=fg_col,
            activebackground="#17181c",
            activeforeground="#ffffff",
            bd=4,
            relief=tk.RAISED,
            cursor="hand2",
            command=action
        )
        btn.grid(row=r_idx, column=c_idx, padx=4, pady=4, sticky="nsew")

root.mainloop()
''''''
import tkinter as tk

state = {"new_input": False}

def on_click(char):
    current = display_var.get()
    
    if char == "AC":
        display_var.set("0")
        history_var.set("")
        state["new_input"] = False
    elif char == "DEL":
        if current not in ("0", "Error", "Cannot divide by 0") and len(current) > 1:
            display_var.set(current[:-1])
        else:
            display_var.set("0")
    elif char == "=":
        try:
            expr = display_var.get().replace('×', '*').replace('÷', '/')
            history_var.set(display_var.get() + " =")
            
            # Safe evaluation
            result = eval(expr, {"__builtins__": None}, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            elif isinstance(result, float):
                result = round(result, 8)
                
            display_var.set(str(result))
            state["new_input"] = True
        except ZeroDivisionError:
            display_var.set("Cannot divide by 0")
            state["new_input"] = True
        except Exception:
            display_var.set("Error")
            state["new_input"] = True
    else:
        if current in ("0", "Error", "Cannot divide by 0") or state["new_input"]:
            if char in ("+", "-", "×", "÷", "%"):
                display_var.set((current if current not in ("Error", "Cannot divide by 0") else "0") + char)
            else:
                display_var.set(char)
            state["new_input"] = False
        else:
            if char == "." and "." in current.split()[-1]:
                return
            display_var.set(current + char)

# Window Setup
root = tk.Tk()
root.title("Glassmorphism Calculator")
root.geometry("360x560")
root.resizable(False, False)
root.configure(bg="#0b0f19")

# Ambient Background Canvas (Glowing Orbs)
bg_canvas = tk.Canvas(root, width=360, height=560, bg="#0b0f19", highlightthickness=0)
bg_canvas.place(x=0, y=0)

# Render glowing blurred backdrop spheres
bg_canvas.create_oval(15, 30, 185, 200, fill="#be185d", outline="")      # Neon Pink orb
bg_canvas.create_oval(170, 320, 350, 500, fill="#4338ca", outline="")    # Deep Indigo orb
bg_canvas.create_oval(40, 360, 180, 500, fill="#0e7490", outline="")     # Cyan Glow orb

# Frosted Glass Floating Card Container
glass_card = tk.Frame(root, bg="#13192b", bd=1, relief=tk.SOLID, highlightbackground="#2e3856", highlightthickness=1)
glass_card.place(x=18, y=24, width=324, height=512)

# Sub-header Brand Badge
brand_lbl = tk.Label(
    glass_card,
    text="FROST GLASS UI",
    font=("Segoe UI", 8, "bold"),
    bg="#13192b",
    fg="#64748b"
)
brand_lbl.pack(anchor="w", padx=16, pady=(12, 0))

# Frosted Glass Display Unit
display_frame = tk.Frame(
    glass_card,
    bg="#0d1322",
    bd=1,
    relief=tk.SOLID,
    highlightbackground="#1e293b",
    highlightthickness=1
)
display_frame.pack(fill="x", padx=14, pady=(6, 16))

history_var = tk.StringVar(value="")
history_lbl = tk.Label(
    display_frame,
    textvariable=history_var,
    font=("Segoe UI", 10),
    bg="#0d1322",
    fg="#64748b",
    anchor="e",
    padx=12,
    pady=(8, 0)
)
history_lbl.pack(fill="x")

display_var = tk.StringVar(value="0")
display_lbl = tk.Label(
    display_frame,
    textvariable=display_var,
    font=("Segoe UI", 24, "bold"),
    bg="#0d1322",
    fg="#f8fafc",
    anchor="e",
    padx=12,
    pady=(0, 10)
)
display_lbl.pack(fill="x")

# Keypad Frame
keypad = tk.Frame(glass_card, bg="#13192b")
keypad.pack(fill="both", expand=True, padx=12, pady=(0, 12))

buttons = [
    [('AC', '#1e293b', '#f43f5e', '#334155'), ('DEL', '#1e293b', '#f43f5e', '#334155'), ('%', '#1e293b', '#38bdf8', '#334155'), ('÷', '#1e293b', '#38bdf8', '#334155')],
    [('7', '#172033', '#f1f5f9', '#24324f'), ('8', '#172033', '#f1f5f9', '#24324f'), ('9', '#172033', '#f1f5f9', '#24324f'), ('×', '#1e293b', '#38bdf8', '#334155')],
    [('4', '#172033', '#f1f5f9', '#24324f'), ('5', '#172033', '#f1f5f9', '#24324f'), ('6', '#172033', '#f1f5f9', '#24324f'), ('-', '#1e293b', '#38bdf8', '#334155')],
    [('1', '#172033', '#f1f5f9', '#24324f'), ('2', '#172033', '#f1f5f9', '#24324f'), ('3', '#172033', '#f1f5f9', '#24324f'), ('+', '#1e293b', '#38bdf8', '#334155')],
    [('0', '#172033', '#f1f5f9', '#24324f'), ('.', '#172033', '#f1f5f9', '#24324f'), ('=', '#6366f1', '#ffffff', '#818cf8'), ('', '', '', '')]
]

# Helper for Hover Lighting Effects
def attach_hover_glow(btn, default_bg, hover_bg):
    btn.bind("<Enter>", lambda e: btn.config(bg=hover_bg))
    btn.bind("<Leave>", lambda e: btn.config(bg=default_bg))

# Layout Grid
for r_idx in range(5):
    keypad.rowconfigure(r_idx, weight=1)
for c_idx in range(4):
    keypad.columnconfigure(c_idx, weight=1)

for r_idx, row in enumerate(buttons):
    for c_idx, (text, bg_col, fg_col, hover_col) in enumerate(row):
        if text == '':
            continue
        
        # Expand '=' over 2 columns
        colspan = 2 if text == '=' else 1

        btn = tk.Button(
            keypad,
            text=text,
            font=("Segoe UI", 12, "bold" if text in ('AC', 'DEL', '=', '÷', '×', '-', '+') else "normal"),
            bg=bg_col,
            fg=fg_col,
            activebackground=hover_col,
            activeforeground=fg_col,
            bd=0,
            relief=tk.FLAT,
            highlightbackground="#2e3856",
            highlightthickness=1,
            cursor="hand2",
            command=lambda t=text: on_click(t)
        )
        btn.grid(row=r_idx, column=c_idx, columnspan=colspan, padx=4, pady=4, sticky="nsew")
        attach_hover_glow(btn, bg_col, hover_col)

root.mainloop()'''
import tkinter as tk
import math

state = {"new_input": False}

def on_click(char):
    current = display_var.get()
    
    if char == "AC":
        display_var.set("0")
        history_var.set("")
        state["new_input"] = False
    elif char == "DEL":
        if current not in ("0", "Error", "Cannot divide by 0") and len(current) > 1:
            display_var.set(current[:-1])
        else:
            display_var.set("0")
    elif char == "=":
        try:
            expr = display_var.get().replace('×', '*').replace('÷', '/')
            history_var.set(display_var.get() + " =")
            
            result = eval(expr, {"__builtins__": None}, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            elif isinstance(result, float):
                result = round(result, 8)
                
            display_var.set(str(result))
            state["new_input"] = True
        except ZeroDivisionError:
            display_var.set("Cannot divide by 0")
            state["new_input"] = True
        except Exception:
            display_var.set("Error")
            state["new_input"] = True
    else:
        if current in ("0", "Error", "Cannot divide by 0") or state["new_input"]:
            if char in ("+", "-", "×", "÷", "%"):
                display_var.set((current if current not in ("Error", "Cannot divide by 0") else "0") + char)
            else:
                display_var.set(char)
            state["new_input"] = False
        else:
            if char == "." and "." in current.split()[-1]:
                return
            display_var.set(current + char)

# Window Setup
root = tk.Tk()
root.title("Liquid Glass Calculator")
root.geometry("380x600")
root.resizable(False, False)
root.configure(bg="#050811")

# Liquid Ambient Canvas (Background Fluid Orbs)
canvas = tk.Canvas(root, width=380, height=600, bg="#050811", highlightthickness=0)
canvas.place(x=0, y=0)

# Fluid Blob Objects: [id, base_x, base_y, radius, speed_x, speed_y, color]
blobs = [
    {"id": None, "x": 60, "y": 90, "r": 90, "dx": 0.035, "dy": 0.025, "col": "#ec4899"},   # Neon Pink
    {"id": None, "x": 300, "y": 140, "r": 110, "dx": 0.020, "dy": 0.040, "col": "#6366f1"}, # Electric Indigo
    {"id": None, "x": 280, "y": 480, "r": 100, "dx": 0.030, "dy": 0.020, "col": "#06b6d4"}, # Vivid Cyan
    {"id": None, "x": 80, "y": 440, "r": 85, "dx": 0.025, "dy": 0.035, "col": "#8b5cf6"}   # Soft Violet
]

for b in blobs:
    b["id"] = canvas.create_oval(
        b["x"] - b["r"], b["y"] - b["r"],
        b["x"] + b["r"], b["y"] + b["r"],
        fill=b["col"], outline=""
    )

# Animation Loop for Continuous Fluid Motion
angle = 0.0
def animate_fluid():
    global angle
    angle += 0.04
    for b in blobs:
        curr_x = b["x"] + math.sin(angle * b["dx"] * 50) * 35
        curr_y = b["y"] + math.cos(angle * b["dy"] * 50) * 30
        canvas.coords(
            b["id"],
            curr_x - b["r"], curr_y - b["r"],
            curr_x + b["r"], curr_y + b["r"]
        )
    root.after(30, animate_fluid)

# Outer Frosted Liquid Card
glass_card = tk.Frame(
    root,
    bg="#0c1322",
    bd=1,
    relief=tk.SOLID,
    highlightbackground="#38bdf8",
    highlightthickness=1
)
glass_card.place(x=20, y=25, width=340, height=550)

# Header Title with Aurora Accent
brand_lbl = tk.Label(
    glass_card,
    text="LIQUID GLASS UI",
    font=("Segoe UI", 9, "bold"),
    bg="#0c1322",
    fg="#38bdf8"
)
brand_lbl.pack(anchor="w", padx=18, pady=(14, 0))

# Sub-Display Frame with Specular Highlight Border
display_frame = tk.Frame(
    glass_card,
    bg="#060c18",
    bd=1,
    relief=tk.SOLID,
    highlightbackground="#1e293b",
    highlightthickness=1
)
display_frame.pack(fill="x", padx=16, pady=(8, 14))

# Equation & Output Labels
history_var = tk.StringVar(value="")
history_lbl = tk.Label(
    display_frame,
    textvariable=history_var,
    font=("Segoe UI", 10),
    bg="#060c18",
    fg="#64748b",
    anchor="e",
    padx=12
)
history_lbl.pack(fill="x", pady=(10, 0))

display_var = tk.StringVar(value="0")
display_lbl = tk.Label(
    display_frame,
    textvariable=display_var,
    font=("Segoe UI", 26, "bold"),
    bg="#060c18",
    fg="#ffffff",
    anchor="e",
    padx=12
)
display_lbl.pack(fill="x", pady=(0, 12))

# Keypad Section
keypad = tk.Frame(glass_card, bg="#0c1322")
keypad.pack(fill="both", expand=True, padx=14, pady=(0, 14))

buttons = [
    [('AC', '#192238', '#f43f5e', '#243252'), ('DEL', '#192238', '#f43f5e', '#243252'), ('%', '#192238', '#38bdf8', '#243252'), ('÷', '#192238', '#38bdf8', '#243252')],
    [('7', '#0f172a', '#e2e8f0', '#1e293b'), ('8', '#0f172a', '#e2e8f0', '#1e293b'), ('9', '#0f172a', '#e2e8f0', '#1e293b'), ('×', '#192238', '#38bdf8', '#243252')],
    [('4', '#0f172a', '#e2e8f0', '#1e293b'), ('5', '#0f172a', '#e2e8f0', '#1e293b'), ('6', '#0f172a', '#e2e8f0', '#1e293b'), ('-', '#192238', '#38bdf8', '#243252')],
    [('1', '#0f172a', '#e2e8f0', '#1e293b'), ('2', '#0f172a', '#e2e8f0', '#1e293b'), ('3', '#0f172a', '#e2e8f0', '#1e293b'), ('+', '#192238', '#38bdf8', '#243252')],
    [('0', '#0f172a', '#e2e8f0', '#1e293b'), ('.', '#0f172a', '#e2e8f0', '#1e293b'), ('=', '#6366f1', '#ffffff', '#818cf8'), ('', '', '', '')]
]

def attach_liquid_hover(btn, default_bg, hover_bg):
    btn.bind("<Enter>", lambda e: btn.config(bg=hover_bg, highlightbackground="#38bdf8"))
    btn.bind("<Leave>", lambda e: btn.config(bg=default_bg, highlightbackground="#1e293b"))

for r_idx in range(5):
    keypad.rowconfigure(r_idx, weight=1)
for c_idx in range(4):
    keypad.columnconfigure(c_idx, weight=1)

for r_idx, row in enumerate(buttons):
    for c_idx, (text, bg_col, fg_col, hover_col) in enumerate(row):
        if text == '':
            continue
        
        colspan = 2 if text == '=' else 1

        btn = tk.Button(
            keypad,
            text=text,
            font=("Segoe UI", 12, "bold" if text in ('AC', 'DEL', '=', '÷', '×', '-', '+') else "normal"),
            bg=bg_col,
            fg=fg_col,
            activebackground=hover_col,
            activeforeground=fg_col,
            bd=0,
            relief=tk.FLAT,
            highlightbackground="#1e293b",
            highlightthickness=1,
            cursor="hand2",
            command=lambda t=text: on_click(t)
        )
        btn.grid(row=r_idx, column=c_idx, columnspan=colspan, padx=4, pady=4, sticky="nsew")
        attach_liquid_hover(btn, bg_col, hover_col)

# Start background fluid animation
animate_fluid()

root.mainloop()