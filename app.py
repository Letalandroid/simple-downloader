import pytube
import os

def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

link = input("Enter the link: ")
yt = pytube.YouTube(link)

print("Downloading...")
print("Title: " + yt.title)
print("Author: " + yt.author)
print("Duration: " + str(segundos_a_segundos_minutos_y_horas(yt.length)))

yt_streams = yt.streams
filter = yt_streams.filter(abr="320kbps", progressive=False)
stream = yt_streams.first()
os.makedirs("downloads", exist_ok=True)
stream.download("./downloads", filename=yt.title + ".mp3")
print("Downloaded")