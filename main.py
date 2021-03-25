from pytube import YouTube
import click, time, os
from cuttpy import Cuttpy

api = Cuttpy("02d674f39d1af11c7c5343a599b5e4070ffc5")
linkYT = str(input("Podaj link do filmu, który chcesz pobrać: "))
yt = YouTube(linkYT)
miniaturka = yt.thumbnail_url
video = yt.streams.filter(only_audio=True).first()
rozmiar = video.filesize
cuttly = api.shorten(miniaturka) # miniaturka skrocona
rozmiarCzytelny = round(rozmiar / 1048576,2)
nazwa = video.default_filename

if yt.age_restricted == False:
    ograniczenia = "Brak"
else:
    ograniczenia = "Występują"

print ("Link do filu: " + linkYT)
print("Tytuł filmu: " + yt.title)
print("Ograniczenia wiekowe: " + ograniczenia)
print("Rozmiar pliku: " + str(rozmiarCzytelny) + "mb")
print("Miniatrua filmu: " + cuttly.shortened_url) # miniaturka skrocona

video.download()
base, ext = os.path.splitext(nazwa)
new_file = base + '.mp3'
os.rename(nazwa, new_file)
time.sleep(5)
# https://youtu.be/iioqPp64HT4