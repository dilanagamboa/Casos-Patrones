from Model.artes_marciales import *
from Model.estrategia_ataque import EstrategiaArteSeleccionada, EstrategiaArtesAleatorias
from Model.jugador import Jugador

class JuegoController:
    def __init__(self):
        self.artes_disponibles = [
            Aikido(), Boxeo(), Capoeira(), JiuJitsu(), Judo(),
            Karate(), KungFu(), Sumo(), Taekwondo(), WingChun()
        ]
        self.jugador1 = Jugador(
            "Player 1", 
            self.artes_disponibles, 
            EstrategiaArteSeleccionada()
        )
        self.jugador2 = Jugador(
            "Player 2", 
            self.artes_disponibles, 
            EstrategiaArtesAleatorias()
        )
        
        self.bitacora = []
    
    def ejecutar_ataque(self, atacante, defensor):
        combo = atacante.obtener_combo_preparado()
        
        if not combo:
            mensaje = f"{atacante.nombre} intenta atacar pero no tiene combo preparado"
            self.bitacora.append(mensaje)
            return False
        
        for golpe in combo:
            dano_total = golpe.poder + golpe.vida_enemigo_extra
            defensor.recibir_dano(dano_total)
            
            if golpe.vida_propia > 0:
                atacante.recuperar_vida(golpe.vida_propia)
            
            # Registrar en la bitácora
            mensaje = f"{atacante.nombre} usa {golpe.nombre} (-{dano_total} HP a {defensor.nombre})"
            if golpe.vida_propia > 0:
                mensaje += f" (+{golpe.vida_propia} HP)"
            
            self.bitacora.append(mensaje)
        
        atacante.limpiar_combo()
        return True
    
    def verificar_ganador(self):
        if self.jugador1.vida <= 0:
            return "Player 2"
        elif self.jugador2.vida <= 0:
            return "Player 1"
        return None
    
    def reiniciar(self):
        self.jugador1 = Jugador(
            "Player 1", 
            self.artes_disponibles, 
            EstrategiaArteSeleccionada()
        )
        
        self.jugador2 = Jugador(
            "Player 2", 
            self.artes_disponibles, 
            EstrategiaArtesAleatorias()
        )
        
        self.bitacora = []