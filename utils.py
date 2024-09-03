def texto_formula(df, var_dependente, excluir_cols):
    """
        Função para gerar o texto utilizado na 
        fórmula para geração do modelo
    """
    variaveis = list(df.columns.values)
    variaveis.remove(var_dependente)
    for col in excluir_cols:
        variaveis.remove(col)
    return var_dependente + ' ~ ' + ' + '.join(variaveis)