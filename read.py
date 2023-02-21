from easy_paddle_ocr import TextRecognizer
import time
import cv2

text_recognizer = TextRecognizer() # for custom weights do TextRecognizer(weights='folder_path')
images = ['broadway.jpeg', 'brooklyn.jpeg', 'casino.jpeg']

for filename in images:
  image = cv2.imread(filename)
  start = time.time()
  prediction = text_recognizer.read(image)
  print(f'\n[+] image: {filename}')
  print(f'[+] text: {prediction["text"]}')
  print(f'[+] confidence: {int(prediction["confidence"]*100)}%')
  print(f'[+] inference time: {int((time.time() - start)*1000)} milliseconds')

print()