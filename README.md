# Walrus detector

## Content
1. [Task](#task)
2. [Results](#results)
3. [Assembling](#assembling)
4. [Usage](#usage)
---
## Task ##
The Nenets walrus population is tracked by
taking pictures of individuals with a drone and their 
subsequent manual counting. It takes a lot of human resources.
Here we provide an algorithm for automatically counting.

---
## Results ##
![Header](https://github.com/Glebbs/walrus-detector/blob/main/walr.jpg)

---
## Assembling ##
1. Install python3.9, [link](https://www.python.org/downloads/)
2. Clone project `git clone https://github.com/qvntz/walrus-detector.git walrus && cd walrus`
3. Install dependencies `pip install -r requirements.txt`
4. Download weights into root directory https://drive.google.com/file/d/11ltQ3723Y8E8OdLlkpADapGPLUpDVAm9/view?usp=sharing
5. Launch `python main.py`

---
## Usage ##
![Header](https://github.com/qvntz/walrus-detector/blob/main/image_2022-05-29_05-41-15.png)
1. Choose a folder with images to process
2. Click "сохранить результат" and choose path to save processed images
3. Wait a while
