import streamlit as st
from streamlit_option_menu import option_menu
import apps.tratamentoBase
import apps.edaFiles
import apps.analiseCurso
import apps.analiseGeral


#criando menu utilizando o streamlit_option_menu
with st.sidebar:
    escolha = option_menu("Menu", 
                        
                        ["Home", 
                        "Tratamento Base Dados", 
                        "Análise Exploratória", 
                        "Análise Geral",
                        "Análise por Curso"],

                         icons=["house", "server", "file-bar-graph", "bar-chart", "bar-chart"], #https://icons.getbootstrap.com/
                         
                         menu_icon="menu-button-wide", 
                         
                         default_index=0,
                         
                         styles={
                                    "container": {"padding": "5!important", "background-color": "#E1117"},
                                    "icon": {"color": "#FF4B4B", "font-size": "25px"}, 
                                    
                                    "nav-link": {"font-size": "12px", "color":"#FFFFFF", "text-align": "left", "margin":"0px", "--hover-color": "#262730", "icon" : "#FF4B4B"},
                                    "nav-link-selected": {"background-color": "#262730"},
                                }
                        )

#mostrando a página selecionada
if escolha == "Home":
    """
        # Trabalho Final Estatística Descritiva e Criação de Dashboards

        **Curso:** MBA em Data Science e Statistics com Python

        **Professor:** Thiago Marques
       
        **Aluno:** Luiz Leonardo Martins


        **Objetivos do trabalho:**

        Realizar análise descritiva da base de micro dados do ENADE.


        **Observações:**

        Foi utilizada a **base de dados completa do ENAD 2019**. São 25 cursos e foram selecionas 25 colunas com 371.049 linhas/alunos, após tratamento. 
        A base original possui 433.930 linhas/alunos e 137 colunas. Para um efeito didático, foram retiradas todas as linhas que possuia valor *nan*. 
        
        **Download Documentos:**

        Caso você queira baixar os documentos utilizados neste trabalho, segue abaixo a listagem:

        1. Código fonte [Acessar](https://github.com/luizmartins1980/enade-analise-descritiva)

        1. Documentos ENADE (Questinário Aluno, Dicionário Variáveis e Manual do Usuário) [Download](https://drive.google.com/drive/folders/1XPQJ4sjBeO_3liT5O3n_3SnpR4Ach38y?usp=sharing)
       
        2. Base Original  [Download](https://drive.google.com/file/d/1XJXa4j_SP19q4K7fxFOEf1riIa43teKU/view?usp=sharing)

        3. Base Tratada Utilizada (CSV) [Download](https://drive.google.com/file/d/1KFDhJ36AsP4t1VSwFgqyVokZpsiEfoCo/view?usp=sharing)
        
        4. Base Tratada (XLSX)  [Download](https://drive.google.com/file/d/1VUts9NjOUr5CXHheg_9GeR_Y4oJyStrF/view?usp=sharing)



    """
elif  escolha == "Tratamento Base Dados":
    apps.tratamentoBase.tratamentoBase()

elif  escolha == "Análise Exploratória":
    apps.edaFiles.edaFiles()

elif  escolha == "Análise por Curso":
    apps.analiseCurso.analiseCurso()

elif  escolha == "Análise Geral":
    apps.analiseGeral.analiseGeral()

    