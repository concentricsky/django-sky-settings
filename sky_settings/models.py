from django.db import models


_base_model = models.Model

try:
    import basic_models
    class _basic_setting_model(basic_models.TimestampedModel, basic_models.UserModel):
        pass
    _base_model = _basic_setting_model
except ImportError as e:
    pass


class Setting(_base_model):
    """
    Setting.cached.get(name='mapbox_api_key')


    Setting.get_value('mapbox_api_key')
    Setting.set_value()
    """
    TYPE_STRING = 's'
    TYPE_BOOLEAN = 'b'
    TYPE_NUMBER = 'n'
    TYPE_CHOICES = (
        (TYPE_STRING, 'String'),
        (TYPE_BOOLEAN, 'Boolean'),
        (TYPE_NUMBER, 'Number'),
    )
    setting_type = models.CharField(max_length=16, choices=TYPE_CHOICES, default=TYPE_STRING)
    name = models.CharField(max_length=1024)
    value = models.TextField()
    description = models.TextField()

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def cast(self):
        if self.setting_type == 's':
            return self.value
        if self.setting_type == 'b':
            return bool(int(self.value))
        if self.setting_type == 'n':
            return float(self.value)

    @classmethod
    def get_value(cls, name, default=None):
        try:
            mngr = getattr(cls, 'cached', cls.objects)
            setting = mngr.get(name=name)
        except Setting.DoesNotExist as e:
            return default
        return setting.cast()

    @classmethod
    def set_value(cls, name, value):
        mngr = getattr(cls, 'cached', cls.objects)
        setting = mngr.get_or_create(name=name)
        setting.value = str(value)
        setting.save()
        return value
