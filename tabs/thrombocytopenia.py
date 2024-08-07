import tkinter as tk
from tkinter import ttk
from utils import copy_to_clipboard

def create_thrombocytopenia_tab(notebook):
    tab = ttk.Frame(notebook)
    follow_up_var = tk.StringVar(value="1 week")
    
    def update_message(*args):
        follow_up_time = follow_up_var.get()
        message = (
            "Problem #1 Thrombocytopenia\n"
            "- Reviewed outside lab results which showed\n"
            "- Pt is asymptomatic; no easy bruising or bleeding.\n"
            "- Will obtain lab work including CBC, CMP, vitamin B12, folate, ANA, RF, CRP, ESR, LDH, TSH, HIV, SPEP, hepatitis panel, and blood smear.\n"
            "- At this time there is no indication for SDP transfusions unless plt count < 10K\n"
            "- Bleeding precaution instructions as well as avoidance of unnecessary use of NSAIDS/ASA were recommended to the patient.\n"
            "- Repeat CBC next visit.\n\n"
            f"RTO in {follow_up_time}"
        )
        message_text_box.delete(1.0, tk.END)
        message_text_box.insert(tk.END, message)

    follow_up_var.trace_add("write", update_message)

    tk.Label(tab, text="Next follow-up visit:").pack(pady=5)
    
    follow_up_frame = tk.Frame(tab)
    follow_up_frame.pack(pady=5)
    
    for text in ["1 week", "2 weeks", "3 weeks", "1 month", "3 months"]:
        tk.Radiobutton(follow_up_frame, text=text, variable=follow_up_var, value=text).pack(anchor=tk.W)
    
    message_text_box = tk.Text(tab, height=10, width=70)
    message_text_box.pack(pady=5)

    tk.Button(tab, text="Copy to Clipboard", command=lambda: copy_to_clipboard(message_text_box)).pack(pady=5)

    update_message()  # Initialize the message display
    return tab
