# Walrus detector

## Content
1. [Task](#task)
2. [Assembling](#assembling)
3. [Usage](#usage)
---
## Task ##
Отслеживание популяции ненецких моржей происходит путем 
съемки особей с беспилотника и последующим их ручным подсчетом
по фото. Это занимает большое количество человеко-ресурсов. 
Необходимо реализовать алгоритм автоматического подсчета моржей
по фотографии.


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
