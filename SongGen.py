import random
import sys
import pandas as pd
import pyttsx3
from flask import Flask




def getSongsFromArtist(artist):
    df = pd.DataFrame()
    df = pd.read_csv("C:\\Users\\Admin\\PycharmProjects\\CUHacking\\songdata.csv")
    list = df[df.artist == artist].text
    return list

def songsToWords(songs):
    lyrics = ""
    for row in songs:
        lyrics = lyrics + row
    words = lyrics.split()
    return words

def generateDict(artist):
    nonword = "\n"  # Since we split on whitespace, this can never be a word
    w1 = nonword
    w2 = nonword
    table = {}
    songs = getSongsFromArtist(artist)
    words = songsToWords(songs)

    for word in words:
        table.setdefault((w1, w2), []).append(word)
        w1, w2 = w2, word

    table.setdefault((w1, w2), []).append(nonword)
    return table

def generateMarkkovChain(table, words):
    nonword = "\n"  # Since we split on whitespace, this can never be a word
    # GENERATE OUTPUT
    w1 = nonword
    w2 = nonword

    maxwords = words

    wordList = []

    for i in range(maxwords):
        newword = random.choice(table[(w1, w2)])
        if newword == nonword: sys.exit()
        print(newword, end=" ")
        wordList.append(newword)
        w1, w2 = w2, newword
    return wordList

app = Flask(__name__)
@app.route('/<artist>')
def speakANewSong(artist):
    dictOfWords = generateDict(artist)

    song = generateMarkkovChain(dictOfWords, 100)

    skip = True
    otherskip = True

    for i in range(len(song)):
        if song[i][-1] in ',?!.' and otherskip:
            song[i] = song[i] +"\n"
            if otherskip:
                otherskip = False
            else:
                otherskip = True
        if i+1!=len(song):
            if song[i+1][0] == song[i+1][0].upper() and song[i+1][0].upper() != "I" and skip:
                song[i] = song[i] + "\n"
                if skip:
                    skip = False
                else:
                    skip = True


    print(" ".join(song))
    f = open("song.txt", "w")
    f.write(" ".join(song))

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(" ".join(song))
    engine.runAndWait()


