from pydub import AudioSegment

def convert_m4a_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="m4a")
    audio.export(output_file, format="wav")

# Replace with your file paths
input_file = "path_to_your_file.m4a"
output_file = "path_to_your_file.wav"

convert_m4a_to_wav(input_file, output_file)

