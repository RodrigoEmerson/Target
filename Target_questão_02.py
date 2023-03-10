numero = int(input("Informe um número: "))
a, b = 0, 1
fibonacci = [a, b]
while fibonacci[-1] < numero:
  proximo = a + b
  fibonacci.append(proximo)
  a, b = b, proximo

if numero in fibonacci:
  print("O número informado pertence à sequência de Fibonacci.")
else:
  print("O número informado não pertence à sequência de Fibonacci.")


 
