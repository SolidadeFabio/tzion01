import requests, re

def consulta_cnpj_api(cnpj: str) -> str:
    razao_social = None  
    cnpj_string = str(cnpj)
    cnpj_sem_traco = re.sub(r'[^\d]', '', cnpj_string)
    url = f'https://api-publica.speedio.com.br/buscarcnpj?cnpj={cnpj_sem_traco}'
    
    try:
        requisicao = requests.get(url=url)
        dados_resposta = requisicao.json()
        razao_social = dados_resposta['RAZAO SOCIAL']
    except Exception as e:
        print(f"Erro na API Consulta de CNPJ: {e}")
        
    return razao_social  