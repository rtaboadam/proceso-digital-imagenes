class Filter(object):
    def __call__(self, message): pass

    def __str__(self):
        return "Aplicando el filtro " + self.__class__.__name__

    def check(self, name):
        if not name == str(self.__class__.__name__):
            raise Exception(self.__class__.__name__ + " no valido.")
