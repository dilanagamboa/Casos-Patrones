from abc import ABC, abstractmethod
import random

class EstrategiaAtaque(ABC):
    @abstractmethod
    def generar_combo(self, jugador):
        pass


class EstrategiaArteSeleccionada(EstrategiaAtaque):
    def generar_combo(self, jugador):
        if not jugador.arte_seleccionada:
            return []
        
        num_golpes = random.randint(3, 6)
        golpes_disponibles = jugador.arte_seleccionada.obtener_golpes()
        
        combo = random.choices(golpes_disponibles, k=num_golpes)
        
        jugador.artes_usadas_combo = [jugador.arte_seleccionada]
        
        return combo


class EstrategiaArtesAleatorias(EstrategiaAtaque):
    
    def generar_combo(self, jugador):
        num_golpes = random.randint(3, 6)
        combo = []
        artes_usadas = []
        
        for _ in range(num_golpes):
            arte_seleccionada = random.choice(jugador.artes_marciales)
            
            golpes_disponibles = arte_seleccionada.obtener_golpes()
            golpe = random.choice(golpes_disponibles)
            
            combo.append(golpe)
            
            if arte_seleccionada not in artes_usadas:
                artes_usadas.append(arte_seleccionada)
        
        jugador.artes_usadas_combo = artes_usadas
        
        return combo