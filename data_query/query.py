import os
import json
import datetime
import db_connection.dbconnect as db

def generate_record(file_type, metadata):
    try:
        if file_type.lower() == "song":
            collection = db.dbconnect()["songs_information"]  # collection name is songs_information
            if list(collection.find({"SongName": metadata["song_name"]})):
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "duplicate found"})
            uploaded_time = datetime.datetime.now()
            collection.insert({"ID": collection.count()+1,
                              "SongName": metadata["song_name"],
                               "SongDuration" : metadata['song_duration'],
                               "UploadedTime": uploaded_time})
            return json.dumps({"status_code": 200, "status": "sucess", "message": "songs uploaded sucess!"})

        if file_type.lower() == "podcast":
            collection = db.dbconnect()["podcast_information"]  # collection name is podcast_information
            if list(collection.find({"PodcastName": metadata["podcast_name"]})):
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "duplicate found"})
            uploaded_time = datetime.datetime.now()
            collection.insert({"ID": collection.count()+1,
                               "PodcastName": metadata["podcast_name"],
                               "PodcastDuration" : metadata['podcast_duration'],
                               "Host": metadata['host'],
                               "Participants": metadata['Participants'],
                               "UploadedTime": uploaded_time})
            return json.dumps({"status_code": 200, "status": "sucess", "message": "podcast uploaded sucess!"})

        if file_type.lower() == "audiobook":
            collection = db.dbconnect()["audiobook_information"]  # collection name is audiobook_information
            if list(collection.find({"AudioBookTitle": metadata["audiobook_title"]})):
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "duplicate found"})
            uploaded_time = datetime.datetime.now()
            collection.insert({"ID": collection.count()+1,
                               "AudioBookTitle": metadata["audiobook_title"],
                               "AudioBookDuration" : metadata['audiobook_duration'],
                               "Author": metadata['audiobook_author'],
                               "Narrator": metadata['audiobook_narrator'],
                               "UploadedTime": uploaded_time})
            return json.dumps({"status_code": 200, "status": "sucess", "message":"audiobook uploaded sucess!"})
    except Exception as e:
        print(e)
        return json.dumps({"status_code": 400, "status": "not sucess", "message": "something went wrong"})



def delete_record(file_type, file_id):
    try:
        if file_type.lower() == "song":
            collection = db.dbconnect()["songs_information"]  # collection name is songs_information
            collection.delete_one({"ID": file_id})
            return json.dumps({"status_code": 200, "status": "sucess", "message": "record deleted with ID {}".format(file_id)})
        if file_type.lower() == "podcast":
            collection = db.dbconnect()["podcast_information"]  # collection name is podcast_information
            collection.delete_one({"ID": file_id})
            return json.dumps({"status_code": 200, "status": "sucess", "message": "record deleted with ID {}".format(file_id)})
        if file_type.lower() == "audiobook":
            collection = db.dbconnect()["audiobook_information"]  # collection name is audiobook_information
            collection.delete_one({"ID": file_id})
            return json.dumps({"status_code": 200, "status": "sucess", "message": "record deleted with ID {}".format(file_id)})
    except Exception as e:
        print(e)
        return json.dumps({"status_code": 400, "status": "not sucess", "message": "something went wrong"})



def update_record(file_type, file_id, metadata):
    try:
        if file_type.lower() == "song":
            collection = db.dbconnect()["songs_information"]  # collection name is songs_information
            if not list(collection.find({"ID": file_id})):
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "Wrong ID!"})
            uploaded_time = datetime.datetime.now()
            collection.update_one({"ID": file_id},
                                  {"$set": {"SongName": metadata["song_name"],
                               "SongDuration": metadata['song_duration'],
                               "UploadedTime": uploaded_time}})
            return json.dumps({"status_code": 200, "status": "sucess", "message": "songs updated sucess!"})

        if file_type.lower() == "podcast":
            collection = db.dbconnect()["podcast_information"]  # collection name is podcast_information
            if not list(collection.find({"ID": file_id})):
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "Wrong ID!"})
            uploaded_time = datetime.datetime.now()
            collection.insert({"ID": file_id},
                              {"$set": {"PodcastName": metadata["podcast_name"],
                               "PodcastDuration": metadata['podcast_duration'],
                               "Host": metadata['host'],
                               "Participants": metadata['Participants'],
                               "UploadedTime": uploaded_time}})
            return json.dumps({"status_code": 200, "status": "sucess", "message": "podcast updated sucess!"})

        if file_type.lower() == "audiobook":
            collection = db.dbconnect()["audiobook_information"]  # collection name is audiobook_information
            if not list(collection.find({"ID": file_id})):
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "Wrong ID!"})
            uploaded_time = datetime.datetime.now()
            collection.insert({"ID": file_id},
                              {"$set": {"AudioBookTitle": metadata["audiobook_title"],
                               "AudioBookDuration": metadata['audiobook_duration'],
                               "Author": metadata['audiobook_author'],
                               "Narrator": metadata['audiobook_narrator'],
                               "UploadedTime": uploaded_time}})
            return json.dumps({"status_code": 200, "status": " sucess", "message": "audiobook updated sucess!"})
    except Exception as e:
        print(e)
        return json.dumps({"status_code": 400, "status": "not sucess", "message": "something went wrong"})



def get_audio_data(file_type, file_id):
    try:
        if file_type.lower() == "song":
            collection = db.dbconnect()["songs_information"]  # collection name is songs_information
            data = list(collection.find({"ID": file_id}))
            if not data :
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "Wrong ID!"})

            return json.dumps({"status_code": 200, "status": "sucess", "audio_file": data[0]["SongName"]})

        if file_type.lower() == "podcast":
            collection = db.dbconnect()["podcast_information"]  # collection name is podcast_information
            data = list(collection.find({"ID": file_id}))
            if not data:
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "Wrong ID!"})

            return json.dumps({"status_code": 200, "status": "sucess", "PodcastName": data[0]["PodcastName"]})

        if file_type.lower() == "audiobook":
            collection = db.dbconnect()["audiobook_information"]  # collection name is audiobook_information
            data = list(collection.find({"ID": file_id}))
            if not data:
                return json.dumps({"status_code": 400, "status": "not sucess", "message": "Wrong ID!"})

            return json.dumps({"status_code": 200, "status": " sucess", "AudioBookTitle": data[0]["AudioBookTitle"]})
    except Exception as e:
        print(e)
        return json.dumps({"status_code": 400, "status": "not sucess", "message": "something went wrong"})
