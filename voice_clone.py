# First install required packages
# pip install TTS torchaudio soundfile

import torch
import torchaudio
from TTS.api import TTS

def validate_hindi_text(text):
    """Basic validation for Hindi text"""
    # Check if text contains Devanagari characters
    devanagari_range = ('\u0900', '\u097F')
    if not any(ord(char) >= ord(devanagari_range[0]) and ord(char) <= ord(devanagari_range[1]) for char in text):
        raise ValueError("Input text doesn't contain valid Hindi (Devanagari) characters")

def clone_hindi_voice(reference_audio_path, hindi_text, output_path):
    """
    Clone voice for Hindi text using reference audio
    
    Args:
        reference_audio_path: Path to reference speaker's audio (min 5-10 seconds of clean speech)
        hindi_text: Hindi text to speak (in Devanagari script)
        output_path: Where to save generated audio (WAV format)
    """
    # Validate input
    validate_hindi_text(hindi_text)
    
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    # Initialize TTS with multilingual model
    # This model supports Hindi and voice cloning
    tts = TTS("tts_models/multilingual/multi-dataset/your_tts").to(device)
    
    # Generate speech with voice cloning
    print("Processing Hindi text and generating speech...")
    tts.tts_to_file(
        text=hindi_text,
        speaker_wav=reference_audio_path,
        language="hi",  # Hindi language code
        file_path=output_path
    )
    
    print(f"Successfully generated cloned Hindi voice at: {output_path}")

if __name__ == "__main__":
    # Example usage
    try:
        reference_audio = "sha.wav"  # Replace with your audio file
        hindi_text = "नमस्ते, यह मेरी क्लोन की हुई आवाज़ है। कृपया इस तकनीक का उपयोग जिम्मेदारी से करें।"
        output_file = "hindi_cloned_voice.wav"
        
        clone_hindi_voice(reference_audio, hindi_text, output_file)
        
        # Play the generated audio (optional)
        import sounddevice as sd
        import soundfile as sf
        
        data, fs = sf.read(output_file)
        print("Playing generated audio...")
        sd.play(data, fs)
        sd.wait()
        
    except Exception as e:
        print(f"Error: {str(e)}")