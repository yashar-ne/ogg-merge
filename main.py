from pydub import AudioSegment
import os
import natsort

from pyrogram import Client


out_filename = 'all.mp3'
directory = '/path/to/dir'

audios = []
for filename in natsort.natsorted(os.listdir(directory)):
    f = os.path.join(directory, filename)
    
    if os.path.isfile(f) and filename.endswith(".ogg"):
        print(f"Processing {f}")
        audios.append(AudioSegment.from_ogg(f))
    
comb = audios[0]
for a in audios[1:]:
    comb += a
    
comb.export(os.path.join(directory, out_filename), format="mp3")
