from flask import Flask, render_template,request
import requests


app = Flask('spotify')



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('ram')
      
        spotify="this is trail"
        print(spotify)
        print(data)


        token = 'BQB-A3FfJbUq56Xf1tOyIP5DY0kX4AwQrhe3UxRrqiSR_cnHRotJKqcoK0oM7co8wmVnnWv6nW_g2p_JgyDYZrtkeqOJLc9o9tSwsnoG2CJ5Maz3GsxVyJrQv3n7EuAKJedoiuVuMcdRT-AQjYBM6z30iWWLEnuOn52FPUn1fvRksPCnbi2_gvCphGvlkhLN_ZTGoft86JgcPLgI-sM'


        user_headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        user_params = {
            "limit": 50
        }
     


        user_profile_response = requests.get(f'https://api.spotify.com/v1/me', params=user_params, headers=user_headers)
        user_dict= user_profile_response.json()
        

        user_tracks_response = requests.get(f'https://api.spotify.com/v1/search?q={data}&type=artist', params=user_params, headers=user_headers)
       
        account=user_dict['display_name']
        aimg = user_dict['images'][0]['url']
        print(aimg)
        result= user_tracks_response.json()
        # print(result['artists']['items'][0])
        ima = result['artists']['items'][0]['images'][0]['url']
        name =  result['artists']['items'][0]['name']
        id = result['artists']['items'][0]['id']
        
     
        user_track_albums = requests.get(f'https://api.spotify.com/v1/artists/{id}/albums?offset=5' ,params=user_params, headers=user_headers)
        tracks = user_track_albums.json()

      
        # print(user_track_albums.json())
       
        final = result['artists']['items'][0]['external_urls']['spotify']
        return render_template('index.html',user_track_albums=tracks ,aimg=aimg,account=account,  data=data , final=final ,ima=ima, name=name)   
    else:
        return render_template("index.html")




# testing





app.run(port=8000)