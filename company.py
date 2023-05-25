import tkinter
class abc():
    def __init__(self):
        self.pencerem=tkinter.Tk()
        self.myset=set()
        dosyam=open("dow.txt","r")
        for line in dosyam:
            line=line.rstrip()
            line=line.split(",")
            self.myset.add(line[0])
        self.listem=list(self.myset)
        self.listem.sort()
        self.liste_tutucu=tkinter.StringVar()
        self.liste_tutucu.set(tuple(self.listem))
        self.yöncubugu=tkinter.Scrollbar(self.pencerem,orient=tkinter.VERTICAL)
        self.yöncubugu.grid(row=0,column=1,rowspan=7,sticky="ns")
        self.listekutum=tkinter.Listbox(self.pencerem,listvariable=self.liste_tutucu,yscrollcommand=self.yöncubugu.set)
        self.listekutum.bind("<<ListboxSelect>>",self.doldur)
        self.yöncubugu.config(command=self.listekutum.yview)
        self.listekutum.grid(row=0,column=0,rowspan=7)
        
        self.etiket_şirket=tkinter.Label(self.pencerem,text="ŞİRKET").grid(row=0,column=2,sticky="s")
        self.şirket_tutucu=tkinter.StringVar()
        self.giriş_şirket=tkinter.Entry(self.pencerem,textvariable=self.şirket_tutucu,state="readonly").grid(row=1,column=2)
        self.etiket_sektör=tkinter.Label(self.pencerem,text="SEKTÖR").grid(row=2,column=2)
        self.sektör_tutucu=tkinter.StringVar()
        self.giriş_sektör=tkinter.Entry(self.pencerem,state="readonly",textvariable=self.sektör_tutucu).grid(row=3,column=2)
        self.etiket_borsa=tkinter.Label(self.pencerem,text="BORSA").grid(row=4,column=3)
        self.borsa_tutucu=tkinter.StringVar()
        self.giriş_borsa=tkinter.Entry(self.pencerem,state="readonly",textvariable=self.borsa_tutucu).grid(row=4,column=4)
        self.etiket_getiri=tkinter.Label(self.pencerem,text="YILLIK GETİRİ").grid(row=5,column=3)
        self.getiri_tutucu=tkinter.StringVar()
        self.giriş_getiri=tkinter.Entry(self.pencerem,textvariable=self.getiri_tutucu,state="readonly").grid(row=5,column=4)
        self.etiket_hiz=tkinter.Label(self.pencerem,text="DEĞİŞİM HIZI").grid(row=6,column=3)
        self.hiz_tutucu=tkinter.StringVar()
        self.giriş_hiz=tkinter.Entry(self.pencerem,textvariable=self.hiz_tutucu,state="readonly").grid(row=6,column=4)
        tkinter.mainloop()
    def doldur(self,event):
        index=self.listekutum.get(self.listekutum.curselection())
        dosyam=open("dow.txt","r")
        for line in dosyam:
            line=line.rstrip()
            line=line.split(",")
            if line[0]==index:
                self.şirket_tutucu.set(line[0])
                self.sektör_tutucu.set(line[1])
                self.borsa_tutucu.set(line[2])
                self.getiri_tutucu.set(line[3])
                self.hiz_tutucu.set(line[4])
        dosyam.close()        
abc()

            




     

    
