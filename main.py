from fastapi import FastAPI

app = FastAPI()

import tkinter as tk
from tkinter import messagebox
import os

def save_entry():
    date = entry_date.get()
    entry_text = text_entry.get("1.0", tk.END)

    if not os.path.exists("diary_entries"):
        os.makedirs("diary_entries")

    filename = f"diary_entries/{date}.txt"
    with open(filename, "w") as f:
        f.write(entry_text)

    messagebox.showinfo("保存", "日記エントリーが保存されました。")

def load_entry():
    date = entry_date.get()
    filename = f"diary_entries/{date}.txt"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            entry_text = f.read()
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, entry_text)
    else:
        messagebox.showinfo("エラー", "その日の日記エントリーは見つかりませんでした。")

# GUIの作成
root = tk.Tk()
root.title("日記アプリ")

label_date = tk.Label(root, text="日付（YYYY-MM-DD）:")
label_date.grid(row=0, column=0, padx=5, pady=5)

entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1, padx=5, pady=5)

label_entry = tk.Label(root, text="日記エントリー:")
label_entry.grid(row=1, column=0, padx=5, pady=5)

text_entry = tk.Text(root, height=10, width=30)
text_entry.grid(row=1, column=1, padx=5, pady=5)

button_save = tk.Button(root, text="保存", command=save_entry)
button_save.grid(row=2, column=0, padx=5, pady=5)

button_load = tk.Button(root, text="読み込み", command=load_entry)
button_load.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
