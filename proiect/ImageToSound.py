from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def hilbert_curve(order):
    """Generate Hilbert curve coordinates."""
    if order == 0:
        return np.array([[0, 0]])

    prev = hilbert_curve(order - 1)
    size = 2 ** (order - 1)
    # Quadrants
    q1 = np.dot(prev, [[0, -1], [1, 0]]) + [0, size - 1]
    q2 = prev + [0, size]
    q3 = prev + [size, size]
    q4 = np.dot(prev, [[0, 1], [-1, 0]]) + [size - 1, size - 1]
    return np.vstack([q1, q2, q3, q4])

def image_to_hilbert(image_path, order):
    """Map an image's pixels to a 1D array based on the Hilbert curve."""
    img = Image.open(image_path).convert('L')  # Grayscale
    img = img.resize((2**order, 2**order))  # Resize to match Hilbert curve
    pixels = np.array(img)

    # Get Hilbert curve coordinates
    curve = hilbert_curve(order)
    curve = curve[curve[:, 0] < pixels.shape[0]]  # Clip out-of-bounds
    hilbert_values = pixels[curve[:, 1], curve[:, 0]]  # Map pixels to Hilbert curve
    return hilbert_values


from scipy.io.wavfile import write
import numpy as np

def pixels_to_sound(pixels, sample_rate=44100, duration=5):
    """Convert pixel values to sound."""
    num_samples = sample_rate * duration
    x = np.linspace(0, len(pixels), num_samples, endpoint=False).astype(int)
    audio = np.interp(x, [0, 255], [-1, 1])  # Normalize to [-1, 1]
    audio = audio * np.sin(2 * np.pi * np.cumsum(audio) / sample_rate)  # Modulate as sine wave
    return (audio * 32767).astype(np.int16)  # Convert to 16-bit PCM

def save_sound(filename, audio, sample_rate=44100):
    """Save audio to a WAV file."""
    write(filename, sample_rate, audio)

def main(image_path, order, output_audio_path):
    pixels = image_to_hilbert(image_path, order)
    audio = pixels_to_sound(pixels)
    save_sound(output_audio_path, audio)
    print(f"Sunetul a fost salvat în {output_audio_path}")

if __name__ == "__main__":
    image_path = input("Introduceți calea imaginii (ex: imagine.png): ")
    order = int(input("Introduceți ordinul curbei lui Hilbert (ex: 5): "))
    output_audio_path = "hilbert_audio.wav"
    main(image_path, order, output_audio_path)
