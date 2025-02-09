from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", source_lang="English", dest_lang="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=source_lang, dest=dest_lang)
    return trans1.text

def data():
    s = combo_sor.get()
    d = combo_dest.get()
    message = Source_txt.get(1.0, END)
    textget = change(text=message, source_lang=s, dest_lang=d)
    
    dest_txt.config(state=NORMAL)  # Enable editing
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)
    dest_txt.config(state=DISABLED)  # Disable editing to prevent user modification

root = Tk()
root.title("Language Translator")
root.geometry("550x800")  # Increased height for better visibility
root.config(bg="Light Blue")
# Title Label
Label(root, text="Translator", font=("Times New Roman", 40, "bold")).place(x=100, y=20, height=50, width=350)
# Source Text Label
Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="black", bg="lavender").place(x=100, y=80, height=30, width=350)
# Source Text Box with Scrollbar
source_frame = Frame(root)
source_frame.place(x=10, y=120, height=180, width=520)
scroll_y_src = Scrollbar(source_frame, orient=VERTICAL)
Source_txt = Text(source_frame, font=("Times New Roman", 15), wrap=WORD, yscrollcommand=scroll_y_src.set)
scroll_y_src.config(command=Source_txt.yview)
scroll_y_src.pack(side=RIGHT, fill=Y)
Source_txt.pack(fill=BOTH, expand=True)
# Language Selection
list_txt = list(LANGUAGES.values())
combo_sor = ttk.Combobox(root, value=list_txt)
combo_sor.place(x=10, y=320, height=40, width=150)
combo_sor.set("English")

Button(root, text="Translate",bg="grey",  font=("Arial", 15, "bold"),relief=RAISED, command=data).place(x=200, y=320, height=40, width=150)

combo_dest = ttk.Combobox(root, value=list_txt)
combo_dest.place(x=380, y=320, height=40, width=150)
combo_dest.set("English")

# Destination Text Label
Label(root, text="Destination Text", font=("Times New Roman", 20, "bold"), fg="black", bg="lavender").place(x=100, y=380, height=30, width=350)

# Destination Text Box with Scrollbar
dest_frame = Frame(root)
dest_frame.place(x=10, y=420, height=250, width=520)  # Increased height

scroll_y_dest = Scrollbar(dest_frame, orient=VERTICAL)
dest_txt = Text(dest_frame, font=("Times New Roman", 15,), wrap=WORD, yscrollcommand=scroll_y_dest.set, state=DISABLED)  # Set to disabled initially
scroll_y_dest.config(command=dest_txt.yview)
scroll_y_dest.pack(side=RIGHT, fill=Y)
dest_txt.pack(fill=BOTH, expand=True)

root.mainloop()
