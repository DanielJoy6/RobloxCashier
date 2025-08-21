import pyautogui
import pydirectinput as directInput
import time
import numpy as np
from PIL import Image
from keras.models import load_model

#Load in both CNN models
cashcardmodel = load_model('cardorcash.keras')
handwritingmodel = load_model('handwritingNN.keras')

#Define area for taking picture of cash/card
Screenshot1 = (1170, 580, 125, 100)

#Function to move the mouse and click at a specific (x,y) coordinate
def moveTo(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.15)
    directInput.moveTo(x+1, y)
    directInput.click()

#Takes picture of specified region and saves to a PNG file
def take_screenshot(region, filename):
    screenshot = pyautogui.screenshot(region=region)
    filename = str(filename) + ".png"
    screenshot.save(filename)
    img = screenshot.convert('RGB')
    return np.array(img.resize((100, 125)), dtype='float32')

#Move to First Item in checkout
time.sleep(1)
moveTo(1400, 790)

#Scan Items by clicking rapidly
for i in range(5):
    pyautogui.click()
    time.sleep(0.3)

#Move to Cash/Card area
moveTo(1230, 660)

#Take screenshot of cash/card
img_array = take_screenshot(Screenshot1, "cashorcard")
img_array = np.expand_dims(img_array, axis=0)

#Get prediction from CNN model
prediction = cashcardmodel.predict(img_array)
print(prediction)
cashorcard = ""

#Split based on card or cash
if(prediction[0][0] == 1): #card
    cashorcard = "card"
    regions = [
    ((685, 583, 20, 40), "tensdigit"),
    ((712, 583, 20, 40), "onesdigit"),
    ((748, 583, 20, 40), "dimes"),
    ((772, 583, 20, 40), "pennies")
    ]
    
elif(prediction[0][1] == 1): #cash
    cashorcard = "cash"
    regions = [
    ((685, 610, 20, 40), "tensdigit"),
    ((707, 583, 20, 40), "onesdigit"),
    ((750, 583, 20, 40), "dimes"),
    ((772, 583, 20, 40), "pennies")
    ]

#Take pictures of 4 digits
total = ""
for coordinates, name in regions:
    image = take_screenshot(coordinates, name)
    prediction = handwritingmodel.predict(np.expand_dims(image, axis=0))
    print(prediction)
    index = np.argmax(prediction)
    print(name, "prediction:", index)
    #Build total
    if(index == 10): #dollar sign
        total += "0"
    else:
        total += str(index)
    if(name == "onesdigit"):
        total += "."

total = float(total)

#Dispense change
if cashorcard == "cash":
    while total >= 50:
        moveTo(1833, 608)  # $50
        time.sleep(0.3)
        total -= 50
    while total >= 20:
        moveTo(1691, 608)  # $20
        time.sleep(0.3)
        total -= 20
    while total >= 10:
        moveTo(1548, 601)  # $10
        time.sleep(0.3)
        total -= 10
    while total >= 5:
        moveTo(1416, 595)  # $5
        time.sleep(0.3)
        total -= 5
    while total >= 1:
        moveTo(1289, 602)  # $1
        time.sleep(0.3)
        total -= 1
    while total >= 0.50:
        moveTo(1841, 848)  # 50¢
        time.sleep(0.3)
        total -= 0.50
    while total >= 0.20:
        moveTo(1692, 844)  # 20¢
        time.sleep(0.3)
        total -= 0.20
    while total >= 0.10:
        moveTo(1562, 834)  # 10¢
        time.sleep(0.3)
        total -= 0.10
    while total >= 0.05:
        moveTo(1417, 842)  # 5¢
        time.sleep(0.3)
        total -= 0.05
    while total >= 0.01:
        moveTo(1293, 837)  # 1¢
        time.sleep(0.3)
        total -= 0.01

#Hit buttons in order of total
elif cashorcard == "card":
    coordinates = [(1524, 855), (1309, 568), (1515, 572), (1731, 562), (1311, 662), (1522, 657), (1718, 653), (1318, 747), (1514, 754), (1725, 759), (1310, 849)]
    total_str = f"{total:.2f}"
    for digit in total_str:
        if(digit == "."):
            moveTo(*coordinates[10]) #Use coordinates at end of list for decimal
        else:
            moveTo(*coordinates[int(digit)]) #Rest of coordinates in list are in numerical order

time.sleep(1)
moveTo(1462, 937) #Hit the okay button
time.sleep(3)
