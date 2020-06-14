# -*- Coding: UTF-8 -*-
#coding: utf-8
#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import pyaudio

def connect_asr():
    model = Model("model")
    rec = KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    return p, stream, rec
