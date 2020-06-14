# -*- Coding: UTF-8 -*-
#coding: utf-8
#!/usr/bin/env python3

import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
