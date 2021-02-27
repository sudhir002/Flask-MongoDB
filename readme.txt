// author - sudhir kumar
// date - 27-02-2021


Technology Used
    Python > 3
    mongoDB

*   In /generate_record API here i am doing Mandetory fields validation also.

imp - read Python_Test 2021.pdf for request data details

1.  /generate_record
        reuest data -
            for song
                {
                    "file_type": "song",
                    "song_name": "xyz",
                    "song_duration": 300
                }
            for podcast
                {
                    "file_type": "podcast",
                    "podcast_name": "Sudpod1",
                    "podcast_duration": 200,
                    "host": "Sudhir",
                    "Participants" : ["", "", "", ""]
                }
            for audiobook
                {
                    "file_type": "audiobook",
                    "audiobook_title": "abc",
                    "audiobook_duration": 200,
                    "audiobook_author": "xyz",
                    "audiobook_narrator": "xyz"
                }
        response -
        {
            "status_code": 200,
            "status": "sucess",
            "message": "uploaded sucess!"
        }

2.  /delete/<file_type>/<file_id>
        response
            {
                "status_code": 200,
                "status": "sucess",
                "message": "record deleted with ID x"
            }

3.  /update/<file_type>/<file_id>
         request
            same as generate_record api
         response
            {
                "status_code": 200,
                "status": "sucess",
                "message": "updated sucess!"
            }


4.  /get_audio_data/<file_type>/<file_id>
        response:
            {
                "status_code": 200,
                "status": " sucess",
                "AudioBookTitle": "xyz"
            }


