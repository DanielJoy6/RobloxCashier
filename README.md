This project is a Python file that simulates the typical mouse clicks 
and decision making I would need to do when playing a specific game on Roblox.
Must be run locally to work.

The folder "Images" contains screenshots that were used to train the cardorcash CNN model
The folder "Images2" contains screenshots that were used to train the digit recognition model

Models were trained on Google Colab and take about 2 minutes to train.

Future work:
* Capturing additional digit screenshots. Currently the model only recognizes the symbols "1", "3", "6", "0", "$"
* Adjusting Model architecture. I have not tested decreasing the size of the models for decreasing loading and prediction times
* Changing coordinates to be based on monitor size 
* General speed optimizations

Topics: Convolutional Neural Networks, Machine Learning, Python
Libraries: PyAutoGui, DirectInput, Keras, Tensorflow
