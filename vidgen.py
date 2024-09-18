import os
import requests
import tenor
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

def save_gif_from_url(url, output_path1):
    try:
        # Send a GET request to the URL to fetch the GIF content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)

        # Ensure that the output directory exists
        os.makedirs(os.path.dirname(output_path1), exist_ok=True)

        # Write the GIF content to the output file
        with open(output_path1, 'wb') as f:
            f.write(response.content)

        print(f"GIF saved to {output_path1}")
    except Exception as e:
        print(f"Error saving GIF: {e}")

def add_audio_to_looping_mp4(gif_path, audio_path, output_path):
    # Load the GIF
    gif_clip = VideoFileClip(gif_path)

    # Load the audio clip
    audio_clip = AudioFileClip(audio_path)

    # Calculate the number of times the GIF should loop to match the audio duration
    num_loops = int(audio_clip.duration / gif_clip.duration) + 1

    # Create a list of GIF clips to concatenate
    gif_clips = [gif_clip] * num_loops

    # Concatenate the GIF clips to create a looping GIF
    looping_gif_clip = concatenate_videoclips(gif_clips)

    # Set the duration of the GIF clip to match the duration of the audio clip
    looping_gif_clip = looping_gif_clip.subclip(0, audio_clip.duration)

    # Set the audio of the GIF clip
    looping_gif_clip = looping_gif_clip.set_audio(audio_clip)

    # Write the combined clip as an MP4 file
    looping_gif_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

    # Close the clips
    looping_gif_clip.close()
    audio_clip.close()


# Set gif_url and paths
gif_url = tenor.fetchURL("mordecai")
print(gif_url)
output_path1 = "tenorfetch\\input.gif"
save_gif_from_url(gif_url, output_path1)

gif_path = output_path1
audio_path = "regular-show-intro_GiLyViP.mp3"
output_path = 'output_with_audio.mp4'
add_audio_to_looping_mp4(gif_path, audio_path, output_path)