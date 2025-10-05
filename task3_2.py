import string
import matplotlib.pyplot as plt
from collections import Counter
import tkinter as tk
from tkinter import filedialog, scrolledtext

def decrypt_substitution(ciphertext, mapping):
    """Giải mã văn bản dựa trên bảng thay thế ký tự."""
    decrypted_text = ciphertext
    for key, value in mapping.items():
        decrypted_text = decrypted_text.replace(key, value)  # Thay thế tất cả các ký hiệu
    return decrypted_text

def analyze_frequency(text):
    symbols = Counter(text)
    sorted_symbols = symbols.most_common()
    return sorted_symbols

def plot_frequency_analysis(text):
    freq_data = analyze_frequency(text)
    symbols, counts = zip(*freq_data)
    
    plt.figure(figsize=(10, 5))
    plt.bar(symbols, counts, color='skyblue')
    plt.xlabel('Ký tự')
    plt.ylabel('Số lần xuất hiện')
    plt.title('Phân tích tần số ký tự')
    plt.show()

def decrypt_and_display():
    ciphertext = text_input.get("1.0", tk.END).strip()
    mapping_text = mapping_input.get("1.0", tk.END).strip()
    if not ciphertext or not mapping_text:
        output_text.insert(tk.END, "Vui lòng nhập văn bản mã hóa và bảng thay thế!\n")
        return
    
    # Chuyển đổi bảng thay thế từ JSON
    try:
        mapping = dict(item.split(':') for item in mapping_text.split(','))
    except:
        output_text.insert(tk.END, "Bảng thay thế không hợp lệ!\n")
        return
    
    decrypted_text = decrypt_substitution(ciphertext, mapping)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)
    
    plot_frequency_analysis(ciphertext)

def load_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, content)

# GUI
root = tk.Tk()
root.title("Giải mã thay thế")

# Nhập văn bản mã hóa
tk.Label(root, text="Nhập văn bản mã hóa:").pack()
text_input = scrolledtext.ScrolledText(root, height=5, width=50)
text_input.pack()

# Nhập bảng thay thế
tk.Label(root, text="Nhập bảng thay thế (dạng a:x, b:y,...):").pack()
mapping_input = scrolledtext.ScrolledText(root, height=3, width=50)
mapping_input.pack()

# Nút giải mã
decrypt_button = tk.Button(root, text="Giải mã", command=decrypt_and_display)
decrypt_button.pack()

# Nút tải file
#load_button = tk.Button(root, text="Tải file", command=load_file)
#load_button.pack()

# Hiển thị văn bản giải mã
tk.Label(root, text="Văn bản giải mã:").pack()
output_text = scrolledtext.ScrolledText(root, height=5, width=50)
output_text.pack()

root.mainloop()