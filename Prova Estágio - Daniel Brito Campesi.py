#!/usr/bin/env python
# coding: utf-8

# # Success Enterprises - Análise do comportamento de vendas durante a pandemia

# ### Importando bibliotecas

# In[1]:


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from datetime import datetime
import io


# 
# 
# ## Parte A

# ##### Importando a base de dados pulando as 3 primeiras linhas

# In[2]:


df = pd.read_excel(r'C:\Users\campe\Documents\Prova estágio\pmc.xlsx', skiprows = range(0,3))


# In[3]:


df.head()


# ##### Renomeando as colunas

# In[4]:


lista = ['data', 'var', 'setor', 'BR', 'CE', 'PE', 'BA', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC', 'RS', 'GO', 'DF']

df.columns = lista


# ##### Convertendo os valores das colunas (BR e siglas de estados) para a classe numérica float

# In[5]:


lista_BR = []
lista_CE = []
lista_PE = []
lista_BA = []
lista_MG = []
lista_ES = []
lista_RJ = []
lista_SP = []
lista_PR = []
lista_SC = []
lista_RS = []
lista_GO = []
lista_DF = []

for valor in df['BR']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_BR.append(valor)
    
    
for valor in df['CE']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_CE.append(valor)
    
    
for valor in df['PE']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_PE.append(valor)
    
    
for valor in df['BA']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_BA.append(valor)
    
    
for valor in df['MG']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_MG.append(valor)
    
    
for valor in df['ES']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_ES.append(valor)
    
    
for valor in df['RJ']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_RJ.append(valor)
    
    
for valor in df['SP']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_SP.append(valor)
    
    
for valor in df['PR']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_PR.append(valor)
    
    
for valor in df['SC']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_SC.append(valor)
    
    
for valor in df['RS']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_RS.append(valor)
    
    
for valor in df['GO']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_GO.append(valor)
    
    
for valor in df['DF']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_DF.append(valor)
       
    
df['BR'] = lista_BR
df['CE'] = lista_CE
df['PE'] = lista_PE
df['BA'] = lista_BA
df['MG'] = lista_MG
df['ES'] = lista_ES
df['RJ'] = lista_RJ
df['SP'] = lista_SP
df['PR'] = lista_PR
df['SC'] = lista_SC
df['RS'] = lista_RS
df['GO'] = lista_GO
df['DF'] = lista_DF


# In[6]:


df.info() # confirmando conversão


# ##### Categorizando as variáveis em receita ou volume e eliminando os dados faltantes

# In[7]:


df.head()


# In[8]:


df.tail()


# In[9]:


df = df.drop(4208)
lista_completar = []

volume = 'Volume'
receita = 'Receita'
quantidade_vezes = 4208 // 16 

lista_de_listas = [(volume[:6] + '').split(',') * 8, (receita[:7] + '').split(',') * 8] * quantidade_vezes


for sublista in lista_de_listas:
    for item in sublista:
        lista_completar.append(item)

df['var'] = lista_completar


# ##### Convertendo as datas para DateTime e eliminando os dados faltantes

# In[10]:


df.info()


# In[11]:


lista_final_pt = []
lista_de_listas = []
quantidade_repeticoes = 16
zero = '0'

df['data'] = df['data'].fillna(0)
df['data'] = df['data'].astype(str)

for valor in df['data']:
    if valor != '0':
        lista_de_listas.append(valor.split(',') * quantidade_repeticoes)


for sublista in lista_de_listas:
    for item in sublista:
        lista_final_pt.append(item)

        
lista_split = []
lista_final_en = []

for data_pt in lista_final_pt:
    lista_split.append(data_pt.split(' '))

for sublista in lista_split:
    if sublista[0] == 'janeiro':
        sublista[0] = 'january'
    elif sublista[0] == 'fevereiro':
        sublista[0] = 'february'
    elif sublista[0] == 'março':
        sublista[0] = 'march'
    elif sublista[0] == 'abril':
        sublista[0] = 'april'
    elif sublista[0] == 'maio':
        sublista[0] = 'may'
    elif sublista[0] == 'junho':
        sublista[0] = 'june'
    elif sublista[0] == 'julho':
        sublista[0] = 'july'
    elif sublista[0] == 'agosto':
        sublista[0] = 'august'
    elif sublista[0] == 'setembro':
        sublista[0] = 'september'
    elif sublista[0] == 'outubro':
        sublista[0] = 'october'
    elif sublista[0] == 'novembro':
        sublista[0] = 'november'
    elif sublista[0] == 'dezembro':
        sublista[0] = 'december'
        
for sublista in lista_split:
    for item in sublista:
        lista_final_en.append(item)        

lista_final_en = [i + ' ' + j for i, j in zip(lista_final_en[::2], lista_final_en[1::2])]       
        
df['data'] = lista_final_en


# In[12]:


df['data'] = df['data'].apply(lambda x: datetime.strptime(x, "%B %Y"))

df.head()


# ##### Removendo as linhas com as variáveis "Receita"

# In[13]:


df.drop(df.loc[df['var']=='Receita'].index, inplace=True)


# In[14]:


df.head()


# In[15]:


df.tail()


# ## Parte B

# ##### Afunilando o DataFrame para o setor de interesse

# In[16]:


df_m_e = df.loc[df['setor'] == 'Móveis e eletrodomésticos']


# In[17]:


df_m_e.head()


# ##### Comparando UFs e dastacando a pandemia para o setor de móveis e eletrodomésticos

# In[18]:


df_m_e.index = df_m_e['data']
df_m_e = df_m_e.drop(columns=['data'])


# In[19]:


df_m_e['media_movel_BR'] = df_m_e.BR.rolling(3).mean()
df_m_e['media_movel_CE'] = df_m_e.CE.rolling(3).mean()
df_m_e['media_movel_PE'] = df_m_e.PE.rolling(3).mean()
df_m_e['media_movel_BA'] = df_m_e.BA.rolling(3).mean()
df_m_e['media_movel_MG'] = df_m_e.MG.rolling(3).mean()
df_m_e['media_movel_ES'] = df_m_e.ES.rolling(3).mean()
df_m_e['media_movel_RJ'] = df_m_e.RJ.rolling(3).mean()
df_m_e['media_movel_SP'] = df_m_e.SP.rolling(3).mean()
df_m_e['media_movel_PR'] = df_m_e.PR.rolling(3).mean()
df_m_e['media_movel_SC'] = df_m_e.SC.rolling(3).mean()
df_m_e['media_movel_RS'] = df_m_e.RS.rolling(3).mean()
df_m_e['media_movel_GO'] = df_m_e.GO.rolling(3).mean()
df_m_e['media_movel_DF'] = df_m_e.DF.rolling(3).mean()


# In[20]:


df_m_e.head()


# In[21]:


df_m_e.tail()


# In[22]:


fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12, ax13) = plt.subplots(13, sharex=True, figsize=(14,24))

ax1.plot(df_m_e['media_movel_BR'], color= 'yellow')
ax1.legend(["Brasil - BR"], bbox_to_anchor = (1.0, 0.6))

ax2.plot(df_m_e['media_movel_CE'], color= 'k')
ax2.legend(["Ceará - CE"], bbox_to_anchor = (1.0, 0.6))

ax3.plot(df_m_e['media_movel_PE'], color= 'r')
ax3.legend(["Pernambuco - PE"], bbox_to_anchor = (1.0, 0.6))

ax4.plot(df_m_e['media_movel_BA'], color= 'c')
ax4.legend(["Bahia - BA"], bbox_to_anchor = (1.0, 0.6))

ax5.plot(df_m_e['media_movel_MG'], color= 'darkred')
ax5.legend(["Minas Gerais - MG"], bbox_to_anchor = (1.0, 0.6))

ax6.plot(df_m_e['media_movel_ES'], color= 'chocolate')
ax6.legend(["Espírito Santo - ES"], bbox_to_anchor = (1.0, 0.6))

ax7.plot(df_m_e['media_movel_RJ'], color = 'tomato')
ax7.legend(["Rio de Janeiro - RJ"], bbox_to_anchor = (1.0, 0.6))

ax8.plot(df_m_e['media_movel_SP'], color = 'blue')
ax8.legend(["São Paulo - SP"], bbox_to_anchor = (1.0, 0.6))

ax9.plot(df_m_e['media_movel_PR'], color = 'darkorange')
ax9.legend(["Paraná - PR"], bbox_to_anchor = (1.0, 0.6))

ax10.plot(df_m_e['media_movel_SC'], color = 'olive')
ax10.legend(["Santa Catarina - SC"], bbox_to_anchor = (1.0, 0.6))

ax11.plot(df_m_e['media_movel_RS'], color = 'green')
ax11.legend(["Rio Grande do Sul - RS"], bbox_to_anchor = (1.0, 0.6))

ax12.plot(df_m_e['media_movel_GO'], color = 'purple')
ax12.legend(["Goiás - GO"], bbox_to_anchor = (1.0, 0.6))

ax13.plot(df_m_e['media_movel_DF'], color = 'hotpink')
ax13.legend(["Destrito Federal - DF"], bbox_to_anchor = (1.0, 0.6))


fig.suptitle('MÉDIA MÓVEL (3 MESES) - VOLUME DE VENDAS DE MÓVEIS E ELETRODOMÉSTICOS POR ESTADO E O AGREGADO NACIONAL', fontsize=13)


# ÁREAS RACHURADAS
ax1.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax2.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax3.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax4.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax5.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax6.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax7.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax8.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax9.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax10.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax11.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax12.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)
ax13.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-11-01'), color='gray', alpha=0.25)



# CARACTERÍSTICAS DAS SETAS 
arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

# SETAS 
ax1.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax2.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax3.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax4.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax5.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax6.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax7.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax8.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax9.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax10.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax11.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax12.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)


ax13.annotate(
    "PANDEMIA", xy=(pd.to_datetime('2020-06-01'), 40),
    xytext=(pd.to_datetime('2017-01-01'), 25),
    arrowprops=arrow_properties)



plt.show()


# In[23]:


df_m_e_colormap = df_m_e.loc[df_m_e.index >= '2019-11-01']
df_m_e_colormap = df_m_e_colormap.drop(columns=['var', 'setor', 'BR', 'CE', 'PE', 'BA', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC',                                                'RS', 'GO', 'DF'])

lista_datas = []
for data in df_m_e_colormap.index:
    lista_datas.append(data.date())
df_m_e_colormap.index = lista_datas


# In[24]:


fig, ax = plt.subplots(figsize=(14,7))
sns.heatmap(df_m_e_colormap, cmap='YlOrBr', ax=ax)

fig.suptitle('Mapa de Calor da média móvel do volume de vendas de móveis e eletrodomésticos em cada UF e no Brasil', fontsize=14)


# ##### Análise da variação percentual na pandemia

# In[25]:


df_m_e_pandemia = df_m_e.loc[df_m_e.index >= '2019-04-01']
df_m_e_pandemia = df_m_e_pandemia.loc[df_m_e_pandemia.index <= '2020-04-01']

variacoes = []

def variacao_percentual(coluna):
    lista = []
    for i in coluna:
        lista.append(i)
    VF = lista[-1]
    VI = lista[0]
    return (VF/VI - 1)/100

variacoes.append(variacao_percentual(df_m_e_pandemia['BR']))
variacoes.append(variacao_percentual(df_m_e_pandemia['CE']))
variacoes.append(variacao_percentual(df_m_e_pandemia['PE']))
variacoes.append(variacao_percentual(df_m_e_pandemia['BA']))
variacoes.append(variacao_percentual(df_m_e_pandemia['MG']))
variacoes.append(variacao_percentual(df_m_e_pandemia['ES']))
variacoes.append(variacao_percentual(df_m_e_pandemia['RJ']))
variacoes.append(variacao_percentual(df_m_e_pandemia['SP']))
variacoes.append(variacao_percentual(df_m_e_pandemia['PR']))
variacoes.append(variacao_percentual(df_m_e_pandemia['SC']))
variacoes.append(variacao_percentual(df_m_e_pandemia['RS']))
variacoes.append(variacao_percentual(df_m_e_pandemia['GO']))
variacoes.append(variacao_percentual(df_m_e_pandemia['DF']))


df_m_e_pandemia['variações percentuais'] = variacoes
lista_datas = []
for data in df_m_e_pandemia.index:
    lista_datas.append(data.date())
df_m_e_pandemia.index = lista_datas

df_m_e_pandemia = df_m_e_pandemia.filter(items=['variações percentuais'])
df_m_e_pandemia['Local'] = ['BR', 'CE', 'PE', 'BA', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC', 'RS', 'GO', 'DF']

ax = plt.subplots()
ax = sns.catplot(x='Local', y="variações percentuais", kind="bar", aspect=2, data=df_m_e_pandemia)
plt.title('VARIAÇÕES PERCENTUAIS DE CADA UF E DO AGREGADO NACIONAL (2019.04 - 2020.04)')


# In[26]:


df_m_e_pandemia.head()


# ##### Destacando SP em relação a BR

# In[27]:


fig = plt.figure(figsize=(14, 5))
line_weight = 3
alpha = .5
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes()
#ax3 = fig.add_axes()

ax2 = ax1.twinx()
#ax3 = ax2.twinx()

lns1 = ax1.plot(df_m_e['media_movel_BR'], color='darkgreen', lw=line_weight, alpha=alpha,  marker='D', label='Brasil')
lns2 = ax2.plot(df_m_e['media_movel_SP'], color='blue', lw=line_weight, alpha=alpha,  marker='*', label='São Paulo')



leg = lns1 + lns2
labs = [l.get_label() for l in leg]
ax1.legend(leg, labs, loc='upper left')

plt.title('Comparativo entre a média móvel (3 meses) do volume de vendas de móveis e eletrodomésticos no Brasil e em São Paulo', fontsize=14)


ax1.set_ylabel('Brasils', color='k')
ax2.set_ylabel('São Paulo', color='k', rotation=-90, labelpad=11)


#DESTAQUE CINZA
plt.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2020-06-01'), color='gray', alpha=0.25)
plt.axvspan(pd.to_datetime('2021-01-01'),pd.to_datetime('2021-06-01'), color='gray', alpha=0.25)


# CARACTERÍSTICAS DAS SETAS 
arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

# SETA 
ax1.annotate(
    "PANDEMIA - 1ª Onda", xy=(pd.to_datetime('2020-05-01'), 60),
    xytext=(pd.to_datetime('2017-01-01'), 55),
    arrowprops=arrow_properties)

# 2 SETA 
ax1.annotate(
    "PANDEMIA - 2ª Onda", xy=(pd.to_datetime('2021-05-01'), 50),
    xytext=(pd.to_datetime('2018-01-01'), 45),
    arrowprops=arrow_properties)


plt.show()


# ##### Comparando os setores no estado de SP

# In[28]:


df_setores_SP = df.filter(items=['data', 'setor', 'SP'])


# In[29]:


df_setores_SP['media_movel'] = df_setores_SP.SP.rolling(3).mean()


# In[30]:


df_setores_SP.head()


# In[31]:


setor1 = df_setores_SP.loc[df_setores_SP['setor'] == 'Combustíveis e lubrificantes']
setor1.index = setor1['data']
setor1 = setor1.filter(items=['SP', 'media_movel'])



setor2 = df_setores_SP.loc[df_setores_SP['setor'] == 'Hipermercados, supermercados, produtos alimentícios, bebidas e fumo']
setor2.index = setor2['data']
setor2 = setor2.filter(items=['SP', 'media_movel'])



setor3 = df_setores_SP.loc[df_setores_SP['setor'] == 'Tecidos, vestuário e calçados']
setor3.index = setor3['data']
setor3 = setor3.filter(items=['SP', 'media_movel'])



setor4 = df_setores_SP.loc[df_setores_SP['setor'] == 'Artigos farmacêuticos, médicos, ortopédicos, de perfumaria e cosméticos']
setor4.index = setor4['data']
setor4 = setor4.filter(items=['SP', 'media_movel'])



setor5 = df_setores_SP.loc[df_setores_SP['setor'] == 'Livros, jornais, revistas e papelaria']
setor5.index = setor5['data']
setor5 = setor5.filter(items=['SP', 'media_movel'])



setor6 = df_setores_SP.loc[df_setores_SP['setor'] == 'Equipamentos e materiais para escritório, informática e comunicação']
setor6.index = setor6['data']
setor6 = setor6.filter(items=['SP', 'media_movel'])



setor7 = df_setores_SP.loc[df_setores_SP['setor'] == 'Outros artigos de uso pessoal e doméstico']
setor7.index = setor7['data']
setor7 = setor7.filter(items=['SP', 'media_movel'])


# In[32]:


fig = plt.figure(figsize=(14, 3.5))
line_weight = 3
alpha = .5
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes()
#ax3 = fig.add_axes()


ax2 = ax1.twinx()
#ax3 = ax2.twinx()

lns1 = ax1.plot(setor1['media_movel'], color='r', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Combustíveis e Lubrificantes"')
lns2 = ax2.plot(df_m_e['media_movel_SP'], color='k', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Móveis e eletrodomésticos"')

ax1.set_ylabel('Combustíveis e Lubrificantes', color='k')
ax2.set_ylabel('Móveis e eletrodomésticos', color='k', rotation=-90, labelpad=11)


#DESTAQUE CINZA
plt.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2020-06-01'), color='gray', alpha=0.25)
plt.axvspan(pd.to_datetime('2021-01-01'),pd.to_datetime('2021-06-01'), color='gray', alpha=0.25)


# CARACTERÍSTICAS DAS SETAS 
arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

# SETA 
ax1.annotate(
    "PANDEMIA - 1ª Onda", xy=(pd.to_datetime('2020-05-01'), 60),
    xytext=(pd.to_datetime('2017-01-01'), 55),
    arrowprops=arrow_properties)

# 2 SETA 
ax1.annotate(
    "PANDEMIA - 2ª Onda", xy=(pd.to_datetime('2021-05-01'), 50),
    xytext=(pd.to_datetime('2018-01-01'), 45),
    arrowprops=arrow_properties)



leg = lns1 + lns2
labs = [l.get_label() for l in leg]
ax1.legend(leg, labs, loc=2)

plt.title('Comparativo de setores no estado de São Paulo', fontsize=14)
plt.show()


# In[33]:


fig = plt.figure(figsize=(14, 3.5))
line_weight = 3
alpha = .5
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes()
#ax3 = fig.add_axes()


ax2 = ax1.twinx()
#ax3 = ax2.twinx()

lns1 = ax1.plot(setor2['media_movel'], color='forestgreen', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Hipermercados, supermercados, produtos alimentícios, bebidas e fumo"')
lns2 = ax2.plot(df_m_e['media_movel_SP'], color='k', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Móveis e eletrodomésticos"')

ax1.set_ylabel('Combustíveis e Lubrificantes', color='k')
ax2.set_ylabel('Móveis e eletrodomésticos', color='k', rotation=-90, labelpad=11)


#DESTAQUE CINZA
plt.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2020-06-01'), color='gray', alpha=0.25)
plt.axvspan(pd.to_datetime('2021-01-01'),pd.to_datetime('2021-06-01'), color='gray', alpha=0.25)


# CARACTERÍSTICAS DAS SETAS 
arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

# SETA 
ax1.annotate(
    "PANDEMIA - 1ª Onda", xy=(pd.to_datetime('2020-05-01'), 70),
    xytext=(pd.to_datetime('2017-01-01'), 65),
    arrowprops=arrow_properties)

# 2 SETA 
ax1.annotate(
    "PANDEMIA - 2ª Onda", xy=(pd.to_datetime('2021-05-01'), 60),
    xytext=(pd.to_datetime('2018-01-01'), 55),
    arrowprops=arrow_properties)



leg = lns1 + lns2
labs = [l.get_label() for l in leg]
ax1.legend(leg, labs, loc=2)

plt.title('Comparativo de setores no estado de São Paulo', fontsize=14)
plt.show()


# In[34]:


fig = plt.figure(figsize=(14, 3.5))
line_weight = 3
alpha = .5
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes()
#ax3 = fig.add_axes()


ax2 = ax1.twinx()
#ax3 = ax2.twinx()

lns1 = ax1.plot(setor3['media_movel'], color='c', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Tecidos, vestuário e calçados"')
lns2 = ax2.plot(df_m_e['media_movel_SP'], color='k', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Móveis e eletrodomésticos"')

ax1.set_ylabel('Combustíveis e Lubrificantes', color='k')
ax2.set_ylabel('Móveis e eletrodomésticos', color='k', rotation=-90, labelpad=11)



#DESTAQUE CINZA
plt.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2020-06-01'), color='gray', alpha=0.25)
plt.axvspan(pd.to_datetime('2021-01-01'),pd.to_datetime('2021-06-01'), color='gray', alpha=0.25)


# CARACTERÍSTICAS DAS SETAS 
arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

# SETA 
ax1.annotate(
    "PANDEMIA - 1ª Onda", xy=(pd.to_datetime('2020-05-01'), 70),
    xytext=(pd.to_datetime('2017-01-01'), 60),
    arrowprops=arrow_properties)

# 2 SETA 
ax1.annotate(
    "PANDEMIA - 2ª Onda", xy=(pd.to_datetime('2021-05-01'), 60),
    xytext=(pd.to_datetime('2018-01-01'), 55),
    arrowprops=arrow_properties)



leg = lns1 + lns2
labs = [l.get_label() for l in leg]
ax1.legend(leg, labs, loc=2)

plt.title('Comparativo de setores no estado de São Paulo', fontsize=14)
plt.show()


# In[35]:


fig = plt.figure(figsize=(14, 3.5))
line_weight = 3
alpha = .5
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes()
#ax3 = fig.add_axes()


ax2 = ax1.twinx()
#ax3 = ax2.twinx()

lns1 = ax1.plot(setor4['media_movel'], color='purple', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Artigos farmacêuticos, médicos, ortopédicos, de perfumaria e cosméticos"')
lns2 = ax2.plot(df_m_e['media_movel_SP'], color='k', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Móveis e eletrodomésticos"')

ax1.set_ylabel('Combustíveis e Lubrificantes', color='k')
ax2.set_ylabel('Móveis e eletrodomésticos', color='k', rotation=-90, labelpad=11)



#DESTAQUE CINZA
plt.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2020-06-01'), color='gray', alpha=0.25)
plt.axvspan(pd.to_datetime('2021-01-01'),pd.to_datetime('2021-06-01'), color='gray', alpha=0.25)


# CARACTERÍSTICAS DAS SETAS 
arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

# SETA 
ax1.annotate(
    "PANDEMIA - 1ª Onda", xy=(pd.to_datetime('2020-05-01'), 60),
    xytext=(pd.to_datetime('2017-01-01'), 55),
    arrowprops=arrow_properties)

# 2 SETA 
ax1.annotate(
    "PANDEMIA - 2ª Onda", xy=(pd.to_datetime('2021-05-01'), 50),
    xytext=(pd.to_datetime('2018-01-01'), 45),
    arrowprops=arrow_properties)



leg = lns1 + lns2
labs = [l.get_label() for l in leg]
ax1.legend(leg, labs, loc=2)

plt.title('Comparativo de setores no estado de São Paulo', fontsize=14)
plt.show()


# In[36]:


fig = plt.figure(figsize=(14, 3.5))
line_weight = 3
alpha = .5
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes()
#ax3 = fig.add_axes()


ax2 = ax1.twinx()
#ax3 = ax2.twinx()

lns1 = ax1.plot(setor5['media_movel'], color='darkorange', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Livros, jornais, revistas e papelaria"')
lns2 = ax2.plot(df_m_e['media_movel_SP'], color='k', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Móveis e eletrodomésticos"')

ax1.set_ylabel('Combustíveis e Lubrificantes', color='k')
ax2.set_ylabel('Móveis e eletrodomésticos', color='k', rotation=-90, labelpad=11)



#DESTAQUE CINZA
plt.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2020-06-01'), color='gray', alpha=0.25)
plt.axvspan(pd.to_datetime('2021-01-01'),pd.to_datetime('2021-06-01'), color='gray', alpha=0.25)


# CARACTERÍSTICAS DAS SETAS 
arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

# SETA 
ax1.annotate(
    "PANDEMIA - 1ª Onda", xy=(pd.to_datetime('2020-05-01'), 60),
    xytext=(pd.to_datetime('2017-01-01'), 55),
    arrowprops=arrow_properties)

# 2 SETA 
ax1.annotate(
    "PANDEMIA - 2ª Onda", xy=(pd.to_datetime('2021-05-01'), 50),
    xytext=(pd.to_datetime('2018-01-01'), 45),
    arrowprops=arrow_properties)



leg = lns1 + lns2
labs = [l.get_label() for l in leg]
ax1.legend(leg, labs, loc=2)

plt.title('Comparativo de setores no estado de São Paulo', fontsize=14)
plt.show()


# In[37]:


fig = plt.figure(figsize=(14, 3.5))
line_weight = 3
alpha = .5
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes()
#ax3 = fig.add_axes()


ax2 = ax1.twinx()
#ax3 = ax2.twinx()

lns1 = ax1.plot(setor6['media_movel'], color='olive', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Equipamentos e materiais para escritório, informática e comunicação"')
lns2 = ax2.plot(df_m_e['media_movel_SP'], color='k', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Móveis e eletrodomésticos"')

ax1.set_ylabel('Combustíveis e Lubrificantes', color='k')
ax2.set_ylabel('Móveis e eletrodomésticos', color='k', rotation=-90, labelpad=11)



#DESTAQUE CINZA
plt.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2020-06-01'), color='gray', alpha=0.25)
plt.axvspan(pd.to_datetime('2021-01-01'),pd.to_datetime('2021-06-01'), color='gray', alpha=0.25)


# CARACTERÍSTICAS DAS SETAS 
arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

# SETA 
ax1.annotate(
    "PANDEMIA - 1ª Onda", xy=(pd.to_datetime('2020-05-01'), 60),
    xytext=(pd.to_datetime('2017-01-01'), 55),
    arrowprops=arrow_properties)

# 2 SETA 
ax1.annotate(
    "PANDEMIA - 2ª Onda", xy=(pd.to_datetime('2021-05-01'), 50),
    xytext=(pd.to_datetime('2018-01-01'), 45),
    arrowprops=arrow_properties)



leg = lns1 + lns2
labs = [l.get_label() for l in leg]
ax1.legend(leg, labs, loc=2)

plt.title('Comparativo de setores no estado de São Paulo', fontsize=14)
plt.show()


# In[38]:


fig = plt.figure(figsize=(14, 3.5))
line_weight = 3
alpha = .5
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes()
#ax3 = fig.add_axes()


ax2 = ax1.twinx()
#ax3 = ax2.twinx()

lns1 = ax1.plot(setor7['media_movel'], color='lime', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Outros artigos de uso pessoal e doméstico"')
lns2 = ax2.plot(df_m_e['media_movel_SP'], color='k', lw=line_weight, alpha=alpha, label='Média Móvel (3 meses) do setor "Móveis e eletrodomésticos"')

ax1.set_ylabel('Combustíveis e Lubrificantes', color='k')
ax2.set_ylabel('Móveis e eletrodomésticos', color='k', rotation=-90, labelpad=11)



#DESTAQUE CINZA
plt.axvspan(pd.to_datetime('2020-01-01'),pd.to_datetime('2020-06-01'), color='gray', alpha=0.25)
plt.axvspan(pd.to_datetime('2021-01-01'),pd.to_datetime('2021-06-01'), color='gray', alpha=0.25)


# CARACTERÍSTICAS DAS SETAS 
arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

# SETA 
ax1.annotate(
    "PANDEMIA - 1ª Onda", xy=(pd.to_datetime('2020-05-01'), 60),
    xytext=(pd.to_datetime('2017-01-01'), 55),
    arrowprops=arrow_properties)

# 2 SETA 
ax1.annotate(
    "PANDEMIA - 2ª Onda", xy=(pd.to_datetime('2021-05-01'), 40),
    xytext=(pd.to_datetime('2018-01-01'), 30),
    arrowprops=arrow_properties)



leg = lns1 + lns2
labs = [l.get_label() for l in leg]
ax1.legend(leg, labs, loc=2)

plt.title('Comparativo de setores no estado de São Paulo', fontsize=14)
plt.show()


# In[39]:


lista_datas = []
for data in df_setores_SP['data']:
    lista_datas.append(data.date())
df_setores_SP['data'] = lista_datas


# In[40]:


ax = plt.subplots()
ax = sns.catplot(x="setor", y="SP",
            kind="bar", aspect=3, data=df_setores_SP)
plt.xticks(rotation=90)

plt.title('Média do volume vendido em cada setor (2000.1 - 2021.11) em São Paulo', fontsize=14)


# ## Parte C

# ##### Lendo a base de dados

# In[41]:


df_rendimento = pd.read_csv(r'C:\Users\campe\Documents\Prova estágio\rendimento_efetivo_real.csv', encoding='UTF-8')


# In[42]:


df_rendimento.head()


# ##### Renomeando as colunas e separando os dados em colunas diferentes

# In[43]:


coluna = ['data ; renda', 'PNAD']
df_rendimento.columns = coluna

df_rendimento = df_rendimento.drop(columns = 'PNAD')


# In[44]:


df_rendimento.head()


# In[45]:


lista_de_listas = []
lista_data = []
lista_renda = []

for valor in df_rendimento['data ; renda']:
    lista_de_listas.append(valor.split(';'))
    
for sublista in lista_de_listas:
    lista_data.append(sublista[0])
    lista_renda.append(sublista[1])
    
df_rendimento['data'] = lista_data
df_rendimento['renda'] = lista_renda
df_rendimento = df_rendimento.drop(columns=['data ; renda'])


# In[46]:


df_rendimento.head()


# ##### Alterando a classe (type) dos dados

# In[47]:


df_rendimento['data'] = pd.to_datetime(df_rendimento['data'])


# In[48]:


lista_renda = []

for valor in df_rendimento['renda']:
    if valor == '-':
        valor = None
    else:
        valor = float(valor)
    lista_renda.append(valor)
    
df_rendimento['renda'] = lista_renda


# In[49]:


df_rendimento.info()


# In[50]:


df_rendimento.head()


# In[51]:


df_rendimento.tail()


# #### Concatenando os DataFrames referente as duas bases de dados

# In[52]:


df_rendimento.index = df_rendimento['data']
df_rendimento = df_rendimento.drop(columns=['data'])


# In[53]:


df_c = df_m_e.loc[df_m_e.index >= '2012-03-01']
df_c = df_c.loc[df_c.index <= '2021-10-01']

df_concat = pd.concat([df_c['setor'], df_c['BR'], df_rendimento], axis=1, sort=False)


# In[54]:


df_concat.rename(columns={'BR':'Volume - BR'},inplace=True)


# In[55]:


df_concat.head()


# In[56]:


df_concat.info()


# ##### Gráficos e análises das duas bases juntas

# In[57]:


fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(16,8))

ax1.plot(df_concat['Volume - BR'], color= 'darkred', label='Volume de vendas de móveis e eletrodomésticos - BR')
ax1.legend(loc="lower left")

ax2.plot(df_concat['renda'], color= 'darkgreen', label='Rendimento do setor de móveis e eletrodomésticos - BR')
ax2.legend(loc="upper left")

fig.suptitle('Comparação entre o rendimento e o volume de vendas do setor de móveis e eletrodomésticos no Brasil', fontsize=14)    


# In[ ]:




