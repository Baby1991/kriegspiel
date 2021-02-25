class Event():
    name = 'ERROR'

    def __str__(self):
        return '{0} {1}'.format(self.name, ' '.join(self.args))
