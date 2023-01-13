class User():

    def __init__(self, id, nombre=None, apellido=None, edad=None) -> None:
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad
        }