import string
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Vigenère Cipher Functions

def vigenere_encrypt(plaintext: str, key: str) -> str:
    alphabet = string.ascii_uppercase
    plaintext = ''.join(filter(str.isalpha, plaintext)).upper()
    key = key.upper()
    ciphertext = []

    for i, char in enumerate(plaintext):
        p_val = alphabet.index(char)
        k_val = alphabet.index(key[i % len(key)])
        c_val = (p_val + k_val) % 26
        ciphertext.append(alphabet[c_val])

    return ''.join(ciphertext)


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    alphabet = string.ascii_uppercase
    key = key.upper()
    plaintext = []

    for i, char in enumerate(ciphertext):
        c_val = alphabet.index(char)
        k_val = alphabet.index(key[i % len(key)])
        p_val = (c_val - k_val + 26) % 26
        plaintext.append(alphabet[p_val])

    return ''.join(plaintext)

# UI Functions

def encrypt_message():
    text = plaintext_box.get("1.0", tk.END).strip()
    key = key_entry.get().strip()

    if not text or not key:
        messagebox.showwarning("Warning", "Please enter both text and key!")
        return

    cipher = vigenere_encrypt(text, key)
    ciphertext_box.delete("1.0", tk.END)
    ciphertext_box.insert(tk.END, cipher)


def decrypt_message():
    text = ciphertext_box.get("1.0", tk.END).strip()
    key = key_entry.get().strip()

    if not text or not key:
        messagebox.showwarning("Warning", "Please enter both ciphertext and key!")
        return

    plain = vigenere_decrypt(text, key)
    plaintext_box.delete("1.0", tk.END)
    plaintext_box.insert(tk.END, plain)


# Tkinter UI Layout

root = tk.Tk()
root.title("Vigenère Cipher Tool")
root.geometry("800x600")
root.resizable(False, False)

# Key input
tk.Label(root, text="Key:", font=("Arial", 12)).pack(pady=5)
key_entry = tk.Entry(root, font=("Arial", 12), width=30)
key_entry.pack()

# Plaintext box
tk.Label(root, text="Plaintext:", font=("Arial", 12)).pack(pady=5)
plaintext_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=("Consolas", 11))
plaintext_box.pack(pady=5)

# Ciphertext box
tk.Label(root, text="Ciphertext:", font=("Arial", 12)).pack(pady=5)
ciphertext_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=("Consolas", 11))
ciphertext_box.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

encrypt_btn = tk.Button(btn_frame, text="🔐 Encrypt", font=("Arial", 12), bg="#4CAF50", fg="white", width=12, command=encrypt_message)
encrypt_btn.pack(side=tk.LEFT, padx=10)

decrypt_btn = tk.Button(btn_frame, text="🔓 Decrypt", font=("Arial", 12), bg="#2196F3", fg="white", width=12, command=decrypt_message)
decrypt_btn.pack(side=tk.LEFT, padx=10)

root.mainloop()
