'''
copy video url: https://www.youtube.com/watch?v=gmvvaobm7eQ&list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw
video id : v=gmvvaobm7eQ
'''
from openai import OpenAI

from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse,parse_qs #to get the video_id dynamically

from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key= os.getenv("openai_key")
)

videoUrl = input("Provide video url: ")
videoUrl = urlparse(videoUrl)
videoID = parse_qs(videoUrl.query)['v'][0]

yt = YouTubeTranscriptApi() #helps to get video transcript
transcript = yt.fetch(video_id= videoID)

video_transcript = ""

video_transcript = "\n".join(it.text for it in transcript)
# print(f"video transcript: {video_transcript}")

print("Ask something about the video...")
while True:
    _input = input("You: ")
    if _input.strip().lower() in ["exit", "quit"]:
        exit(0)
    
    response = client.chat.completions.create(
        model = "gpt-5.4-mini",
        messages = [
            {
                "role": "system",
                "content":'''
                You are expert youtube video analysis agent.
                answer only relavant informatoin available in provided youtube video transcript.
                answer regarding video like how many people were talking, about what topic they talked etc.
                apart from that reply: "No info available regarding that.
                '''
            },
            {
                "role": "user",
                "content":f'''
                YouTube Video Transcript : {video_transcript},
                Quention : {_input}
                answer user queries properly.
                '''
            }
        ]
    )
    msg = response.choices[0].message.content
    print("Agent: ", msg)
