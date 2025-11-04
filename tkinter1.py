import tkinter as tk 
import tkinter.messagebox as msg
top =  tk.Tk()
top.title = "My Tkinter Window"
top.geometry = 400 * 300
top.configure(bg="purple")
def pesanHello():
    msg.showinfo("Pesan", "CUMAN EVOSSS!!!")
tombol = tk.Button(top, text="Klik Saya", command=pesanHello)
tombol = tk.Button(top, text="klik Saya", command=pesanHello)
ChekVar1=tk.IntVar()
ChekVar2=tk.IntVar()
Check1=tk.Checkbutton(top, text="Pilihan 1", variable=ChekVar1)
Check2=tk.Checkbutton(top, text="Pilihan 2", variable=ChekVar2)
Check1.pack()
Check2.pack()
L1=tk.Label(top, text="Masukkan nama")
L1.pack(side=tk.LEFT)
E1=tk.Entry(top, bd=5)
E1.pack(side=tk.LEFT)
def tampilkanNama():
    nama =E1.get()
    msg.showinfo("Nama Anda", f"Nama Anda Adalah = {nama}")
tombolNama = tk.Button(top, text="Tampilkan Nama", command=tampilkanNama)
tombolNama.pack(side=tk.BOTTOM) #pady=20
top.mainloop()