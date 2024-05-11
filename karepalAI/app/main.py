from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
import google.generativeai as genai
from dotenv import load_dotenv
import os
from flask_cors import CORS
import PIL.Image
import pickle
from requests_oauthlib import OAuth1Session
import json
import telebot
from telebot import types
import hexebaML

load_dotenv(".env")
gkey = os.getenv("GOOGLE_KEY")

binance_key = os.getenv("BINANCE-KEY")
binance_secret = os.getenv("BINANCE-SECRET")

admincode = os.getenv("ADMIN_CODE")
telegrambotapi = os.getenv("TELEGRAM_API")

clicktablename = os.getenv("CLICK_TABLE_NAME")
password = os.getenv("SERVER2_PASSWORD")
url = os.getenv("URL")
remote_server = hexebaML.mysqlconnect(url,password)





bot = telebot.TeleBot(telegrambotapi)
genai.configure(api_key=gkey)

model1 = genai.GenerativeModel("gemini-pro")








app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")
api = Api(app)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

class Receivechat(Resource):
    def post(self):
        code = request.form["admincode"]
        if code == admincode:
            msg = request.form["chatsent"]
            responsex = model1.generate_content(str(msg))
            return responsex.text
api.add_resource(Receivechat, "/receivechat")

class Sendtweet(Resource):
    def post(self):
        try:
            code = request.form["admincode"]
            if code == admincode:
                message = request.form["tweetmesage"]
            # if(state=="real"):
                load_dotenv()

                # Load the oauth variable from the saved file using pickle
                with open("oauth.pkl", "rb") as file:
                    oauth = pickle.load(file)
            
                tweet_text = message
                print(tweet_text)


                # Payload for the tweet
                payload = {"text": tweet_text}

                # Making the request
                response = oauth.post(
                    "https://api.twitter.com/2/tweets",
                    json=payload,
                )

                if response.status_code != 201:
                    raise Exception(
                        "Request returned an error: {} {}".format(response.status_code, response.text)
                    )

                print("Response code: {}".format(response.status_code))

                # Saving the response as JSON
                json_response = response.json()
                print(json.dumps(json_response, indent=4, sort_keys=True))
    
           # return "Successful"
            
                msg = "Successful"
                return jsonify({'message': "{}".format(msg)})
            else:
                return jsonify({'message': 'Invalid admin code'})
        except Exception as e:
            return jsonify({'error': str(e)})      
            # responsex = model1.generate_content(str(msg))
            # return responsex.text
api.add_resource(Sendtweet, "/sendtweet")


class Telegrammessage(Resource):
    def post(self):
        try:
            code = request.form["admincode"]
            if code == admincode:
                message = request.form["telegrammessage"]
                chatid = request.form["chatid"]
                bot.send_message(chatid,message)
                msg = "Successful"
                return jsonify({'message': "{}".format(msg)})
            else:
                return jsonify({'message': 'Invalid admin code'})
        except Exception as e:
            return jsonify({'error': str(e)})         

api.add_resource(Telegrammessage, "/telegrammessage")

class Receiveimage(Resource):
    def post(self):
        try:
            code = request.form["admincode"]
            if code == admincode:
                msg = request.form["chatsent"]
                filedata = request.files['file']
                filenamex = request.form["filename"]
                filedata.save(os.path.join('upload', filenamex))
                
                # img = PIL.Image.open(os.path.join('upload', filenamex))
                img = PIL.Image.open(('upload/{}'.format(filenamex)))
                model2 = genai.GenerativeModel("gemini-pro-vision")
                responsey = model2.generate_content([msg,img])
                # responsey = model1.generate_content(str(msg))
               # return responsey.text
                
                return jsonify({'message': "{}".format(responsey.text)})
            else:
                return jsonify({'message': 'Invalid admin code'})
        except Exception as e:
            return jsonify({'error': str(e)})
api.add_resource(Receiveimage, "/receiveimage")

# class Testmarket(Resource):
#     def get(self):
#         m = hexeba_binance.check_price(binance_key,binance_secret,"BTCUSDT")
#         return jsonify({'Btc-Price': str(m)})
# api.add_resource(Testmarket, "/testmarket")

class Testmessage(Resource):
    def get(self):
        m="CONNECTED"
        return jsonify({'message': str(m)})
api.add_resource(Testmessage, "/testmessage")

# class Trackclick(Resource):
#     def post(self):
#    #     buttonname = request.form["buttonname"]
#         buttonname = request.json.get('buttonname')
#         tablename = clicktablename
#         remote_server.track_click(tablename,buttonname)
#         m="Click Registered"
#         return jsonify({'message': str(m)})
# api.add_resource(Trackclick, "/trackclick")


@app.route('/trackclick', methods=['POST','GET'])
def track_click():
    # Extract buttonname from the request JSON data
    buttonname = request.json.get('buttonname')
    tablename = clicktablename
    columndatastring = "column1=buttonname&column2=clicks&column3=clickdate"
    columnnumber = 3
    try:
        remote_server.create_table(tablename,columnnumber,columndatastring,)
    except Exception as e:
        print(e)
    
    
    remote_server.track_click(tablename,buttonname)
    # Do something with the buttonname, such as saving it to a database
    # For now, let's just print it
    print("Button Name:", buttonname)

    # Return a JSON response indicating success
    return jsonify({"message": "Button click tracked successfully"})






# if __name__ == "__main__":
#     app.run(debug=True)
class Receiveimage2(Resource):
    def post(self):
        try:
            code = request.form["admincode"]
            if code == admincode:
                msg = request.form["chatsent"]
                filedata = request.files['file']
                filenamex = request.form["filename"]
                filedata.save(os.path.join('upload', filenamex))
                
                # img = PIL.Image.open(os.path.join('upload', filenamex))
                img = PIL.Image.open(('upload/{}'.format(filenamex)))
                model2 = genai.GenerativeModel("gemini-pro-vision")
                responsey = model2.generate_content([msg,img])
                # responsey = model1.generate_content(str(msg))
               # return responsey.text
                
                return jsonify({'message': "{}".format(responsey.text)})
            else:
                return jsonify({'message': 'Invalid admin code'})
        except Exception as e:
            return jsonify({'error': str(e)})
api.add_resource(Receiveimage2, "/getimage")