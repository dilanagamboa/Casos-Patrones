from Model.artes_marciales import (
    Aikido, Boxeo, Capoeira, JiuJitsu, Judo,
    Karate, KungFu, Sumo, Taekwondo, WingChun
)

class ArteMarcialFactory:
    
    _artes_disponibles = {
        'aikido': Aikido,
        'boxeo': Boxeo,
        'capoeira': Capoeira,
        'jiujitsu': JiuJitsu,
        'judo': Judo,
        'karate': Karate,
        'kungfu': KungFu,
        'sumo': Sumo,
        'taekwondo': Taekwondo,
        'wingchun': WingChun
    }
    
    @staticmethod
    def crear_arte(nombre_arte):
        # crea una instancia de arte marcial por nombre
        nombre_normalizado = nombre_arte.lower().replace('-', '').replace(' ', '')
        
        clase_arte = ArteMarcialFactory._artes_disponibles.get(nombre_normalizado)
        
        if clase_arte:
            return clase_arte()
        else:
            raise ValueError(f"Arte marcial '{nombre_arte}' no existe")
    
    @staticmethod
    def crear_todas_las_artes():
        # crea una lista con todas las artes marciales disponibles
        return [clase() for clase in ArteMarcialFactory._artes_disponibles.values()]
    
    @staticmethod
    def obtener_nombres_disponibles():
        # retorna lista de nombres de artes marciales disponibles
        return list(ArteMarcialFactory._artes_disponibles.keys())