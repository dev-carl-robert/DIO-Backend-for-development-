<<<<<<< HEAD
import pytz
from datetime import datetime
# import pytz

data_hora_atual = datetime.now()
data_hora_str = "2023-19-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))


data = datetime.now(pytz.timezone('Europe/Oslo'))

=======
import pytz
from datetime import datetime
# import pytz

data_hora_atual = datetime.now()
data_hora_str = "2023-19-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))


data = datetime.now(pytz.timezone('Europe/Oslo'))

>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
print(data)