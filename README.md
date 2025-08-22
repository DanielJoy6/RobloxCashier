This project is a Python automation tool that uses convolutional neural networks (CNNs) and PyAutoGUI to simulate the mouse clicks and decision-making process needed when playing a specific cashier-based game on Roblox.

Features:
* Predicts cash/card using CNN
* Reads digits from game image
* Simulates mouse clicks to dispense correct change

The folder "Images" contains screenshots that were used to train the cardorcash CNN model
The folder "Images2" contains screenshots that were used to train the digit recognition model

Workflow:
1. roblox_supermarket_neural_networks.py trains 2 models: Card/Cash classifier & digit recognition
2. CashierAgent.py takes screenshots, uses pyautogui to simulate mouse clicks, uses CNN to predict digits

Requirements:
* Python
* pyautogui
* pydirectinput
* numpy
* pillow
* keras
* tensorflow

Future work:
* Capturing additional digit screenshots. Currently the model only recognizes the symbols "1", "3", "6", "0", "$"
* Experiment with smaller Model architecture to reduce loading & prediction times while maintaining accuracy.
* Dynamic screenshot/mouse coordinates based on monitor size 
* General speed optimizations

Topics: Convolutional Neural Networks, Machine Learning, Python
Libraries: PyAutoGui, DirectInput, Keras, Tensorflow
