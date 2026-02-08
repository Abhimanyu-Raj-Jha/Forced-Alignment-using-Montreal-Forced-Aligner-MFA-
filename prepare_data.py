import os
import shutil

WAV_DIR = "wav"
TXT_DIR = "transcripts"
CORPUS_DIR = "corpus"

os.makedirs(CORPUS_DIR, exist_ok=True)

wav_files = [f for f in os.listdir(WAV_DIR) if f.endswith(".wav")]

for wav in wav_files:
    utt_id = os.path.splitext(wav)[0]
    txt_path = os.path.join(TXT_DIR, utt_id + ".txt")

    if not os.path.exists(txt_path):
        print(f"Missing transcript for {utt_id}")
        continue

    utt_dir = os.path.join(CORPUS_DIR, utt_id)
    os.makedirs(utt_dir, exist_ok=True)

    shutil.copy(os.path.join(WAV_DIR, wav), utt_dir)
    shutil.copy(txt_path, utt_dir)

print("Corpus prepared successfully")
