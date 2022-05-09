import zipfile
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components
import codecs
import sweetviz as sv
import webbrowser

def edaFiles():


    st.title("Gerando Relatórios de Análise Exploratória de Dados Usando Bibliotecas")
    
    texto = """
            
            A análise exploratória de dados (EDA) é usada por cientistas de dados para analisar e investigar conjuntos de dados
            e resumir suas principais características, muitas vezes usando métodos de visualização de dados. Ela permite determinar 
            a melhor forma de controlar as fontes de dados para obter as respostas que você precisa, tornando mais fácil para os 
            cientistas de dados descobrir padrões, detectar anomalias, testar uma hipótese ou verificar suposições. (Trecho retirado do link:
            https://www.ibm.com/br-pt/cloud/learn/exploratory-data-analysis)

            \n\n
            Para a EDA, utilizei as bibliotecas Pandas Profiling e Sweetviz, que as principais bibliotecas para Python. 

            \n\n
            Saiba mais em:

            **Pandas Profiling** - https://pandas-profiling.ydata.ai/docs/master/index.html

            **Sweetviz** - https://pypi.org/project/sweetviz/

            \n\n
            Selecione abaixo qual relatório que você deseja visualizar.
            
            """
    
    st.markdown(texto)

    relatorio = st.selectbox('',('Selecione um Relatório' , '1 - Pandas Profiling' , '2 - Sweetviz'))

    #devido à base ser muito grande a geração das análises exloratórias, levam muito tempo e muitas vezes dando timeout no share streamlit
    #com isso, criei os relatórios localmente, visto que, a base é estática.
    # para gerar em seu local descomente as linhas abaixo. 
    
    """if  relatorio[0:1] == '1':

        with st.spinner('Por favor, aguarde a geração. Este processo poderá ser demorado.'):
        
            #Lendo a base

            with zipfile.ZipFile("./data/BaseTratada.zip") as zip:
                with zip.open("BaseTratada.csv") as arq:
                    df = pd.read_csv(arq,delimiter=";", decimal=",",  encoding="ISO-8859-1")
             
            #trocando tipo        
            df = df.astype({"NotaGeral"         :"float64", 
                            "NotaConhGeral"     :"float64", 
                            "NotaConhEspecifico":"float64"})

            #Passando argumentos para a função (utlizando cache) de geração do relatório
            pr = gen_profile_report(df, title= "Relatório Pandas Profiling",explorative=True)

            #print
            st_profile_report(pr)
    

    if  relatorio[0:1] == '2':

        with st.spinner('Por favor, aguarde a geração. Este processo poderá ser demorado.'):
        
            #Lendo a base
            with zipfile.ZipFile("./data/BaseTratada.zip") as zip:
                with zip.open("BaseTratada.csv") as arq:
                    df = pd.read_csv(arq,delimiter=";", decimal=",",  encoding="ISO-8859-1")

            df = df.astype({"NotaGeral"         :"float64", 
                            "NotaConhGeral"     :"float64", 
                            "NotaConhEspecifico":"float64"})

            #Passando argumentos para a função (utlizando cache) de geração do relatório
            pr = gen_sweet_report(df)

            #print
            pr.show_html(filepath='./SWEETVIZ_REPORT.html', open_browser=True, layout='vertical', scale=1.0)
           

#Optimizando a perfomance com cache e criando a função para o profile report
@st.cache(allow_output_mutation=True)
def gen_profile_report(df, *report_args, **report_kwargs):
    return df.profile_report(*report_args, **report_kwargs)

#Optimizando a perfomance com cache e criando a função para o analyser
@st.cache(allow_output_mutation=True)
def gen_sweet_report(df):
    return sv.analyze(df)"""

    if  relatorio[0:1] == '1':

           webbrowser.open_new_tab("https://htmlpreview.github.io/?https://github.com/luizmartins1980/enade-analise-descritiva/blob/main/reports/profilingReport.html")

    elif  relatorio[0:1] == '2':

           webbrowser.open_new_tab("https://htmlpreview.github.io/?https://github.com/luizmartins1980/enade-analise-descritiva/blob/main/reports/SWEETVIZ_REPORT.html")           