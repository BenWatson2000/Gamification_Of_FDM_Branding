from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'mainFDM'

    # make sure to load the signals file
    def ready(self):
        from mainFDM import signals
