import tkinter as tk
from tkinter import ttk
from utils import copy_to_clipboard

def create_anemia_tab(notebook):
    tab = ttk.Frame(notebook)

    
    left_frame = tk.Frame(tab, bg='skyblue')
    left_frame.pack(side='left', fill='both', padx=5, pady=5, expand=True)
    
    right_frame = tk.Frame(tab, bg='lightgreen')
    right_frame.pack(side='right', fill='both', padx=5, pady=5, expand=True)
    
    def update_message(*args):
        hgb_value = hgb_var.get()
        follow_up_time = follow_up_var.get()
        message = (
            "Problem #1 Anemia\n"
            f"- Today's CBC showed microcytic hypochromic anemia with Hgb {hgb_value}; pt is unable to tolerate PO iron due to GI side effects\n"
            "- There is no evidence of active bleed at this time.\n"
            "- Will obtain lab work including CBC, CMP, iron studies, vitamin B12, folate, reticulocyte, EPO, TSH, SPEP\n"
            "- Patient is asymptomatic and there is no indication for urgent blood product support unless Hg is less than 7.\n"
            "- Repeat CBC next visit\n"
            "- Will start patient on IV iron tx with Venofer\n\n"
            f"RTO in {follow_up_time} for IV iron tx"
        )
        message_text_box.delete(1.0, tk.END)
        message_text_box.insert(tk.END, message)

    hgb_var = tk.StringVar()
    hgb_var.trace_add("write", update_message)
    
    follow_up_var = tk.StringVar(value="1 week")
    follow_up_var.trace_add("write", update_message)

    tk.Label(left_frame, text="Enter Hgb value:").pack(pady=5)
    tk.Entry(left_frame, textvariable=hgb_var, width=30).pack(pady=5)

    # follow_up_frame = tk.Frame(tab)
    # follow_up_frame.pack(pady=5)
    tk.Label(left_frame, text="Next follow-up visit:").pack(pady=5)
    
    fu_frame = tk.Frame(left_frame)
    fu_frame.pack(pady=5)
    for text in ["1 week", "2 weeks", "3 weeks", "1 month", "3 months"]:
        tk.Radiobutton(fu_frame, text=text, variable=follow_up_var, value=text).pack(side='left', padx=5)
    
    message_text_box = tk.Text(right_frame, height=15, width=70)
    message_text_box.pack(pady=5)

    tk.Button(right_frame, text="Copy to Clipboard", command=lambda: copy_to_clipboard(message_text_box)).pack(pady=5)

    update_message()  # Initialize the message display
    return tab
