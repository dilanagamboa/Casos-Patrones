import random

class Jugador:
    def __init__(self, nombre, artes_disponibles, estrategia_ataque):
        self.nombre = nombre
        self.vida = 200
        self.artes_marciales = random.sample(artes_disponibles, 3)
        self.arte_seleccionada = None
        self.estrategia_ataque = estrategia_ataque  # se aplica Pattern
        self.combo_preparado = []
        self.artes_usadas_combo = [] 
    
    def seleccionar_arte(self, indice):
        if 0 <= indice < len(self.artes_marciales):
            self.arte_seleccionada = self.artes_marciales[indice]
    
    def reasignar_artes(self, artes_disponibles):
        self.artes_marciales = random.sample(artes_disponibles, 3)
        self.arte_seleccionada = None
        self.combo_preparado = []
        self.artes_usadas_combo = [] 
    
    def generar_combo(self):
        self.combo_preparado = self.estrategia_ataque.generar_combo(self)
        return self.combo_preparado
    
    def obtener_combo_preparado(self):
        return self.combo_preparado
    
    def limpiar_combo(self):
        self.combo_preparado = []
        self.artes_usadas_combo = [] 
    
    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
    
    def recuperar_vida(self, cantidad):
        self.vida += cantidad
        if self.vida > 200:
            self.vida = 200