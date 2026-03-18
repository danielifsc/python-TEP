from django.db import models
from module import user 

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    preco = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    qtde = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    itemVenda = model.ManyToManyField(Venda)

    def __str__(self):
        return self.nome


class Venda(models.Model):
 data = models.DateTimeField(auto_now_add=True)
 cliente = models.ForeignKey(User,on_delete = models.CASCADE)
 
def __str__(self):
 return self.data


class Perfil (models.Model):
 telefone = models.CharField(max_length=10, null=True, blank=True)
 endereco = models.CharField(max_length=100, null=True, blank=True)
 numero = models.positedIntegerField(max_length=100, null=True, blank=True)
 bairro = models.charField(max_length=100, null=True, blank=True)
 cidade = models.charField(max_length=100, null=True, blank=True)
 complemento = models.charField(max_length=100, null=True, blank=True)
 cep = models.charField(max_length=100, null=True, blank=True)
 cliente = models.OneToOneField(User, on_delete = models.CASCADE)

 
 def __str__(self):
    return f'Perfil de {self.cliente.username}'

class itemVenda(models.model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtde = models.IntegerField(null=True, blank=True)

def __str__(self):
 return f'{self.produto.nome}'
