import pilasengine

pilas = pilasengine.iniciar()
pilas.fondos.Selva()

try:
  pilas.forzar_habilitacion_de_audio()
except AttributeError:
  print "Omitiendo forzar la inicializacion, version anterior a 1.4.8"

sonido_wav = None
sonido_ogg = None

try:
    sonido_wav = pilas.musica.cargar("rayman.wav")
except:
    print("Imposible leer el archivo .wav")

try:
    sonido_ogg = pilas.musica.cargar("rayman.ogg")
except:
    print("Imposible leer el archivo .ogg")

def reproducir_wav():
    if not sonido_wav:
        print("No se pudo cargar el archivo ogg")
    else:
        print("reproduciendo wav")
        sonido_wav.reproducir()

def reproducir_ogg():
    if not sonido_ogg:
        print("No se pudo cargar el archivo ogg")
    else:
        print("reproduciendo ogg")
        sonido_ogg.reproducir()




pilas.actores.Menu(
        [
            ('reproducir wav', reproducir_wav),
            ('reproducir ogg', reproducir_ogg),
        ])

pilas.ejecutar()
