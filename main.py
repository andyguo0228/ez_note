import tkinter as tk
from tkinter import ttk
from tabs.anemia import create_anemia_tab
from tabs.thrombocytopenia import create_thrombocytopenia_tab
from tabs.leukopenia import create_leukopenia_tab

def main():
    root = tk.Tk()
    root.title("Hematologic Conditions App")
    root.geometry("1200x500")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    anemia_tab = create_anemia_tab(notebook)
    notebook.add(anemia_tab, text="Anemia")

    thrombocytopenia_tab = create_thrombocytopenia_tab(notebook)
    notebook.add(thrombocytopenia_tab, text="Thrombocytopenia")

    leukopenia_tab = create_leukopenia_tab(notebook)
    notebook.add(leukopenia_tab, text="Leukopenia")

    root.mainloop()

if __name__ == "__main__":
    main()
