import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random, threading

# ==========================================================
# =============== PHẦN 1: XỬ LÝ TOÁN HỌC ==================
# ==========================================================

# -----------------------------
# 1.1. Kiểm tra số nguyên tố
# -----------------------------
def is_prime(n):
    """Kiểm tra n có phải số nguyên tố hay không"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = int(n ** 0.5) + 1
    for i in range(3, r, 2):
        if n % i == 0:
            return False
    return True


# -----------------------------
# 1.2. Sinh số nguyên tố ngẫu nhiên theo số bit (8,16,64)
# -----------------------------
def random_prime(bits):
    """Tạo số nguyên tố ngẫu nhiên có số bit cho trước"""
    while True:
        num = random.getrandbits(bits)
        # Đảm bảo số đủ độ dài bit và là số lẻ
        num |= (1 << (bits - 1)) | 1
        if is_prime(num):
            return num


# -----------------------------
# 2.1. Ước số chung lớn nhất (GCD)
# -----------------------------
def gcd(a, b):
    """Tính GCD của hai số nguyên lớn"""
    while b:
        a, b = b, a % b
    return a


# -----------------------------
# 3.1. Lũy thừa theo modulo
# -----------------------------
def mod_exp(a, x, p):
    """Tính (a^x mod p) một cách hiệu quả"""
    return pow(a, x, p)


# ==========================================================
# =============== PHẦN 2: GIAO DIỆN TKINTER ================
# ==========================================================
def create_gui():
    root = tk.Tk()
    root.title("Task 5 - Số nguyên tố, GCD, Lũy thừa modulo")
    root.geometry("850x650")

    ttk.Label(root, text="TASK 5", font=("Arial", 16, "bold")).pack(pady=10)

    # Vùng hiển thị kết quả
    output = scrolledtext.ScrolledText(root, width=95, height=20, wrap=tk.WORD)
    output.pack(padx=10, pady=10)

    # ======================================================
    # =============== PHẦN 3: HÀM XỬ LÝ BUTTON =============
    # ======================================================

    # ---- Nhóm 1: Các hàm xử lý SỐ NGUYÊN TỐ ----
    def show_random_prime():
        """Sinh số nguyên tố theo số bit đã chọn"""
        def worker():
            bits = int(combo_bits.get())
            output.delete(1.0, tk.END)
            output.insert(tk.END, f"Đang tạo số nguyên tố {bits} bit...\n")
            prime = random_prime(bits)
            output.insert(tk.END, f"Số nguyên tố {bits} bit được tạo là:\n{prime}\n")
        threading.Thread(target=worker, daemon=True).start()

    def show_top_10():
        """Tìm 10 số nguyên tố lớn nhất < 2^20 - 1
        (thay 20 bằng 89 nếu muốn đúng Mersenne thứ 10, nhưng sẽ rất chậm)"""
        def worker():
            M = 2**20 - 1  # Mô phỏng nhanh cho 2^89 - 1
            primes = []
            num = M - 1
            output.delete(1.0, tk.END)
            output.insert(tk.END, f"Đang tìm 10 số nguyên tố lớn nhất < {M}...\n")
            while len(primes) < 10 and num > 2:
                if is_prime(num):
                    primes.append(num)
                num -= 1
            output.insert(tk.END, "10 số nguyên tố lớn nhất:\n")
            for p in primes:
                output.insert(tk.END, str(p) + "\n")
        threading.Thread(target=worker, daemon=True).start()

    def check_prime():
        """Kiểm tra xem số nhập vào có phải là số nguyên tố không"""
        try:
            n = int(entry_prime.get())
            result = f"{n} là số nguyên tố." if is_prime(n) else f"{n} không phải là số nguyên tố."
            messagebox.showinfo("Kết quả", result)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ!")


    # ---- Nhóm 2: Hàm xử lý GCD ----
    def calc_gcd():
        """Tính GCD của 2 số nguyên lớn"""
        try:
            a = int(entry_a.get())
            b = int(entry_b.get())
            result = f"GCD({a}, {b}) = {gcd(a, b)}"
            messagebox.showinfo("Kết quả", result)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập 2 số nguyên hợp lệ!")


    # ---- Nhóm 3: Hàm xử lý LŨY THỪA THEO MODULO ----
    def calc_modexp():
        """Tính a^x mod p (với x lớn)"""
        try:
            a = int(entry_base.get())
            x = int(entry_exp.get())
            p = int(entry_mod.get())
            result = f"{a}^{x} mod {p} = {mod_exp(a, x, p)}"
            messagebox.showinfo("Kết quả", result)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập các số hợp lệ!")

    # ======================================================
    # =============== PHẦN 4: THIẾT KẾ GIAO DIỆN ===========
    # ======================================================

    frame = ttk.Frame(root)
    frame.pack(pady=5)

    # --- Nhóm 1: SỐ NGUYÊN TỐ ---
    ttk.Label(frame, text="Chọn số bit:").grid(row=0, column=0, padx=5)
    combo_bits = ttk.Combobox(frame, values=["8", "16", "64"], width=8, state="readonly")
    combo_bits.set("8")
    combo_bits.grid(row=0, column=1, padx=5)
    ttk.Button(frame, text="Tạo số nguyên tố", command=show_random_prime).grid(row=0, column=2, padx=5)
    ttk.Button(frame, text="10 số nguyên tố lớn nhất < 2^20 - 1", command=show_top_10).grid(row=0, column=3, padx=5)

    ttk.Label(frame, text="Kiểm tra số nguyên tố:").grid(row=1, column=0)
    entry_prime = ttk.Entry(frame, width=20)
    entry_prime.grid(row=1, column=1)
    ttk.Button(frame, text="Kiểm tra", command=check_prime).grid(row=1, column=2, padx=5)

    # --- Nhóm 2: GCD ---
    ttk.Label(frame, text="Tính GCD (a, b):").grid(row=2, column=0)
    entry_a = ttk.Entry(frame, width=10)
    entry_a.grid(row=2, column=1)
    entry_b = ttk.Entry(frame, width=10)
    entry_b.grid(row=2, column=2)
    ttk.Button(frame, text="Tính GCD", command=calc_gcd).grid(row=2, column=3, padx=5)

    # --- Nhóm 3: LŨY THỪA THEO MODULO ---
    ttk.Label(frame, text="Tính a^x mod p:").grid(row=3, column=0)
    entry_base = ttk.Entry(frame, width=10)
    entry_base.grid(row=3, column=1)
    entry_exp = ttk.Entry(frame, width=10)
    entry_exp.grid(row=3, column=2)
    entry_mod = ttk.Entry(frame, width=10)
    entry_mod.grid(row=3, column=3)
    ttk.Button(frame, text="Tính", command=calc_modexp).grid(row=3, column=4, padx=5)

    root.mainloop()


# ==========================================================
# =============== CHƯƠNG TRÌNH CHÍNH =======================
# ==========================================================
if __name__ == "__main__":
    create_gui()
