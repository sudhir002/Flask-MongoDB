import os
import json
from flask import Flask, request
import data_query.query as query

app = Flask(__name__)


@app.route('/generate_record')
def generate_record():
    try:
        req = request.json
        audio_file_type = req["file_type"]
        '''______________________mandetory field validation_________________________'''
        if audio_file_type.lower() == "song":
            if "song_name" in list(req.keys()) and "song_duration" in list(req.keys()):
                if type(req["song_name"]) != str:
                    return json.dumps({"status_code": 400, "status": "not sucess", "message": "request parameters are not valid (song name should be in string"})
                if len(req["song_name"]) > 100 or len(req["song_name"]) == 0:
                    return json.dumps({"status_code": 400, "status": "not sucess", "message": "request parameters are not valid-(song name length max 100 char"})
                if type(req["song_duration"]) != int:
                    return json.dumps({"status_code": 400, "status": "not sucess", "message": "request parameters are not valid-(song duration should be in integer"})
                if req["song_duration"] <0:
                    return json.dumps({"status_code": 400, "status": "not sucess", "message": "request parameters are not valid-(song duration should not be in negetive"})
            else:
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "not valid request data"})

        if audio_file_type.lower() == "podcast":
            if "podcast_name" in list(req.keys()) and "podcast_duration" in list(req.keys()) and "host" in list(req.keys()):
                if type(req["podcast_name"]) != str:
                    return json.dumps({"status_code": 400, "status": "not sucess", "message": "request parameters are not valid ( name should be in string"})
                if len(req["podcast_name"]) >100 or len(req["podcast_name"]) ==0:
                    return json.dumps({"status_code": 400, "status": "not sucess", "message": "request parameters are not valid-( name length max 100 char"})
                if type(req["podcast_duration"]) != int:
                    return json.dumps({"status_code": 400, "status": "not sucess", "message": "request parameters are not valid-( duration should be in integer"})
                if req["podcast_duration"] <0:
                    return json.dumps({"status_code": 400, "status": "not sucess", "message": "request parameters are not valid-( duration should be in posotive"})
                if type(req["host"]) != str:
                    return json.dumps({"status_code": 400, "status": "not sucess", "message": "request parameters are not valid-(host should be in string"})
                if len(req["host"]) >100:
                    return json.dumps({"status_code": 400, "status": "not sucess", "message": "request parameters are not valid-(host length not more then 100"})
            else:
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "not valid request data"})

        if audio_file_type.lower() == "audiobook":
            if "audiobook_title" in list(req.keys()) and "audiobook_duration" in list(req.keys()) and "audiobook_author" in list(req.keys()) and "audiobook_narrator" in list(req.keys()):
                print(len(req["audiobook_title"]))
                if type(req["audiobook_title"]) != str:
                    return json.dumps({"status_code": 400, "status": "not sucess","message": "request parameters are not valid-(title should be in string"})
                if len(req["audiobook_title"]) >100 or len(req["audiobook_title"]) ==0 :
                    return json.dumps({"status_code": 400, "status": "not sucess","message": "request parameters are not valid-(title should not have length more then 100 char"})
                if type(req["audiobook_duration"]) != int:
                    return json.dumps({"status_code": 400, "status": "not sucess","message": "request parameters are not valid-( duration should be in integer"})
                if req["audiobook_duration"] <0:
                    return json.dumps({"status_code": 400, "status": "not sucess","message": "request parameters are not valid-( duration should be positive"})
                if type(req["audiobook_author"]) != str:
                    return json.dumps({"status_code": 400, "status": "not sucess","message": "request parameters are not valid-(audiobook_author should be in string"})
                if len(req["audiobook_author"]) >100 or len(req["audiobook_author"]) == 0:
                    return json.dumps({"status_code": 400, "status": "not sucess","message": "request parameters are not valid-(audiobook_author should not have lenght more then 100 char"})
                if type(req["audiobook_narrator"]) != str:
                    return json.dumps({"status_code": 400, "status": "not sucess","message": "request parameters are not valid-(audiobook_narrator should be in string"})
                if len(req["audiobook_narrator"]) >100 or len(req["audiobook_narrator"]) == 0:
                    return json.dumps({"status_code": 400, "status": "not sucess","message": "request parameters are not valid-(audiobook_narrator should not have char more then 100"})
            else:
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "not valid request data"})

        '''___________________________________________________________________________'''

        res = query.generate_record(audio_file_type, req)
        return res
    except Exception as e:
        print(e)
        return json.dumps({"status_code": 400, "status": "not sucess", "message": "something went wrong"})


@app.route('/delete/<file_type>/<file_id>')
def delete(file_type, file_id):
    try:
        if file_type.lower() not in ["song", "podcast", "audiobook"]:
            return json.dumps({"status_code": 400, "status": "not sucess", "message": "audio file type is not correct"})
        res = query.delete_record(file_type, int(file_id))
        return res
    except Exception as e:
        print(e)
        return json.dumps({"status_code": 400, "status": "not sucess", "message": "something went wrong"})



@app.route('/update/<file_type>/<file_id>')
def update(file_type, file_id):
    try:
        if file_type.lower() not in ["song", "podcast", "audiobook"]:
            return json.dumps({"status_code": 400, "status": "not sucess", "message": "audio file type is not correct"})
        res = query.update_record(file_type, int(file_id), request.json)
        return res
    except Exception as e:
        print(e)
        return json.dumps({"status_code": 400, "status": "not sucess", "message": "something went wrong"})



@app.route('/get_audio_data/<file_type>/<file_id>')
def get_audio_data(file_type, file_id):
    try:
        if file_type.lower() not in ["song", "podcast", "audiobook"]:
            return json.dumps({"status_code": 400, "status": "not sucess", "message": "audio file type is not correct"})
        res = query.get_audio_data(file_type, int(file_id))
        return res
    except Exception as e:
        print(e)
        return json.dumps({"status_code": 400, "status": "not sucess", "message": "something went wrong"})



if __name__ == '__main__':
    app.run(port= 3332, host= "localhost")