# Criar um código que consuma uma api de clima informe
# a temperatura e a descrição do clima em um lugar especifico


# etapa 
# 1. Definir chave de API e o link da requisição
import requests

api_key ='2a1ac38a32354cb7b19133643251408'
cidade = input('Digite o nome da cidade: ').strip()
url=f'https://api.weatherapi.com/v1/current.json' # url da api

#2. Paramêtros da requisisão
parametros ={
    'key':api_key,
    'q':cidade,
    'lang':'pt' # define a língua da resposta como português
}

# 3. Fazer a requisição
resposta = requests.get(url, params=parametros) # utilizamos o método get e informamos os parâmetros dessa requisição

# 4. Verificiar se a requisição foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json() #convertendo a resposta JSON em um dicionário Python
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'Temperatura na cidade {cidade}é {temperatura}°C.') 
    print(f'Descroção: {descricao}')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)



