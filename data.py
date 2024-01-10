from datetime import datetime, timedelta


class DataBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                 "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses[mes_cadastro]

    def semana_cadastro(self):
        dias_da_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]
        dia = self.momento_cadastro.weekday()
        return dias_da_semana[dia]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro

