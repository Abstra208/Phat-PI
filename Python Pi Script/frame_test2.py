import tkinter as tk
from tkinter import TclError, ttk

def show_text():
    text = 'test '
    print(text)

def create_input_frame(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Find what
    ttk.Label(frame, text='Find what:').grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_button_frame(container):

    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Show Text',command=show_text).grid(column=0, row=0)
    ttk.Button(frame, text='Close').grid(column=0, row=1)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_main_window():
    root = tk.Tk()
    root.title('Replace')
    root.resizable(0, 0)
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()
