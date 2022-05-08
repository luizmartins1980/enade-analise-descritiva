import zipfile
import streamlit as st
import pandas as pd
import numpy as np
import math
import apps.descricaoColunas as dc
import plotly.express as px
import plotly.figure_factory as ff
from scipy.stats import skew, kurtosis

def analiseGeral():
    
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

    

