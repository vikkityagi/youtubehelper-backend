from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from youtube_transcript_api import YouTubeTranscriptApi
from ai_search import search_video

app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Video Recommendation API"}

@app.get("/search")
def search(query: str):
    result = search_video(query)
    url = result['url']
    videoId = url.split("/")[-1].split("?")[0]
    # print(videoId)
    transcript = get_transcript(videoId)
    # print('Trans-script - ',transcript)
    return {
        "video": result,
        "transcript": transcript
    }

# def get_transcript(video_id: str):
#     transcript = YouTubeTranscriptApi.get_transcript(video_id)
#     return transcript

# def get_transcript(video_id: str):

#     ytt_api = YouTubeTranscriptApi()

#     transcript = ytt_api.fetch(video_id)

#     return transcript

def get_transcript(video_id: str):
    try:
        ytt_api = YouTubeTranscriptApi()

        transcript = ytt_api.fetch(video_id, languages=['hi','en'])

        return transcript
    except Exception as e:
        return []