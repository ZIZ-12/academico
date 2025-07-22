from django.db import models

class Funcao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nutricionista ou usuário comum")

    def __str__(self):
        return self.nome


class Exercicio(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do exercício")
    descricao = models.CharField(max_length=100, verbose_name="Músculo alvo")
    duracao = models.DurationField(verbose_name="Tempo de duração")  # melhor usar DurationField
    intensidade = models.CharField(max_length=100, verbose_name="Fácil, médio e difícil")
    exemplo = models.CharField(max_length=100, verbose_name="Como executar")

    def __str__(self):
        return self.nome


class Alimento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do alimento")
    preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço do alimento")
    kcal = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quantidade de quilocalorias em 100g")
    carbo = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quantidade de carboidratos em 100g")
    proteina = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quantidade de proteínas em 100g")
    gorduratotais = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quantidade de gorduras totais em 100g")
    gorduratrans = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quantidade de gorduras trans em 100g")
    gordurasaturada = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quantidade de gorduras saturadas em 100g")
    fibra = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quantidade de fibras em 100g")
    sodio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quantidade de sódio em 100g")

    def __str__(self):
        return self.nome


class DiaSemana(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Dia da semana")

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF da pessoa")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(max_length=100, verbose_name="Email da pessoa")
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso da pessoa (kg)")
    altura = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Altura da pessoa (m)", default=1.70)
    imc = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="IMC da pessoa")
    tem_sentado = models.DurationField(verbose_name="Tempo que a pessoa passa sentada ou parada")
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class HorarioDormir(models.Model):
    tempo = models.DurationField(verbose_name="Quantidade de tempo que a pessoa dormiu")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.tempo}"


class Meta(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Qual é sua meta")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


class ExercicioFavorito(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.exercicio.nome}"


class Feedback(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Feedback")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


class Dieta(models.Model):
    quantidade = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quanto de alimento você consumirá")
    horario = models.TimeField(verbose_name="Horário que consumirá")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    dia = models.ForeignKey(DiaSemana, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.dia.nome} - {self.alimento.nome}"


class AvaliacaoFisica(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    niv_sedenta = models.CharField(max_length=100, verbose_name="Nível de sedentarismo")

    def __str__(self):
        return f"{self.pessoa.nome} - {self.niv_sedenta}"
