from operator import index
import zipfile
from matplotlib.axis import YAxis
import streamlit as st
import pandas as pd
import numpy as np
import math
import apps.descricaoColunas as dc
import plotly.express as px
import plotly.figure_factory as ff
from scipy.stats import skew, kurtosis
import seaborn as sns
import matplotlib.pyplot as plt

def analiseGeral():
    
        #print usando markdown
        st.markdown("# **Análise Descritiva Geral**")

        #print usando markdown
        st.markdown("---")

        #lendo a base de dados
        with zipfile.ZipFile("./data/BaseTratada.zip") as zip:
                with zip.open("BaseTratada.csv") as arq:
                        dfBase = pd.read_csv(arq, delimiter=";", decimal=",",  encoding="ISO-8859-1")

        #alterando o tipo de dados das notas
        dfBase = dfBase.astype({"NotaGeral"         :"float64", 
                                "NotaConhGeral"     :"float64", 
                                "NotaConhEspecifico":"float64"})

                
        #criando "cards" com algumas informações relevantes
        st.markdown("**1 - Quantidade, Idade e Nota Geral**")
    
        #variáveis para utilizar no card
        totRow  = dfBase.shape[0]
        totFem  = dfBase[dfBase["Sexo"] == "Feminino"].shape[0]
        totMasc = dfBase[dfBase["Sexo"] == "Masculino"].shape[0]
    
        #criando colunas para dividir tela dos cards
        cola, colb, colc = st.columns(3)
    
        #coluna 1 - quantidade
        with cola:

                st.metric("Quantidade Total Alunos", totRow  , delta="100%", delta_color="off")
                st.metric("Quantidade Feminino", totFem ,  delta=str(round((totFem/totRow)*100,2)) + "%", delta_color="off")
                st.metric("Quantidade Masculino", totMasc, delta=str(round((totMasc/totRow)*100,2)) + "%", delta_color="off")
    
        #coluna 2 - média idade
        with colb:

                st.metric("Média Idade Geral", round(dfBase["Idade"].mean(),2), delta="Min: " + str(dfBase["Idade"].min()) + " - Max: " + str(dfBase["Idade"].max()) , delta_color="off")
                st.metric("Média Idade Feminino", round(dfBase[dfBase["Sexo"] == "Feminino"]["Idade"].mean(),2), delta="Min: " + str(dfBase[dfBase["Sexo"] == "Feminino"]["Idade"].min()) + " - Max: " + str(dfBase[dfBase["Sexo"] == "Feminino"]["Idade"].max()), delta_color="off")
                st.metric("Média Idade Masculino", round(dfBase[dfBase["Sexo"] == "Masculino"]["Idade"].mean(),2), delta="Min: " + str(dfBase[dfBase["Sexo"] == "Masculino"]["Idade"].min()) + " - Max: " + str(dfBase[dfBase["Sexo"] == "Masculino"]["Idade"].max()) , delta_color="off")
    
        #coluna 3 - nota geral
        with colc:

                st.metric("Nota Média Geral", round(dfBase["NotaGeral"].mean(),2), delta="Min: " + str(dfBase["NotaGeral"].min()) + " - Max: " + str(dfBase["NotaGeral"].max()) , delta_color="off")
                st.metric("Nota Média Feminino", round(dfBase[dfBase["Sexo"] == "Feminino"]["NotaGeral"].mean(),2), delta="Min: " + str(dfBase[dfBase["Sexo"] == "Feminino"]["NotaGeral"].min()) + " - Max: " + str(dfBase[dfBase["Sexo"] == "Feminino"]["NotaGeral"].max()) , delta_color="off")
                st.metric("Nota Média Masculino", round(dfBase[dfBase["Sexo"] == "Masculino"]["NotaGeral"].mean(),2), delta="Min: " + str(dfBase[dfBase["Sexo"] == "Masculino"]["NotaGeral"].min()) + " - Max: " + str(dfBase[dfBase["Sexo"] == "Masculino"]["NotaGeral"].max()) , delta_color="off")

        #print usando markdown
        st.markdown("---")


        st.markdown("**2 - Histograma e Análise da Nota Geral**")
            
        #plot histograma
        fig2 = ff.create_distplot([dfBase["NotaGeral"]],
                                    ["Nota Geral"], 
                                    histnorm= "probability",
                                    bin_size=  1+3.3*math.log10(dfBase["NotaGeral"].count()), #calculando o bin size
                                    show_hist=True, show_curve=True, show_rug=False )
        st.plotly_chart(fig2, use_container_width=True)
    

        #curtose
        curtose = round(dfBase["NotaGeral"].kurtosis(),4)

        if curtose == 0.263:
                textCurtose = "MESOCÚRTICA"
        elif curtose > 0.263:
                textCurtose = "PLATICÚRTICA"
        else:
                textCurtose = "LEPTOCÚRTICA"

        #assimetria
        assimetria = round(dfBase["NotaGeral"].skew(),4)
        
        if assimetria == 0:
                analise = f"""
                                O gráfico possui assimetria **NULA**, com valor de **{assimetria}**, com isso, podemos afirmar que a concentração de dados estão à direita.
    
                                Quanto a curtose, devido ao seu valor de **{curtose}**, podemos afirmar que a curva formada é **{textCurtose}**
                        """
        elif assimetria < 0:
                analise = f"""
                                O gráfico possui assimetria **NEGATIVA**, com valor de **{assimetria}**, com isso, podemos afirmar que a concentração de dados estão à direita.
    
                                Quanto a curtose, devido ao seu valor de **{curtose}**, podemos afirmar que a curva formada é **{textCurtose}**
                        """
        else: 
                analise = f"""
                                O gráfico possui assimetria **POSITIVA**, com valor de **{assimetria}**, com isso, podemos afirmar que a concentração de dados estão à esqueda. 
            
                                Quanto à curtose, devido ao seu valor de **{curtose}**, podemos afirmar que a curva formada é **{textCurtose}**
                        """

        #print usando markdown da análise
        st.markdown(analise)

        #print usando markdown
        st.markdown("---")
    
        #variável para numerar os títulos das distribuições de frequência
        count = 3

        #for na lista desejada para criação das distribuições de frequência
        for freq in ["NotaGeral", "Idade"]:
            
                #printando o título
                st.markdown(f"**{count} - Distribuição de Frequência por {str(freq)}**")

                #criando DF com a coluna desejada
                dfFreq = dfBase[freq]

                #calculando tamanho, largura, bin 
                tamClasse = int(np.log2(dfFreq.size).round()) + 1
                largClasse = round((dfFreq.max() - dfFreq.min()) / tamClasse)
                bins = np.arange(0, dfFreq.max()+largClasse+1, largClasse)

                #array numpy 
                hist = np.histogram(dfFreq, bins)[0]
                
                #acumulando 
                cumsum = hist.cumsum()

                #criando o DF com a distribuição
                dfIdade= pd.DataFrame({#"Classe": (bins[1:] + bins[:-1]) / 2,
                                "Frequência": hist,
                                #"Frequência Acumulada": cumsum,
                                "Frequência Relativa (%)": (hist / cumsum[-1]) * 100},
                                #"Frequência Acumulada Realtiva": (cumsum / cumsum[-1]) * 100},
                        index=pd.Index([f"{bins[i]} ⊢ {bins[i+1]}" for i in range(hist.size)],name="class"))
        
    
                #tirando as sequências zeradas
                st.table(dfIdade[dfIdade["Frequência"] > 0])

                #adicionando mais um no contador
                count += 1

                #print usando markdown
                st.markdown("---")


        #print usando mardown
        st.markdown("**4 - Correlação Pearson**")
   
        #criando a correlação
        correlacao = dfBase.corr(method="pearson")
        
        #plot correlação
        fig = plt.figure(figsize=(8, 6))
        sns.heatmap(correlacao, annot=True)
        st.pyplot(fig, use_container_width=True)
        
        #print usando markdown
        st.markdown("---")
        
    
        #print usando markdown
        st.markdown("**5 - Rank Cursos por Quantidade de Alunos**")

                
        dfPlot = dfBase.groupby(["Curso", "Sexo"]).size().reset_index(name="Count")
        fig = px.bar(       dfPlot, 
                            x = "Count",
                            y="Curso", 
                            orientation='h' ,
                            color = "Sexo",
                            color_discrete_map={
                            "Feminino": "#DD4477",
                            "Masculino": "#316395"})
        fig.update_layout(yaxis={"categoryorder":"total ascending"})                            
        st.plotly_chart(fig, use_container_width=True)

        #print usando markdown
        st.markdown("---")
        
        #criando DF para ser usado nos gráficos abaixo
        dfPlot = dfBase.groupby("Curso")[["NotaGeral", "NotaConhGeral", "NotaConhEspecifico", "Idade"]].mean().reset_index()
        
        #contador para numerar as variáveis selecionadas 
        count = 6
        
        #for nas variáveis selecionadas para plotar os gráficos
        for coluna in  ["NotaGeral", "NotaConhGeral", "NotaConhEspecifico", "Idade"]:

                #não é a melhor opção, porém mais rápida. se fosse mais itens o certo seria criar uma tabela
                if coluna == "NotaGeral":
                        descricao = "Nota Geral"
                elif coluna == "NotaConhGeral":
                        descricao = "Nota Conhecimento Geral"
                elif coluna == "Idade":
                        descricao = coluna
                else:
                        descricao = "Nota Conhecimento Específico"

                #printando o título
                st.markdown(f"**{count} - Rank Cursos por {descricao}**")

                #plot gráfico
                fig = px.bar(           dfPlot, 
                                        x= coluna, 
                                        y="Curso", 
                                        orientation="h")
                fig.update_layout(yaxis={"categoryorder":"total ascending"})
                st.plotly_chart(fig, use_container_width=True)

                count += 1

                #print usando markdown
                st.markdown("---")

        #criando um df com a relação de colunas
        dfTabelaColuna = pd.DataFrame(dc.tabelaColuna)

        #contador para numerar as variáveis selecionadas 
        count = 1
        
        #for nas variáveis selecionadas para estudo
        for coluna in dfTabelaColuna["Coluna"].tolist():

                #recupera nome da coluna para utilização nos df"s
                descricao = dfTabelaColuna["Descricao"][dfTabelaColuna["Coluna"] == coluna].to_string(index = False)
                with st.expander("10." + str(count) + " - " + descricao, expanded=False):

                        #pulando linhas
                        st.text("")
                        st.text("")
                
                        #cria pivot table agrupado por sexo da variável
                        tabela =  pd.pivot_table(dfBase, index= coluna, columns="Sexo", values="NotaGeral", aggfunc= [len, np.mean], margins=True, margins_name="Geral")
                              
                        #criando join para deixar tudo apenas com uma linha de cabeçalho
                        tabela.columns = list(map("_".join, tabela.columns))
                              
                        #renomeando os cabeçalhos das colunas
                        tabela.rename(columns={ "len_Feminino"  : "Qtd. Feminino",
                                                "len_Masculino" : "Qtd. Masculino",
                                                "len_Geral"     : "Qtd. Total",
                                                "mean_Feminino" : "Nota Média Feminino",
                                                "mean_Masculino": "Nota Média Masculino",
                                                "mean_Geral"    : "Nota Média Geral"
                                                }, inplace=True)

                        #print título
                        st.write("10." + str(count) + ".1 - Tabela")                        
                        
                        #print df      
                        st.table(tabela)

                        #print título
                        st.write("10." + str(count) + ".2 - Gráfico Quantidade de Alunos Agrupado por Sexo")
                        
                        #plot gráfico de barras agrupado por sexo
                        dfPlot = dfBase.groupby([coluna,"Sexo"]).count().reset_index()
                        fig = px.bar(    dfPlot, 
                                        x=coluna, 
                                        y="Curso", 
                                        color = "Sexo",  
                                        labels={"Curso":"Quantidade de Alunos"},
                                        color_discrete_map={
                                        "Feminino": "#DD4477",
                                        "Masculino": "#316395"})
                        st.plotly_chart(fig, use_container_width=True)

                        #print título
                        st.write("10." + str(count) + ".3 - Gráfico Notas por Categoria e Sexo")
        
                        #plot boxplot notas por sexo
                        fig = px.box(dfBase, x=coluna, y="NotaGeral", title="", color="Sexo", color_discrete_map={"Feminino": "#DD4477","Masculino": "#316395"})
                        st.plotly_chart(fig, use_container_width=True)

                #incrementando
                count += 1