"""
Servicio para cargar y gestionar imágenes
"""
import os
from PIL import Image, ImageTk

class CargadorImagenes:
    def __init__(self):
        self.ruta_fotos = self.encontrar_carpeta_fotos()
        self.imagenes = {}
        self.cargar_imagenes()
    
    def encontrar_carpeta_fotos(self):
        """Busca la carpeta Fotos en diferentes ubicaciones"""
        if os.path.exists("Fotos"):
            return "Fotos"
        elif os.path.exists("../Fotos"):
            return "../Fotos"
        
        for root, dirs, files in os.walk("."):
            if "Fotos" in dirs:
                return os.path.join(root, "Fotos")
        return None
    
    def cargar_imagenes(self):
        """Carga todas las imágenes de las artes marciales"""
        if not self.ruta_fotos:
            print("Advertencia: No se encontró la carpeta 'Fotos'")
            return
        
        nombres_archivos = [
            "aikido.png", "boxeo.png", "capoeira.png", "jiu jitsu.png",
            "judo.png", "karate.png", "kung fu.png", "sumo.png",
            "taekwondo.png", "wing chun.png"
        ]
        
        for nombre in nombres_archivos:
            ruta_completa = os.path.join(self.ruta_fotos, nombre)
            if os.path.exists(ruta_completa):
                try:
                    img = Image.open(ruta_completa)
                    img = img.resize((100, 100), Image.Resampling.LANCZOS)
                    self.imagenes[nombre] = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f"Error cargando {nombre}: {e}")
    
    def obtener_imagen(self, nombre_archivo):
        """Obtiene una imagen por su nombre de archivo"""
        return self.imagenes.get(nombre_archivo, None)