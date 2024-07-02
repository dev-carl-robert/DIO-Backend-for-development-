<<<<<<< HEAD
##### timedelta ####
from datetime import timedelta, datetime, date, time


tipo_carro = "P" # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()
data_atual_formatada = data_atual.strftime("%d/%m/%Y %H:%M")
data_estimada = 0


match tipo_carro:
    case "P":
        data_estimada = data_atual +  timedelta(minutes=tempo_pequeno) 
        print(f"o carro chegou: {data_atual_formatada} e ficará pronto às {data_estimada}")
    case "M":
        data_estimada = data_atual +  timedelta(minutes=tempo_medio) 
        print(f"o carro chegou: {data_atual_formatada} e ficará pronto às {data_estimada}")
    case "G":
        data_estimada = data_atual +  timedelta(minutes=tempo_grande) 
        print(f"o carro chegou: {data_atual_formatada} e ficará pronto às {data_estimada}")
     
        
print(date.today() - timedelta(days=1))

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

=======
##### timedelta ####
from datetime import timedelta, datetime, date, time


tipo_carro = "P" # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()
data_atual_formatada = data_atual.strftime("%d/%m/%Y %H:%M")
data_estimada = 0


match tipo_carro:
    case "P":
        data_estimada = data_atual +  timedelta(minutes=tempo_pequeno) 
        print(f"o carro chegou: {data_atual_formatada} e ficará pronto às {data_estimada}")
    case "M":
        data_estimada = data_atual +  timedelta(minutes=tempo_medio) 
        print(f"o carro chegou: {data_atual_formatada} e ficará pronto às {data_estimada}")
    case "G":
        data_estimada = data_atual +  timedelta(minutes=tempo_grande) 
        print(f"o carro chegou: {data_atual_formatada} e ficará pronto às {data_estimada}")
     
        
print(date.today() - timedelta(days=1))

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
