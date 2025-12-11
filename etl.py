import pandas as pd
import json

# --- PARTE 1: CRIANDO A "FONTE DE DADOS" (EXTRACT) ---
# Vamos criar um arquivo CSV simples com IDs e Áreas de Interesse
dados = {
    'UserID': [1, 2, 3, 4],
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Interesse': ['Front-end', 'Dados', 'Mobile', 'Cloud']
}
# Salvando como se fosse a planilha original
df = pd.read_csv('SDW2023.csv') if False else pd.DataFrame(dados) # Truque para criar local
df.to_csv('SDW2023.csv', index=False)

print("✅ Passo 1: Arquivo 'SDW2023.csv' gerado com sucesso.")

# --- PARTE 2: TRANSFORMANDO OS DADOS (TRANSFORM) ---
# Aqui a mágica acontece. Em vez do ChatGPT, usamos lógica Python.
print("🔄 Passo 2: Iniciando transformação...")

# Convertendo CSV para Dicionário (JSON)
usuarios = df.to_dict(orient='records')

# Função que simula a IA gerando mensagens
def gerar_mensagem(interesse):
    mensagens = {
        'Front-end': "Aprenda HTML e CSS para criar interfaces incríveis!",
        'Dados': "Domine Python e SQL para analisar grandes volumes de dados.",
        'Mobile': "Estude Kotlin ou Swift para criar apps modernos.",
        'Cloud': "Certificações em AWS ou Azure são o futuro da infraestrutura."
    }
    return mensagens.get(interesse, "Continue estudando tecnologia!")

# Aplicando a transformação
for usuario in usuarios:
    msg = gerar_mensagem(usuario['Interesse'])
    usuario['news'] = [{
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": f"Olá {usuario['Nome']}! {msg}"
    }]

print("✅ Transformação concluída.")

# --- PARTE 3: CARREGANDO OS DADOS (LOAD) ---
# Salvando o resultado final em um arquivo JSON
print("💾 Passo 3: Salvando resultados...")

with open('santander_etl_final.json', 'w', encoding='utf-8') as f:
    json.dump(usuarios, f, indent=4, ensure_ascii=False)

print("✅ SUCESSO! O arquivo 'santander_etl_final.json' foi criado.")
print("   (Copie este código para colocar no seu GitHub)")
