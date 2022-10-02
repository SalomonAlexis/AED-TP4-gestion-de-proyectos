class Proyecto:
    def __init__(self, nombre_usuario, repositorio, descripcion, fecha_actualizacion, lenguaje, likes, tags, url):
        self.nombre_usuario = nombre_usuario
        self.repositorio = repositorio
        self.descripcion = descripcion
        self.fecha_actualizacion = fecha_actualizacion
        self.lenguaje = lenguaje
        self.likes = likes
        self.tags = tags
        self.url = url

    def __str__(self):

        if self.tags != '':
            mensaje = "{:<30}".format('Usuario: ' + str(self.nombre_usuario))
            mensaje += "{:<75}".format('Repositorio: ' + str(self.repositorio))
            mensaje += "{:<35}".format('Fecha de actualizacion:' + str(self.fecha_actualizacion))
            mensaje += "{:<30}".format('Lenguaje: ' + str(self.lenguaje))
            mensaje += "{:<15}".format('Likes: ' + str(self.likes))
            mensaje += "{:<150}".format('Tags: ' + str(self.tags))
            mensaje += "{:<30}".format('URL: ' + str(self.url))

        else:
            mensaje = "{:<30}".format('Usuario: ' + str(self.nombre_usuario))
            mensaje += "{:<75}".format('Repositorio: ' + str(self.repositorio))
            mensaje += "{:<35}".format('Fecha de actualizacion: ' + str(self.fecha_actualizacion))
            mensaje += "{:<30}".format('Lenguaje: ' + str(self.lenguaje))
            mensaje += "{:<165}".format('Likes: ' + str(self.likes))
            mensaje += "{:<30}".format('URL: ' + str(self.url))

        return mensaje


    def estrella(self):
        if self.likes[-1] == 'k':
            cant = self.likes[:-1]
        else:
            cant = self.likes

        cant = float(cant)

        if cant >= 0 and cant <= 10:
            est = 1
        elif cant >= 10.1 and cant <= 20:
            est = 2
        elif cant >= 20.1 and cant <= 30:
            est = 3
        elif cant >= 30.1 and cant <= 40:
            est = 4
        elif cant > 40:
            est = 5

        return est


class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = int(dia)
        self.mes = int(mes)
        self.año = int(año)

    def __str__(self):
        mensaje = f"{self.año}-{self.mes}-{self.dia}"
        return mensaje

    def set(self, fecha):
        fecha = fecha.split("-")
        self.dia = int(fecha[2])
        self.mes = int(fecha[1])
        self.año = int(fecha[0])


class Popularidad:
    def __init__(self, mes, estrella, cantidad):
        self.mes = mes
        self.estrella = estrella
        self.cantidad = cantidad
