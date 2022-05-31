import pandas as pd

locale_input = input('Digite o local e o nome do arquivo para entrada: ')[1:-1]
locale_output = input('Digite o local e o nome do arquivo para saída: ')[1:-1]
tabela = pd.read_excel(r"{locale_in}".format(locale_in = locale_input), engine='openpyxl', sheet_name = "Database")

def tratar_comparativo(tabela):
    tabela = tabela.drop(columns=['NO_DE_REGS'])
    tabela = tabela.reindex(columns=["TIPO", "DESCRIÇÃO", "CONTA", "SALDO_I_ABR_SOMA", "DEB_ABR_SOMA", "CRE_ABR_SOMA", "MOV_ABR_SOMA", "VAR_ABR", "DEB_MAI_SOMA", "CRE_MAI_SOMA", "MOV_MAI_SOMA", "VAR_MAI", "DEB_JUN_SOMA", "CRE_JUN_SOMA", "MOV_JUN_SOMA", "VAR_JUN", "DEB_JUL_SOMA", "CRE_JUL_SOMA", "MOV_JUL_SOMA", "VAR_JUL", "DEB_AGO_SOMA", "CRE_AGO_SOMA", "MOV_AGO_SOMA", "VAR_AGO", "DEB_SET_SOMA", "CRE_SET_SOMA", "MOV_SET_SOMA", "VAR_SET", "DEB_OUT_SOMA", "CRE_OUT_SOMA", "MOV_OUT_SOMA", "VAR_OUT", "DEB_NOV_SOMA", "CRE_NOV_SOMA", "MOV_NOV_SOMA", "VAR_NOV", "DEB_DEZ_SOMA", "CRE_DEZ_SOMA", "MOV_DEZ_SOMA", "VAR_DEZ", "DEB_JAN22_SOMA", "CRE_JAN22_SOMA", "MOV_JAN22_SOMA", "VAR_JAN22",  "DEB_FEV22_SOMA", "CRE_FEV22_SOMA", "MOV_FEV22_SOMA", "VAR_FEV22",  "DEB_MAR22_SOMA", "CRE_MAR22_SOMA", "MOV_MAR22_SOMA", "SALDO_F_MAR22_SOMA", "SALDO_FINAL", "CONFERÊNCIA_AUDITORIA"])
    tabela.to_excel(r"{locale_out}".format(locale_out = locale_output), sheet_name='Database', index=False)


def tratar_anual(tabela):
    tabela = tabela.drop(columns=['NO_DE_REGS'])
    tabela = tabela.reindex(columns=["TIPO","RED","CONTA", "DESCRIÇÃO_DA_CONTA", "SALDO_I_JAN_SOMA", "DEB_JAN_SOMA", "CRE_JAN_SOMA", "MOV_JAN_SOMA", "VAR_JAN", "DEB_FEV_SOMA", "CRE_FEV_SOMA", "MOV_FEV_SOMA", "VAR_FEV", "DEB_MAR_SOMA", "CRE_MAR_SOMA", "MOV_MAR_SOMA", "VAR_MAR", "DEB_ABR_SOMA", "CRE_ABR_SOMA", "MOV_ABR_SOMA", "VAR_MAR", "DEB_MAI_SOMA", "CRE_MAI_SOMA", "MOV_MAI_SOMA", "VAR_MAI", "DEB_JUN_SOMA", "CRE_JUN_SOMA", "MOV_JUN_SOMA", "VAR_JUN", "DEB_JUL_SOMA", "CRE_JUL_SOMA", "MOV_JUL_SOMA", "VAR_JUL", "DEB_AGO_SOMA", "CRE_AGO_SOMA", "MOV_AGO_SOMA", "VAR_AGO", "DEB_SET_SOMA", "CRE_SET_SOMA", "MOV_SET_SOMA", "VAR_SET", "DEB_OUT_SOMA", "CRE_OUT_SOMA", "MOV_OUT_SOMA", "VAR_OUT", "DEB_NOV_SOMA", "CRE_NOV_SOMA", "MOV_NOV_SOMA", "VAR_NOV", "DEB_DEZ_SOMA", "CRE_DEZ_SOMA", "MOV_DEZ_SOMA", "SALDO_F_DEZ_SOMA", "SALDO_FINAL", "CONFERÊNCIA_AUDITORIA"])
    tabela.to_excel(r"{locale_out}".format(locale_out = locale_output), sheet_name='Database', index=False)

def tratar_onze_meses(tabela):
    tabela = tabela.drop(columns=['NO_DE_REGS'])
    tabela = tabela.reindex(columns=["TIPO", "DESCRIÇÃO", "CONTA", "SALDO_I_JAN_SOMA", "DEB_JAN_SOMA", "CRE_JAN_SOMA", "MOV_JAN_SOMA", "VAR_JAN", "DEB_FEV_SOMA", "CRE_FEV_SOMA", "MOV_FEV_SOMA", "VAR_FEV", "DEB_MAR_SOMA", "CRE_MAR_SOMA", "MOV_MAR_SOMA", "VAR_MAR", "DEB_ABR_SOMA", "CRE_ABR_SOMA", "MOV_ABR_SOMA", "VAR_MAR", "DEB_MAI_SOMA", "CRE_MAI_SOMA", "MOV_MAI_SOMA", "VAR_MAI", "DEB_JUN_SOMA", "CRE_JUN_SOMA", "MOV_JUN_SOMA", "VAR_JUN", "DEB_JUL_SOMA", "CRE_JUL_SOMA", "MOV_JUL_SOMA", "VAR_JUL", "DEB_AGO_SOMA", "CRE_AGO_SOMA", "MOV_AGO_SOMA", "VAR_AGO", "DEB_SET_SOMA", "CRE_SET_SOMA", "MOV_SET_SOMA", "VAR_SET", "DEB_OUT_SOMA", "CRE_OUT_SOMA", "MOV_OUT_SOMA", "VAR_OUT", "DEB_NOV_SOMA", "CRE_NOV_SOMA", "MOV_NOV_SOMA",  "SALDO_F_NOV_SOMA", "SALDO_FINAL", "CONFERÊNCIA_AUDITORIA"])
    tabela.to_excel(r"{locale_out}".format(locale_out = locale_output), sheet_name='Database', index=False)

def tratar_dez_meses(tabela):

    tabela = tabela.drop(columns=['NO_DE_REGS'])
    tabela = tabela.reindex(columns=["TIPO", "DESCRIÇÃO", "CONTA", "SALDO_I_JAN_SOMA", "DEB_JAN_SOMA", "CRE_JAN_SOMA", "MOV_JAN_SOMA", "VAR_JAN", "DEB_FEV_SOMA", "CRE_FEV_SOMA", "MOV_FEV_SOMA", "VAR_FEV", "DEB_MAR_SOMA", "CRE_MAR_SOMA", "MOV_MAR_SOMA", "VAR_MAR", "DEB_ABR_SOMA", "CRE_ABR_SOMA", "MOV_ABR_SOMA", "VAR_MAR", "DEB_MAI_SOMA", "CRE_MAI_SOMA", "MOV_MAI_SOMA", "VAR_MAI", "DEB_JUN_SOMA", "CRE_JUN_SOMA", "MOV_JUN_SOMA", "VAR_JUN", "DEB_JUL_SOMA", "CRE_JUL_SOMA", "MOV_JUL_SOMA", "VAR_JUL", "DEB_AGO_SOMA", "CRE_AGO_SOMA", "MOV_AGO_SOMA", "VAR_AGO", "DEB_SET_SOMA", "CRE_SET_SOMA", "MOV_SET_SOMA", "VAR_SET", "DEB_OUT_SOMA", "CRE_OUT_SOMA", "MOV_OUT_SOMA", "SALDO_F_OUT_SOMA", "SALDO_FINAL", "CONFERÊNCIA_AUDITORIA"])
    tabela.to_excel(r"{locale_out}".format(locale_out = locale_output), sheet_name='Database', index=False)
    
def tratar_nove_meses(tabela):

    tabela = tabela.drop(columns=['NO_DE_REGS']) 
    tabela = tabela.reindex(columns=["TIPO", "DESCRIÇÃO", "CONTA", "SALDO_I_JAN_SOMA", "DEB_JAN_SOMA", "CRE_JAN_SOMA", "MOV_JAN_SOMA", "VAR_JAN", "DEB_FEV_SOMA", "CRE_FEV_SOMA", "MOV_FEV_SOMA", "VAR_FEV", "DEB_MAR_SOMA", "CRE_MAR_SOMA", "MOV_MAR_SOMA", "VAR_MAR", "DEB_ABR_SOMA", "CRE_ABR_SOMA", "MOV_ABR_SOMA", "VAR_MAR", "DEB_MAI_SOMA", "CRE_MAI_SOMA", "MOV_MAI_SOMA", "VAR_MAI", "DEB_JUN_SOMA", "CRE_JUN_SOMA", "MOV_JUN_SOMA", "VAR_JUN", "DEB_JUL_SOMA", "CRE_JUL_SOMA", "MOV_JUL_SOMA", "VAR_JUL", "DEB_AGO_SOMA", "CRE_AGO_SOMA", "MOV_AGO_SOMA", "VAR_AGO", "DEB_SET_SOMA", "CRE_SET_SOMA", "MOV_SET_SOMA", "SALDO_F_SET_SOMA", "SALDO_FINAL", "CONFERÊNCIA_AUDITORIA"])
    tabela.to_excel(r"{locale_out}".format(locale_out = locale_output), sheet_name='Database', index=False)

def tratar_trimestral(tabela):
    
    tabela = tabela.drop(columns=['NO_DE_REGS',])
    tabela = tabela.reindex(columns=["TIPO", "DESCRIÇÃO", "CONTA","RED", "SALDO_I_JAN_SOMA", "DEB_JAN_SOMA", "CRE_JAN_SOMA", "MOV_JAN_SOMA", "VAR_JAN", "DEB_FEV_SOMA", "CRE_FEV_SOMA", "MOV_FEV_SOMA", "VAR_FEV", "DEB_MAR_SOMA", "CRE_MAR_SOMA", "MOV_MAR_SOMA", "SALDO_F_DEZ_SOMA", "SALDO_FINAL", "CONFERÊNCIA_AUDITORIA"])
    tabela.to_excel(r"{locale_out}".format(locale_out = locale_output), sheet_name='Database', index=False)
    
def tratar_semestral(tabela):
    tabela = tabela.drop(columns=['NO_DE_REGS'])
    tabela = tabela.reindex(columns=["TIPO", "DESCRIÇÃO", "CONTA", "SALDO_I_JAN_SOMA", "DEB_JAN_SOMA", "CRE_JAN_SOMA", "MOV_JAN_SOMA", "VAR_JAN", "DEB_FEV_SOMA", "CRE_FEV_SOMA", "MOV_FEV_SOMA", "VAR_FEV", "DEB_MAR_SOMA", "CRE_MAR_SOMA", "MOV_MAR_SOMA", "VAR_MAR", "DEB_ABR_SOMA", "CRE_ABR_SOMA", "MOV_ABR_SOMA", "VAR_MAR", "DEB_MAI_SOMA", "CRE_MAI_SOMA", "MOV_MAI_SOMA", "VAR_MAI", "DEB_JUN_SOMA", "CRE_JUN_SOMA", "MOV_JUN_SOMA", "SALDO_F_DEZ_SOMA", "SALDO_FINAL", "CONFERÊNCIA_AUDITORIA"])
    tabela.to_excel(r"{locale_out}".format(locale_out = locale_output), sheet_name='Database', index=False)
    return tabela

tratar_anual(tabela)
