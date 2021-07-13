
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
from features import *


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            web_link=str(request.form['link'])
            print(web_link)
            model = int(request.form['model'])
            print(model)

            data=featureExtraction(web_link)
            print(data)

            if model==1:
                filename = 'DecisionTree.pickle'
                loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
                # predictions using the loaded model file
                prediction=loaded_model.predict([data])
                print('prediction is', prediction[0])
            else:

                filename = 'RandomForest.pickle'
                loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
                # predictions using the loaded model file
                prediction=loaded_model.predict([data])
                print('prediction is', prediction[0])
            if prediction[0]==1:
                return render_template('result.html', pred =True  ,link=web_link )
            else:
                 return render_template('result.html', pred =False  ,link=web_link )
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=False) # running the app