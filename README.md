# cancer-prediction

# Description:
I have used a CNN architecture to train a model for classifying brain MRI images - cancerous or healthy. The training accuracy is 99.14% and validation accuracy is 97.64%. The training.py contains the code for training the model. The trained model is saved on disk and used for prediction. Prediction.py contains the code for prediction. UI.py contains the code for a simple UI that asks to upload an image and then makes a prediction - cancerous or healthy.


# How to run:

Step 1: To install all required packages:

pip install -r requirements.txt

Step 2: To run the User Interface:

export FLASK_APP=UI.py

flask run

# Test-images
The folder Unit_Testing contains two sub folders- healthy and cancerous. Both subfolders contain some images which can be used to test the UI.
