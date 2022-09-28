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
        mensaje = "{:<30}".format('Usuario: ' + str(self.nombre_usuario))
        mensaje += "{:<30}".format('Repositorio: ' + str(self.repositorio))
        mensaje += "{:<30}".format('Fecha de actualizacion:' + str(self.fecha_actualizacion))
        mensaje += "{:<30}".format('Lenguaje: ' + (self.lenguaje))
        mensaje += "{:<30}".format('Likes: ' + str(self.likes))
        mensaje += "{:<30}".format('Tags: ' + str(self.tags))
        mensaje += "{:<30}".format('URL: ' + str(self.url))

        return mensaje


class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        mensaje = f"{self.año}-{self.mes}-{self.dia}"
        return mensaje

    def año(self):
        return self.año

    def mes(self):
        return self.mes

    def dia(self):
        return self.dia

