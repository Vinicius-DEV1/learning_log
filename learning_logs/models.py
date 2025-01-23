from django.db import models

# Create your models here.
class Topic(models.Model):
    """um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def ___str___(self):
        """devolve uma representação em string do modelo"""
        return self.text