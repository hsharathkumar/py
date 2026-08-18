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

bg_canvas.create_oval(15, 30, 185, 200, fill="#be185d", outline="")      # Neon Pink orb
bg_canvas.create_oval(170, 320, 350, 500, fill="#4338ca", outline="")    # Deep Indigo orb
bg_canvas.create_oval(40, 360, 180, 500, fill="#0e7490", outline="")     # Cyan Glow orb

# Frosted Glass Card Container
glass_card = tk.Frame(root, bg="#13192b", bd=1, relief=tk.SOLID, highlightbackground="#2e3856", highlightthickness=1)
glass_card.place(x=18, y=24, width=324, height=512)

# Brand Badge
brand_lbl = tk.Label(
    glass_card,
    text="FROST GLASS UI",
    font=("Segoe UI", 8, "bold"),
    bg="#13192b",
    fg="#64748b"
)
brand_lbl.pack(anchor="w", padx=16, pady=(12, 0))

# Display Frame
display_frame = tk.Frame(
    glass_card,
    bg="#0d1322",
    bd=1,
    relief=tk.SOLID,
    highlightbackground="#1e293b",
    highlightthickness=1
)
display_frame.pack(fill="x", padx=14, pady=(6, 16))

# Fixed History and Output Labels
history_var = tk.StringVar(value="")
history_lbl = tk.Label(
    display_frame,
    textvariable=history_var,
    font=("Segoe UI", 10),
    bg="#0d1322",
    fg="#64748b",
    anchor="e",
    padx=12
)
history_lbl.pack(fill="x", pady=(8, 0))

display_var = tk.StringVar(value="0")
display_lbl = tk.Label(
    display_frame,
    textvariable=display_var,
    font=("Segoe UI", 24, "bold"),
    bg="#0d1322",
    fg="#f8fafc",
    anchor="e",
    padx=12
)
display_lbl.pack(fill="x", pady=(0, 10))

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

def attach_hover_glow(btn, default_bg, hover_bg):
    btn.bind("<Enter>", lambda e: btn.config(bg=hover_bg))
    btn.bind("<Leave>", lambda e: btn.config(bg=default_bg))

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
            highlightbackground="#2e3856",
            highlightthickness=1,
            cursor="hand2",
            command=lambda t=text: on_click(t)
        )
        btn.grid(row=r_idx, column=c_idx, columnspan=colspan, padx=4, pady=4, sticky="nsew")
        attach_hover_glow(btn, bg_col, hover_col)

root.mainloop()