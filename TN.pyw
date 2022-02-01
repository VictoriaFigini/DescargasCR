import tkinter as tk
from tkinter import *
from tkinter import ttk, StringVar, filedialog
from tkinter.ttk import Style
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import descargar




class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        #Hacer la ventana responsiva
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, pad=10,  weight=1)
            self.rowconfigure(index=index, pad=10, weight=1)

        # self.labelframe1=ttk.LabelFrame(self.ventana1, text="Generador de Actuaciones")
        # self.labelframe1.grid(column=0, row=0, padx=10, pady=10)

        #Control de Variables
        self.textdefoult=StringVar(value='C:\\')
        self.sel=StringVar(value='')
        self.sel2=StringVar(value='')


        self.agregar_componentes()
        #self.ventana1.mainloop()

    def agregar_componentes(self):

        # Panedwindow general
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=0, padx=(25,5), pady=(5, 5), sticky="nsew", rowspan=3)

        # Notebook, Frame para las pestañas
        self.panel = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.panel, weight=3)


        # Notebook, panel notebok #2
        self.notebook = ttk.Notebook(self.panel)
        self.notebook.pack(fill="both", expand=True)

        # Tab #1
        self.tab_1 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_1.columnconfigure(index=index, weight=1)
            self.tab_1.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_1, text="Pagos")

        # Tab #2
        self.tab_2 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_2.columnconfigure(index=index, weight=1)
            self.tab_2.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_2, text="Asignaciones")
        
        
        #Contenido Tab_1
        self.label=ttk.Label(self.tab_1, text="Ruta de destino:")
        self.label.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.entry=ttk.Entry(self.tab_1, textvariable=self.textdefoult, width=30)
        self.entry.grid(column=1, row=1, padx=5, pady=5)
        self.boton=ttk.Button(self.tab_1, text="Abrir", command=self.archivo_destino)
        self.boton.grid(column=2, row=1, padx=(5,35), pady=5, sticky="we")
        self.label2=ttk.Label(self.tab_1, text="Seleccionar tipo de Descarga:")
        self.label2.grid(column=0, row=2, padx=(35, 5), pady=5, sticky="e")  
        self.combo=ttk.Combobox(self.tab_1, width=27)
        self.combo.grid(column=1, row=2, padx=5, pady=5)
        self.combo["values"]=["Asignaciones", "Stock", "Pagos"]
        self.label3=ttk.Label(self.tab_1, text="Fecha Desde:")
        self.label3.grid(column=0, row=3, padx=5, pady=5, sticky="e")
        self.entry1=DateEntry(self.tab_1, selectmode="day", date_pattern='dd/mm/Y', textvariable=self.sel)
        self.entry1.grid(column=1, row=3, padx=5, pady=5)
        self.label4=ttk.Label(self.tab_1, text="Fecha Hasta:")
        self.label4.grid(column=0, row=4, padx=5, pady=5, sticky="e")
        self.entry2=DateEntry(self.tab_1, selectmode="day", date_pattern='dd/mm/Y', textvariable=self.sel2)
        self.entry2.grid(column=1, row=4, padx=5, pady=5)
        self.boton1=ttk.Button(self.tab_1, text="Descargar", style="Accent.TButton", command=self.descargar)
        self.boton1.grid(column=1, row=6, padx=5, pady=(15,35), sticky="we")

        #Contenido Tab_2
        # self.label1=ttk.Label(self.tab_2, text="Seleccionar Archivo:")
        # self.label1.grid(column=0, row=0, padx=5, pady=(50,5), sticky="e")
        # self.entry1=ttk.Entry(self.tab_2, width=30)
        # self.entry1.grid(column=1, row=0, padx=0, pady=(50,5))
        # self.boton2=ttk.Button(self.tab_2, text="Buscar", command=self.archivo_ubicacion)
        # self.boton2.grid(column=2, row=0, padx=(5,40), pady=(50,5), sticky="ew")
        # self.label3=ttk.Label(self.tab_2, text="Tipo de acción:")
        # self.label3.grid(column=0, row=1, padx=5, pady=5, sticky="e")  
        # self.combo=ttk.Combobox(self.tab_2, width=27)
        # self.combo.grid(column=1, row=1, padx=0, pady=5)
        # self.combo["values"]=["Abrir procesos", "Verificar procesos abiertos", "Cerrar Procesos"]
        # self.label2=ttk.Label(self.tab_2, text="Comentario/Coment:")
        # self.label2.grid(column=1, row=2, padx=5, pady=(10,5))
        # self.entry2=ttk.Entry(self.tab_2, width=40)
        # self.entry2.grid(column=1, row=3, padx=10, pady=5, ipady=20)
        # self.boton1=ttk.Button(self.tab_2, text="Descargar", style="Accent.TButton", command=self.procesar_procesos)
        # self.boton1.grid(column=1, row=5, padx=5, pady=(30,30), sticky="ew")

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))


    def archivo_destino(self):
        self.dirname=filedialog.askdirectory(initialdir="/", title="Elegir destino")
        #print(self.dirname)
        self.textdefoult=StringVar(value=str(self.dirname))
        self.entry.configure(textvariable=self.textdefoult)
        #return self.filename


    def descargar(self):
        fechadesde= self.sel.get() 
        fechadesde= str(fechadesde)      
        fechahasta= self.sel2.get() 
        fechahasta= str(fechahasta)
        destino= self.entry.get()

        if len(destino) == 0:
            mb.showerror("Error", "Debe ingresar la ruta destino")
        if len(self.combo.get())!="":
            accion=str(self.combo.get())
            if accion == "Asignacion":
                a=descargar.get_pagos(fechadesde, fechahasta, destino)
                mb.showinfo("Archivos generados", str(a))
            elif accion == "Stock":
                a=descargar.get_pagos(fechadesde, fechahasta, destino)
                mb.showinfo("Archivos generados", str(a))
            elif accion == "Pagos":
                a=descargar.get_pagos(fechadesde, fechahasta, destino)
                mb.showinfo("Pagos descargados", str(a))


    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("")

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()
    
#aplicacion1=Aplicacion() 
