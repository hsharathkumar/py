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
root.title("Liquid Glass Calculator")
root.geometry("380x600")
root.resizable(False, False)
root.configure(bg="#e2e8f0")

# Liquid Ambient Canvas (Soft Mesh Gradient Backdrop)
bg_canvas = tk.Canvas(root, width=380, height=600, bg="#e2e8f0", highlightthickness=0)
bg_canvas.place(x=0, y=0)

# Iridescent / Liquid Fluid Blobs
bg_canvas.create_oval(-40, 20, 220, 260, fill="#c7d2fe", outline="")     # Soft Periwinkle
bg_canvas.create_oval(160, -30, 390, 200, fill="#fbcfe8", outline="")    # Iridescent Rose
bg_canvas.create_oval(140, 300, 420, 580, fill="#a7f3d0", outline="")    # Mint Aquamarine
bg_canvas.create_oval(-30, 360, 220, 590, fill="#fed7aa", outline="")    # Peach Radiance

# Outer Luminous Refraction Ring (Simulates liquid glass edges)
edge_glow = tk.Frame(root, bg="#ffffff", highlightbackground="#ffffff", highlightthickness=2)
edge_glow.place(x=20, y=20, width=340, height=560)

# Main White Liquid Glass Panel
glass_body = tk.Frame(edge_glow, bg="#f8fafc", bd=0)
glass_body.place(x=2, y=2, width=332, height=552)

# Specular Liquid Header Accent
header = tk.Frame(glass_body, bg="#f8fafc")
header.pack(fill="x", padx=18, pady=(16, 4))

tk.Label(
    header,
    text="LIQUID GLASS",
    font=("Segoe UI", 9, "bold"),
    bg="#f8fafc",
    fg="#64748b"
).pack(side="left")

tk.Label(
    header,
    text="TRANSPARENT SCREEN",
    font=("Segoe UI", 7, "bold"),
    bg="#f8fafc",
    fg="#94a3b8"
).pack(side="right")

# Crystal-Clear Transparent Screen Container
screen_container = tk.Frame(
    glass_body,
    bg="#f1f5f9",
    bd=1,
    relief=tk.SOLID,
    highlightbackground="#cbd5e1",
    highlightthickness=1
)
screen_container.pack(fill="x", padx=16, pady=(10, 18))

# Screen Labels
history_var = tk.StringVar(value="")
history_lbl = tk.Label(
    screen_container,
    textvariable=history_var,
    font=("Segoe UI", 11),
    bg="#f1f5f9",
    fg="#64748b",
    anchor="e",
    padx=16
)
history_lbl.pack(fill="x", pady=(12, 0))

display_var = tk.StringVar(value="0")
display_lbl = tk.Label(
    screen_container,
    textvariable=display_var,
    font=("Segoe UI", 26, "bold"),
    bg="#f1f5f9",
    fg="#0f172a",
    anchor="e",
    padx=16
)
display_lbl.pack(fill="x", pady=(0, 14))

# Keypad Matrix
keypad = tk.Frame(glass_body, bg="#f8fafc")
keypad.pack(fill="both", expand=True, padx=14, pady=(0, 16))

# Button Definitions: (Text, Base BG, Text Color, Hover BG)
buttons = [
    [('AC', '#ffe4e6', '#e11d48', '#fecdd3'), ('DEL', '#ffe4e6', '#e11d48', '#fecdd3'), ('%', '#e0f2fe', '#0284c7', '#bae6fd'), ('÷', '#e0f2fe', '#0284c7', '#bae6fd')],
    [('7', '#ffffff', '#1e293b', '#f1f5f9'), ('8', '#ffffff', '#1e293b', '#f1f5f9'), ('9', '#ffffff', '#1e293b', '#f1f5f9'), ('×', '#e0f2fe', '#0284c7', '#bae6fd')],
    [('4', '#ffffff', '#1e293b', '#f1f5f9'), ('5', '#ffffff', '#1e293b', '#f1f5f9'), ('6', '#ffffff', '#1e293b', '#f1f5f9'), ('-', '#e0f2fe', '#0284c7', '#bae6fd')],
    [('1', '#ffffff', '#1e293b', '#f1f5f9'), ('2', '#ffffff', '#1e293b', '#f1f5f9'), ('3', '#ffffff', '#1e293b', '#f1f5f9'), ('+', '#e0f2fe', '#0284c7', '#bae6fd')],
    [('0', '#ffffff', '#1e293b', '#f1f5f9'), ('.', '#ffffff', '#1e293b', '#f1f5f9'), ('=', '#3b82f6', '#ffffff', '#2563eb'), ('', '', '', '')]
]

def attach_hover(btn, default_bg, hover_bg):
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
            font=("Segoe UI", 13, "bold" if text in ('AC', 'DEL', '=', '÷', '×', '-', '+') else "normal"),
            bg=bg_col,
            fg=fg_col,
            activebackground=hover_col,
            activeforeground=fg_col,
            bd=0,
            relief=tk.FLAT,
            highlightbackground="#e2e8f0" if text != '=' else "#60a5fa",
            highlightthickness=1,
            cursor="hand2",
            command=lambda t=text: on_click(t)
        )
        btn.grid(row=r_idx, column=c_idx, columnspan=colspan, padx=4, pady=4, sticky="nsew")
        attach_hover(btn, bg_col, hover_col)

root.mainloop()