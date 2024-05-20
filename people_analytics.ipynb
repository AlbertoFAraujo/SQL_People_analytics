{
    "metadata": {
        "kernelspec": {
            "name": "SQL",
            "display_name": "SQL",
            "language": "sql"
        },
        "language_info": {
            "name": "sql",
            "version": ""
        }
    },
    "nbformat_minor": 2,
    "nbformat": 4,
    "cells": [
        {
            "cell_type": "markdown",
            "source": [
                "# Exploração de dados People Analytics\n",
                "\n",
                "Trata-se de uma base de dados de RH com dados de funcionários ativos e inativos, contemplando informações de <span style=\"color: var(--vscode-foreground);\">Nome, Gênero, Data_Nascimento, Idade, Nível, Escolaridade, Área, Salário, Data_Admissão, Data_Demissão, Contrato, Motivo_Demissão, PCD, tipos de benefícios e status atual. O objetivo desta exploração de dados é responder algumas perguntas de negócios para posteriormente criar um painel de visualização com as métricas estratégicas para tomada de decisão do gestor da área, facilitando a compreensão e análise dos indicadores de forma visual, atrativa e eficiente. As seguintes perguntas de negócios são questionadas:</span>\n",
                "\n",
                "1.  <span style=\"font-size: 14px;\">&nbsp;Total de funcionários na empresa ao longo do tempo, ativos e inativos;</span>\n",
                "2. Total de funcionários por genero;\n",
                "3. Frequência de funcionários por idade;\n",
                "4. Distribuição de funcionários por nível hierárquico;\n",
                "5.  Distribuição de funcionários por Escolaridade;\n",
                "6. Distribuição de funcionários por Área da empresa;\n",
                "7. Salário médio por nível hierárquico;\n",
                "8. Despesa total em salários?;\n",
                "9. Quanto é gasto em valor de benefício \"Combustível\"?;\n",
                "10. Qual a média salarial por escolaridade;\n",
                "11. Qual mês obteve o maior percentual de admissões em relação ao anterior?;\n",
                "12. Qual mês obteve o maior percentual de demissões em relação ao anterior?;\n",
                "13. Total de funcionários por tipo de contrato;\n",
                "14. Área vs tipo de contrato e percentual em relação ao total da área;\n",
                "15. Área vs tipo de contrato e percentual em relação ao total da área;\n",
                "16. Total de funcionários afastados ou de férias.\n",
                "\n",
                "<span style=\"color: var(--vscode-foreground);\">Embora o Azure Data Studio gere automaticamente gráficos nos outputs, a ideia desta exploração é apenas responder as questões mencionadas.</span>\n",
                "\n",
                "<span style=\"color: var(--vscode-foreground);\"><b>Obs:</b> Os dados foram gerados de forma sintética com o&nbsp;</span>  <span style=\"font-size: 14px;\"><a href=\"https://www.mockaroo.com/\" data-href=\"https://www.mockaroo.com/\" title=\"https://www.mockaroo.com/\" is-markdown=\"true\" is-absolute=\"false\">https://www.mockaroo.com/</a></span>"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "865ef5ff-a7a2-409a-b826-833b6de4fd72"
            },
            "attachments": {}
        },
        {
            "cell_type": "code",
            "source": [
                "-- Visualizando a base de dados\r\n",
                "SELECT TOP(10) * FROM baseRH"
            ],
            "metadata": {
                "azdata_cell_guid": "f5c4f762-ff98-4a15-8a6a-37a83d09cc49",
                "language": "sql",
                "tags": []
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(10 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.008"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 2,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Nome"
                                    },
                                    {
                                        "name": "Gênero"
                                    },
                                    {
                                        "name": "Data_Nascimento"
                                    },
                                    {
                                        "name": "Idade"
                                    },
                                    {
                                        "name": "Nível"
                                    },
                                    {
                                        "name": "Escolaridade"
                                    },
                                    {
                                        "name": "Área"
                                    },
                                    {
                                        "name": "Salário"
                                    },
                                    {
                                        "name": "Data_Admissão"
                                    },
                                    {
                                        "name": "Data_Demissão"
                                    },
                                    {
                                        "name": "Contrato"
                                    },
                                    {
                                        "name": "Motivo_Demissão"
                                    },
                                    {
                                        "name": "PCD"
                                    },
                                    {
                                        "name": "Alimentação"
                                    },
                                    {
                                        "name": "Saúde"
                                    },
                                    {
                                        "name": "Odont"
                                    },
                                    {
                                        "name": "Transporte"
                                    },
                                    {
                                        "name": "Creche"
                                    },
                                    {
                                        "name": "Combustível"
                                    },
                                    {
                                        "name": "Benefícios"
                                    },
                                    {
                                        "name": "Mês_admissão"
                                    },
                                    {
                                        "name": "Mês_demissão"
                                    },
                                    {
                                        "name": "Status"
                                    },
                                    {
                                        "name": "Faixa_Idade"
                                    },
                                    {
                                        "name": "Tempo_dias"
                                    },
                                    {
                                        "name": "Faixa_dias"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Nome": "Kylie Rame",
                                    "Gênero": "Masculino",
                                    "Data_Nascimento": "1996-03-17",
                                    "Idade": "28",
                                    "Nível": "Supervisor",
                                    "Escolaridade": "Ensino Médio",
                                    "Área": "Financeiro",
                                    "Salário": "7000",
                                    "Data_Admissão": "2019-01-01",
                                    "Data_Demissão": "NULL",
                                    "Contrato": "CLT",
                                    "Motivo_Demissão": "NULL",
                                    "PCD": "NULL",
                                    "Alimentação": "1200",
                                    "Saúde": "1200",
                                    "Odont": "1200",
                                    "Transporte": "1200",
                                    "Creche": "NULL",
                                    "Combustível": "500",
                                    "Benefícios": "5300",
                                    "Mês_admissão": "1",
                                    "Mês_demissão": "-",
                                    "Status": "NULL",
                                    "Faixa_Idade": "24-34",
                                    "Tempo_dias": "364",
                                    "Faixa_dias": "270-364"
                                },
                                {
                                    "Nome": "Dwayne Betun",
                                    "Gênero": "Masculino",
                                    "Data_Nascimento": "1988-02-28",
                                    "Idade": "36",
                                    "Nível": "Gerente",
                                    "Escolaridade": "Pós-graduação",
                                    "Área": "Recursos Humanos",
                                    "Salário": "15000",
                                    "Data_Admissão": "2019-01-02",
                                    "Data_Demissão": "NULL",
                                    "Contrato": "CLT",
                                    "Motivo_Demissão": "NULL",
                                    "PCD": "NULL",
                                    "Alimentação": "1200",
                                    "Saúde": "1200",
                                    "Odont": "1200",
                                    "Transporte": "1200",
                                    "Creche": "NULL",
                                    "Combustível": "500",
                                    "Benefícios": "5300",
                                    "Mês_admissão": "1",
                                    "Mês_demissão": "-",
                                    "Status": "Férias",
                                    "Faixa_Idade": "35-44",
                                    "Tempo_dias": "363",
                                    "Faixa_dias": "270-364"
                                },
                                {
                                    "Nome": "Chrisse Oxbrough",
                                    "Gênero": "Masculino",
                                    "Data_Nascimento": "1988-09-22",
                                    "Idade": "36",
                                    "Nível": "Gerente",
                                    "Escolaridade": "Ensino Superior",
                                    "Área": "Marketing",
                                    "Salário": "15000",
                                    "Data_Admissão": "2019-01-02",
                                    "Data_Demissão": "NULL",
                                    "Contrato": "CLT",
                                    "Motivo_Demissão": "NULL",
                                    "PCD": "NULL",
                                    "Alimentação": "1200",
                                    "Saúde": "1200",
                                    "Odont": "1200",
                                    "Transporte": "1200",
                                    "Creche": "NULL",
                                    "Combustível": "500",
                                    "Benefícios": "5300",
                                    "Mês_admissão": "1",
                                    "Mês_demissão": "-",
                                    "Status": "NULL",
                                    "Faixa_Idade": "35-44",
                                    "Tempo_dias": "363",
                                    "Faixa_dias": "270-364"
                                },
                                {
                                    "Nome": "Kimmy Fardy",
                                    "Gênero": "Feminino",
                                    "Data_Nascimento": "1988-03-14",
                                    "Idade": "36",
                                    "Nível": "Gerente",
                                    "Escolaridade": "Pós-graduação",
                                    "Área": "Produção",
                                    "Salário": "15000",
                                    "Data_Admissão": "2019-01-02",
                                    "Data_Demissão": "NULL",
                                    "Contrato": "CLT",
                                    "Motivo_Demissão": "NULL",
                                    "PCD": "NULL",
                                    "Alimentação": "1200",
                                    "Saúde": "1200",
                                    "Odont": "1200",
                                    "Transporte": "1200",
                                    "Creche": "NULL",
                                    "Combustível": "500",
                                    "Benefícios": "5300",
                                    "Mês_admissão": "1",
                                    "Mês_demissão": "-",
                                    "Status": "NULL",
                                    "Faixa_Idade": "35-44",
                                    "Tempo_dias": "363",
                                    "Faixa_dias": "270-364"
                                },
                                {
                                    "Nome": "Mata Steynor",
                                    "Gênero": "Masculino",
                                    "Data_Nascimento": "1994-06-28",
                                    "Idade": "30",
                                    "Nível": "Analista Sr",
                                    "Escolaridade": "Ensino Técnico",
                                    "Área": "Produção",
                                    "Salário": "5000",
                                    "Data_Admissão": "2019-01-02",
                                    "Data_Demissão": "NULL",
                                    "Contrato": "CLT",
                                    "Motivo_Demissão": "NULL",
                                    "PCD": "NULL",
                                    "Alimentação": "600",
                                    "Saúde": "600",
                                    "Odont": "600",
                                    "Transporte": "600",
                                    "Creche": "NULL",
                                    "Combustível": "500",
                                    "Benefícios": "2900",
                                    "Mês_admissão": "1",
                                    "Mês_demissão": "-",
                                    "Status": "NULL",
                                    "Faixa_Idade": "24-34",
                                    "Tempo_dias": "363",
                                    "Faixa_dias": "270-364"
                                },
                                {
                                    "Nome": "Rivi Ofen",
                                    "Gênero": "Feminino",
                                    "Data_Nascimento": "1981-10-19",
                                    "Idade": "43",
                                    "Nível": "Supervisor",
                                    "Escolaridade": "Ensino Superior",
                                    "Área": "Financeiro",
                                    "Salário": "7000",
                                    "Data_Admissão": "2019-01-03",
                                    "Data_Demissão": "NULL",
                                    "Contrato": "CLT",
                                    "Motivo_Demissão": "NULL",
                                    "PCD": "NULL",
                                    "Alimentação": "1200",
                                    "Saúde": "1200",
                                    "Odont": "1200",
                                    "Transporte": "1200",
                                    "Creche": "NULL",
                                    "Combustível": "500",
                                    "Benefícios": "5300",
                                    "Mês_admissão": "1",
                                    "Mês_demissão": "-",
                                    "Status": "NULL",
                                    "Faixa_Idade": "35-44",
                                    "Tempo_dias": "362",
                                    "Faixa_dias": "270-364"
                                },
                                {
                                    "Nome": "Ross Tutchell",
                                    "Gênero": "Masculino",
                                    "Data_Nascimento": "1991-05-14",
                                    "Idade": "33",
                                    "Nível": "Assistente",
                                    "Escolaridade": "Ensino Médio",
                                    "Área": "Produção",
                                    "Salário": "2500",
                                    "Data_Admissão": "2019-01-03",
                                    "Data_Demissão": "NULL",
                                    "Contrato": "CLT",
                                    "Motivo_Demissão": "NULL",
                                    "PCD": "NULL",
                                    "Alimentação": "600",
                                    "Saúde": "600",
                                    "Odont": "600",
                                    "Transporte": "600",
                                    "Creche": "500",
                                    "Combustível": "NULL",
                                    "Benefícios": "2900",
                                    "Mês_admissão": "1",
                                    "Mês_demissão": "-",
                                    "Status": "NULL",
                                    "Faixa_Idade": "24-34",
                                    "Tempo_dias": "362",
                                    "Faixa_dias": "270-364"
                                },
                                {
                                    "Nome": "Lisa De Antoni",
                                    "Gênero": "Feminino",
                                    "Data_Nascimento": "1961-04-28",
                                    "Idade": "63",
                                    "Nível": "Estagiário",
                                    "Escolaridade": "Ensino Médio",
                                    "Área": "Administração",
                                    "Salário": "1200",
                                    "Data_Admissão": "2019-01-03",
                                    "Data_Demissão": "NULL",
                                    "Contrato": "Estágio",
                                    "Motivo_Demissão": "NULL",
                                    "PCD": "NULL",
                                    "Alimentação": "200",
                                    "Saúde": "200",
                                    "Odont": "200",
                                    "Transporte": "200",
                                    "Creche": "NULL",
                                    "Combustível": "NULL",
                                    "Benefícios": "800",
                                    "Mês_admissão": "1",
                                    "Mês_demissão": "-",
                                    "Status": "NULL",
                                    "Faixa_Idade": "55-64",
                                    "Tempo_dias": "362",
                                    "Faixa_dias": "270-364"
                                },
                                {
                                    "Nome": "Bethena Josephs",
                                    "Gênero": "Feminino",
                                    "Data_Nascimento": "1978-08-08",
                                    "Idade": "46",
                                    "Nível": "Analista Jr",
                                    "Escolaridade": "Ensino Técnico",
                                    "Área": "TI",
                                    "Salário": "3500",
                                    "Data_Admissão": "2019-01-03",
                                    "Data_Demissão": "NULL",
                                    "Contrato": "CLT",
                                    "Motivo_Demissão": "NULL",
                                    "PCD": "NULL",
                                    "Alimentação": "600",
                                    "Saúde": "600",
                                    "Odont": "600",
                                    "Transporte": "600",
                                    "Creche": "NULL",
                                    "Combustível": "NULL",
                                    "Benefícios": "2400",
                                    "Mês_admissão": "1",
                                    "Mês_demissão": "-",
                                    "Status": "NULL",
                                    "Faixa_Idade": "45-54",
                                    "Tempo_dias": "362",
                                    "Faixa_dias": "270-364"
                                },
                                {
                                    "Nome": "Kellia Koppel",
                                    "Gênero": "Feminino",
                                    "Data_Nascimento": "1970-07-19",
                                    "Idade": "54",
                                    "Nível": "Assistente",
                                    "Escolaridade": "Ensino Superior",
                                    "Área": "Recursos Humanos",
                                    "Salário": "2500",
                                    "Data_Admissão": "2019-01-03",
                                    "Data_Demissão": "NULL",
                                    "Contrato": "CLT",
                                    "Motivo_Demissão": "NULL",
                                    "PCD": "NULL",
                                    "Alimentação": "600",
                                    "Saúde": "600",
                                    "Odont": "600",
                                    "Transporte": "600",
                                    "Creche": "NULL",
                                    "Combustível": "NULL",
                                    "Benefícios": "2400",
                                    "Mês_admissão": "1",
                                    "Mês_demissão": "-",
                                    "Status": "NULL",
                                    "Faixa_Idade": "45-54",
                                    "Tempo_dias": "362",
                                    "Faixa_dias": "270-364"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Nome</th><th>Gênero</th><th>Data_Nascimento</th><th>Idade</th><th>Nível</th><th>Escolaridade</th><th>Área</th><th>Salário</th><th>Data_Admissão</th><th>Data_Demissão</th><th>Contrato</th><th>Motivo_Demissão</th><th>PCD</th><th>Alimentação</th><th>Saúde</th><th>Odont</th><th>Transporte</th><th>Creche</th><th>Combustível</th><th>Benefícios</th><th>Mês_admissão</th><th>Mês_demissão</th><th>Status</th><th>Faixa_Idade</th><th>Tempo_dias</th><th>Faixa_dias</th></tr>",
                            "<tr><td>Kylie Rame</td><td>Masculino</td><td>1996-03-17</td><td>28</td><td>Supervisor</td><td>Ensino Médio</td><td>Financeiro</td><td>7000</td><td>2019-01-01</td><td>NULL</td><td>CLT</td><td>NULL</td><td>NULL</td><td>1200</td><td>1200</td><td>1200</td><td>1200</td><td>NULL</td><td>500</td><td>5300</td><td>1</td><td>-</td><td>NULL</td><td>24-34</td><td>364</td><td>270-364</td></tr>",
                            "<tr><td>Dwayne Betun</td><td>Masculino</td><td>1988-02-28</td><td>36</td><td>Gerente</td><td>Pós-graduação</td><td>Recursos Humanos</td><td>15000</td><td>2019-01-02</td><td>NULL</td><td>CLT</td><td>NULL</td><td>NULL</td><td>1200</td><td>1200</td><td>1200</td><td>1200</td><td>NULL</td><td>500</td><td>5300</td><td>1</td><td>-</td><td>Férias</td><td>35-44</td><td>363</td><td>270-364</td></tr>",
                            "<tr><td>Chrisse Oxbrough</td><td>Masculino</td><td>1988-09-22</td><td>36</td><td>Gerente</td><td>Ensino Superior</td><td>Marketing</td><td>15000</td><td>2019-01-02</td><td>NULL</td><td>CLT</td><td>NULL</td><td>NULL</td><td>1200</td><td>1200</td><td>1200</td><td>1200</td><td>NULL</td><td>500</td><td>5300</td><td>1</td><td>-</td><td>NULL</td><td>35-44</td><td>363</td><td>270-364</td></tr>",
                            "<tr><td>Kimmy Fardy</td><td>Feminino</td><td>1988-03-14</td><td>36</td><td>Gerente</td><td>Pós-graduação</td><td>Produção</td><td>15000</td><td>2019-01-02</td><td>NULL</td><td>CLT</td><td>NULL</td><td>NULL</td><td>1200</td><td>1200</td><td>1200</td><td>1200</td><td>NULL</td><td>500</td><td>5300</td><td>1</td><td>-</td><td>NULL</td><td>35-44</td><td>363</td><td>270-364</td></tr>",
                            "<tr><td>Mata Steynor</td><td>Masculino</td><td>1994-06-28</td><td>30</td><td>Analista Sr</td><td>Ensino Técnico</td><td>Produção</td><td>5000</td><td>2019-01-02</td><td>NULL</td><td>CLT</td><td>NULL</td><td>NULL</td><td>600</td><td>600</td><td>600</td><td>600</td><td>NULL</td><td>500</td><td>2900</td><td>1</td><td>-</td><td>NULL</td><td>24-34</td><td>363</td><td>270-364</td></tr>",
                            "<tr><td>Rivi Ofen</td><td>Feminino</td><td>1981-10-19</td><td>43</td><td>Supervisor</td><td>Ensino Superior</td><td>Financeiro</td><td>7000</td><td>2019-01-03</td><td>NULL</td><td>CLT</td><td>NULL</td><td>NULL</td><td>1200</td><td>1200</td><td>1200</td><td>1200</td><td>NULL</td><td>500</td><td>5300</td><td>1</td><td>-</td><td>NULL</td><td>35-44</td><td>362</td><td>270-364</td></tr>",
                            "<tr><td>Ross Tutchell</td><td>Masculino</td><td>1991-05-14</td><td>33</td><td>Assistente</td><td>Ensino Médio</td><td>Produção</td><td>2500</td><td>2019-01-03</td><td>NULL</td><td>CLT</td><td>NULL</td><td>NULL</td><td>600</td><td>600</td><td>600</td><td>600</td><td>500</td><td>NULL</td><td>2900</td><td>1</td><td>-</td><td>NULL</td><td>24-34</td><td>362</td><td>270-364</td></tr>",
                            "<tr><td>Lisa De Antoni</td><td>Feminino</td><td>1961-04-28</td><td>63</td><td>Estagiário</td><td>Ensino Médio</td><td>Administração</td><td>1200</td><td>2019-01-03</td><td>NULL</td><td>Estágio</td><td>NULL</td><td>NULL</td><td>200</td><td>200</td><td>200</td><td>200</td><td>NULL</td><td>NULL</td><td>800</td><td>1</td><td>-</td><td>NULL</td><td>55-64</td><td>362</td><td>270-364</td></tr>",
                            "<tr><td>Bethena Josephs</td><td>Feminino</td><td>1978-08-08</td><td>46</td><td>Analista Jr</td><td>Ensino Técnico</td><td>TI</td><td>3500</td><td>2019-01-03</td><td>NULL</td><td>CLT</td><td>NULL</td><td>NULL</td><td>600</td><td>600</td><td>600</td><td>600</td><td>NULL</td><td>NULL</td><td>2400</td><td>1</td><td>-</td><td>NULL</td><td>45-54</td><td>362</td><td>270-364</td></tr>",
                            "<tr><td>Kellia Koppel</td><td>Feminino</td><td>1970-07-19</td><td>54</td><td>Assistente</td><td>Ensino Superior</td><td>Recursos Humanos</td><td>2500</td><td>2019-01-03</td><td>NULL</td><td>CLT</td><td>NULL</td><td>NULL</td><td>600</td><td>600</td><td>600</td><td>600</td><td>NULL</td><td>NULL</td><td>2400</td><td>1</td><td>-</td><td>NULL</td><td>45-54</td><td>362</td><td>270-364</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 2
        },
        {
            "cell_type": "code",
            "source": [
                "-- Total de funcionários na empresa ao longo do tempo, ativos e inativos\r\n",
                "DECLARE @funcionarios_ativos INT = (SELECT COUNT(*) FROM baseRH WHERE Data_Demissão IS NOT NULL)\r\n",
                "DECLARE @funcionarios_inativos INT = (SELECT COUNT(*) FROM baseRH WHERE Data_Demissão IS NULL)\r\n",
                "\r\n",
                "SELECT  \r\n",
                "    COUNT(*) AS Total_histórico,\r\n",
                "    @funcionarios_ativos AS Ativos,\r\n",
                "    FORMAT(1.0 * @funcionarios_ativos/COUNT(*), '0.00%') AS Percentual_Ativos,\r\n",
                "    @funcionarios_inativos AS Inativos,\r\n",
                "    FORMAT(1.0 * @funcionarios_inativos/COUNT(*), '0.00%') AS Percentual_Inativos\r\n",
                "FROM baseRH"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "6ea20270-1c2b-46fa-8c61-6a7c456d6e84",
                "tags": []
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(1 row affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.014"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "execution_count": 24,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Total_histórico"
                                    },
                                    {
                                        "name": "Ativos"
                                    },
                                    {
                                        "name": "Percentual_Ativos"
                                    },
                                    {
                                        "name": "Inativos"
                                    },
                                    {
                                        "name": "Percentual_Inativos"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Total_histórico": "1000",
                                    "Ativos": "71",
                                    "Percentual_Ativos": "7,10%",
                                    "Inativos": "929",
                                    "Percentual_Inativos": "92,90%"
                                }
                            ]
                        },
                        "text/html": "<table><tr><th>Total_histórico</th><th>Ativos</th><th>Percentual_Ativos</th><th>Inativos</th><th>Percentual_Inativos</th></tr><tr><td>1000</td><td>71</td><td>7,10%</td><td>929</td><td>92,90%</td></tr></table>"
                    },
                    "metadata": {}
                }
            ],
            "execution_count": 24
        },
        {
            "cell_type": "code",
            "source": [
                "-- Criando uma nova View somente com funcionários ativos\r\n",
                "CREATE VIEW baseRH_ativos AS\r\n",
                "(\r\n",
                "    SELECT  \r\n",
                "        *\r\n",
                "    FROM baseRH\r\n",
                "    WHERE Data_Demissão IS NULL\r\n",
                ")"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "a1e3714a-eb7f-4bbc-96c6-e5a609f790b2",
                "tags": []
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Commands completed successfully."
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.009"
                    },
                    "metadata": {}
                }
            ],
            "execution_count": 36
        },
        {
            "cell_type": "code",
            "source": [
                "-- Total de funcionários por genero\r\n",
                "DECLARE @Total_funcionarios INT = (SELECT COUNT(*) FROM baseRH_ativos)\r\n",
                "\r\n",
                "SELECT\r\n",
                "    Gênero,\r\n",
                "    COUNT(*) AS Total,\r\n",
                "    FORMAT(1.0 * COUNT(*)/@Total_funcionarios, '0.00%') AS Percentual\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Gênero"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "cd2d8f5e-8f31-4000-b3a2-3ea37a7d303b"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(2 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.012"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "execution_count": 39,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Gênero"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "Percentual"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Gênero": "Masculino",
                                    "Total": "468",
                                    "Percentual": "50,38%"
                                },
                                {
                                    "Gênero": "Feminino",
                                    "Total": "461",
                                    "Percentual": "49,62%"
                                }
                            ]
                        },
                        "text/html": "<table><tr><th>Gênero</th><th>Total</th><th>Percentual</th></tr><tr><td>Masculino</td><td>468</td><td>50,38%</td></tr><tr><td>Feminino</td><td>461</td><td>49,62%</td></tr></table>"
                    },
                    "metadata": {}
                }
            ],
            "execution_count": 39
        },
        {
            "cell_type": "code",
            "source": [
                "-- Frequência de funcionários por idade\r\n",
                "DECLARE @Total_funcionarios INT = (SELECT COUNT(*) FROM baseRH_ativos)\r\n",
                "\r\n",
                "SELECT\r\n",
                "    Faixa_Idade,\r\n",
                "    COUNT(*) AS Total,\r\n",
                "    FORMAT(1.0 * COUNT(*)/@Total_funcionarios, '0.00%') AS Percentual\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Faixa_Idade"
            ],
            "metadata": {
                "azdata_cell_guid": "92c14e00-0758-4e2c-b482-e6604b589019",
                "language": "sql"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(4 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.015"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "execution_count": 41,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Faixa_Idade"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "Percentual"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Faixa_Idade": "24-34",
                                    "Total": "235",
                                    "Percentual": "25,30%"
                                },
                                {
                                    "Faixa_Idade": "35-44",
                                    "Total": "237",
                                    "Percentual": "25,51%"
                                },
                                {
                                    "Faixa_Idade": "45-54",
                                    "Total": "232",
                                    "Percentual": "24,97%"
                                },
                                {
                                    "Faixa_Idade": "55-64",
                                    "Total": "225",
                                    "Percentual": "24,22%"
                                }
                            ]
                        },
                        "text/html": "<table><tr><th>Faixa_Idade</th><th>Total</th><th>Percentual</th></tr><tr><td>24-34</td><td>235</td><td>25,30%</td></tr><tr><td>35-44</td><td>237</td><td>25,51%</td></tr><tr><td>45-54</td><td>232</td><td>24,97%</td></tr><tr><td>55-64</td><td>225</td><td>24,22%</td></tr></table>"
                    },
                    "metadata": {}
                }
            ],
            "execution_count": 41
        },
        {
            "cell_type": "code",
            "source": [
                "--Distribuição de funcionários por nível hierárquico\r\n",
                "SELECT\r\n",
                "    Nível,\r\n",
                "    COUNT(*) AS Total\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Nível\r\n",
                "ORDER BY Total DESC"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "d0d66d98-ee94-4ce2-aef4-14b888dfc503"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(7 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.018"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 6,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Nível"
                                    },
                                    {
                                        "name": "Total"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Nível": "Assistente",
                                    "Total": "136"
                                },
                                {
                                    "Nível": "Supervisor",
                                    "Total": "133"
                                },
                                {
                                    "Nível": "Analista Sr",
                                    "Total": "133"
                                },
                                {
                                    "Nível": "Estagiário",
                                    "Total": "133"
                                },
                                {
                                    "Nível": "Analista Jr",
                                    "Total": "133"
                                },
                                {
                                    "Nível": "Coordenador",
                                    "Total": "132"
                                },
                                {
                                    "Nível": "Gerente",
                                    "Total": "129"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Nível</th><th>Total</th></tr>",
                            "<tr><td>Assistente</td><td>136</td></tr>",
                            "<tr><td>Supervisor</td><td>133</td></tr>",
                            "<tr><td>Analista Sr</td><td>133</td></tr>",
                            "<tr><td>Estagiário</td><td>133</td></tr>",
                            "<tr><td>Analista Jr</td><td>133</td></tr>",
                            "<tr><td>Coordenador</td><td>132</td></tr>",
                            "<tr><td>Gerente</td><td>129</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 6
        },
        {
            "cell_type": "code",
            "source": [
                "-- Distribuição de funcionários por Escolaridade\r\n",
                "SELECT\r\n",
                "    Escolaridade,\r\n",
                "    COUNT(*) AS Total,\r\n",
                "    FORMAT(1.0 * COUNT(*)/SUM(COUNT(*))OVER(), '0.00%') AS Percentual\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Escolaridade\r\n",
                "ORDER BY Total DESC"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "d9f7aaad-921b-429d-adbd-88b2e0cc1470"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(5 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.876"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 9,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Escolaridade"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "Percentual"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Escolaridade": "Ensino Médio",
                                    "Total": "256",
                                    "Percentual": "27,56%"
                                },
                                {
                                    "Escolaridade": "Ensino Técnico",
                                    "Total": "239",
                                    "Percentual": "25,73%"
                                },
                                {
                                    "Escolaridade": "Ensino Superior",
                                    "Total": "202",
                                    "Percentual": "21,74%"
                                },
                                {
                                    "Escolaridade": "Pós-graduação",
                                    "Total": "161",
                                    "Percentual": "17,33%"
                                },
                                {
                                    "Escolaridade": "Mestrado",
                                    "Total": "71",
                                    "Percentual": "7,64%"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Escolaridade</th><th>Total</th><th>Percentual</th></tr>",
                            "<tr><td>Ensino Médio</td><td>256</td><td>27,56%</td></tr>",
                            "<tr><td>Ensino Técnico</td><td>239</td><td>25,73%</td></tr>",
                            "<tr><td>Ensino Superior</td><td>202</td><td>21,74%</td></tr>",
                            "<tr><td>Pós-graduação</td><td>161</td><td>17,33%</td></tr>",
                            "<tr><td>Mestrado</td><td>71</td><td>7,64%</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 9
        },
        {
            "cell_type": "code",
            "source": [
                "--Distribuição de funcionários por Área da empresa\r\n",
                "SELECT\r\n",
                "    Área,\r\n",
                "    COUNT(*) AS Total,\r\n",
                "    FORMAT(1.0 * COUNT(*)/SUM(COUNT(*))OVER(), '0.00%') AS Percentual\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Área\r\n",
                "ORDER BY Total DESC"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "f4229cf1-5567-4c09-9208-640172b2d326"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(9 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.048"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 10,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Área"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "Percentual"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Área": "Administração",
                                    "Total": "107",
                                    "Percentual": "11,52%"
                                },
                                {
                                    "Área": "Financeiro",
                                    "Total": "107",
                                    "Percentual": "11,52%"
                                },
                                {
                                    "Área": "Produção",
                                    "Total": "105",
                                    "Percentual": "11,30%"
                                },
                                {
                                    "Área": "Vendas",
                                    "Total": "105",
                                    "Percentual": "11,30%"
                                },
                                {
                                    "Área": "Recursos Humanos",
                                    "Total": "105",
                                    "Percentual": "11,30%"
                                },
                                {
                                    "Área": "Marketing",
                                    "Total": "102",
                                    "Percentual": "10,98%"
                                },
                                {
                                    "Área": "TI",
                                    "Total": "101",
                                    "Percentual": "10,87%"
                                },
                                {
                                    "Área": "Operações",
                                    "Total": "101",
                                    "Percentual": "10,87%"
                                },
                                {
                                    "Área": "Logística",
                                    "Total": "96",
                                    "Percentual": "10,33%"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Área</th><th>Total</th><th>Percentual</th></tr>",
                            "<tr><td>Administração</td><td>107</td><td>11,52%</td></tr>",
                            "<tr><td>Financeiro</td><td>107</td><td>11,52%</td></tr>",
                            "<tr><td>Produção</td><td>105</td><td>11,30%</td></tr>",
                            "<tr><td>Vendas</td><td>105</td><td>11,30%</td></tr>",
                            "<tr><td>Recursos Humanos</td><td>105</td><td>11,30%</td></tr>",
                            "<tr><td>Marketing</td><td>102</td><td>10,98%</td></tr>",
                            "<tr><td>TI</td><td>101</td><td>10,87%</td></tr>",
                            "<tr><td>Operações</td><td>101</td><td>10,87%</td></tr>",
                            "<tr><td>Logística</td><td>96</td><td>10,33%</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 10
        },
        {
            "cell_type": "code",
            "source": [
                "--Salário médio por nível hierárquico\r\n",
                "SELECT\r\n",
                "    Nível,\r\n",
                "    AVG(Salário) AS Total,\r\n",
                "    FORMAT(1.0 *AVG(Salário)/SUM(AVG(Salário))OVER(), '0.00%') AS Percentual\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Nível\r\n",
                "ORDER BY Total DESC"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "1c8088a3-5312-4c16-8298-98fcfa7c3fe5"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(7 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.014"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 12,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Nível"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "Percentual"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Nível": "Gerente",
                                    "Total": "15000",
                                    "Percentual": "33,94%"
                                },
                                {
                                    "Nível": "Coordenador",
                                    "Total": "10000",
                                    "Percentual": "22,62%"
                                },
                                {
                                    "Nível": "Supervisor",
                                    "Total": "7000",
                                    "Percentual": "15,84%"
                                },
                                {
                                    "Nível": "Analista Sr",
                                    "Total": "5000",
                                    "Percentual": "11,31%"
                                },
                                {
                                    "Nível": "Analista Jr",
                                    "Total": "3500",
                                    "Percentual": "7,92%"
                                },
                                {
                                    "Nível": "Assistente",
                                    "Total": "2500",
                                    "Percentual": "5,66%"
                                },
                                {
                                    "Nível": "Estagiário",
                                    "Total": "1200",
                                    "Percentual": "2,71%"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Nível</th><th>Total</th><th>Percentual</th></tr>",
                            "<tr><td>Gerente</td><td>15000</td><td>33,94%</td></tr>",
                            "<tr><td>Coordenador</td><td>10000</td><td>22,62%</td></tr>",
                            "<tr><td>Supervisor</td><td>7000</td><td>15,84%</td></tr>",
                            "<tr><td>Analista Sr</td><td>5000</td><td>11,31%</td></tr>",
                            "<tr><td>Analista Jr</td><td>3500</td><td>7,92%</td></tr>",
                            "<tr><td>Assistente</td><td>2500</td><td>5,66%</td></tr>",
                            "<tr><td>Estagiário</td><td>1200</td><td>2,71%</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 12
        },
        {
            "cell_type": "code",
            "source": [
                "--Despesa total em salários?\r\n",
                "SELECT \r\n",
                "    CONCAT('R$', FORMAT(SUM(Salário),'0.00')) AS Total\r\n",
                "FROM baseRH_ativos"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "1573d21f-5d33-4fd2-a9d5-90e6d8ee7e09",
                "tags": []
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(1 row affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.012"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 21,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Total"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Total": "R$5816100,00"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Total</th></tr>",
                            "<tr><td>R$5816100,00</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 21
        },
        {
            "cell_type": "code",
            "source": [
                "-- Quanto é gasto em valor de benefício \"Combustível\"?\r\n",
                "SELECT\r\n",
                "    sum(Combustível) AS 'Combustível'\r\n",
                "FROM baseRH_ativ"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "b9a47187-be95-4274-a760-af5cbc742f8f",
                "tags": []
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Aviso: o valor nulo é eliminado por uma agregação ou outra operação SET."
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(1 row affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.014"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 24,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Combustível"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Combustível": "263500"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Combustível</th></tr>",
                            "<tr><td>263500</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 24
        },
        {
            "cell_type": "code",
            "source": [
                "--Qual a média salarial por escolaridade\r\n",
                "SELECT\r\n",
                "    Escolaridade,\r\n",
                "    AVG(Salário) AS Total,\r\n",
                "    FORMAT(1.0 *AVG(Salário)/SUM(AVG(Salário))OVER(), '0.00%') AS Percentual\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Escolaridade\r\n",
                "ORDER BY Total DESC"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "80d1ed66-be92-47cf-95f8-2ed3edf3fee3"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(5 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.014"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 25,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Escolaridade"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "Percentual"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Escolaridade": "Mestrado",
                                    "Total": "10971",
                                    "Percentual": "31,16%"
                                },
                                {
                                    "Escolaridade": "Pós-graduação",
                                    "Total": "7838",
                                    "Percentual": "22,26%"
                                },
                                {
                                    "Escolaridade": "Ensino Superior",
                                    "Total": "6235",
                                    "Percentual": "17,71%"
                                },
                                {
                                    "Escolaridade": "Ensino Técnico",
                                    "Total": "5125",
                                    "Percentual": "14,56%"
                                },
                                {
                                    "Escolaridade": "Ensino Médio",
                                    "Total": "5041",
                                    "Percentual": "14,32%"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Escolaridade</th><th>Total</th><th>Percentual</th></tr>",
                            "<tr><td>Mestrado</td><td>10971</td><td>31,16%</td></tr>",
                            "<tr><td>Pós-graduação</td><td>7838</td><td>22,26%</td></tr>",
                            "<tr><td>Ensino Superior</td><td>6235</td><td>17,71%</td></tr>",
                            "<tr><td>Ensino Técnico</td><td>5125</td><td>14,56%</td></tr>",
                            "<tr><td>Ensino Médio</td><td>5041</td><td>14,32%</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 25
        },
        {
            "cell_type": "code",
            "source": [
                "-- Variação percentual de funcionários admitidos por mês\r\n",
                "-- Qual mês obteve o maior percentual de admissões em relação ao anterior?\r\n",
                "SELECT\r\n",
                "    Mês_admissão,\r\n",
                "    COUNT(*) AS 'Total',\r\n",
                "    FORMAT(1.0 * (COUNT(*) - LAG(COUNT(*),1)OVER(ORDER BY Mês_admissão))/COUNT(*),'0.00%') AS 'MoM'\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Mês_admissão\r\n",
                "ORDER BY Mês_admissão ASC"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "ba331233-6152-435e-b808-05cbb9812362"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(12 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.013"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 43,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Mês_admissão"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "MoM"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Mês_admissão": "1",
                                    "Total": "91",
                                    "MoM": "NULL"
                                },
                                {
                                    "Mês_admissão": "2",
                                    "Total": "64",
                                    "MoM": "-42,19%"
                                },
                                {
                                    "Mês_admissão": "3",
                                    "Total": "84",
                                    "MoM": "23,81%"
                                },
                                {
                                    "Mês_admissão": "4",
                                    "Total": "74",
                                    "MoM": "-13,51%"
                                },
                                {
                                    "Mês_admissão": "5",
                                    "Total": "81",
                                    "MoM": "8,64%"
                                },
                                {
                                    "Mês_admissão": "6",
                                    "Total": "84",
                                    "MoM": "3,57%"
                                },
                                {
                                    "Mês_admissão": "7",
                                    "Total": "85",
                                    "MoM": "1,18%"
                                },
                                {
                                    "Mês_admissão": "8",
                                    "Total": "79",
                                    "MoM": "-7,59%"
                                },
                                {
                                    "Mês_admissão": "9",
                                    "Total": "63",
                                    "MoM": "-25,40%"
                                },
                                {
                                    "Mês_admissão": "10",
                                    "Total": "79",
                                    "MoM": "20,25%"
                                },
                                {
                                    "Mês_admissão": "11",
                                    "Total": "66",
                                    "MoM": "-19,70%"
                                },
                                {
                                    "Mês_admissão": "12",
                                    "Total": "79",
                                    "MoM": "16,46%"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Mês_admissão</th><th>Total</th><th>MoM</th></tr>",
                            "<tr><td>1</td><td>91</td><td>NULL</td></tr>",
                            "<tr><td>2</td><td>64</td><td>-42,19%</td></tr>",
                            "<tr><td>3</td><td>84</td><td>23,81%</td></tr>",
                            "<tr><td>4</td><td>74</td><td>-13,51%</td></tr>",
                            "<tr><td>5</td><td>81</td><td>8,64%</td></tr>",
                            "<tr><td>6</td><td>84</td><td>3,57%</td></tr>",
                            "<tr><td>7</td><td>85</td><td>1,18%</td></tr>",
                            "<tr><td>8</td><td>79</td><td>-7,59%</td></tr>",
                            "<tr><td>9</td><td>63</td><td>-25,40%</td></tr>",
                            "<tr><td>10</td><td>79</td><td>20,25%</td></tr>",
                            "<tr><td>11</td><td>66</td><td>-19,70%</td></tr>",
                            "<tr><td>12</td><td>79</td><td>16,46%</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 43
        },
        {
            "cell_type": "code",
            "source": [
                "-- Variação percentual de funcionários demitidos por mês\r\n",
                "-- Qual mês obteve o maior percentual de demissões em relação ao anterior?\r\n",
                "SELECT\r\n",
                "    Mês_demissão,\r\n",
                "    COUNT(*) AS 'Total',\r\n",
                "    FORMAT(1.0 * (COUNT(*) - LAG(COUNT(*),1)OVER(ORDER BY CAST(Mês_demissão AS INT)))/COUNT(*),'0.00%') AS 'MoM'\r\n",
                "FROM baseRH\r\n",
                "WHERE Mês_demissão <> '-'\r\n",
                "GROUP BY Mês_demissão\r\n",
                "ORDER BY CAST(Mês_demissão AS INT) ASC"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "2f0bc4c9-43d2-41f0-809a-d24058a13fb7"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(11 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.011"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 49,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Mês_demissão"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "MoM"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Mês_demissão": "2",
                                    "Total": "2",
                                    "MoM": "NULL"
                                },
                                {
                                    "Mês_demissão": "3",
                                    "Total": "5",
                                    "MoM": "60,00%"
                                },
                                {
                                    "Mês_demissão": "4",
                                    "Total": "5",
                                    "MoM": "0,00%"
                                },
                                {
                                    "Mês_demissão": "5",
                                    "Total": "3",
                                    "MoM": "-66,67%"
                                },
                                {
                                    "Mês_demissão": "6",
                                    "Total": "7",
                                    "MoM": "57,14%"
                                },
                                {
                                    "Mês_demissão": "7",
                                    "Total": "5",
                                    "MoM": "-40,00%"
                                },
                                {
                                    "Mês_demissão": "8",
                                    "Total": "6",
                                    "MoM": "16,67%"
                                },
                                {
                                    "Mês_demissão": "9",
                                    "Total": "10",
                                    "MoM": "40,00%"
                                },
                                {
                                    "Mês_demissão": "10",
                                    "Total": "6",
                                    "MoM": "-66,67%"
                                },
                                {
                                    "Mês_demissão": "11",
                                    "Total": "7",
                                    "MoM": "14,29%"
                                },
                                {
                                    "Mês_demissão": "12",
                                    "Total": "15",
                                    "MoM": "53,33%"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Mês_demissão</th><th>Total</th><th>MoM</th></tr>",
                            "<tr><td>2</td><td>2</td><td>NULL</td></tr>",
                            "<tr><td>3</td><td>5</td><td>60,00%</td></tr>",
                            "<tr><td>4</td><td>5</td><td>0,00%</td></tr>",
                            "<tr><td>5</td><td>3</td><td>-66,67%</td></tr>",
                            "<tr><td>6</td><td>7</td><td>57,14%</td></tr>",
                            "<tr><td>7</td><td>5</td><td>-40,00%</td></tr>",
                            "<tr><td>8</td><td>6</td><td>16,67%</td></tr>",
                            "<tr><td>9</td><td>10</td><td>40,00%</td></tr>",
                            "<tr><td>10</td><td>6</td><td>-66,67%</td></tr>",
                            "<tr><td>11</td><td>7</td><td>14,29%</td></tr>",
                            "<tr><td>12</td><td>15</td><td>53,33%</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 49
        },
        {
            "cell_type": "code",
            "source": [
                "-- Total de funcionários por tipo de contrato\r\n",
                "DECLARE @totalFunc INT = (SELECT COUNT(*) FROM baseRH_ativos)\r\n",
                "\r\n",
                "SELECT \r\n",
                " Contrato,\r\n",
                " COUNT(*) AS Total,\r\n",
                " FORMAT(1.0 * COUNT(*)/@totalFunc,'0.00%') AS Percentual\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Contrato"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "459a40e4-9a64-4838-a732-9442a4cb38e4",
                "tags": []
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(2 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.011"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 54,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Contrato"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "Percentual"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Contrato": "CLT",
                                    "Total": "796",
                                    "Percentual": "85,68%"
                                },
                                {
                                    "Contrato": "Estágio",
                                    "Total": "133",
                                    "Percentual": "14,32%"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Contrato</th><th>Total</th><th>Percentual</th></tr>",
                            "<tr><td>CLT</td><td>796</td><td>85,68%</td></tr>",
                            "<tr><td>Estágio</td><td>133</td><td>14,32%</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 54
        },
        {
            "cell_type": "code",
            "source": [
                "-- Área vs tipo de contrato e percentual em relação ao total da área\r\n",
                "SELECT \r\n",
                " Área,\r\n",
                " Contrato,\r\n",
                " COUNT(*) AS Total,\r\n",
                " FORMAT(1.0 * COUNT(*)/SUM(COUNT(*))OVER(PARTITION BY Área),'0.00%') AS Percentual\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Área, Contrato\r\n",
                "ORDER BY Área ASC"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "3b1c4b8c-9cfb-41a4-9522-323e01637f02"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(18 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.020"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 58,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Área"
                                    },
                                    {
                                        "name": "Contrato"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "Percentual"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Área": "Administração",
                                    "Contrato": "CLT",
                                    "Total": "92",
                                    "Percentual": "85,98%"
                                },
                                {
                                    "Área": "Administração",
                                    "Contrato": "Estágio",
                                    "Total": "15",
                                    "Percentual": "14,02%"
                                },
                                {
                                    "Área": "Financeiro",
                                    "Contrato": "CLT",
                                    "Total": "91",
                                    "Percentual": "85,05%"
                                },
                                {
                                    "Área": "Financeiro",
                                    "Contrato": "Estágio",
                                    "Total": "16",
                                    "Percentual": "14,95%"
                                },
                                {
                                    "Área": "Logística",
                                    "Contrato": "CLT",
                                    "Total": "82",
                                    "Percentual": "85,42%"
                                },
                                {
                                    "Área": "Logística",
                                    "Contrato": "Estágio",
                                    "Total": "14",
                                    "Percentual": "14,58%"
                                },
                                {
                                    "Área": "Marketing",
                                    "Contrato": "CLT",
                                    "Total": "88",
                                    "Percentual": "86,27%"
                                },
                                {
                                    "Área": "Marketing",
                                    "Contrato": "Estágio",
                                    "Total": "14",
                                    "Percentual": "13,73%"
                                },
                                {
                                    "Área": "Operações",
                                    "Contrato": "CLT",
                                    "Total": "88",
                                    "Percentual": "87,13%"
                                },
                                {
                                    "Área": "Operações",
                                    "Contrato": "Estágio",
                                    "Total": "13",
                                    "Percentual": "12,87%"
                                },
                                {
                                    "Área": "Produção",
                                    "Contrato": "CLT",
                                    "Total": "90",
                                    "Percentual": "85,71%"
                                },
                                {
                                    "Área": "Produção",
                                    "Contrato": "Estágio",
                                    "Total": "15",
                                    "Percentual": "14,29%"
                                },
                                {
                                    "Área": "Recursos Humanos",
                                    "Contrato": "CLT",
                                    "Total": "90",
                                    "Percentual": "85,71%"
                                },
                                {
                                    "Área": "Recursos Humanos",
                                    "Contrato": "Estágio",
                                    "Total": "15",
                                    "Percentual": "14,29%"
                                },
                                {
                                    "Área": "TI",
                                    "Contrato": "CLT",
                                    "Total": "85",
                                    "Percentual": "84,16%"
                                },
                                {
                                    "Área": "TI",
                                    "Contrato": "Estágio",
                                    "Total": "16",
                                    "Percentual": "15,84%"
                                },
                                {
                                    "Área": "Vendas",
                                    "Contrato": "CLT",
                                    "Total": "90",
                                    "Percentual": "85,71%"
                                },
                                {
                                    "Área": "Vendas",
                                    "Contrato": "Estágio",
                                    "Total": "15",
                                    "Percentual": "14,29%"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Área</th><th>Contrato</th><th>Total</th><th>Percentual</th></tr>",
                            "<tr><td>Administração</td><td>CLT</td><td>92</td><td>85,98%</td></tr>",
                            "<tr><td>Administração</td><td>Estágio</td><td>15</td><td>14,02%</td></tr>",
                            "<tr><td>Financeiro</td><td>CLT</td><td>91</td><td>85,05%</td></tr>",
                            "<tr><td>Financeiro</td><td>Estágio</td><td>16</td><td>14,95%</td></tr>",
                            "<tr><td>Logística</td><td>CLT</td><td>82</td><td>85,42%</td></tr>",
                            "<tr><td>Logística</td><td>Estágio</td><td>14</td><td>14,58%</td></tr>",
                            "<tr><td>Marketing</td><td>CLT</td><td>88</td><td>86,27%</td></tr>",
                            "<tr><td>Marketing</td><td>Estágio</td><td>14</td><td>13,73%</td></tr>",
                            "<tr><td>Operações</td><td>CLT</td><td>88</td><td>87,13%</td></tr>",
                            "<tr><td>Operações</td><td>Estágio</td><td>13</td><td>12,87%</td></tr>",
                            "<tr><td>Produção</td><td>CLT</td><td>90</td><td>85,71%</td></tr>",
                            "<tr><td>Produção</td><td>Estágio</td><td>15</td><td>14,29%</td></tr>",
                            "<tr><td>Recursos Humanos</td><td>CLT</td><td>90</td><td>85,71%</td></tr>",
                            "<tr><td>Recursos Humanos</td><td>Estágio</td><td>15</td><td>14,29%</td></tr>",
                            "<tr><td>TI</td><td>CLT</td><td>85</td><td>84,16%</td></tr>",
                            "<tr><td>TI</td><td>Estágio</td><td>16</td><td>15,84%</td></tr>",
                            "<tr><td>Vendas</td><td>CLT</td><td>90</td><td>85,71%</td></tr>",
                            "<tr><td>Vendas</td><td>Estágio</td><td>15</td><td>14,29%</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 58
        },
        {
            "cell_type": "code",
            "source": [
                "-- Área vs tipo de contrato e percentual em relação ao total da área\r\n",
                "SELECT \r\n",
                " Área,\r\n",
                " COALESCE(PCD,'Não') AS 'PCD?',\r\n",
                " COUNT(*) AS Total,\r\n",
                " FORMAT(1.0 * COUNT(*)/SUM(COUNT(*))OVER(PARTITION BY Área),'0.00%') AS Percentual\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY Área, PCD\r\n",
                "ORDER BY Área ASC"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "ea3a6f70-2860-4eaa-a5ed-23c180f1b74a"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(18 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.021"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 71,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Área"
                                    },
                                    {
                                        "name": "PCD?"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "Percentual"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Área": "Administração",
                                    "PCD?": "Não",
                                    "Total": "95",
                                    "Percentual": "88,79%"
                                },
                                {
                                    "Área": "Administração",
                                    "PCD?": "Sim",
                                    "Total": "12",
                                    "Percentual": "11,21%"
                                },
                                {
                                    "Área": "Financeiro",
                                    "PCD?": "Não",
                                    "Total": "97",
                                    "Percentual": "90,65%"
                                },
                                {
                                    "Área": "Financeiro",
                                    "PCD?": "Sim",
                                    "Total": "10",
                                    "Percentual": "9,35%"
                                },
                                {
                                    "Área": "Logística",
                                    "PCD?": "Não",
                                    "Total": "82",
                                    "Percentual": "85,42%"
                                },
                                {
                                    "Área": "Logística",
                                    "PCD?": "Sim",
                                    "Total": "14",
                                    "Percentual": "14,58%"
                                },
                                {
                                    "Área": "Marketing",
                                    "PCD?": "Não",
                                    "Total": "89",
                                    "Percentual": "87,25%"
                                },
                                {
                                    "Área": "Marketing",
                                    "PCD?": "Sim",
                                    "Total": "13",
                                    "Percentual": "12,75%"
                                },
                                {
                                    "Área": "Operações",
                                    "PCD?": "Não",
                                    "Total": "87",
                                    "Percentual": "86,14%"
                                },
                                {
                                    "Área": "Operações",
                                    "PCD?": "Sim",
                                    "Total": "14",
                                    "Percentual": "13,86%"
                                },
                                {
                                    "Área": "Produção",
                                    "PCD?": "Não",
                                    "Total": "92",
                                    "Percentual": "87,62%"
                                },
                                {
                                    "Área": "Produção",
                                    "PCD?": "Sim",
                                    "Total": "13",
                                    "Percentual": "12,38%"
                                },
                                {
                                    "Área": "Recursos Humanos",
                                    "PCD?": "Não",
                                    "Total": "92",
                                    "Percentual": "87,62%"
                                },
                                {
                                    "Área": "Recursos Humanos",
                                    "PCD?": "Sim",
                                    "Total": "13",
                                    "Percentual": "12,38%"
                                },
                                {
                                    "Área": "TI",
                                    "PCD?": "Não",
                                    "Total": "95",
                                    "Percentual": "94,06%"
                                },
                                {
                                    "Área": "TI",
                                    "PCD?": "Sim",
                                    "Total": "6",
                                    "Percentual": "5,94%"
                                },
                                {
                                    "Área": "Vendas",
                                    "PCD?": "Não",
                                    "Total": "97",
                                    "Percentual": "92,38%"
                                },
                                {
                                    "Área": "Vendas",
                                    "PCD?": "Sim",
                                    "Total": "8",
                                    "Percentual": "7,62%"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Área</th><th>PCD?</th><th>Total</th><th>Percentual</th></tr>",
                            "<tr><td>Administração</td><td>Não</td><td>95</td><td>88,79%</td></tr>",
                            "<tr><td>Administração</td><td>Sim</td><td>12</td><td>11,21%</td></tr>",
                            "<tr><td>Financeiro</td><td>Não</td><td>97</td><td>90,65%</td></tr>",
                            "<tr><td>Financeiro</td><td>Sim</td><td>10</td><td>9,35%</td></tr>",
                            "<tr><td>Logística</td><td>Não</td><td>82</td><td>85,42%</td></tr>",
                            "<tr><td>Logística</td><td>Sim</td><td>14</td><td>14,58%</td></tr>",
                            "<tr><td>Marketing</td><td>Não</td><td>89</td><td>87,25%</td></tr>",
                            "<tr><td>Marketing</td><td>Sim</td><td>13</td><td>12,75%</td></tr>",
                            "<tr><td>Operações</td><td>Não</td><td>87</td><td>86,14%</td></tr>",
                            "<tr><td>Operações</td><td>Sim</td><td>14</td><td>13,86%</td></tr>",
                            "<tr><td>Produção</td><td>Não</td><td>92</td><td>87,62%</td></tr>",
                            "<tr><td>Produção</td><td>Sim</td><td>13</td><td>12,38%</td></tr>",
                            "<tr><td>Recursos Humanos</td><td>Não</td><td>92</td><td>87,62%</td></tr>",
                            "<tr><td>Recursos Humanos</td><td>Sim</td><td>13</td><td>12,38%</td></tr>",
                            "<tr><td>TI</td><td>Não</td><td>95</td><td>94,06%</td></tr>",
                            "<tr><td>TI</td><td>Sim</td><td>6</td><td>5,94%</td></tr>",
                            "<tr><td>Vendas</td><td>Não</td><td>97</td><td>92,38%</td></tr>",
                            "<tr><td>Vendas</td><td>Sim</td><td>8</td><td>7,62%</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 71
        },
        {
            "cell_type": "code",
            "source": [
                "-- Total de funcionários afastados ou de férias\r\n",
                "DECLARE @totalFunc INT = (SELECT COUNT(*) FROM baseRH_ativos)\r\n",
                "\r\n",
                "SELECT\r\n",
                "    COALESCE([Status],'Ativos') AS Status,\r\n",
                "    COUNT(*) AS Total,\r\n",
                "    FORMAT(1.0 * COUNT(*)/@totalFunc,'0.00%') AS Percentual\r\n",
                "FROM baseRH_ativos\r\n",
                "GROUP BY [Status]"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "c00e35ca-edb5-4257-a09c-6af317286b43"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(3 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.008"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 69,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Status"
                                    },
                                    {
                                        "name": "Total"
                                    },
                                    {
                                        "name": "Percentual"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Status": "Ativos",
                                    "Total": "900",
                                    "Percentual": "96,88%"
                                },
                                {
                                    "Status": "Licença",
                                    "Total": "5",
                                    "Percentual": "0,54%"
                                },
                                {
                                    "Status": "Férias",
                                    "Total": "24",
                                    "Percentual": "2,58%"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Status</th><th>Total</th><th>Percentual</th></tr>",
                            "<tr><td>Ativos</td><td>900</td><td>96,88%</td></tr>",
                            "<tr><td>Licença</td><td>5</td><td>0,54%</td></tr>",
                            "<tr><td>Férias</td><td>24</td><td>2,58%</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 69
        }
    ]
}