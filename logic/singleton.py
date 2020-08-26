class Singleton():

    _instance = None
    _valueScores = []
    _valueNames = []

    @classmethod
    def get_instance(cls):  # Constructor alternativo que retorna una nueva instancia
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def get_valueScore(self):
        return self._valueScores

    def set_valueScore(self, v):
        self._valueScores = v

    def get_valueNames(self):
        return self._valueNames

    def set_valueNames(self, v):
        self._valueNames = v
