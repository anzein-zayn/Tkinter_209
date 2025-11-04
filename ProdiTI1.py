import tkinter as tk
import tkinter.messagebox as msg
top =tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
lbl_judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", bg=("Purple"), font=("Arial Black", 14, "bold" ))
lbl_judul.pack(pady=10)

top.geometry("500x600")
top.configure(bg="purple")

for i in range(10):
    L1=tk.Label(top, text = f"Nilai {i + 1} ")
    L1.pack(side=tk.TOP)
    E1=tk.Entry(top, bd=5)
    E1.pack(side=tk.TOP)

def tampilkanHasil():
    hasil =E1.get()
    msg.showinfo("Hasil Prediksi", f"Prodi Anda Adalah = Prodi TI")

tombolNama = tk.Button(top, text="Hasil Prediksi", font=("Times New Roman", 7, "bold"), command=tampilkanHasil)
tombolNama.pack(pady= 20) #pady=20
top.mainloop()