import json, pyaudio
from vosk import Model, KaldiRecognizer


model = Model('small_model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer["text"]:
                yield answer["text"]

def recording():
    print("Начало записи!")
    for text in listen():
        if text != "":
            print(text)
            return text