from gtts import gTTS
from moviepy.editor import ColorClip, AudioFileClip

def create_video(script):
    # Voice
    tts = gTTS(text=script, lang="en")
    tts.save("voice.mp3")

    audio = AudioFileClip("voice.mp3")

    # Simple 9:16 background (NO TextClip)
    video = ColorClip(
        size=(1080, 1920),
        color=(15, 15, 15),
        duration=audio.duration
    ).set_audio(audio)

    video.write_videofile(
        "output.mp4",
        fps=30,
        codec="libx264",
        audio_codec="aac"
    )
