# Desafio: duracao de um evento
# Calcule quanto tempo um evento durou a partir dos horarios HH:MM.


def converter_para_minutos(horario):
    try:
        horas, minutos = horario.split(":")
        horas = int(horas)
        minutos = int(minutos)
    except ValueError:
        return None

    if 0 <= horas <= 23 and 0 <= minutos <= 59:
        return horas * 60 + minutos
    return None


while True:
    inicio = converter_para_minutos(input("Horario de inicio (HH:MM): ").strip())
    fim = converter_para_minutos(input("Horario de termino (HH:MM): ").strip())

    if inicio is None or fim is None:
        print("Use horarios validos no formato HH:MM.")
    elif fim <= inicio:
        print("O termino precisa acontecer depois do inicio no mesmo dia.")
    else:
        duracao = fim - inicio
        print(f"Duracao do evento: {duracao // 60} hora(s) e {duracao % 60} minuto(s).")
        break
