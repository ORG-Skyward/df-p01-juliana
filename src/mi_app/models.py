from django.db import models

class HistorialCalculadora(models.Model):
    usuario = models.CharField(max_length=100, default='Anónimo', verbose_name="Nombre de Usuario")
    operacion = models.CharField(max_length=255, verbose_name="Operación Matemática")
    resultado = models.CharField(max_length=100, verbose_name="Resultado")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de Registro")

    class Meta:
        verbose_name = "Historial de Calculadora"
        verbose_name_plural = "Historiales de Calculadora"
        ordering = ['-fecha']  # Muestra primero las operaciones más recientes

    def __str__(self):
        return f"{self.usuario} | {self.operacion} = {self.resultado}"
     