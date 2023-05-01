def openfile(mode:str = "a"):
     from tkinter import filedialog
     file = filedialog.askopenfile(mode=mode)
     return file.name


def encrypt(file):
    key = b'KQ0JTqwSiyq_EdwsB7mHLhAP9mWm3qV1WoCGTfYfu3w='

    from fernet import Fernet
    with open(file, 'rb') as f:
        content = f.read()
    content = Fernet(key).encrypt(content)
    with open(file, 'wb') as w:
        w.write(content)

def decrypt(file):
    key = b'KQ0JTqwSiyq_EdwsB7mHLhAP9mWm3qV1WoCGTfYfu3w='
    
    from fernet import Fernet
    with open(file, 'rb') as f:
        content = f.read()
    content = Fernet(key).decrypt(content)
    with open(file, 'wb') as w:
        w.write(content)



def viewfile():
     filepath = openfile("r")
     return filepath


def entry():
     path = openfile()

     import tkinter as tk
     from tkinter import ttk

     def print_contents(event, entry, next_entry, meta):
          with open(path, "a") as file:
               decrypt(path)
               file.write(meta, entry.get() + "\n")
               encrypt(path)

          entry.delete(0, tk.END)
          next_entry.focus_set()

          with open(path, "a") as file:
               decrypt(path)
               file.write(entry.get() + "\n")
               encrypt(path)

          entry.delete(0, tk.END)
          next_entry.focus_set()

          

     root = tk.Tk()
     root.geometry("300x200")

# First label and entry widget
     label1 = tk.Label(root, text="site:")
     label1.grid(row=0, column=0, padx=10, pady=10)

     entry1 = tk.Entry(root)
     entry1.grid(row=0, column=1, padx=10, pady=10)

# Second label and entry widget
     label2 = tk.Label(root, text="password:")
     label2.grid(row=1, column=0, padx=10, pady=10)

     entry2 = tk.Entry(root)
     entry2.grid(row=1, column=1, padx=10, pady=10)

# Third label and entry widget
     label3 = tk.Label(root, text="username:")
     label3.grid(row=2, column=0, padx=10, pady=10)

     entry3 = tk.Entry(root)
     entry3.grid(row=2, column=1, padx=10, pady=10)


     entry1.bind("<Return>", lambda event: print_contents(event, entry1, entry2, "site:"))

     entry2.bind("<Return>", lambda event: print_contents(event, entry2, entry3, "password:"))

     entry3.bind("<Return>", lambda event: print_contents(event, entry3, entry1, "username:"))


     button = tk.Button(root, text="Close", command=root.destroy)
     button.grid(row=3, column=1, pady=10)


     root.mainloop()


def view():
    import tkinter as tk
    # Create the root window
    path = openfile()

    decrypt(path)

    root = tk.Tk()

    # Create a scrollable text widget
    text_widget = tk.Text(root, wrap="none")
    text_widget.pack(side="left", fill="both", expand=True)

    # Create a scrollbar and attach it to the text widget
    scrollbar = tk.Scrollbar(root, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar.set)

    # Open the file and insert its contents into the text widget
    with open(path, "r") as file:
        contents = file.read()
        text_widget.insert("1.0", contents)

    # Start the main loop
    root.mainloop()

    encrypt(path)

def menu():
     import tkinter as tk
     from tkinter import ttk

     root = tk.Tk()
     root.geometry("400x300")

     frm = ttk.Frame(root, padding=10)
     frm.pack(expand=True)

     btn = ttk.Button(frm, text="view File", command=view, padding=10)
     btn.pack(padx=10, pady=10)

     btn1 = ttk.Button(frm, text="enter a password", command=entry, padding=10)
     btn1.pack(padx=10, pady=10)

     root.mainloop()
