import numpy as np
from scipy.io.wavfile import write
from PIL import Image

# Frecvențe pentru gama C Major (Do, Re, Mi, Fa, Sol, La, Si)
C_MAJOR = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]  # Hz

# Funcție pentru maparea intensității unui pixel la o notă muzicală
def intensity_to_note(intensity):
    index = int((intensity / 255) * (len(C_MAJOR) - 1))  # Normalizează intensitatea
    return C_MAJOR[index]

# Generarea punctelor din curba lui Hilbert
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

# Generarea unei melodii din datele imaginii, folosind curba lui Hilbert
def generate_melody(image_data, duration_per_pixel=0.05, sample_rate=44100):
    n = int(np.log2(min(image_data.shape[:2])))  # Determinăm ordinul curbei lui Hilbert
    hilbert_points = hilbert_curve(n)
    audio_data = []

    for (x, y) in hilbert_points:
        if x < image_data.shape[0] and y < image_data.shape[1]:
            intensity = image_data[x, y]  # Extragem intensitatea pixelului
            freq = intensity_to_note(intensity)  # Mapăm intensitatea la o frecvență

            # Generăm undă sinusoidală pentru frecvență
            t = np.linspace(0, duration_per_pixel, int(sample_rate * duration_per_pixel), endpoint=False)
            wave = 0.5 * np.sin(2 * np.pi * freq * t)
            audio_data.append(wave)

    return np.concatenate(audio_data)

# Conversia imaginii în sunet folosind intensitățile de gri și curba lui Hilbert
def image_to_sound(image_path, output_path="output_sound.wav", duration_per_pixel=0.05):
    # Deschidem imaginea și o convertim în tonuri de gri
    image = Image.open(image_path).convert("L")
    image_data = np.array(image)  # Transformăm imaginea în array numpy

    # Generăm melodia
    melody = generate_melody(image_data, duration_per_pixel)

    # Salvăm rezultatul ca fișier WAV
    write(output_path, 44100, np.int16(melody * 32767))
    print(f"Sunetul a fost salvat în '{output_path}'.")

# Exemplu de rulare
def main():
    image_path = input("Introduceți calea imaginii: ")
    output_path = "grayscale_melodic_sound.wav"
    image_to_sound(image_path, output_path)

if __name__ == "__main__":
    main()
