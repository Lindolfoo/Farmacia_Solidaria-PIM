from datetime import datetime, date

def str_para_data(data_str):
    """
    Converte string YYYY-MM-DD em date
    """
    return datetime.strptime(data_str, "%Y-%m-%d").date()

def dias_para_vencer(data_validade):
    """
    Retorna quantos dias faltam para vencer
    (negativo = vencido)
    """
    return (data_validade - date.today()).days
