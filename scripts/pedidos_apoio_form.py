import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

pedidos_apoio_url = os.getenv('PEDIDOS_APOIO_URL')
# Read the file using pandas
df = pd.read_csv(pedidos_apoio_url)
# Remove the unwanted columns
df.drop(df.iloc[:, [1, 5, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]].columns, axis=1, inplace=True)

# Define new column names
new_columns_name = [
    'id',
    'data_envio',
    'nome_solicitante',
    'email_solicitante',
    'sigla_orgao_solicitante',
    'nome_orgao_solicitante',
    'nome_processo',
    'detalhamento_processo',
    'processo_replicavel',
    'conhecimento_equipe_power_automate',
    'conhecimento_equipe_excel_bando_dados',
    'conhecimento_equipe_programacao',
    'ligado_projeto_estrategico',
    'nome_projeto_estragegico',
    'nivel_automacao_processo',
    'detalhamento_automacao_processo',
    'possui_banco_dados',
    'detalhamento_banco_dados',
    'frequencia_processo',
    'numero_ocorrencias',
    'minutos_por_ocorrencia',
    'gera_impacto_na_arrecadacao',
    'impacto_na_arrecadacao',
    'nota_arrecadacao',
    'nota_volume',
    'nota_equipe',
    'nota_facilidade',
    'nota_projeto_estrategico',
    'nota_projeto_replicavel',
    'nota_final',
    'classificacao',
]
# Replace new line to space in string fields
df.columns = new_columns_name
for column in df.columns:
    if df[column].dtype != 'float64' and  df[column].dtype != 'int64':
        df[column] = df[column].str.replace('\n', ' ')

# Filter NaN values in 'classificacao' field
df.dropna(subset=['classificacao'], inplace=True)
# Sort by final result
df.sort_values(
               by='nota_final',
               ascending=False,
               inplace=True
               )
# Save result in data/pedidos_apoio.csv file
df.to_csv('data/pedidos_apoio.csv', index=False)
