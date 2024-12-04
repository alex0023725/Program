import tkinter as tk

def spustit_kod():

    slova = ["ALFA", "BRAVO", "CHARLIE", "DELTA", "ECHO", "FOXTROT", "GOLF",
             "HOTEL", "INDIA", "JULIET", "KILO", "LIMA", "MIKE", "NOVEMBER", "OSCAR"]


    slova_s_A = [slovo for slovo in slova if "A" in slovo]


    result_window = tk.Toplevel(root)
    result_window.title("Vysledky")
    result_window.geometry("400x300")
    result_window.configure(bg="#4B145B")


    result_label = tk.Label(
        result_window,
        text="Slová obsahujúce písmeno 'A':",
        font=("Arial", 16),
        bg="#4B145B",
        fg="white"
    )
    result_label.pack(pady=(10, 10))


    for slovo in slova_s_A:
        word_label = tk.Label(
            result_window,
            text=slovo,
            font=("Arial", 14),
            bg="#4B145B",
            fg="white"
        )
        word_label.pack()


root = tk.Tk()
root.title("Programovacie techniky")
root.geometry("600x400")
root.configure(bg="#4B145B")

title_label = tk.Label(
    root,
    text="Programovacie techniky",
    font=("Arial", 24),
    bg="#4B145B",
    fg="white"
)
title_label.pack(pady=(50, 10))


subtitle_label = tk.Label(
    root,
    text="Kondratiev Oleksandr",
    font=("Arial", 16),
    bg="#4B145B",
    fg="white"
)
subtitle_label.pack(pady=(0, 30))

# Кнопка "Start"
start_button = tk.Button(
    root,
    text="Start",
    font=("Arial", 14),
    bg="#CE8FC2",
    fg="white",
    activebackground="#BA70AC",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    command=spustit_kod
)
start_button.pack()
root.mainloop()
