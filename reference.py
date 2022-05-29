import torch
import pandas as pd
import tqdm
import glob
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', device='cpu').to('cpu')


def inference(path_to_input_folder, path_to_output_folder, path_to_write_images=None):
    images = sorted(glob.glob(path_to_input_folder + '/*'))
    for img_path in tqdm.tqdm(images):
        image_name = img_path.split('/')[-1].split('\\')[-1]
        res = model(img_path, augment=True, size=1280)
        q = res.pandas().xyxy[0]
        q = q[q['confidence'] > 0.5]
        data = pd.DataFrame([[0, 0]] * len(q), columns=["x", "y"])
        image = cv2.imread(img_path)
        colors = [(64, 224, 208), (100, 149, 237), (204, 204, 255), (159, 226, 191), (222, 49, 99)]
        for i in range(len(q)):
            p = q.loc[i]
            image = cv2.circle(image, (
                int(p['xmin'] + (p['xmax'] - p['xmin']) / 2), int(p['ymin'] + (p['ymax'] - p['ymin']) / 2)), 3,
                               (0, 0, 0),
                               3)
            data["x"][i] = round(p['xmin'] + (p['xmax'] - p['xmin']) / 2)
            data["y"][i] = round(p['ymin'] + (p['ymax'] - p['ymin']) / 2)
        if path_to_write_images:
            cv2.imwrite(path_to_write_images + '/' + image_name, image)
        data.to_csv(path_to_output_folder + '/' + image_name.replace('.jpg', '.csv'), index=False)


inference('C:/Users/Evgeniy/Desktop/walrus_dataset/images', 'G:/PycharmProjects/walrus-detector/csvs',
          'G:/PycharmProjects/walrus-detector/processed_images')
