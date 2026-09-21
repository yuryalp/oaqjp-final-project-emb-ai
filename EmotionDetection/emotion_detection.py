import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    emotions_res = {'anger' : 0, 'disgust' : 0, 'fear' : 0, 'joy' : 0, 'sadness' : 0, 'dominant_emotion' : None}
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
            if (emotion_name == 'anger'):
                emotions_res['anger'] = emotion_score
            elif (emotion_name == 'disgust'):
                emotions_res['disgust'] = emotion_score
            elif (emotion_name == 'fear'):
                emotions_res['fear'] = emotion_score
            elif (emotion_name == 'joy'):
                emotions_res['joy'] = emotion_score
            elif (emotion_name == 'sadness'):
                emotions_res['sadness'] = emotion_score
            
            if (emotion_score > dominant_emotion_score):
                emotions_res["dominant_emotion"] = emotion_name
                dominant_emotion_score = emotion_score
        
        break
    return emotions_res
