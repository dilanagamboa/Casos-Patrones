from abc import ABC, abstractmethod
import random

class EstrategiaAtaque(ABC):
    @abstractmethod
    def generar_combo(self, jugador):
        pass


class EstrategiaArteSeleccionada(EstrategiaAtaque):    
    def generar_combo(self, jugador):
        if not jugador.arte_seleccionada:
            return []  # no puede generar combo sin arte seleccionada
        num_golpes = random.randint(3, 6)
        return jugador.arte_seleccionada.ejecutar_combo(num_golpes)


class EstrategiaArtesAleatorias(EstrategiaAtaque):
    def generar_combo(self, jugador):
        num_golpes = random.randint(3, 6)
        golpes_combo = []
        artes_usadas = []
        
        for i in range(num_golpes):
            # seleccionar arte aleatoria
            arte_seleccionada = random.choice(jugador.artes_marciales)
            
            # aeleccionar golpe aleatorio
            golpes_disponibles = arte_seleccionada.obtener_golpes()
            golpe = random.choice(golpes_disponibles)
            
            golpes_combo.append(golpe)
            
            if arte_seleccionada not in artes_usadas:
                artes_usadas.append(arte_seleccionada)
        
        jugador.artes_usadas_combo = artes_usadas
        
        return golpes_combo