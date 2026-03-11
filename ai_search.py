from sentence_transformers import SentenceTransformer
import json

# model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

with open("video_data.json") as f:
    videos = json.load(f)

video_vectors = [model.encode(v["text"]) for v in videos]

def search_video(query):
    query_vector = model.encode(query)

    best_index = 0
    best_score = 0

    for i, vector in enumerate(video_vectors):
        score = sum(query_vector * vector)
        if score > best_score:
            best_score = score
            best_index = i

    return videos[best_index]
# from sentence_transformers import SentenceTransformer
# import json

# model = None
# videos = None
# video_vectors = None


# def load_resources():
#     global model, videos, video_vectors

#     if model is None:
#         print("Loading AI model...")
#         model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

#     if videos is None:
#         print("Loading video data...")
#         with open("video_data.json") as f:
#             videos = json.load(f)

#     if video_vectors is None:
#         print("Encoding videos...")
#         video_vectors = [model.encode(v["text"]) for v in videos]


# def search_video(query):
#     load_resources()

#     query_vector = model.encode(query)

#     best_index = 0
#     best_score = 0

#     for i, vector in enumerate(video_vectors):
#         score = sum(query_vector * vector)
#         if score > best_score:
#             best_score = score
#             best_index = i

#     return videos[best_index]