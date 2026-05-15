import soundfile as sf
import pyloudnorm as pyln
import pydub
import tempfile


#pydub.AudioSegment.converter = 'C:/Users/Lucas/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.' \
 #                              'Source_8wekyb3d8bbwe/ffmpeg-8.1.1-full_build/bin/ffmpeg.exe'
#pydub.AudioSegment.ffprobe = "C:/Users/Lucas/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget." \
 #                            "Source_8wekyb3d8bbwe/ffmpeg-8.1.1-full_build/bin/ffprobe.exe"

tempfile.mktemp(suffix='flac', prefix='tmp', dir=None)
data, rate = sf.read("C:/Users/Lucas/PycharmProjects/prespotify/audio test folder/isntitweird.wav")
peak_normalized_audio = pyln.normalize.peak(data, -1.0)
print(data)
print(rate)
meter = pyln.Meter(rate)

lufs = meter.integrated_loudness(data)
print(lufs)

normalizedAudio = pyln.normalize.loudness(peak_normalized_audio, lufs, -14.0)

sf.write('C:/Users/Lucas/PycharmProjects/prespotify/audio test folder/new_file.flac', normalizedAudio, 44100)

fromFlac = pydub.AudioSegment.from_file("C:/Users/Lucas/PycharmProjects/prespotify/audio test folder/new_file.flac",
                                        format="flac")

fromFlac.export("C:/Users/Lucas/PycharmProjects/prespotify/audio test folder/normalized.ogg", format="ogg")

