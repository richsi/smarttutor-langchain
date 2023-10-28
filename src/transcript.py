import re
from youtube_transcript_api import YouTubeTranscriptApi 

def get_transcript(youtube_url):


  # youtube_url = "https://youtu.be/iR2O2GPbB0E?si=Pd53jg7lDcX__FZg"
  # youtube_url = "https://youtu.be/SnpAAX9CkIc?si=dMlL5Fw7k4r7XuZY"
  match = re.search(r"be/([^?]+)", youtube_url)

  if match:
      video_id = match.group(1)
      srt = YouTubeTranscriptApi.get_transcript(video_id)

      file_name = video_id + ".txt"
      path = 'data/' + file_name

      with open(path, 'w') as f:
        f.write(str(srt))
      
      return file_name
  else:
      print("Video ID not found in the URL.")
      return None




