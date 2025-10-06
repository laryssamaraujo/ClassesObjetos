class Calculadora:
    
    def __init__(self):
        pass
    
    def somar(self, a, b):
       return a + b
        
    def subtrair(self, a, b):
       return a - b
   
calc = Calculadora()

resultado_soma = calc.somar (15, 60)
resultado_subtrair = calc.subtrair (50,30)
        
print(f"Resultados da Calculadora")
print(f"A soma de 15 + 60 é: {resultado_soma}")
print(f"A subtração de 50 - 30 é: {resultado_subtrair}")
print(f"Você terá na soma o valor de 75 e na subtração o valor de 20.")
print(f"Obrigada.")