import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    ANGER = 'anger'
    DISGUST = 'disgust'
    FEAR = 'fear'
    JOY = 'joy'
    SADNESS = 'sadness'
    DOMINANT_EMOTION = 'dominant_emotion'
    emotions_res = {ANGER : 0, DISGUST : 0, FEAR : 0, JOY : 0, SADNESS : None, DOMINANT_EMOTION : None}
    if (response.status_code == 400):
        em_keys = emotions_res.keys()
        for key in em_keys:
            emotions_res[key] = None
        return emotions_res
    response_json = json.loads(response.text)
    for emotion_dic in response_json["emotionPredictions"]:
        emotions = emotion_dic["emotion"]
        dominant_emotion_score = 0
        for emotion_name, emotion_score in emotions.items():
            if (emotion_name == ANGER):
                emotions_res[ANGER] = emotion_score
            elif (emotion_name == DISGUST):
                emotions_res[DISGUST] = emotion_score
            elif (emotion_name == FEAR):
                emotions_res[FEAR] = emotion_score
            elif (emotion_name == JOY):
                emotions_res[JOY] = emotion_score
            elif (emotion_name == SADNESS):
                emotions_res[SADNESS] = emotion_score
            
            if (emotion_score > dominant_emotion_score):
                emotions_res[DOMINANT_EMOTION] = emotion_name
                dominant_emotion_score = emotion_score
        
        break
    return emotions_res
