import numpy as np
from scipy.io.wavfile import write
from PIL import Image

RANGE_RED = (100, 400)  # Hz
RANGE_GREEN = (400, 1000)  # Hz
RANGE_BLUE = (1000, 4000)  # Hz

def map_color_to_frequency(value, freq_range):
    return freq_range[0] + (value / 255) * (freq_range[1] - freq_range[0])

def hilbert_curve(n):
    def hilbert(x, y, xi, xj, yi, yj, n):
        if n <= 0:
            return [(x + (xi + yi) // 2, y + (xj + yj) // 2)]
        points = []
        points += hilbert(x, y, yi // 2, yj // 2, xi // 2, xj // 2, n - 1)
        points += hilbert(x + xi // 2, y + xj // 2, xi // 2, xj // 2, yi // 2, yj // 2, n - 1)
        points += hilbert(x + xi // 2 + yi // 2, y + xj // 2 + yj // 2, xi // 2, xj // 2, yi // 2, yj // 2, n - 1)
        points += hilbert(x + xi // 2 + yi, y + xj // 2 + yj, -yi // 2, -yj // 2, -xi // 2, -xj // 2, n - 1)
        return points

    size = 2 ** n
    return hilbert(0, 0, size, 0, 0, size, n)

def generate_melody(image_data, duration_per_pixel=0.05, sample_rate=44100):
    n = int(np.log2(min(image_data.shape[:2])))
    hilbert_points = hilbert_curve(n)
    audio_data = []

    for (x, y) in hilbert_points:
        if x < image_data.shape[0] and y < image_data.shape[1]:
            r, g, b = image_data[x, y]
            freq_r = map_color_to_frequency(r, RANGE_RED)
            freq_g = map_color_to_frequency(g, RANGE_GREEN)
            freq_b = map_color_to_frequency(b, RANGE_BLUE)

            t = np.linspace(0, duration_per_pixel, int(sample_rate * duration_per_pixel), endpoint=False)
            wave_r = 0.5 * np.sin(2 * np.pi * freq_r * t)
            wave_g = 0.5 * np.sin(2 * np.pi * freq_g * t)
            wave_b = 0.5 * np.sin(2 * np.pi * freq_b * t)

            combined_wave = wave_r + wave_g + wave_b
            audio_data.append(combined_wave)

    return np.concatenate(audio_data)

def image_to_sound(image_path, output_path="output_sound.wav", duration_per_pixel=0.05):
    image = Image.open(image_path).convert("RGB")
    image_data = np.array(image)

    melody = generate_melody(image_data, duration_per_pixel)

    write(output_path, 44100, np.int16(melody * 32767))
    print(f"Sunetul a fost salvat în '{output_path}'.")

def main():
    image_path = input("Introduceți calea imaginii: ")
    output_path = "color_melodic_sound.wav"
    image_to_sound(image_path, output_path)

if __name__ == "__main__":
    main()
