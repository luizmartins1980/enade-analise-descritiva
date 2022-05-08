import zipfile
import streamlit as st
import pandas as pd
import numpy as np
import math
import apps.descricaoColunas as dc
import plotly.express as px
import plotly.figure_factory as ff
from scipy.stats import skew, kurtosis

def analiseCurso():
    
      #print usando markdown
      st.markdown("# **Análise Descritiva por Curso**")
      
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

      
      #criando select box com os cursos da base
      cursoEscolhido = st.selectbox("Selecione um Curso (*):",["--- Selecione um Curso ---"] + sorted(dfBase["Curso"].unique().tolist()))
      
      #print usando markdown
      st.markdown("---")

      #criando um df com a relação de colunas
      dfTabelaColuna = pd.DataFrame(dc.tabelaColuna)

      #pegando os valores da descrição e ordernando
      listaVariaveis = sorted(dfTabelaColuna["Descricao"])
      
      #criando container ("gato" para carregar todas as variáveis)
      container = st.container()

      #criando checkbox para selecionar todas as variáveis
      todas = st.checkbox("Selecionar Todas")
      
      #print usando markdown
      st.markdown("---")
      
      #print usando text
      st.text("Opções para as variáveis:")      

      #criando colunas para os chekcboxes das opções
      col1, col2 = st.columns(2)

      #coluna 1 opção para plotar gráfico para a variável escolhida
      with col1:
            grafico = st.checkbox("Mostrar Gráficos")
      
      #coluna 2 opção para agrupar por sexo
      with col2:
            sexo = st.checkbox("Agrupar por Sexo")

      #print usando markdown
      st.markdown("---")
 
      #verificando a opção do user... todas ou não
      if todas:
            selecionados = container.multiselect("Selecione uma ou Mais Variáveis para Estudo: (*)", listaVariaveis, listaVariaveis)
      else:
            selecionados =  container.multiselect("Selecione uma ou Mais Variáveis para Estudo: (*)", listaVariaveis)

      #prosseguir com um curso escolhido e pelo menos uma variável
      if cursoEscolhido != "--- Selecione um Curso ---" and len(selecionados) > 0 :
            
            #filtrando o curso
            dfBase = dfBase[dfBase["Curso"] == cursoEscolhido]

            #variáveis para utilizar no card
            totRow  = dfBase.shape[0]
            totFem  = dfBase[dfBase["Sexo"] == "Feminino"].shape[0]
            totMasc = dfBase[dfBase["Sexo"] == "Masculino"].shape[0]

            #criando "cards" com algumas informações relevantes
            st.markdown("**1 - Quantidade, Idade e Nota Geral**")
            
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
            
            #print usando markdown
            st.markdown("**2 - Describe do Curso Selecionado**")
            
            #show describe
            st.table(dfBase.describe())

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


            #Mostrando o head (cinco primeiras linhas)
            st.markdown("**5 - Head da Base**")
            st.dataframe(dfBase.head())

            #print usando markdown
            st.markdown("---")

            #Mostrando o tail (cinco últimas linhas)
            st.markdown("**6 - Tail da Base**")
            st.dataframe(dfBase.tail())

            #print usando markdown
            st.markdown("---")

            #print usando markdown
            st.markdown("**7 - Histograma e Análise da Nota Geral**")
            
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

            #print usando markdown
            st.markdown("**8 - Variáveis Selecionadas**")

            #contador para numerar as variáveis selecionadas 
            count = 1
            
            #for nas variáveis selecionadas para estudo
            for descricao in selecionados:

                  #recupera nome da coluna para utilização nos df"s
                  coluna = dfTabelaColuna["Coluna"][dfTabelaColuna["Descricao"] == descricao].to_string(index = False)

                  #criando o expnader para a variável
                  with st.expander("8." + str(count) + " - " + descricao, expanded=False):

                        #pulando linhas
                        st.text("")
                        st.text("")

                        #verifica agrupamento por sexo
                        if sexo:
                              
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

                        else:
                              
                              #cria pivot table agrupado por sexo da variável
                              tabela =  pd.pivot_table(dfBase, index= coluna, values="NotaGeral", aggfunc= [len, np.mean], margins=True, margins_name="Geral")
                              
                              #criando join para deixar tudo apenas com uma linha de cabeçalho
                              tabela.columns = list(map("_".join, tabela.columns))

                              #adicionando % por opção 
                              tabela["%"] = (tabela["len_NotaGeral"]/dfBase.shape[0]) * 100

                              #reorganizando as colunas  do df
                              tabela = tabela[["len_NotaGeral","%","mean_NotaGeral"]]
                              
                              #renomeando os cabeçalhos das colunas
                              tabela.rename(columns={ 
                                                      "len_NotaGeral"     : "Qtd. Total",
                                                      "mean_NotaGeral"    : "Nota Média Geral"
                                                    }, inplace=True)
                        
                        #print título
                        st.write("8." + str(count) + ".1 - Tabela")                        
                        
                        #print df      
                        st.table(tabela)
                        
                        #plot gráficos quando seleicionado
                        if grafico:
                              
                              #plot agrupamento por sexo
                              if sexo:

                                    #print título
                                    st.write("8." + str(count) + ".2 - Gráfico Quantidade de Alunos Agrupado por Sexo")
                                    
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
                                    st.write("8." + str(count) + ".3 - Gráfico Notas por Categoria e Sexo")
                        
                                    #plot boxplot notas por sexo
                                    fig = px.box(dfBase, x=coluna, y="NotaGeral", title="", color="Sexo", color_discrete_map={"Feminino": "#DD4477","Masculino": "#316395"})
                                    st.plotly_chart(fig, use_container_width=True)
                                    
                              else:

                                    #print título
                                    st.write("8." + str(count) + ".2 - Gráfico Quantidade de Alunos")

                                    #plot gráfico de barras geral      
                                    dfPlot = dfBase.groupby([coluna]).count().reset_index()
                                    fig = px.bar(    dfPlot, 
                                                      x=coluna, 
                                                      y="Curso", 
                                                      labels={"Curso":"Quantidade de Alunos"})
                                    st.plotly_chart(fig, use_container_width=True)

                                    #print título
                                    st.write("8." + str(count) + ".3 - Gráfico Notas por Categoria")
                                    
                                    #plot bloxplot notas geral
                                    fig = px.box(dfBase, x=coluna, y="NotaGeral", title="", color=coluna)
                                    st.plotly_chart(fig, use_container_width=True)
                  
                  #somando 1 no contador
                  count += 1
            
            
            



    












    