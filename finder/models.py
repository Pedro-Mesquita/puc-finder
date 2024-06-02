from django.db import models

# Create your models here.

class Disciplina(models.Model):
    nomedisc = models.CharField(_(""), max_length=7)
    qtt_provas = models.PositiveSmallIntegerField(_(""))
    qtt_listas = models.PositiveSmallIntegerField(_(""))

class Exercicios(models.Model):
    nomearq = models.CharField(_(""), max_length=7)
    arq = models.BinaryField(_(""))
    data_submit = models.DateField(_(""), auto_now_add=True)
    aprovado = models.BooleanField(_(""))
    data_aprov = models.DateField(_(""))

