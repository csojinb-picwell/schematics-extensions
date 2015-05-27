from schematics.models import Model


class Model(Model):

    @classmethod
    def get_null_object(cls, overrides=None):
        if overrides is None:
            overrides = {}
        values = {}
        for name, field in cls.fields.items():
            if name not in overrides:
                values[name] = field.null()
        values.update(overrides)
        return cls(values)

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self._data)
