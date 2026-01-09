from django.db import models

class Config(models.Model):
    """
    Modelo para configurações globais do sistema
    """

    preco = models.FloatField(null=False, blank=False)
    desconto = models.PositiveIntegerField(null=False, blank=False, default=30)
    vagas = models.PositiveIntegerField(null=False, blank=False)

    @classmethod
    def get_instance(cls):
        if not cls.objects.first():
            cls.objects.create(preco=10.00, vagas=50, desconto=30)
        return cls.objects.first()
    
    def __str__(self):
        return 'Configurações do Sistema'
