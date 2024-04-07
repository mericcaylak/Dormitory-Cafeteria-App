import tkinter as tk
import sqlite3

con = sqlite3.connect('muratpasakyk.db')
cursor = con.cursor()

window = tk.Tk()
window.geometry('880x650')
window.title('Muratpaşa Fast Food')
window.configure(bg='#DFDFDF')
window.resizable(False, False)

def set_window_position(window, x, y):
    window.geometry(f"+{x}+{y}")

def set_window_size(window, width, height):
    window.geometry(f"{width}x{height}")

window_width = 850
window_height = 615

x_position = 380
y_position = 135

set_window_position(window, x_position, y_position)
set_window_size(window, window_width, window_height)

header = ["Sıra\n", "Ad Soyad\n", "Sipariş\n", "Soslar\n", "Durum\n"]
column_widths = [8, 20, 23, 30, 10]
tablo = tk.Frame(window)
tablo.grid(row=0, column=0)

def satırSil(sıra_numarası):
    def sil_ve_guncelle():
        sorgu = f"DELETE FROM TSiparisler WHERE sira_numarasi = {sıra_numarası}"
        cursor.execute(sorgu)
        cursor.execute(f"UPDATE TSiparisler SET sira_numarasi = sira_numarasi - 1 WHERE sira_numarasi > {sıra_numarası}")
        con.commit()
        updateDatabase()
    return sil_ve_guncelle

def createOnayButton(row_number):
    onayButon=tk.Button(tablo, text='Onay', font=('Bahnschrift', 13), width=8, border=3, command=satırSil(row_number),bg='#75C864', fg='black',cursor='hand2',activebackground='lightblue')
    
    #onayButon Hover
    def on_enter_onayButon(event):
        onayButon.config(bg='lightblue', fg='black')
    
    def on_leave_onayButon(event):
        onayButon.config(bg='#75C864', fg='black')
    
    onayButon.bind('<Enter>', on_enter_onayButon)
    onayButon.bind('<Leave>', on_leave_onayButon)
        
    return onayButon 

def updateDatabase():
    for widget in tablo.winfo_children():
        widget.grid_forget()
    cursor.execute("SELECT * FROM TSiparisler LIMIT 10")
    data = []
    for veri in cursor.fetchall():
        salca = ''
        if 'tost' in veri[2].lower():
            salca = f'Salça {veri[6]}'
        else:
            salca = ''
        if veri != None:
            data.append([f'{veri[0]}\n', f'{veri[1]}\n', f'{veri[3]} adet {veri[2]}\n', f'Ketçap {veri[4]}, Mayonez {veri[5]}\n{salca}'])

    for i, col_name in enumerate(header):
        label = tk.Label(tablo, text=col_name, relief=tk.RIDGE, width=column_widths[i], font=('Bahnschrift Bold', 13))
        label.grid(row=0, column=i)

    for i, row in enumerate(data):
        onay_buton = createOnayButton(i + 1)
        onay_buton.grid(row=i + 1, column=4)
        for j, cell in enumerate(row):
            label = tk.Label(tablo, text=cell, relief=tk.RIDGE, width=column_widths[j], font=('Bahnschrift SemiLight', 13))
            label.grid(row=i + 1, column=j)

def listeSil():
    windowListeSil = tk.Tk()
    windowListeSil.title('Muratpaşa Fast Food')
    windowListeSil.resizable(False, False)
    windowListeSil.configure(bg='#DFDFDF')

    def set_window_position(windowListeSil, x, y):
        windowListeSil.geometry(f"+{x}+{y}")

    def set_window_size(window, width, height):
        windowListeSil.geometry(f"{width}x{height}")

    window_width = 400
    window_height = 275

    x_position = 555
    y_position = 275

    set_window_position(windowListeSil, x_position, y_position)
    set_window_size(windowListeSil, window_width, window_height)

    listeSilLabel = tk.Label(windowListeSil, text='Sipariş Listesini silmek istediğinize\nemin misiniz ?', font=('Bahnschrift', 14), bg='#DFDFDF')
    listeSilLabel.place(x=40, y=60)

    def listeSil():
        cursor.execute("DELETE FROM TSiparisler")
        con.commit()
        windowListeSil.destroy()
        updateDatabase()
        
    def listeSilme():
        windowListeSil.destroy()

    listeSilEvetButon = tk.Button(windowListeSil, text='Evet !!', font=('Bahnschrift', 12),width=8, border=2, command=listeSil, bg='#B6B6B6', fg='black',cursor='hand2',activebackground='#CA484E')
    listeSilEvetButon.place(x=80, y=165)
 
    listeSilHayırButon = tk.Button(windowListeSil, text='Hayır', font=('Bahnschrift', 12),width=8, border=2, command=listeSilme, bg='#B6B6B6', fg='black',cursor='hand2',activebackground='lightblue')
    listeSilHayırButon.place(x=230, y=165)

    #listeSilEvetButon Hover
    def on_enter_listeSilEvetButon(event):
        listeSilEvetButon.config(bg='#CA484E', fg='black')

    def on_leave_listeSilEvetButon(event):
        listeSilEvetButon.config(bg='#B6B6B6', fg='black')

    listeSilEvetButon.bind('<Enter>', on_enter_listeSilEvetButon)
    listeSilEvetButon.bind('<Leave>', on_leave_listeSilEvetButon)
    
    #listeSilEvetButon Hover
    def on_enter_listeSilHayırButon(event):
        listeSilHayırButon.config(bg='lightblue', fg='black')

    def on_leave_listeSilHayırButon(event):
        listeSilHayırButon.config(bg='#B6B6B6', fg='black')

    listeSilHayırButon.bind('<Enter>', on_enter_listeSilHayırButon)
    listeSilHayırButon.bind('<Leave>', on_leave_listeSilHayırButon)
    
yenileButon = tk.Button(text='Yenile', font=('Bahnschrift', 13), width=10, border=3, command=updateDatabase,bg='#B6B6B6', fg='black',cursor='hand2',activebackground='lightblue')
yenileButon.place(x=475, y=550)

#yenileButon Hover
def on_enter_yenileButon(event):
    yenileButon.config(bg='lightblue', fg='black')

def on_leave_yenileButon(event):
    yenileButon.config(bg='#B6B6B6', fg='black')

yenileButon.bind('<Enter>', on_enter_yenileButon)
yenileButon.bind('<Leave>', on_leave_yenileButon)

listeSilButon = tk.Button(text='Listeyi Sil', font=('Bahnschrift', 13), width=10, border=3, command=listeSil,bg='#B6B6B6', fg='black',cursor='hand2',activebackground='lightblue')
listeSilButon.place(x=350, y=550)

#listeSilButon Hover
def on_enter_ListeSilButon(event):
    listeSilButon.config(bg='lightblue', fg='black')

def on_leave_ListeSilButon(event):
    listeSilButon.config(bg='#B6B6B6', fg='black')

listeSilButon.bind('<Enter>', on_enter_ListeSilButon)
listeSilButon.bind('<Leave>', on_leave_ListeSilButon)

def kapat():
    window.destroy()

kapatButon = tk.Button(text='Kapat', font=('Bahnschrift', 13), width=10, border=3, command=kapat,bg='#B6B6B6', fg='black',cursor='hand2',activebackground='lightblue')
kapatButon.place(x=648, y=550)

#butonKapat Hover
def on_enter_kapatButon(event):
    kapatButon.config(bg='lightblue', fg='black')

def on_leave_kapatButon(event):
    kapatButon.config(bg='#B6B6B6', fg='black')

kapatButon.bind('<Enter>', on_enter_kapatButon)
kapatButon.bind('<Leave>', on_leave_kapatButon)

updateDatabase()
window.mainloop()
con.close()


