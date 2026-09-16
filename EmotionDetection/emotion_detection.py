import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    response_json = json.loads(response.text)
    emotions = {}
    for emotion_dic in response_json["emotionPredictions"]:
        emotions = emotion_dic["emotion"]
        dominant_emotion = ""
        dominant_emotion_score = 0
        for emotion_name, emotion_score in emotions.items():
            if(emotion_score > dominant_emotion_score):
                dominant_emotion = emotion_name
                dominant_emotion_score = emotion_score
        emotions["dominant_emotion"] = dominant_emotion
        break
    return emotions
