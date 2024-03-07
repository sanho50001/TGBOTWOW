import torch
import sounddevice as sd
import time
import os
language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'xenia'
device = torch.device('cpu')
text = 'Это слишком долгое и очень затянутое воспроизведение текста, так, что я хотел уснуть"'

torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
                                   local_file)

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)
sample_rate = 48000

audio_paths = model.save_wav(text=text,
                             speaker=speaker,
                             sample_rate=sample_rate)

# print(audio)