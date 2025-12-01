import random
from Model.arte_marcial import ArteMarcial
from Model.golpe import Golpe

class Aikido(ArteMarcial):
    def __init__(self):
        super().__init__("Aikido", "aikido.png")
        self.golpes = [Golpe("Ikkyo", 10, vida_propia=12), Golpe("Nikyo", 15), Golpe("Sankyo", 20)]
    
    def obtener_golpes(self):
        return self.golpes
    
    def ejecutar_combo(self, num_golpes):
        return random.choices(self.golpes, k=num_golpes)


class Boxeo(ArteMarcial):
    def __init__(self):
        super().__init__("Boxeo", "boxeo.png")
        self.golpes = [Golpe("Jab", 8), Golpe("Gancho", 15), Golpe("Uppercut", 40)]
    
    def obtener_golpes(self):
        return self.golpes
    
    def ejecutar_combo(self, num_golpes):
        return random.choices(self.golpes, k=num_golpes)


class Capoeira(ArteMarcial):
    def __init__(self):
        super().__init__("Capoeira", "capoeira.png")
        self.golpes = [Golpe("Armada", 8), Golpe("Martillo", 28), Golpe("Ponteira", 13)]
    
    def obtener_golpes(self):
        return self.golpes
    
    def ejecutar_combo(self, num_golpes):
        return random.choices(self.golpes, k=num_golpes)


class JiuJitsu(ArteMarcial):
    def __init__(self):
        super().__init__("Jiu-Jitsu", "jiu jitsu.png")
        self.golpes = [Golpe("Armbar", 22), Golpe("Triangle", 28, vida_enemigo_extra=7), Golpe("Rear choke", 30)]
    
    def obtener_golpes(self):
        return self.golpes
    
    def ejecutar_combo(self, num_golpes):
        return random.choices(self.golpes, k=num_golpes)


class Judo(ArteMarcial):
    def __init__(self):
        super().__init__("Judo", "judo.png")
        self.golpes = [Golpe("Tai-Otoshi", 8), Golpe("Koshi-guruma", 8, vida_enemigo_extra=5), Golpe("Osoto-gari", 13)]
    
    def obtener_golpes(self):
        return self.golpes
    
    def ejecutar_combo(self, num_golpes):
        return random.choices(self.golpes, k=num_golpes)


class Karate(ArteMarcial):
    def __init__(self):
        super().__init__("Karate", "karate.png")
        self.golpes = [Golpe("Mae geri", 10), Golpe("Yoko geri", 5, vida_propia=5), Golpe("Mawashi geri", 30)]
    
    def obtener_golpes(self):
        return self.golpes
    
    def ejecutar_combo(self, num_golpes):
        return random.choices(self.golpes, k=num_golpes)


class KungFu(ArteMarcial):
    def __init__(self):
        super().__init__("Kung Fu", "kung fu.png")
        self.golpes = [Golpe("Ch'ien", 10), Golpe("Kuan tau", 11, vida_propia=10), Golpe("Pei tsu", 22)]
    
    def obtener_golpes(self):
        return self.golpes
    
    def ejecutar_combo(self, num_golpes):
        return random.choices(self.golpes, k=num_golpes)


class Sumo(ArteMarcial):
    def __init__(self):
        super().__init__("Sumo", "sumo.png")
        self.golpes = [Golpe("Tsuppari", 18), Golpe("Oshi-dashi", 25, vida_propia=8), Golpe("Yorikiri", 20)]
    
    def obtener_golpes(self):
        return self.golpes
    
    def ejecutar_combo(self, num_golpes):
        return random.choices(self.golpes, k=num_golpes)


class Taekwondo(ArteMarcial):
    def __init__(self):
        super().__init__("Taekwondo", "taekwondo.png")
        self.golpes = [Golpe("Ap chagi", 15), Golpe("Dollyo chagi", 20, vida_propia=8), Golpe("Naeryo chagi", 18)]
    
    def obtener_golpes(self):
        return self.golpes
    
    def ejecutar_combo(self, num_golpes):
        return random.choices(self.golpes, k=num_golpes)


class WingChun(ArteMarcial):
    def __init__(self):
        super().__init__("Wing Chun", "wing chun.png")
        self.golpes = [Golpe("Chain punch", 12), Golpe("Pak sao", 10, vida_propia=7), Golpe("Bong sao", 18)]
    
    def obtener_golpes(self):
        return self.golpes
    
    def ejecutar_combo(self, num_golpes):
        return random.choices(self.golpes, k=num_golpes)