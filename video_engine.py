from gtts import gTTS
from moviepy.editor import ColorClip, TextClip, CompositeVideoClip, AudioFileClip

def create_video(script):
    # Text to Speech
    tts = gTTS(text=script, lang="en")
    tts.save("voice.mp3")

    audio = AudioFileClip("voice.mp3")

    # Background (9:16)
    background = ColorClip(
        size=(1080, 1920),
        color=(12, 12, 12),
        duration=audio.duration
    ).set_audio(audio)

    # Channel Name Overlay
    watermark = TextClip(
        "@YourChannelName",
        fontsize=60,
        color="white",
        method="caption",
        size=(1080, None)
    ).set_position(("center", "bottom")).set_duration(audio.duration)

    final_video = CompositeVideoClip([background, watermark])
    final_video.write_videofile(
        "output.mp4",
        fps=30,
        codec="libx264",
        audio_codec="aac"
    )
