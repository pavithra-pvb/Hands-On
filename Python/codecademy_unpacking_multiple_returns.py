def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper


the_scream, the_whisper = scream_and_whisper("Hello World!")

print(the_scream)
print(the_whisper)

