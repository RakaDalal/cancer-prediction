
from flask import render_template, request, Flask
from werkzeug import secure_filename
#from PIL import Image
from keras.models import model_from_json
import numpy as np
from keras.preprocessing import image
import os 

app = Flask(__name__)

#setting the upload folder app->templates->test_images 
##could add a configuration to check for uploaded file formats 
##and filter out files that are not images
UPLOAD_FOLDER = 'templates/test_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")

def prediction(classifier, test_image):
    test_image = image.img_to_array(test_image)
    test_image = test_image.astype('float32')/255
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    if result[0][0] >= 0.5:
        prediction = 'NON-CANCEROUS'
    else:
        prediction = 'CANCEROUS'
    return (prediction)

#main page that comes up first 
@app.route('/')
@app.route('/index')
def index():
	#renders the templade with Choose File and Submit buttons
    return render_template('upload.html', title='Home')

#the page that loads after the upload with function output
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
    	#requesting the file from the upload
    	f = request.files['file']
    	image_name = f.filename
    	#concatenates file path from upload folder defined above and the image name
    	image_path = app.config['UPLOAD_FOLDER'] + "/" + secure_filename(image_name)
       	#saving the file inside the specified biosight folder 
    	f.save(image_path)
        test_image = image.load_img(image_path, target_size = (64, 64))
        result= prediction(loaded_model, test_image)
    	#removing the image
        os.remove(image_path)
        #renders the template for displaying the image manipulation
        return render_template('post.html', result = result)

