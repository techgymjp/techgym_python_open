import numpy as np
import wave
import struct

def generate_tone(filename, freq=440, duration_ms=200, volume=0.5, sample_rate=44100):
    n_samples = int(sample_rate * duration_ms / 1000)
    t = np.linspace(0, duration_ms / 1000, n_samples, False)
    tone = np.sin(freq * 2 * np.pi * t) * volume

    # 16bit PCMデータに変換
    audio = (tone * 32767).astype(np.int16)

    with wave.open(filename, "w") as f:
        f.setparams((1, 2, sample_rate, n_samples, "NONE", "not compressed"))
        for sample in audio:
            f.writeframes(struct.pack('h', sample))

# 例：各効果音の生成
generate_tone("shoot.wav", freq=800, duration_ms=100, volume=0.4)
generate_tone("hit.wav", freq=600, duration_ms=150, volume=0.5)
generate_tone("player_hit.wav", freq=300, duration_ms=300, volume=0.5)
generate_tone("win.wav", freq=1000, duration_ms=500, volume=0.6)
generate_tone("lose.wav", freq=200, duration_ms=500, volume=0.6)

print("効果音ファイルを生成しました。")
