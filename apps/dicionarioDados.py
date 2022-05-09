#Campos que serão tratados

''' 
    CO_CATEGAD          -> Categoria administrativa da IES (TipoInstituicao)
    CO_GRUPO            -> Área de enquadramento do curso no Enade (Curso)
    CO_REGIAO_CURSO     -> Código da região de funcionamento do curso (Regiao)
    CO_TURNO_GRADUACAO  -> Código do turno de graduação (Turno)
    TP_SEXO             -> Sexo estudante (Sexo)
    QE_I01              -> Estado Civil (EstadoCivil)
    QE_I02              -> Cor ou raça (Raca)
    QE_I04              -> Até que etapa de escolarização seu pai concluiu? (EscolaridadePai)
    QE_I05              -> Até que etapa de escolarização sua mãe concluiu? (EscolaridadeMae)
    QE_I06              -> Onde e com quem você mora atualmente? (Moradia)
    QE_I08              -> Qual a renda total de sua família, incluindo seus rendimentos? (RendaFamiliar)
    QE_I09              -> Qual alternativa a seguir melhor descreve sua situação financeira (incluindo bolsas)? (SituacaoFinanceira)
    QE_I10              -> Qual alternativa a seguir melhor descreve sua situação de trabalho (exceto estágio ou bolsas)? (Emprego)
    QE_I11              -> Que tipo de bolsa de estudos ou financiamento do curso você recebeu para custear todas ou a maior parte das mensalidades? (BolsaEstudos)
    QE_I15              -> Seu ingresso no curso de graduação se deu por meio de políticas de ação afirmativa ou inclusão social? (InclusaoSocial)
    QE_I17              -> Em que tipo de escola você cursou o ensino médio? (EscolaEnsinoMedio)
    QE_I18              -> Qual modalidade de ensino médio você concluiu? (ModalidadeEnsinoMedio)
    QE_I19              -> Quem mais lhe incentivou a cursar a graduação? (IncentivoGraduacao)
    QE_I20              -> Algum dos grupos abaixo foi determinante para você enfrentar dificuldades durante seu curso superior e conclui-lo? (Dificuldade)
    QE_I23              -> Quantas horas por semana, aproximadamente, você dedicou aos estudos, excetuando as horas de aula? (DedicacaoEstudo)
    QE_I25              -> Qual o principal motivo para você ter escolhido este curso? (MotivoEscolha)

'''
#Criando os dicionários

#Categoria administrativa da IES
dct_CO_CATEGAD = {10001 : "Pública",  #=Pessoa Jurídica de Direito Público - Estadual
                  10002 : "Pública",  #=Pessoa Jurídica de Direito Público - Federal
                  10003 : "Pública",  #=Pessoa Jurídica de Direito Público - Municipal
                  10005 : "Privada",  #=Privada com fins lucrativos
                  10006 : "Privada",  #=Pessoa Jurídica de Direito Privado - Com fins lucrativos - Sociedade Mercantil ou Comercial
                  10007 : "Privada",  #=Pessoa Jurídica de Direito Privado - Sem fins lucrativos - Associação de Utilidade Pública
                  10008 : "Privada",  #=Privada sem fins lucrativos
                  10009 : "Privada",  #=Pessoa Jurídica de Direito Privado - Sem fins lucrativos - Sociedade
                  115   : "Pública",  #=Pessoa Jurídica de Direito Público - Estadual
                  116   : "Pública",  #=Pessoa Jurídica de Direito Público - Municipal
                  118   : "Privada",  #=Pessoa Jurídica de Direito Privado - Com fins lucrativos - Sociedade Civil
                  120   : "Privada",  #=Pessoa Jurídica de Direito Privado - Sem fins lucrativos - Associação de Utilidade Pública
                  121   : "Privada",  #=Pessoa Jurídica de Direito Privado - Sem fins lucrativos - Fundação
                  17634 : "Privada",  #=Fundação Pública de Direito Privado Municipal
                  895   : "Pública",  #=Administração pública em geral
                  93    : "Pública"}  #=Pessoa Jurídica de Direito Público - Federal                

#Área de enquadramento do curso no Enade
dict_CO_GRUPO = {5   : "MEDICINA VETERINÁRIA", 
                 6   : "ODONTOLOGIA", 
                12   : "MEDICINA", 
                17   : "AGRONOMIA",
                19   : "FARMÁCIA",
                21   : "ARQUITETURA E URBANISMO",
                23   : "ENFERMAGEM",
                27   : "FONOAUDIOLOGIA",
                28   : "NUTRIÇÃO",
                36   : "FISIOTERAPIA",
                51   : "ZOOTECNIA",
                55   : "BIOMEDICINA",
                69   : "TECNOLOGIA EM RADIOLOGIA",
                90   : "TECNOLOGIA EM AGRONEGÓCIOS",
                91   : "TECNOLOGIA EM GESTÃO HOSPITALAR",
                92   : "TECNOLOGIA EM GESTÃO AMBIENTAL",
                95   : "TECNOLOGIA EM ESTÉTICA E COSMÉTICA",
                3501 : "EDUCAÇÃO FÍSICA (BACHARELADO)",
                4003 : "ENGENHARIA DA COMPUTAÇÃO",
                5710 : "ENGENHARIA CIVIL",
                5806 : "ENGENHARIA ELÉTRICA",
                5814 : "ENGENHARIA DE CONTROLE E AUTOMAÇÃO",
                5902 : "ENGENHARIA MECÂNICA",
                6002 : "ENGENHARIA DE ALIMENTOS",
                6008 : "ENGENHARIA QUÍMICA",
                6208 : "ENGENHARIA DE PRODUÇÃO",
                6307 : "ENGENHARIA AMBIENTAL",
                6405 : "ENGENHARIA FLORESTAL",
                6410 : "TECNOLOGIA EM SEGURANÇA NO TRABALHO"}                    

#Código da região de funcionamento do curso
dct_CO_REGIAO_CURSO = {1 : "Região Norte (NO)",
                       2 : "Região Nordeste (NE)",
                       3 : "Região Sudeste (SE)",
                       4 : "Região Sul (SUL)",
                       5 : "Região Centro-Oeste (CO)"}

#Código do turno de graduação
dct_CO_TURNO_GRADUACAO =  {1 : "Matutino",
                           2 : "Vespertino",
                           3 : "Integral",
                           4 : "Noturno"}

#Sexo
dct_TP_SEXO = {"F" : "Feminino", 
               "M" : "Masculino"}
#Estado Civil
dct_QE_I01 = {"A": "Solteiro(a)", 
              "B": "Casado(a)",
              "C": "Separado(a) judicialmente/divorciado(a)", 
              "D": "Viúvo(a)", 
              "E": "Outro"}

#Cor ou Raça
dct_QE_I02 = {"A" : "Branca", 
              "B" : "Preta", 
              "C" : "Amarela", 
              "D" : "Parda", 
              "E" : "Indígena", 
              "F" : "Não declarado"}

#Até que etapa de escolarização seu pai concluiu?
dct_QE_I04 = {"A" : "Nenhuma",
              "B" : "Ensino Fundamental I",
              "C" : "Ensino Fundamental II",
              "D" : "Ensino Médio",
              "E" : "Ensino Superior",
              "F" : "Pós-graduação"}

#Até que etapa de escolarização sua mãe concluiu?
dct_QE_I05 = {"A" : "Nenhuma",
              "B" : "Ensino Fundamental I",
              "C" : "Ensino Fundamental II",
              "D" : "Ensino Médio",
              "E" : "Ensino Superior",
              "F" : "Pós-graduação"}

#Onde e com quem você mora atualmente?
dct_QE_I06 = {"A" : "Sozinho",                  #Em casa ou apartamento, sozinho"
              "B" : "Pais ou Parentes",         #Em casa ou apartamento, com pais e/ou parentes.
              "C" : "Cônjuge e/ou Filhos",      #Em casa ou apartamento, com cônjuge e/ou filhos.
              "D" : "Outras Pessoas",           #Em casa ou apartamento, com outras pessoas (incluindo república).
              "E" : "Alojamento Universitário", #Em alojamento universitário da própria instituição.
              "F" : "Outros"}                   #Em outros tipos de habitação individual ou coletiva (hotel, hospedaria, pensão ou outro).

#Qual a renda total de sua família, incluindo seus rendimentos?
dct_QE_I08 =   {"A" : "Até 1,5 Sal. Min.",              #Até 1,5 salário mínimo (até R$ 1.431,00).
                "B" : "De 1,5 a 3 Sal. Min.",           #De 1,5 a 3 salários mínimos (R$ 1.431,01 a R$ 2.862,00).
                "C" : "De 3 a 4,5 Sal. Min." ,          #De 3 a 4,5 salários mínimos (R$ 2.862,01 a R$ 4.293,00).
                "D" : "De 4,5 a 6 Sal. Min.",           #De 4,5 a 6 salários mínimos (R$ 4.293,01 a R$ 5.724,00).
                "E" : "De 6 a 10 Sal. Min.",            #De 6 a 10 salários mínimos (R$ 5.724,01 a R$ 9.540,00).
                "F" : "De 10 a 30 Sal. Min.",           #De 10 a 30 salários mínimos (R$ 9.540,01 a R$ 28.620,00).
                "G" : "Acima de 30 Sal. Min."}          #Acima de 30 salários mínimos (mais de R$ 28.620,00).

#Qual alternativa a seguir melhor descreve sua situação financeira (incluindo bolsas)?
dct_QE_I09 = {  "A" : "Não tenho renda e meus gastos são financiados por programas governamentais",
                "B" : "Não tenho renda e meus gastos são financiados pela minha família ou por outras pessoas",
                "C" : "Tenho renda, mas recebo ajuda da família ou de outras pessoas para financiar meus gastos",
                "D" : "Tenho renda e não preciso de ajuda para financiar meus gastos",
                "E" : "Tenho renda e contribuo com o sustento da família",
                "F" : "Sou o principal responsável pelo sustento da família"}


#Qual alternativa a seguir melhor descreve sua situação de trabalho (exceto estágio ou bolsas)?
dct_QE_I10 = {  "A" : "Não estou trabalhando",
                "B" : "Trabalho eventualmente",
                "C" : "Trabalho até 20 horas semanais",
                "D" : "Trabalho de 21 a 39 horas semanais",
                "E" : "Trabalho 40 horas semanais ou mais"}


#Que tipo de bolsa de estudos ou financiamento do curso você recebeu para custear todas ou a maior parte das mensalidades? 
dct_QE_I11 = {  "A" : "Nenhum, pois meu curso é gratuito",
                "B" : "Nenhum, embora meu curso não seja gratuito",
                "C" : "ProUni integral",
                "D" : "ProUni parcial, apenas",
                "E" : "FIES, apenas",
                "F" : "ProUni Parcial e FIES",
                "G" : "Bolsa oferecida por governo estadual, distrital ou municipal",
                "H" : "Bolsa oferecida pela própria instituição",
                "I" : "Bolsa oferecida por outra entidade (empresa, ONG, outra)",
                "J" : "Financiamento oferecido pela própria instituição",
                "K" : "Financiamento bancário"}

#Seu ingresso no curso de graduação se deu por meio de políticas de ação afirmativa ou inclusão social?
dct_QE_I15 = {  "A" : "Não",
                "B" : "Sim, por critério étnico-racial",
                "C" : "Sim, por critério de renda",
                "D" : "Sim, por ter estudado em escola pública ou particular com bolsa de estudos",
                "E" : "Sim, por sistema que combina dois ou mais critérios anteriores",
                "F" : "Sim, por sistema diferente dos anteriores"}

#Em que tipo de escola você cursou o ensino médio?
dct_QE_I17 = {  "A" : "Todo em escola pública",
                "B" : "Todo em escola privada (particular)",
                "C" : "Todo no exterior",
                "D" : "A maior parte em escola pública",
                "E" : "A maior parte em escola privada (particular)",
                "F" : "Parte no Brasil e parte no exterior"}


#Qual modalidade de ensino médio você concluiu?
dct_QE_I18 = {  "A" : "Ensino médio tradicional",
                "B" : "Profissionalizante técnico",
                "C" : "Profissionalizante magistério",
                "D" : "Educação de Jovens e Adultos (EJA) e/ou Supletivo",
                "E" : "Outro modalidade"}

#Quem mais lhe incentivou a cursar a graduação?
dct_QE_I19 = {  "A" : "Ninguém",
                "B" : "Pais",
                "C" : "Outros membros da família que não os pais",
                "D" : "Professores",
                "E" : "Líder ou representante religioso",
                "F" : "Colegas/Amigos",
                "G" : "Outras pessoas"}


#Algum dos grupos abaixo foi determinante para você enfrentar dificuldades durante seu curso superior e conclui-lo?
dct_QE_I20 = {  "A" : "Não tive dificuldade",
                "B" : "Não recebi apoio para enfrentar dificuldades",
                "C" : "Pais",
                "D" : "Avós",
                "E" : "Irmãos, primos ou tios",
                "F" : "Líder ou representante religioso",
                "G" : "Colegas de curso ou amigos",
                "H" : "Professores do curso",
                "I" : "Profissionais do serviço de apoio ao estudante da IES",
                "J" : "Colegas de trabalho",
                "K" : "Outro grupo"}
   
#Quantas horas por semana, aproximadamente, você dedicou aos estudos, excetuando as horas de aula?
dct_QE_I23 = {"A" : "Nenhuma, apenas assisto às aulas", 
              "B" : "De uma a três",
              "C" : "De quatro a sete", 
              "D" : "De oito a doze", 
              "E" : "Mais de doze"}

#Qual o principal motivo para você ter escolhido este curso?
dct_QE_I25 = {  "A" : "Inserção no mercado de trabalho",
                "B" : "Influência familiar",
                "C" : "Valorização profissional",
                "D" : "Prestígio Social",
                "E" : "Vocação",
                "F" : "Oferecido na modalidade a distância",
                "G" : "Baixa concorrência para ingresso",
                "H" : "Outro motivo"}
