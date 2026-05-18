# Importamos las herramientas necesarias de Kivy y KivyMD
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

# Aquí definimos el diseño visual usando lenguaje KV
KV = '''
# ScreenManager permite manejar varias pantallas
ScreenManager:
    Pantalla1:
    Pantalla2:

# -------- PRIMERA PANTALLA --------
<Pantalla1>:
    name: "pantalla1"  # Nombre para poder cambiar entre pantallas

    MDBoxLayout:
        orientation: "vertical"  # Elementos en columna
        padding: 20
        spacing: 20

        # Barra superior
        MDTopAppBar:
            title: "Pantalla 1"

        # Campo de texto para escribir el nombre
        MDTextField:
            id: nombre  # ID para acceder al texto desde Python
            hint_text: "Escribe tu nombre"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8

        # Botón para ir a la segunda pantalla
        MDRaisedButton:
            text: "Ir a la siguiente pantalla"
            pos_hint: {"center_x": 0.5}
            on_release:
                # Guardamos el nombre en una variable global de la app
                app.nombre_usuario = nombre.text
                # Cambiamos de pantalla
                app.root.current = "pantalla2"

# -------- SEGUNDA PANTALLA --------
<Pantalla2>:
    name: "pantalla2"

    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        # Barra superior
        MDTopAppBar:
            title: "Pantalla 2"

        # Texto que muestra el nombre ingresado
        MDLabel:
            text: "Hola " + app.nombre_usuario  # Mensaje personalizado
            halign: "center"

        # Botón para regresar a la primera pantalla
        MDRaisedButton:
            text: "Regresar"
            pos_hint: {"center_x": 0.5}
            on_release:
                app.root.current = "pantalla1"
'''

# Clase para la primera pantalla (no necesita lógica adicional)
class Pantalla1(Screen):
    pass

# Clase para la segunda pantalla
class Pantalla2(Screen):
    pass

# Clase principal de la aplicación
class MiApp(MDApp):
    def build(self):
        # Variable donde se guardará el nombre del usuario
        self.nombre_usuario = ""
        # Carga el diseño KV
        return Builder.load_string(KV)

# Ejecuta la aplicación
if __name__ == "__main__":
    MiApp().run()