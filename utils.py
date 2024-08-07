from tkinter import messagebox

def copy_to_clipboard(text_widget):
    text = text_widget.get(1.0, 'end').strip()
    text_widget.clipboard_clear()
    text_widget.clipboard_append(text)
    messagebox.showinfo("Info", "Message copied to clipboard!")
