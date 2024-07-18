from pygame import mixer # type: ignore
import asyncio
import re

#The function convert_time is used to convert a time string into the total number of seconds.
def convert_time(time_str):
    if time_str.isdigit():
        return int(time_str)

    parts = list(map(int, re.split('[:]', time_str)))

    if len(parts) == 3:
        horas, minutos, segundos = parts
    elif len(parts) == 2:
        horas = 0
        minutos, segundos = parts
    else:
        raise ValueError("Formato de tiempo no válido. 'Usa hh:mm:ss' o 'mm:ss'.")
    
    return horas * 3600 + minutos * 60 + segundos

#The function timer is used to play the sound for default when the "timesleep" it's over.
async def timer():
    time_str = input("Ingrese el tiempo (hh:mm:ss o mm:ss): ")

    try:
        time = convert_time(time_str)

        await asyncio.sleep(time)

        mixer.init()
        mixer.music.load("alarma.mp3")
        mixer.music.play()

        print('¡El tiempo ha sido completado!')

        while mixer.music.get_busy():
            await asyncio.sleep(1)

    except ValueError as e:
        print(f"Error {e} ")
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(timer())