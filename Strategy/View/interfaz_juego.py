from tkinter import *
from View.cargador_imagenes import CargadorImagenes

FUENTE_MINECRAFT = ("Minecraftia", 10)
COLOR_FONDO = 'white smoke'
COLOR_JUGADOR1 = 'sea green'
COLOR_JUGADOR2 = 'steel blue'
COLOR_BOTONES_ESPECIALES = 'gainsboro'

class InterfazJuego:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.cargador_img = CargadorImagenes()
        
        self.configurar_ventana()
        self.crear_interfaz()
        self.actualizar_interfaz()
    
    def configurar_ventana(self):
        self.root.title("Juego de Artes Marciales - Strategy Pattern")
        self.root.geometry("1500x700")
        self.root.resizable(False, False)
        self.root.config(bg=COLOR_FONDO)
    
    def crear_boton(self, parent, texto, x, y, width, height=1, command=None, color=None):
        if color is None:
            color = COLOR_BOTONES_ESPECIALES
        
        estilo = {'font': FUENTE_MINECRAFT,'bg': color,'fg': 'black' if color == 'gainsboro' else 'white','borderwidth': 5}
        
        btn = Button(parent, text=texto, width=width, height=height,command=command, **estilo)
        btn.place(x=x, y=y)
        return btn
    
    def crear_interfaz(self):
        self.crear_seccion_jugador1()
        self.crear_seccion_jugador2()
        self.crear_seccion_central()
        self.crear_bitacora()
    
    def crear_seccion_jugador1(self):
        self.label_jugador1 = Label(
            self.root, text="PLAYER 1", font=("Minecraftia", 14),
            bg=COLOR_FONDO, fg=COLOR_JUGADOR1
        )
        self.label_jugador1.place(x=175, y=10)
        
        # botones de artes marciales
        self.btns_artes_j1 = []
        for i in range(3):
            btn = self.crear_boton(
                self.root, "", 65 + i*157, 50, 14, 2,
                lambda idx=i: self.seleccionar_arte_j1(idx),
                color=COLOR_JUGADOR1
            )
            self.btns_artes_j1.append(btn)
        
        # labels de golpes
        self.labels_golpes_j1 = []
        for i in range(3):
            y_base = 110
            labels = []
            for j in range(3):
                lbl = Label(
                    self.root, text="", font=("Minecraftia", 8),
                    bg=COLOR_FONDO, anchor='w', width=18
                )
                lbl.place(x=65 + i*157, y=y_base + j*20)
                labels.append(lbl)
            self.labels_golpes_j1.append(labels)
        
        Label(self.root, text="Arte Marcial",
              font=FUENTE_MINECRAFT, bg=COLOR_FONDO).place(x=145, y=210)
        Label(self.root, text="Seleccionada:",
              font=FUENTE_MINECRAFT, bg=COLOR_FONDO).place(x=145, y=250)
        
        self.label_imagen_j1 = Label(
            self.root, bg='white', relief=SOLID, borderwidth=2
        )
        self.label_imagen_j1.place(x=305, y=190, width=110, height=110)
        
        Label(self.root, text="Combo:",
              font=FUENTE_MINECRAFT, bg=COLOR_FONDO).place(x=145, y=320)
        self.label_combo_j1 = Label(
            self.root, text="", font=("Minecraftia", 8),
            bg=COLOR_FONDO, wraplength=250, justify=LEFT, anchor='w'
        )
        self.label_combo_j1.place(x=200, y=320, width=260, height=40)
        
        self.crear_boton(
            self.root, "Generar Combo", 105, 370, 18, 2,
            self.generar_combo_j1, color=COLOR_JUGADOR1
        )
        self.crear_boton(
            self.root, "Atacar", 305, 370, 18, 2,
            self.atacar_j1, color=COLOR_JUGADOR1
        )
        self.crear_boton(
            self.root, "Asignar", 205, 450, 18, 2,
            lambda: self.reasignar_artes(1), color=COLOR_JUGADOR1
        )
    
    def crear_seccion_jugador2(self):
        self.label_jugador2 = Label(
            self.root, text="PLAYER 2", font=("Minecraftia", 14),
            bg=COLOR_FONDO, fg=COLOR_JUGADOR2
        )
        self.label_jugador2.place(x=1055, y=10)
        
        # botones de artes marciales (solo informativos)
        self.btns_artes_j2 = []
        for i in range(3):
            btn = self.crear_boton(
                self.root, "", 950 + i*157, 50, 14, 2,
                lambda idx=i: self.mostrar_info_arte_j2(idx),
                color=COLOR_JUGADOR2
            )
            self.btns_artes_j2.append(btn)
        
        # labels de golpes
        self.labels_golpes_j2 = []
        for i in range(3):
            y_base = 110
            labels = []
            for j in range(3):
                lbl = Label(
                    self.root, text="", font=("Minecraftia", 8),
                    bg=COLOR_FONDO, anchor='w', width=18
                )
                lbl.place(x=950 + i*157, y=y_base + j*20)
                labels.append(lbl)
            self.labels_golpes_j2.append(labels)
        
        Label(self.root, text="Artes Usadas en Combo:",
            font=FUENTE_MINECRAFT, bg=COLOR_FONDO).place(x=1045, y=175)
        
        # crear 3 cuadritos para imágenes del j2
        self.labels_imagenes_j2 = []
        for i in range(3):
            lbl = Label(
                self.root, bg='white', relief=SOLID, borderwidth=2
            )
            lbl.place(x=1015 + i*120, y=200, width=110, height=110)
            self.labels_imagenes_j2.append(lbl)
        
        Label(self.root, text="Combo:",
            font=FUENTE_MINECRAFT, bg=COLOR_FONDO).place(x=1040, y=320)
        self.label_combo_j2 = Label(
            self.root, text="", font=("Minecraftia", 8),
            bg=COLOR_FONDO, wraplength=250, justify=LEFT, anchor='w'
        )
        self.label_combo_j2.place(x=1100, y=320, width=260, height=40)
        
        self.crear_boton(
            self.root, "Generar Combo", 990, 370, 18, 2,
            self.generar_combo_j2, color=COLOR_JUGADOR2
        )
        self.crear_boton(
            self.root, "Atacar", 1190, 370, 18, 2,
            self.atacar_j2, color=COLOR_JUGADOR2
        )
        self.crear_boton(
            self.root, "Asignar", 1090, 450, 18, 2,
            lambda: self.reasignar_artes(2), color=COLOR_JUGADOR2
        )
    
    def actualizar_imagenes_j2(self):
        for lbl in self.labels_imagenes_j2:
            lbl.config(image='', text='', bg='white')
        
        # obtener las artes usadas en el combo actual del jugador
        artes_usadas = getattr(self.controller.jugador2, 'artes_usadas_combo', [])
        
        # mostrar las imágenes en posiciones fijas
        for i, arte in enumerate(artes_usadas[:3]):
            lbl = self.labels_imagenes_j2[i]
            
            nombre_img = arte.nombre_imagen
            img = self.cargador_img.obtener_imagen(nombre_img)
            if img:
                lbl.config(image=img, text='', bg='white')
                lbl.image = img
            else:
                lbl.config(
                    image='',
                    text=arte.nombre,
                    bg='light gray',
                    font=("Minecraftia", 8),
                    wraplength=100
                )
            
    def crear_seccion_central(self):
        self.crear_boton(
            self.root, "ATACARSE\nMUTUAMENTE", 650, 210, 15, 3,
            self.atacarse_mutuo, color=COLOR_BOTONES_ESPECIALES
        )
        self.crear_boton(
            self.root, "REINICIAR\nJUEGO", 650, 310, 15, 3,
            self.reiniciar_juego, color=COLOR_BOTONES_ESPECIALES
        )
        
        self.label_ganador = Label(
            self.root, text="", font=("Minecraftia", 14),
            bg=COLOR_FONDO, fg='red'
        )
        self.label_ganador.place(x=610, y=410)
    
    def crear_bitacora(self):
        Label(
            self.root, text="BITÁCORA DE COMBATE",
            font=("Minecraftia", 12), bg=COLOR_FONDO, fg='navy'
        ).place(x=650, y=520)
        
        frame_bitacora = Frame(
            self.root, bg='white', relief=SOLID, borderwidth=2
        )
        frame_bitacora.place(x=100, y=550, width=1300, height=140)
        
        self.text_bitacora = Text(
            frame_bitacora, font=("Minecraftia", 8), wrap=WORD
        )
        self.text_bitacora.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = Scrollbar(frame_bitacora, command=self.text_bitacora.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text_bitacora.config(yscrollcommand=scrollbar.set)
    
    def seleccionar_arte_j1(self, indice):
        self.controller.jugador1.seleccionar_arte(indice)
        self.actualizar_imagen_j1()
        arte_nombre = self.controller.jugador1.arte_seleccionada.nombre
        self.agregar_bitacora(f"J1 seleccionó {arte_nombre}")
    
    def mostrar_info_arte_j2(self, indice):
        arte = self.controller.jugador2.artes_marciales[indice]
        self.agregar_bitacora(f"J2 tiene disponible: {arte.nombre}")
    
    def generar_combo_j1(self):
        combo = self.controller.jugador1.generar_combo()
        if combo:
            nombres = ", ".join([g.nombre for g in combo])
            self.label_combo_j1.config(text=nombres)
            arte = self.controller.jugador1.arte_seleccionada.nombre
            self.agregar_bitacora(f"J1 generó combo de {arte}: {nombres}")
        else:
            self.label_combo_j1.config(text="Sin arte seleccionada")
            self.agregar_bitacora("J1 debe seleccionar un arte marcial primero")
    
    def generar_combo_j2(self):
        combo = self.controller.jugador2.generar_combo()
        if combo:
            nombres = ", ".join([g.nombre for g in combo])
            self.label_combo_j2.config(text=nombres)
            self.actualizar_imagenes_j2()
            
            # mostrar las artes usadas
            artes_usadas = [arte.nombre for arte in self.controller.jugador2.artes_usadas_combo]
            self.agregar_bitacora(f"J2 generó combo usando: {', '.join(artes_usadas)}")
    
    def atacar_j1(self):
        exito = self.controller.ejecutar_ataque(
            self.controller.jugador1,
            self.controller.jugador2
        )
        
        if exito:
            self.label_combo_j1.config(text="")
        
        self.actualizar_interfaz()
        self.verificar_fin_juego()
    
    def atacar_j2(self):
        exito = self.controller.ejecutar_ataque(
            self.controller.jugador2,
            self.controller.jugador1
        )
        
        if exito:
            self.label_combo_j2.config(text="")
            # limpiar imágenes después del ataque
            for lbl in self.labels_imagenes_j2:
                lbl.config(image='', text='', bg='white')
        
        self.actualizar_interfaz()
        self.verificar_fin_juego()
    
    def atacarse_mutuo(self):
        self.atacar_j1()
        if not self.controller.verificar_ganador():
            self.atacar_j2()
        
    def reasignar_artes(self, jugador):
        if jugador == 1:
            self.controller.jugador1.reasignar_artes(
                self.controller.artes_disponibles
            )
            self.label_imagen_j1.config(image='', text='')
            self.label_combo_j1.config(text='')
            self.agregar_bitacora("J1 reasignó sus artes marciales")
        else:
            self.controller.jugador2.reasignar_artes(
                self.controller.artes_disponibles
            )
            self.label_combo_j2.config(text='')
            # limpiar imágenes del j2
            for lbl in self.labels_imagenes_j2:
                lbl.config(image='', text='', bg='white')
            self.agregar_bitacora("J2 reasignó sus artes marciales")
    
        self.actualizar_interfaz()

    def reiniciar_juego(self):
        self.controller.reiniciar()
        self.label_imagen_j1.config(image='', text='')
        self.label_combo_j1.config(text='')
        self.label_combo_j2.config(text='')
        self.label_ganador.config(text='')
    
        for lbl in self.labels_imagenes_j2:
            lbl.config(image='', text='', bg='white')
        
        self.actualizar_interfaz()
        self.agregar_bitacora("=== JUEGO REINICIADO ===")


    def actualizar_imagen_j1(self):
        if self.controller.jugador1.arte_seleccionada:
            nombre_img = self.controller.jugador1.arte_seleccionada.nombre_imagen
            img = self.cargador_img.obtener_imagen(nombre_img)
            if img:
                self.label_imagen_j1.config(image=img, text='')
                self.label_imagen_j1.image = img
            else:
                self.label_imagen_j1.config(
                    image='',
                    text=self.controller.jugador1.arte_seleccionada.nombre
                )

    def actualizar_interfaz(self):
        # actualizar j1
        for i, arte in enumerate(self.controller.jugador1.artes_marciales):
            self.btns_artes_j1[i].config(text=arte.nombre)
            golpes = arte.obtener_golpes()
            for j, golpe in enumerate(golpes):
                texto = f"{golpe.nombre}: {golpe.poder}"
                if golpe.vida_propia > 0:
                    texto += f" (+{golpe.vida_propia})"
                if golpe.vida_enemigo_extra > 0:
                    texto += f" (+{golpe.vida_enemigo_extra} extra)"
                self.labels_golpes_j1[i][j].config(text=texto)
        
        # actualizar j2
        for i, arte in enumerate(self.controller.jugador2.artes_marciales):
            self.btns_artes_j2[i].config(text=arte.nombre)
            golpes = arte.obtener_golpes()
            for j, golpe in enumerate(golpes):
                texto = f"{golpe.nombre}: {golpe.poder}"
                if golpe.vida_propia > 0:
                    texto += f" (+{golpe.vida_propia})"
                if golpe.vida_enemigo_extra > 0:
                    texto += f" (+{golpe.vida_enemigo_extra} extra)"
                self.labels_golpes_j2[i][j].config(text=texto)
        
        self.label_jugador1.config(
            text=f"PLAYER 1 - {self.controller.jugador1.vida}/200 HP"
        )
        self.label_jugador2.config(
            text=f"PLAYER 2 - {self.controller.jugador2.vida}/200 HP"
        )
        
        # actualizar bitácora
        self.text_bitacora.delete(1.0, END)
        for entrada in self.controller.bitacora:
            self.text_bitacora.insert(END, entrada + "\n")
        self.text_bitacora.see(END)

    def agregar_bitacora(self, mensaje):
        self.controller.bitacora.append(mensaje)
        self.actualizar_interfaz()

    def verificar_fin_juego(self):
        ganador = self.controller.verificar_ganador()
        if ganador:
            self.agregar_bitacora(f"\n{'='*50}")
            self.agregar_bitacora(f"¡¡¡ {ganador} GANA LA BATALLA !!!")
            self.agregar_bitacora(f"{'='*50}")
            self.label_ganador.config(text=f"★ GANADOR: {ganador} ★")