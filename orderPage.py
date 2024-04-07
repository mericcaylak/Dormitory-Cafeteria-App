import tkinter as tk
from tkinter import ttk
import sqlite3  
from tkinter import messagebox
from tkinter import *

con=sqlite3.connect('muratpasakyk.db')
cursor=con.cursor() 

def Main():
    
    def fastfood_tablo_olustur():
        cursor.execute("CREATE TABLE IF NOT EXISTS TSiparisler (sira_numarasi INTEGER PRIMARY KEY,isim_soyisim TEXT,siparis TEXT,adet INTEGER,ketcap_durum TEXT,mayonez_durum TEXT,salca_durum TEXT)")
        con.commit()

    fastfood_tablo_olustur()
        
    window=tk.Tk()
    window.title('Muratpaşa Fast Food')
    window.configure(bg='#DFDFDF')
    window.resizable(False, False)
    
    def set_window_position(window, x, y):
        window.geometry(f"+{x}+{y}")

    def set_window_size(window, width, height):
        window.geometry(f"{width}x{height}")
      
    window_width = 650  
    window_height = 550  

    x_position = 434
    y_position = 141

    set_window_position(window, x_position, y_position)
    set_window_size(window, window_width, window_height)
      
    title=tk.Label(text='Kantin Sipariş Formu',font=('Bahnschrift',19),bg='#DFDFDF')
    title.place(x=200,y=25)

    tostlarLabel=tk.Label(window,text='Tostlar',font=('Bahnschrift',15),bg='#DFDFDF')
    tostlarLabel.place(x=60,y=135)

    lineUnderTostlar = tk.Frame(window, height=1, width=600, background="black")
    lineUnderTostlar.place(x=20,y=170)
        
    def siparisEkran():
        window.withdraw()
        
        window2=tk.Tk()
        window2.title('Muratpaşa Fast Food')
        window2.geometry('400x300')
        window2.configure(bg='#DFDFDF')
        window2.resizable(False, False)    
        
        def set_window_position(window2, x, y):
            window2.geometry(f"+{x}+{y}")
        def set_window_size(window2, width, height):
            window2.geometry(f"{width}x{height}")
        
        window_width = 400  
        window_height = 300  
        
        x_position = 568
        y_position = 272
        
        set_window_position(window2, x_position, y_position)
        set_window_size(window2, window_width, window_height)
        
        isimSoyisimLabel=tk.Label(window2,text='Ad Soyad',font=('Bahnschrift',14),bg='#DFDFDF')
        isimSoyisimLabel.place(x=50,y=45)
        
        adetSecimi = tk.StringVar()
        adetSecimi.set("1")
        
        AdetLabel=tk.Label(window2,text='Adet',font=('Bahnschrift',12),bg='#DFDFDF')
        AdetLabel.place(x=285,y=50)
        
        comboVar = tk.StringVar()
        combo = ttk.Combobox(window2, textvariable=comboVar, values=[1,2,3,4,5],width=4,cursor='hand2')
        combo.set(1)
        combo.place(x=285,y=85)
        
        isimEntry=tk.Entry(window2,font=('Bahnschrift',14),width=18,borderwidth=2)
        isimEntry.place(x=50,y=82)
        
        sos1V=tk.IntVar(window2,True)
        sos1=tk.Checkbutton(window2,text='Ketçap',variable=sos1V,bg='#DFDFDF',cursor='hand2')
        sos1.grid(row=1,column=1)
        sos1.place(x=50,y=135)
        
        sos2V=tk.IntVar(window2,True)
        sos2=tk.Checkbutton(window2,text='Mayonez',variable=sos2V,bg='#DFDFDF',cursor='hand2')
        sos2.grid(row=1,column=1)
        sos2.place(x=50,y=163)
        
        if 'tost' in urun.lower():
            sos3V=tk.IntVar(window2,False)
            sos3=tk.Checkbutton(window2,text='Salça',variable=sos3V,bg='#DFDFDF',cursor='hand2')
            sos3.grid(row=1,column=1)
            sos3.place(x=150,y=135)
        
        def siparisVer():
            isimVeri=isimEntry.get()
            isimVeri=isimVeri.replace('.','').replace(',','').replace(';','').replace('<','').replace('>','').replace(':','').replace('-','').replace('_','').replace('*','').replace('"','').strip()
            if isimVeri=='':
                messagebox.showerror('Error','Lütfen Ad Soyad kısmını doldurunuz.')
                return
            if ' ' in isimVeri:
                isimVeri=isimVeri.split(' ')
                name1=isimVeri[0][0].upper()+isimVeri[0][1:]
                name2=isimVeri[1][0].upper()+isimVeri[1][1:]
                result=name1+' '+name2
                isimVeri=result
            else:
                name=isimVeri[0].upper()+isimVeri[1:]
                isimVeri=name
            adetVeri=combo.get()
            sos1Veri=sos1V.get()
            sos2Veri=sos2V.get()
            if 'tost' in urun.lower():
                sos3Veri=sos3V.get()

            if sos1Veri==1:
                sos1Veri='Var'
            else:
                sos1Veri='Yok'
            
            if sos2Veri==1:
                sos2Veri='Var'
            else:
                sos2Veri='Yok'
            if 'tost' in urun.lower():
                if sos3Veri==1:
                    sos3Veri='Var'
                else:       
                    sos3Veri='Yok'
            else:
                sos3Veri=''
            cursor.execute("INSERT INTO TSiparisler (isim_soyisim, siparis, adet, ketcap_durum, mayonez_durum, salca_durum) VALUES (?, ?, ?, ?, ?, ?)",
                (isimVeri,urun,adetVeri,sos1Veri,sos2Veri,sos3Veri))
            con.commit()    
            
            window.deiconify()
            window2.destroy()
            
        siparisVerButon=tk.Button(window2,text='Sipariş Ver',font=('Bahnschrift',12),bg='#75C864',activebackground='lightblue',cursor='hand2',command=siparisVer)
        siparisVerButon.place(x=256,y=235)
        
        def geri():
            window.deiconify()
            window2.destroy()  
            
        geriButon=tk.Button(window2,text='Geriye Dön',font=('Bahnschrift',12),bg='#B6B6B6',activebackground='lightblue',cursor='hand2',command=geri)
        geriButon.place(x=50,y=235)
        
        #siparisVerButon Hover
        def on_enter_siparisVerButon(event):
            siparisVerButon.config(bg='lightblue', fg='black')

        def on_leave_siparisVerButon(event):
            siparisVerButon.config(bg='#75C864', fg='black')

        siparisVerButon.bind('<Enter>', on_enter_siparisVerButon)
        siparisVerButon.bind('<Leave>', on_leave_siparisVerButon)
        
        #geriButon Hover
        def on_enter_geriButon(event):
            geriButon.config(bg='lightblue', fg='black')

        def on_leave_geriButon(event):
            geriButon.config(bg='#B6B6B6', fg='black')

        geriButon.bind('<Enter>', on_enter_geriButon)
        geriButon.bind('<Leave>', on_leave_geriButon)
            
        window2.mainloop() 
        
    def kapat():
        window.destroy()
        LoginWindow()

    def SonSiparisSilEkran():
        windowSonSiparisSil=tk.Tk()
        windowSonSiparisSil.title('Muratpaşa Fast Food')
        windowSonSiparisSil.resizable(False, False)
        windowSonSiparisSil.configure(bg='#DFDFDF')
        
        def set_window_position(windowSonSiparisSil, x, y):
            windowSonSiparisSil.geometry(f"+{x}+{y}")
            
        def set_window_size(windowSonSiparisSil, width, height):
            windowSonSiparisSil.geometry(f"{width}x{height}")
        
        window_width = 400  
        window_height = 275  

        x_position = 555
        y_position = 275

        set_window_position(windowSonSiparisSil, x_position, y_position)
        set_window_size(windowSonSiparisSil, window_width, window_height)
        
        silLabel=tk.Label(windowSonSiparisSil,text='Son verilen siparişi silmek istediğinize\nemin misiniz ?',font=('Bahnschrift',14),bg='#DFDFDF')
        silLabel.place(x=30,y=60)
        
        def SonSiparisSil():
            cursor.execute("SELECT MAX(sira_numarasi) FROM TSiparisler")
            enSonKayıt=cursor.fetchone()[0]
            if enSonKayıt is not None:
                cursor.execute("DELETE FROM TSiparisler WHERE sira_numarasi=?",(enSonKayıt,))
                con.commit()
            windowSonSiparisSil.destroy()
        
        def SonSiparisSilme():
            windowSonSiparisSil.destroy()
            
        sonSiparisSilEvetButon=tk.Button(windowSonSiparisSil,text='Evet !!',font=('Bahnschrift',12),bg='#B6B6B6',fg='black',activebackground='#CA484E',cursor='hand2',width=8,border=2,command=SonSiparisSil)
        sonSiparisSilEvetButon.place(x=80,y=165)
        
        sonSiparisSilHayırButon=tk.Button(windowSonSiparisSil,text='Hayır',font=('Bahnschrift',12),bg='#B6B6B6',fg='black',activebackground='lightblue',cursor='hand2',width=8,border=2,command=SonSiparisSilme)
        sonSiparisSilHayırButon.place(x=230,y=165)
        
        #sonSiparisSilEvetButon Hover
        def on_enter_sonSiparisSilEvetButon(event):
            sonSiparisSilEvetButon.config(bg='#CA484E', fg='black')

        def on_leave_sonSiparisSilEvetButon(event):
            sonSiparisSilEvetButon.config(bg='#B6B6B6', fg='black')

        sonSiparisSilEvetButon.bind('<Enter>', on_enter_sonSiparisSilEvetButon)
        sonSiparisSilEvetButon.bind('<Leave>', on_leave_sonSiparisSilEvetButon)
            
        #sonSiparisSilHayırButon Hover
        def on_enter_sonSiparisSilHayırButon(event):
            sonSiparisSilHayırButon.config(bg='lightblue', fg='black')

        def on_leave_sonSiparisSilHayırButon(event):
            sonSiparisSilHayırButon.config(bg='#B6B6B6', fg='black')

        sonSiparisSilHayırButon.bind('<Enter>', on_enter_sonSiparisSilHayırButon)
        sonSiparisSilHayırButon.bind('<Leave>', on_leave_sonSiparisSilHayırButon)
            
    def karısıkTost():
        global urun
        urun='Karışık Tost'
        siparisEkran()

    def kasarlıTost():
        global urun
        urun='Kaşarlı Tost'
        siparisEkran()

    def sucukluTost():
        global urun
        urun='Sucuklu Tost'
        siparisEkran()

    def doner():
        global urun
        urun='Döner'
        siparisEkran()

    def sinitzel():
        global urun
        urun='Şinitzel'
        siparisEkran()
        
    def nugget():
        global urun
        urun='Nugget'
        siparisEkran()

    def burger():
        global urun
        urun='Burger'
        siparisEkran()

    def pizza():
        global urun
        urun='Pizza'
        siparisEkran()
        
    karısıkTostButon=tk.Button(text='Karışık Tost',font=('Bahnschrift',12),bg='#D5B880',fg='black',activebackground='lightblue',cursor='hand2',command=karısıkTost)
    karısıkTostButon.place(x=60,y=190)

    kasarlıTostButon=tk.Button(text='Kaşarlı Tost',font=('Bahnschrift',12),bg='#D5B880',fg='black',activebackground='lightblue',cursor='hand2',command=kasarlıTost)
    kasarlıTostButon.place(x=200,y=190)

    sucukluTostButon=tk.Button(text='Sucuklu Tost',font=('Bahnschrift',12),bg='#D5B880',fg='black',activebackground='lightblue',cursor='hand2',command=sucukluTost)
    sucukluTostButon.place(x=340,y=190)

    DigerFastFoodlarLabel=tk.Label(window,text='Diğer Fast Foodlar',font=('Bahnschrift',15),bg='#DFDFDF')
    DigerFastFoodlarLabel.place(x=60,y=295)

    lineUnderDigerFastFoodlarLabel = tk.Frame(window, height=1, width=600, background="black")
    lineUnderDigerFastFoodlarLabel.place(x=20,y=330)

    donerButon=tk.Button(text='Döner',font=('Bahnschrift',12),bg='#D5B880',fg='black',activebackground='lightblue',cursor='hand2',command=doner)
    donerButon.place(x=60,y=350)

    sinitzelButon=tk.Button(text='Şinitzel',font=('Bahnschrift',12),bg='#D5B880',fg='black',activebackground='lightblue',cursor='hand2',command=sinitzel)
    sinitzelButon.place(x=162,y=350)

    nuggetButon=tk.Button(text='Nugget',font=('Bahnschrift',12),bg='#D5B880',fg='black',activebackground='lightblue',cursor='hand2',command=nugget)
    nuggetButon.place(x=271,y=350)

    burgerButon=tk.Button(text='Burger',font=('Bahnschrift',12),bg='#D5B880',fg='black',activebackground='lightblue',cursor='hand2',command=burger)
    burgerButon.place(x=379,y=350)

    pizzaButon=tk.Button(text='Pizza',font=('Bahnschrift',12),bg='#D5B880',fg='black',activebackground='lightblue',cursor='hand2',command=pizza)
    pizzaButon.place(x=484,y=350)

    kapatButon=tk.Button(text='Kapat',font=('Bahnschrift',13),bg='#B6B6B6',fg='black',activebackground='lightblue',cursor='hand2',width=10,border=2,command=kapat)
    kapatButon.place(x=495,y=480)

    silButon=tk.Button(window,text='Son Siparişi Sil',font=('Bahnschrift',13),bg='#B6B6B6',fg='black',activebackground='lightblue',cursor='hand2',width=14,border=2,command=SonSiparisSilEkran)
    silButon.place(x=60,y=480)
    
    #karısıkTostButon Hover
    def on_enter_karısıkTostButon(event):
        karısıkTostButon.config(bg='lightblue', fg='black')

    def on_leave_karısıkTostButon(event):
        karısıkTostButon.config(bg='#D5B880', fg='black')

    karısıkTostButon.bind('<Enter>', on_enter_karısıkTostButon)
    karısıkTostButon.bind('<Leave>', on_leave_karısıkTostButon)

    #kasarlıTostButon Hover
    def on_enter_kasarlıTostButon(event):
        kasarlıTostButon.config(bg='lightblue', fg='black')

    def on_leave_kasarlıTostButon(event):
        kasarlıTostButon.config(bg='#D5B880', fg='black')

    kasarlıTostButon.bind('<Enter>', on_enter_kasarlıTostButon)
    kasarlıTostButon.bind('<Leave>', on_leave_kasarlıTostButon)
    
    #sucukluTostButon Hover
    def on_enter_sucukluTostButon(event):
        sucukluTostButon.config(bg='lightblue', fg='black')

    def on_leave_sucukluTostButon(event):
        sucukluTostButon.config(bg='#D5B880', fg='black')

    sucukluTostButon.bind('<Enter>', on_enter_sucukluTostButon)
    sucukluTostButon.bind('<Leave>', on_leave_sucukluTostButon)
    
    #donerButon Hover
    def on_enter_donerButon(event):
        donerButon.config(bg='lightblue', fg='black')

    def on_leave_donerButon(event):
        donerButon.config(bg='#D5B880', fg='black')

    donerButon.bind('<Enter>', on_enter_donerButon)
    donerButon.bind('<Leave>', on_leave_donerButon)
    
    #sinitzelButon Hover
    def on_enter_sinitzelButon(event):
        sinitzelButon.config(bg='lightblue', fg='black')

    def on_leave_sinitzelButon(event):
        sinitzelButon.config(bg='#D5B880', fg='black')

    sinitzelButon.bind('<Enter>', on_enter_sinitzelButon)
    sinitzelButon.bind('<Leave>', on_leave_sinitzelButon)
    
    #nuggetButon Hover
    def on_enter_nuggetButon(event):
        nuggetButon.config(bg='lightblue', fg='black')

    def on_leave_nuggetButon(event):
        nuggetButon.config(bg='#D5B880', fg='black')

    nuggetButon.bind('<Enter>', on_enter_nuggetButon)
    nuggetButon.bind('<Leave>', on_leave_nuggetButon)
    
    #burgerButon Hover
    def on_enter_burgerButon(event):
        burgerButon.config(bg='lightblue', fg='black')

    def on_leave_burgerButon(event):
        burgerButon.config(bg='#D5B880', fg='black')

    burgerButon.bind('<Enter>', on_enter_burgerButon)
    burgerButon.bind('<Leave>', on_leave_burgerButon)
    
    #pizzaButon Hover
    def on_enter_pizzaButon(event):
        pizzaButon.config(bg='lightblue', fg='black')

    def on_leave_pizzaButon(event):
        pizzaButon.config(bg='#D5B880', fg='black')

    pizzaButon.bind('<Enter>', on_enter_pizzaButon)
    pizzaButon.bind('<Leave>', on_leave_pizzaButon)

    #kapatButon Hover
    def on_enter_kapatButon(event):
        kapatButon.config(bg='lightblue', fg='black')

    def on_leave_kapatButon(event):
        kapatButon.config(bg='#B6B6B6', fg='black')

    kapatButon.bind('<Enter>', on_enter_kapatButon)
    kapatButon.bind('<Leave>', on_leave_kapatButon)
    
    #silButon Hover
    def on_enter_silButon(event):
        silButon.config(bg='lightblue', fg='black')

    def on_leave_silButon(event):
        silButon.config(bg='#B6B6B6', fg='black')

    silButon.bind('<Enter>', on_enter_silButon)
    silButon.bind('<Leave>', on_leave_silButon)

    window.mainloop()

def kullanici_tablo_olustur():
        cursor.execute("CREATE TABLE IF NOT EXISTS TKullanici (kullanici_adi TEXT,sifre TEXT)")
        con.commit()

kullanici_tablo_olustur()

cursor.execute("SELECT * FROM TKullanici")
row=cursor.fetchone()
kullaniciAdi=row[0]
sifre=row[1]

def LoginWindow():
    windowLogin=tk.Tk()
    windowLogin.title('Muratpaşa Fast Food Login')
    windowLogin.geometry('350x400')
    windowLogin.configure(bg='#DFDFDF')
    windowLogin.resizable(False, False)

    def set_window_position(windowLogin, x, y):
        windowLogin.geometry(f"+{x}+{y}")

    def set_window_size(windowLogin, width, height):
        windowLogin.geometry(f"{width}x{height}")

    window_width = 400  
    window_height = 400  
            
    x_position = 568
    y_position = 225

    set_window_position(windowLogin, x_position, y_position)
    set_window_size(windowLogin, window_width, window_height)

    def on_enter_kullaniciAdiEntry(e):
        kullaniciAdiEntry.delete(0,'end')

    def on_leave_kullaniciAdiEntry(e):
        name=kullaniciAdiEntry.get()
        if name=='':
            kullaniciAdiEntry.insert(0,'Kullanıcı Adı')
        
    def on_enter_sifreEntry(e):
        sifreEntry.delete(0,'end')
        sifreEntry.config(show='•')
        
    def on_leave_sifreEntry(e):
        name=sifreEntry.get()
        if name=='':
            sifreEntry.insert(0,'Şifre')
            sifreEntry.config(show='')
        else:
            sifreEntry.config(show='•')
            
    kullaniciAdiEntry=tk.Entry(font=('Bahnschrift',15),width=25,border=0,bg='#DFDFDF',fg='#353535')
    kullaniciAdiEntry.place(x=50,y=80)
    kullaniciAdiEntry.insert(0,'Kullanıcı Adı')
    kullaniciAdiEntry.bind('<FocusIn>',on_enter_kullaniciAdiEntry)
    kullaniciAdiEntry.bind('<FocusOut>',on_leave_kullaniciAdiEntry)

    Frame(windowLogin,width=295,height=2,bg='black').place(x=50,y=115)

    sifreEntry=tk.Entry(show='',font=('Bahnschrift',15),width=25,border=0,bg='#DFDFDF',fg='#353535')
    sifreEntry.place(x=50,y=165)
    sifreEntry.insert(0,'Şifre')
    sifreEntry.bind('<FocusIn>',on_enter_sifreEntry)
    sifreEntry.bind('<FocusOut>',on_leave_sifreEntry)
        
    Frame(windowLogin,width=295,height=2,bg='black').place(x=50,y=200)

    def sifreGet():
        global sifreVeri
        sifreVeri=sifreEntry.get()
        sifreVeri=sifreVeri.strip()
        sifreVeri=sifreVeri
        return sifreVeri

    def kullaniciAdiGet():
        global kullaniciAdiVeri
        kullaniciAdiVeri=kullaniciAdiEntry.get()
        kullaniciAdiVeri=kullaniciAdiVeri.strip()
        return kullaniciAdiVeri

    def kontrol():
        sifreGet()
        kullaniciAdiGet()
        if kullaniciAdi==kullaniciAdiVeri and sifre==sifreVeri:
            windowLogin.destroy()
            Main()
        else:
            if kullaniciAdiVeri=='Kullanıcı Adı' or sifreVeri=='Şifre':
                messagebox.showerror('Error','Lütfen Kullanıcı Adı ve Şifre giriniz !')    
            else:
                messagebox.showerror('Error','Şifre veya Kullanıcı Adı hatalı !')
            
    girisButon=tk.Button(text='Giriş',font=('Bahnschrift',13),width=32,border=2,command=kontrol,bg='#57a1f8',fg='black',cursor='hand2',activebackground='lightblue')
    girisButon.place(x=48,y=240)

    def sifreDegistir():
        windowLogin.withdraw()          
        windowSifreDegistir=tk.Tk()     
        windowSifreDegistir.title('Muratpaşa Fast Food Change Password')
        windowSifreDegistir.configure(bg='#DFDFDF')
        windowSifreDegistir.resizable(False, False)
        
        def set_window_position(windowSifreDegistir, x, y):
            windowSifreDegistir.geometry(f"+{x}+{y}")

        def set_window_size(windowSifreDegistir, width, height):
            windowSifreDegistir.geometry(f"{width}x{height}")
        
        window_width = 400  
        window_height = 400  

        x_position = 568
        y_position = 225

        set_window_position(windowSifreDegistir, x_position, y_position)
        set_window_size(windowSifreDegistir, window_width, window_height)
        
        def on_enter_eskiSifreEntry(e):
            eskiSifreEntry.delete(0,'end')
            eskiSifreEntry.config(show='•')
            
        def on_leave_eskiSifreEntry(e):
            name=eskiSifreEntry.get()
            if name=='':
                eskiSifreEntry.insert(0,'Şifre')
                eskiSifreEntry.config(show='')
            else:
                eskiSifreEntry.config(show='•')
                
        def on_enter_yeniSifreEntry(e):
            yeniSifreEntry.delete(0,'end')
            yeniSifreEntry.config(show='•')
            
        def on_leave_yeniSifreEntry(e):
            name=yeniSifreEntry.get()
            if name=='':
                yeniSifreEntry.insert(0,'Yeni Şifre')
                yeniSifreEntry.config(show='')
            else:
                yeniSifreEntry.config(show='•')
            
        eskiSifreEntry=tk.Entry(windowSifreDegistir,show='',font=('Bahnschrift',15),width=25,border=0,bg='#DFDFDF',fg='#353535')
        eskiSifreEntry.place(x=50,y=80)
        eskiSifreEntry.insert(0,'Şifre')
        eskiSifreEntry.bind('<FocusIn>',on_enter_eskiSifreEntry)
        eskiSifreEntry.bind('<FocusOut>',on_leave_eskiSifreEntry)
        
        Frame(windowSifreDegistir,width=295,height=2,bg='black').place(x=50,y=115)
        
        yeniSifreEntry=tk.Entry(windowSifreDegistir,show='',font=('Bahnschrift',15),width=25,border=0,bg='#DFDFDF',fg='#353535')
        yeniSifreEntry.place(x=50,y=165)
        yeniSifreEntry.insert(0,'Yeni Şifre')
        yeniSifreEntry.bind('<FocusIn>',on_enter_yeniSifreEntry)
        yeniSifreEntry.bind('<FocusOut>',on_leave_yeniSifreEntry)
            
        Frame(windowSifreDegistir,width=295,height=2,bg='black').place(x=50,y=200)
            
        def onayla():
            global sifre
            eskiSifre=eskiSifreEntry.get()
            yeniSifre=yeniSifreEntry.get()
            if eskiSifre=='' or yeniSifre=='':
                    messagebox.showerror('Error','Lütfen gerekli alanları doldurunuz !')
            
            elif eskiSifre==sifre:
                if eskiSifre==yeniSifre:
                    messagebox.showerror('Error','Yeni şifreniz ile eski şifreniz aynı olamaz !')
                else:
                    cursor.execute("UPDATE TKullanici SET sifre = ? WHERE kullanici_adi = ?", (yeniSifre, 'muratpasakyk'))
                    con.commit()
                    sifre=yeniSifre        
                    messagebox.showinfo('Succes','Şifre başarıyla değiştirildi !')
                    windowSifreDegistir.destroy()
                    windowLogin.deiconify()
                    
            else:
                messagebox.showerror('Error','Şifrenizi yanlış girdiniz !')
        
        def geri():
            windowSifreDegistir.destroy()
            windowLogin.deiconify() 
            
        onaylaButon=tk.Button(windowSifreDegistir,text='Onayla',font=('Bahnschrift',13),width=32,border=2,command=onayla,bg='#57a1f8',fg='black',cursor='hand2',activebackground='lightblue')
        onaylaButon.place(x=48,y=240)
        
        geriButon=tk.Button(windowSifreDegistir,text='Geri Dön',font=('Bahnschrift',13),width=12,border=0,command=geri,bg='#DFDFDF',fg='black',cursor='hand2',activebackground='#DFDFDF')
        geriButon.place(x=251,y=320)
        
        def on_enter_onaylaButon(event):
            onaylaButon.config(bg='lightblue', fg='black')

        def on_leave_onaylaButon(event):
            onaylaButon.config(bg='#57a1f8', fg='black')

        onaylaButon.bind('<Enter>', on_enter_onaylaButon)
        onaylaButon.bind('<Leave>', on_leave_onaylaButon)
        
        #geriButon Hover
        def on_enter_geriButon(event):
            geriButon.config(fg='#4747E9')

        def on_leave_geriButon(event):
            geriButon.config(fg='black')

        geriButon.bind('<Enter>', on_enter_geriButon)
        geriButon.bind('<Leave>', on_leave_geriButon)

    sifreDegistirButon=tk.Button(text='Şifre Değiştir',font=('Bahnschrift',13),width=12,border=0,bg='#DFDFDF', fg='black',cursor='hand2',activebackground='#DFDFDF',command=sifreDegistir)
    sifreDegistirButon.place(x=237,y=298)

    #girisButon Hover
    def on_enter_girisButon(event):
        girisButon.config(bg='lightblue', fg='black')

    def on_leave_girisButon(event):
        girisButon.config(bg='#57a1f8', fg='black')

    girisButon.bind('<Enter>', on_enter_girisButon)
    girisButon.bind('<Leave>', on_leave_girisButon)

    #sifreDegistirButon Hover
    def on_enter_sifreDegistirButon(event):
        sifreDegistirButon.config(fg='#4747E9')

    def on_leave_sifreDegistirButon(event):
        sifreDegistirButon.config(fg='black')

    sifreDegistirButon.bind('<Enter>', on_enter_sifreDegistirButon)
    sifreDegistirButon.bind('<Leave>', on_leave_sifreDegistirButon)

    windowLogin.mainloop()
    
LoginWindow()
con.close()
