from posixpath import sep
import tkinter as tk
from tkinter import messagebox, ttk
from Sandwiches.Model.sandwich import SandwichSize
from Sandwiches.Controller.order_controller import OrderController
from Sandwiches.Model.ingredients import Ingredients

class SandwichApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("760x560")
        self.title("Sandwich Builder")
        self.controller = OrderController()

        # listas desde el enum
        self.proteins = [p for p in Ingredients if p.tipo() == "Proteina"]
        self.extras = [e for e in Ingredients if e.tipo() == "Extra"]

        # ventanas (Toplevels) se crearán según flujo
        self.show_welcome()

    # ---- Ventana 1: Bienvenida ----
    def show_welcome(self):
        self.clear_root()
        frm = ttk.Frame(self, padding=20)
        frm.pack(fill="both", expand=True)

        lbl = ttk.Label(frm, text="Bienvenido a Sandwich Builder", font=("Arial", 18))
        lbl.pack(pady=(10,20))

        start_btn = ttk.Button(frm, text="Empezar armado", command=self.show_size_and_proteins)
        start_btn.pack(ipadx=10, ipady=5)

    # ---- Ventana 2: Selección de tamaño y proteína ----
    def show_size_and_proteins(self):
        self.clear_root()
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill="both", expand=True)

        ttk.Label(frm, text="Elige el tamaño:", font=("Arial", 12)).pack(anchor="w")
        size_var = tk.StringVar(value=SandwichSize.SMALL.value)
        sizes_frame = ttk.Frame(frm)
        sizes_frame.pack(anchor="w", pady=(0,10))
        ttk.Radiobutton(sizes_frame, text="15 cm (small)", variable=size_var, value=SandwichSize.SMALL.value).pack(side="left", padx=5)
        ttk.Radiobutton(sizes_frame, text="30 cm (big)", variable=size_var, value=SandwichSize.BIG.value).pack(side="left", padx=5)

        ttk.Label(frm, text="Selecciona 1 proteína:", font=("Arial", 12)).pack(anchor="w", pady=(8,4))

        # checkboxes de proteínas (permitimos seleccionar varias en la UI, pero validamos EXACTAMENTE 1 antes de avanzar)
        self.protein_vars = {}
        proteins_frame = ttk.Frame(frm)
        proteins_frame.pack(fill="both", expand=True)

        for p in self.proteins:
            row = ttk.Frame(proteins_frame)
            row.pack(fill="x", pady=4)
            var = tk.IntVar(value=0)
            chk = ttk.Checkbutton(row, text=p.nombre(), variable=var)
            chk.pack(side="left")
            price_label = ttk.Label(row, text=f"{p.precio(SandwichSize.SMALL):.2f}/{p.precio(SandwichSize.BIG):.2f} (S/B)")
            price_label.pack(side="left", padx=6)
            self.protein_vars[p] = var

        btns = ttk.Frame(frm)
        btns.pack(fill="x", pady=12)
        back = ttk.Button(btns, text="Volver", command=self.show_welcome)
        back.pack(side="left")
        next_btn = ttk.Button(btns, text="Seguir al armado", command=lambda: self._validate_protein_and_continue(size_var.get()))
        next_btn.pack(side="right")

    def _validate_protein_and_continue(self, size_value:str):
        # validar EXACTAMENTE 1 proteína seleccionada
        selected = [p for p, var in self.protein_vars.items() if var.get() == 1]
        if len(selected) != 1:
            messagebox.showerror("Selección inválida", "Debe seleccionar exactamente 1 proteína para el sandwich.")
            return
        # iniciar builder en controller con el tamaño elegido
        size = SandwichSize.SMALL if size_value == SandwichSize.SMALL.value else SandwichSize.BIG
        builder = self.controller.start_new(size)
        # añadir la proteína seleccionada
        protein = selected[0]
        builder.add(protein, 1)
        # pasar a la ventana de armado con builder ya con la proteína
        self.show_assembly()

    # ---- Ventana 3: Armado con adicionales ----
    def show_assembly(self):
        self.clear_root()
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill="both", expand=True)

        ttk.Label(frm, text="Armado del sandwich", font=("Arial", 14)).pack(anchor="w", pady=(0,8))

        # Mostrar resumen actual (proteína + tamaño)
        self.summary_var = tk.StringVar()
        self._update_summary()
        ttk.Label(frm, textvariable=self.summary_var, relief="ridge", padding=8).pack(fill="x", pady=(0,8))

        # Lista de extras con botones + y -
        extras_frame = ttk.Frame(frm)
        extras_frame.pack(fill="both", expand=True)
        self.extra_qty_vars = {}  # map ingredient -> IntVar

        for e in self.extras:
            row = ttk.Frame(extras_frame, padding=4)
            row.pack(fill="x", pady=2)
            lbl_name = ttk.Label(row, text=f"{e.nombre()} ({e.precio(self.controller.builder.base.size()):.2f})")
            lbl_name.pack(side="left", padx=6)

            minus = ttk.Button(row, text="-", width=3, command=lambda ing=e: self._change_extra(ing, -1))
            minus.pack(side="right", padx=2)
            qty_var = tk.IntVar(value=0)
            qty_lbl = ttk.Label(row, textvariable=qty_var, width=3, anchor="center", relief="sunken")
            qty_lbl.pack(side="right", padx=2)
            plus = ttk.Button(row, text="+", width=3, command=lambda ing=e: self._change_extra(ing, +1))
            plus.pack(side="right", padx=2)

            self.extra_qty_vars[e] = qty_var

        # botones abajo: Finalizar pedido y Seguir el pedido
        bottom = ttk.Frame(frm, padding=(0,8))
        bottom.pack(fill="x", pady=12)
        finish = ttk.Button(bottom, text="Finalizar pedido (mostrar factura)", command=self._on_finalize)
        finish.pack(side="right", padx=6)
        seguir = ttk.Button(bottom, text="Seguir pidiendo (agregar sandwich)", command=self._on_follow_order)
        seguir.pack(side="right", padx=6)
        back = ttk.Button(bottom, text="Volver selección proteína", command=self.show_size_and_proteins)
        back.pack(side="left")

    def _change_extra(self, ingredient: Ingredients, delta: int):
        # actualizar builder y var
        if not self.controller.builder:
            return
        v = self.extra_qty_vars[ingredient]
        new = max(0, v.get() + delta)
        prev = v.get()
        if new > prev:
            self.controller.add_ingredient(ingredient, new - prev)
        elif new < prev:
            self.controller.remove_ingredient(ingredient, prev - new)
        v.set(new)
        self._update_summary()

    def _update_summary(self):
        b = self.controller.builder
        if not b:
            self.summary_var.set("No hay sandwich en construcción.")
            return
        # construir descripción provisional y precio
        s = b.build()
        desc = s.description()
        price = s.price()
        self.summary_var.set(f"{desc} — Total: ₡{price:.2f}")

    # ---- acciones de botones: finalizar / seguir ----
    def _on_finalize(self):
        # finalizar agrega el sandwich a orders y abre la factura
        sand = self.controller.finalize_current()
        if not sand:
            messagebox.showwarning("Nada para finalizar", "No hay sandwich para finalizar.")
            return
        self.show_invoice()

    def _on_follow_order(self):
        # agregar el sandwich actual a pedidos y volver a selección para añadir otro sandwich
        sand = self.controller.finalize_current()
        if not sand:
            messagebox.showwarning("Nada para agregar", "No hay sandwich para agregar al pedido.")
            return
        # reset y volver a selección
        messagebox.showinfo("Añadido", "Sandwich agregado al pedido. Puedes agregar otro.")
        self.show_size_and_proteins()

    # ---- Ventana 4: Factura / resumen de pedidos ----
    def show_invoice(self):
        self.clear_root()
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill="both", expand=True)

        ttk.Label(frm, text="Factura - Pedidos", font=("Arial", 14)).pack(anchor="w", pady=(0,10))

        orders = self.controller.get_orders()

        # Frame superior: área con scroll
        list_frame = ttk.Frame(frm)
        list_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(list_frame)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        inner = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner, anchor="nw")

        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Construcción de sandwiches
        total = 0.0

        for idx, s in enumerate(orders, start=1):
            # Paquetito (se deja que se autoajuste)
            s_frame = ttk.LabelFrame(inner, text=f"Sandwich {idx}", padding=8)
            s_frame.pack(fill="x", pady=10, padx=12)

            # Contenedor interno para control fino del padding
            content = ttk.Frame(s_frame, padding=(10, 8))
            content.pack(fill="both", expand=True)

            # Descripción (solo esto, sin summary de ingredientes)
            desc_text = s.description() if s.description() else "Descripción no disponible"
            desc_lbl = ttk.Label(
                content,
                text=desc_text,
                wraplength=740,   # ajustar si cambias el ancho
                justify="left"
            )
            desc_lbl.pack(anchor="w", fill="x")

            sep = ttk.Separator(content, orient="horizontal")
            sep.pack(fill="x", pady=(6,6))

            # Subtotal alineado a la derecha
            subtotal_lbl = ttk.Label(content, text=f"Subtotal: ₡{s.price():.2f}", font=("Arial", 10, "bold"))
            subtotal_lbl.pack(anchor="e", pady=(12,0))

            # --- GARANTIZAR ALTURA MÍNIMA SIN CORTAR CONTENIDO ---
            content.update_idletasks()
            min_height = 110  # ajusta la altura mínima si quieres más espacio
            req_h = content.winfo_reqheight()
            if req_h < min_height:
                spacer_h = min_height - req_h
                spacer = ttk.Frame(content, height=spacer_h)
                spacer.pack(fill="x")

            total += s.price()

        # Aseguramos que el inner tenga un ancho cómodo
        inner.update_idletasks()
        try:
            inner.config(width=max(inner.winfo_width(), 800))
        except Exception:
            pass






        # Frame inferior (total + botones)
        bottom = ttk.Frame(frm, padding=10)
        bottom.pack(fill="x")

        bottom.columnconfigure(0, weight=1)
        bottom.columnconfigure(1, weight=1)
        bottom.columnconfigure(2, weight=1)

        # TOTAL
        total_lbl = ttk.Label(bottom, text=f"TOTAL: ₡{total:.2f}", font=("Arial", 12, "bold"))
        total_lbl.grid(row=0, column=2, sticky="e", pady=(0,10), padx=6)

        # Botones
        clear_btn = ttk.Button(bottom, text="Limpiar pedido", command=lambda: self._clear_orders())
        clear_btn.grid(row=1, column=0, sticky="w", padx=6)

        continue_btn = ttk.Button(bottom, text="Seguir pidiendo", command=self._continue_from_invoice)
        continue_btn.grid(row=1, column=1)

        exit_btn = ttk.Button(bottom, text="Salir", command=self.quit)
        exit_btn.grid(row=1, column=2, sticky="e", padx=6)



    def _continue_from_invoice(self):
        # volver a la selección para agregar otro sandwich
        self.show_size_and_proteins()

    def _clear_orders(self):
        if messagebox.askyesno("Confirmar", "¿Deseas limpiar todos los pedidos?"):
            self.controller.clear_orders()
            messagebox.showinfo("Limpio", "Pedidos borrados.")
            self.show_welcome()

    # utilitarios
    def clear_root(self):
        for w in self.winfo_children():
            w.destroy()