from django.apps import apps
from django.test import TestCase
from webar.apps import WebarConfig

class WebarConfigTest(TestCase):
    def test_apps(self):
        # Verifica que el nombre de la aplicación sea correcto
        self.assertEqual(WebarConfig.name,"webar")

        # Obtén la configuración de la app usando el nombre de la app
        app_config = apps.get_app_config("webar")
        
        # Verifica que el verbose_name sea correcto
        self.assertEqual(app_config.verbose_name, "we-bar")