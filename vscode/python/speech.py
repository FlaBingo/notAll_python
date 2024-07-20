"""Synthesizes speech from the input string of text."""
from google.cloud import texttospeech as ts

client = ts.TextToSpeechClient()

input_text = ts.SynthesisInput(text="This code creates a basic, responsive e-commerce webpage. You can replace the placeholder images and links with actual Amazon affiliate product images and links. If you need more customization.")

# Note: the voice can also be specified by name.
# Names of voices can be retrieved with client.list_voices().
voice = ts.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Studio-O",
)

audio_config = ts.AudioConfig(
    audio_encoding=ts.AudioEncoding.LINEAR16,
    speaking_rate=1
)

response = client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config}
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')