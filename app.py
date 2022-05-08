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

        Realizar análise descritiva na base de micro dados do ENADE.


        **Observações:**

        Foi utilizada a **base de dados completa do ENAD 2019**.


        **Colunas Utilizadas:**


        **Download Documentos:**


    """
elif  escolha == "Tratamento Base Dados":
    apps.tratamentoBase.tratamentoBase()

elif  escolha == "Análise Exploratória":
    apps.edaFiles.edaFiles()

elif  escolha == "Análise por Curso":
    apps.analiseCurso.analiseCurso()

elif  escolha == "Análise por Curso":
    apps.analiseGeral.analiseGeral()

    