from datetime import datetime, timedelta

# Obtener la fecha y hora actual
ahora = datetime.now()
print("Fecha y hora actual:", ahora)

# Sumar 5 días a la fecha actual
futuro = ahora + timedelta(days=5)
print("Fecha futura:", futuro)