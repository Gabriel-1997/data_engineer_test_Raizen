import pandas as pd
import requests as rq

base = rq.get("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/vdpb/vendas-combustiveis-m3.xls", allow_redirects=True)
open('base-vendas.xls', 'wb').write(base.content)

# df_petroleo = pd.read_excel("base-vendas.xls", "Planilha2")
# df_diesel = pd.read_excel("vendas-combustiveis.xls", "Planilha3")

# print(df_petroleo)
# print(df_diesel)

