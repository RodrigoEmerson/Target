import json


valor_minimo = None
valor_maximo = None
media_mensal = 0
dias_acima_media = 0


with open('dados.json') as json_file:
    dados = json.load(json_file)


valor_minimo = min([dado['valor'] for dado in dados if dado['valor'] != 0])


valor_maximo = max([dado['valor'] for dado in dados if dado['valor'] != 0])


soma_valores = 0
for dado in dados:
    if dado['valor'] != 0:
        soma_valores += dado['valor']
media_mensal = soma_valores/len(dados)


for dado in dados:
    if dado['valor'] > media_mensal and dado['valor'] != 0:
        dias_acima_media += 1


print('Valor Mínimo: R$ {:.2f}'.format(valor_minimo))
print('Valor Máximo: R$ {:.2f}'.format(valor_maximo))
print('Média Mensal: R$ {:.2f}'.format(media_mensal))
print('Dias Acima da Média:', dias_acima_media)

