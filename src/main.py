import gpt
import transcript

def main():
  youtube_id = transcript.get_transcript("https://youtu.be/4b4MUYve_U8?si=O6zV7S7WqCQXEih5")
  gpt.print_chat_completion(youtube_id)

if __name__ == "__main__":
  main()