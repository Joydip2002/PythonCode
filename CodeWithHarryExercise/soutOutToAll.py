# import win32com.client as wincl

# speaker_number = 1
# spk = wincl.Dispatch("SAPI.SpVoice")
# vcs = spk.GetVoices()
# SVSFlag = 11
# print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
# spk.Voice
# spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
# spk.Speak("Hello, Joydip Manna")

import win32com.client as wc

speaker = wc.Dispatch("SAPI.SpVoice")
name = ["Joydip Manna","Suman Rajak","Tanumoy Das"]
l = len(name)
# print(l)
for i in range(l):
    speaker.speak(f"Sout Out For! {name[i]}")
    print(f"Sout Out For!,{name[i]}")
