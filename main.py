import pandas as pd
import datetime as dt

df1 = pd.read_csv('gasolina_2000+.csv')
df2 = pd.read_csv('gasolina_2010+.csv')

df=pd.concat([df1,df2])

df.info


#CONVERTENDO DE STRING PARA DETETIME
pd.to_datetime(df['DATA INICIAL'])
pd.to_datetime(df['DATA FINAL'])
type(df.loc[3,'DATA INICIAL'])


#EXTRAINDO MES E ANO A COLUNA DATA FINAL
df['ANO/MES']=pd.to_datetime(df['DATA FINAL']).dt.strftime('%m-%Y')

#CONTANDO TODOS OS PRODUTOS NA BASE DE DADOS
df['PRODUTO'].value_counts()

#PEGANDO DADOS SOMENTE DA GASOLINA
df_gasolina_comum= df[df['PRODUTO'] =='GASOLINA COMUM']

#PREÇO MÉDIO DE REVENDA DO MES DE AGOSTO DE 2008
df_preco_medio_gasolina=df_gasolina_comum.groupby('ANO/MES')[['PREÇO MÉDIO REVENDA']].mean()
df_preco_medio_gasolina.reset_index(inplace=True)
df_preco_medio_gasolina.index 
df_preco_medio_gasolina[df_preco_medio_gasolina['ANO/MES']=='2008-08']

#PREÇO MÉDIO REVENDA DA GASOLUNA EM MAIO DE 2014 EM SP
df_filtro_estado=df_gasolina_comum[['PRODUTO','ESTADO','ANO/MES','PREÇO MÉDIO REVENDA']]

df_filtro_estado_2=df_filtro_estado[(df_filtro_estado['ANO/MES']=='2014-05') & (df_filtro_estado['ESTADO']=='SAO PAULO')]

df_filtro_estado_2.groupby(['ESTADO','PRODUTO','ANO/MES'])[['PREÇO MÉDIO REVENDA']].mean()


#ESTADOS ONDE A GASOLINA PASSOU DE R$5,00
df_gasolina_comum[['ESTADO','ANO/MES','PREÇO MÉDIO REVENDA']][df_gasolina_comum['PREÇO MÉDIO REVENDA'] >= 5]

#MÉDIA DE  PREÇO DOS ESTADOS DA REGIÃO SUL

df['ANO/MES']=pd.to_datetime(df['ANO/MES'], format='%m-%Y')
type(df.loc[1,'ANO/MES'])
df.set_index('ANO/MES',inplace=True)
df_sul=df[['ESTADO','PREÇO MÉDIO REVENDA']][(df['REGIÃO']=='SUL') & (df.index.year==2012)]
df_sul.groupby('ESTADO')[['PREÇO MÉDIO REVENDA']].mean()

#PEGANDO COEFICIENTE DE VARIAÇÃO PARA O ESTADO DO RIO DE JANEIRO ANO A ANO
df.reset_index(inplace=True)
df_rj=df[['COEF DE VARIAÇÃO REVENDA','ESTADO','ANO/MES']][df['ESTADO']=='RIO DE JANEIRO']
df_rj.set_index('ANO/MES', inplace=True)
df_rj.groupby(df_rj.index.year)[['COEF DE VARIAÇÃO REVENDA']].sum()/12


#DESAFIO
df_maiores =df[['ESTADO','PREÇO MÁXIMO REVENDA','ANO/MES']].sort_values(by='PREÇO MÁXIMO REVENDA',ascending=False)
df_menores =df[['ESTADO','PREÇO MÍNIMO REVENDA','ANO/MES']].sort_values(by='PREÇO MÍNIMO REVENDA',ascending=True)

































































