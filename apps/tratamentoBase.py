import streamlit as st
import pandas as pd
import numpy as np
import apps.dicionarioDados as dd
import zipfile


def tratamentoBase():
    
    #Título
    st.markdown("# **Tratamento da Base de Dados**")
    
    #importando base
    with zipfile.ZipFile("./data/microdados_enade_2019.zip") as zip:
        with zip.open("microdados_enade_2019.csv") as arq:
            dfPrincipal = pd.read_csv(arq,delimiter=";", decimal=",")

    
    #análise base de dados
    intLinhas = dfPrincipal.shape[0]
    intColunas = dfPrincipal.shape[1]

    
    #colunas necessárias para a análise (liberando espaço)
    lstColunasFinais = ["CO_CATEGAD",
                        "CO_GRUPO",
                        "CO_REGIAO_CURSO",
                        "NU_IDADE",
                        "TP_SEXO",
                        "CO_TURNO_GRADUACAO",
                        "NT_GER",
                        "NT_OBJ_FG",
                        "NT_OBJ_CE",
                        "QE_I01",
                        "QE_I02",
                        "QE_I04",
                        "QE_I05",
                        "QE_I06",
                        "QE_I08",
                        "QE_I09",
                        "QE_I10",
                        "QE_I11",
                        "QE_I15",
                        "QE_I17",
                        "QE_I18",
                        "QE_I19",
                        "QE_I20",
                        "QE_I23",
                        "QE_I25"]

    #dropando colunas desnecessárias
    dfPrincipal = dfPrincipal[dfPrincipal.columns.intersection(lstColunasFinais)]


    #eliminando espaços vazios (ATENÇÃO AO USAR ESTE COMANDO - No caso desta BASE podemos fazer uma troca geral sem especificar as colunas)
    dfPrincipal = dfPrincipal.replace(r"^\s*$", np.nan, regex=True)
    

    #Dropando NaN
    dfPrincipal = dfPrincipal.dropna()

   
    #Forçando a troca de decimal (ATENÇÃO AO USAR ESTE COMANDO - No caso desta BASE podemos fazer uma troca geral sem especificar as colunas)
    dfPrincipal = dfPrincipal.replace({",": "."}, regex=True)

    #Modificando Tipo de Dados                                
    dfPrincipal = dfPrincipal.astype({"NT_GER"   :"float64", 
                                      "NT_OBJ_FG":"float64", 
                                      "NT_OBJ_CE":"float64"})

    #Implementando os dicionários criados

    dfPrincipal["CO_CATEGAD"]         = dfPrincipal["CO_CATEGAD"].apply(lambda x: dd.dct_CO_CATEGAD[x])
    dfPrincipal["CO_GRUPO"]           = dfPrincipal["CO_GRUPO"].apply(lambda x: dd.dict_CO_GRUPO[x])
    dfPrincipal["CO_REGIAO_CURSO"]    = dfPrincipal["CO_REGIAO_CURSO"].apply(lambda x: dd.dct_CO_REGIAO_CURSO[x])
    dfPrincipal["CO_TURNO_GRADUACAO"] = dfPrincipal["CO_TURNO_GRADUACAO"].apply(lambda x: dd.dct_CO_TURNO_GRADUACAO[x])
    dfPrincipal["TP_SEXO"]            = dfPrincipal["TP_SEXO"].apply(lambda x: dd.dct_TP_SEXO[x])    
    

    dfPrincipal["QE_I01"] = dfPrincipal["QE_I01"].apply(lambda x: dd.dct_QE_I01[x])
    dfPrincipal["QE_I02"] = dfPrincipal["QE_I02"].apply(lambda x: dd.dct_QE_I02[x])
    dfPrincipal["QE_I04"] = dfPrincipal["QE_I04"].apply(lambda x: dd.dct_QE_I04[x])
    dfPrincipal["QE_I05"] = dfPrincipal["QE_I05"].apply(lambda x: dd.dct_QE_I05[x])
    dfPrincipal["QE_I06"] = dfPrincipal["QE_I06"].apply(lambda x: dd.dct_QE_I06[x])
    dfPrincipal["QE_I08"] = dfPrincipal["QE_I08"].apply(lambda x: dd.dct_QE_I08[x])
    dfPrincipal["QE_I09"] = dfPrincipal["QE_I09"].apply(lambda x: dd.dct_QE_I09[x])
    dfPrincipal["QE_I10"] = dfPrincipal["QE_I10"].apply(lambda x: dd.dct_QE_I10[x])                    
    dfPrincipal["QE_I11"] = dfPrincipal["QE_I11"].apply(lambda x: dd.dct_QE_I11[x])
    dfPrincipal["QE_I15"] = dfPrincipal["QE_I15"].apply(lambda x: dd.dct_QE_I15[x])
    dfPrincipal["QE_I17"] = dfPrincipal["QE_I17"].apply(lambda x: dd.dct_QE_I17[x])
    dfPrincipal["QE_I18"] = dfPrincipal["QE_I18"].apply(lambda x: dd.dct_QE_I18[x])
    dfPrincipal["QE_I19"] = dfPrincipal["QE_I19"].apply(lambda x: dd.dct_QE_I19[x])
    dfPrincipal["QE_I20"] = dfPrincipal["QE_I20"].apply(lambda x: dd.dct_QE_I20[x])            
    dfPrincipal["QE_I23"] = dfPrincipal["QE_I23"].apply(lambda x: dd.dct_QE_I23[x])            
    dfPrincipal["QE_I25"] = dfPrincipal["QE_I25"].apply(lambda x: dd.dct_QE_I25[x])                


    #Renomeando Colunas
    dfPrincipal.rename(columns={"CO_CATEGAD" : "TipoInstituicao",
                                "CO_GRUPO" : "Curso",
                                "CO_REGIAO_CURSO" : "Regiao",
                                "NU_IDADE" : "Idade",
                                "TP_SEXO" : "Sexo",
                                "CO_TURNO_GRADUACAO" : "Turno",
                                "NT_GER" : "NotaGeral",
                                "NT_OBJ_FG" : "NotaConhGeral",
                                "NT_OBJ_CE" : "NotaConhEspecifico",
                                "QE_I01" : "EstadoCivil",
                                "QE_I02" : "Raca",
                                "QE_I04" : "EscolaridadePai",
                                "QE_I05" : "EscolaridadeMae",
                                "QE_I06" : "Moradia",
                                "QE_I08" : "RendaFamiliar",
                                "QE_I09" : "SituacaoFinanceira",
                                "QE_I10" : "Emprego",
                                "QE_I11" : "BolsaEstudos",
                                "QE_I15" : "InclusaoSocial",
                                "QE_I17" : "EscolaEnsinoMedio",
                                "QE_I18" : "ModalidadeEnsinoMedio",
                                "QE_I19" : "IncentivoGraduacao",
                                "QE_I20" : "Dificuldade",
                                "QE_I23" : "HoraEstudo",
                                "QE_I25" : "MotivoEscolha",
                                }, inplace = True)


    #criando df para mostrar infos
    st.markdown("### **1 - Tratamento da Base de Dados**")
    st.text("")
    st.text("")
    
    
    st.markdown("**1.1 - Dados Originais da Base**")
    st.dataframe(pd.DataFrame([[intLinhas, intColunas]], columns =["Qtd. Linhas","Qtd. Colunas"])   )
    st.text("")
    
    st.markdown("**1.2 - Dados Tratados da Base**")
    st.dataframe(pd.DataFrame([[(intColunas - dfPrincipal.shape[1]), (intLinhas - dfPrincipal.shape[0])]], columns =["Qtd. Colunas Excluídas","Qtd. Linhas NaN Excluídas"])   )
    st.text("")
   
    st.markdown("**1.3 - Dados Após Tratamento da Base**")
    st.dataframe(pd.DataFrame([[dfPrincipal.shape[1], dfPrincipal.shape[0]]], columns =["Qtd. Colunas","Qtd. Linhas"]))
 
    st.text("")
    st.text("")

    st.markdown("*Para saber mais informações acercas das colunas ulizadas, verifique a página Home.*")
    
    #Mostrando colunas e tipos de dados após tratamento
    st.markdown("**Colunas e Tipo de Dados Após Tratamento**")
    dt = {'Colunas': dfPrincipal.columns.values,
          'Tipo'   : dfPrincipal.dtypes.astype(str).tolist()}
    st.table(dt)


    st.text("")
    st.text("")

    with st.expander("Download Bases", False):

        col1, col2, col3 = st.columns(3)
            
        with col1:
            st.write("Base Original  [Download](https://drive.google.com/file/d/1XJXa4j_SP19q4K7fxFOEf1riIa43teKU/view?usp=sharing)")

        with col2:
            st.write("Base Tratada (CSV) [Download](https://drive.google.com/file/d/1KFDhJ36AsP4t1VSwFgqyVokZpsiEfoCo/view?usp=sharing)")

        with col3:
            st.write("Base Original (XLSX)  [Download](https://drive.google.com/file/d/1VUts9NjOUr5CXHheg_9GeR_Y4oJyStrF/view?usp=sharing)")
    
    
    #exportando para o csv - descomente a linha abaixo caso queira exportar
    #dfPrincipal.to_csv("BaseTratada.csv", sep=";", index=False, encoding="iso-8859-1")
    
    #exportando para o xlsx - descomente a linha abaixo caso queira exportar
    #dfPrincipal.to_excel("baseTratada_2.xlsx", index=False, encoding= "iso-8859-1")
 

