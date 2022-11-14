from django.db import models

class Tecnogias(models.Model):
  tecnologia = models.CharField(max_length=50)

  def __str__(self):
    return self.tecnologia

class Empresa(models.Model):
  logo = models.ImageField(upload_to="logo_empresa", null=True)
  nome = models.CharField(max_length=30)
  email = models.EmailField()
  cidade = models.CharField(max_length=30)
  endereco = models.CharField(max_length=30)
  caracteristica_empresa = models.TextField()
  choices_nicho_mercado=(
    ("M", "Marketing"),
    ("N", "Nutrição"),
    ("D", "Design")
  )
  nicho_mercado = models.CharField(max_length=3, choices=choices_nicho_mercado)
  tecnologias = models.ManyToManyField(Tecnogias)

  def __str__(self):
    return self.nome