#line

import requests
#from PIL import Image
import cv2

url = "https://notify-api.line.me/api/notify"
headers = {
    "Authorization": "Bearer xaWfMfwJgPqMXKDsOH0O0H3qajKtV8YQlWXTHzEpw5N"
}

data = {
    "message": "哈哈哈哈"
}

# 读取影片数据
#video_path = "C:/Users/asus/Desktop/靜靜的/音樂/全職高手/每天回家都會看到我哥在玩榮耀.mp4"
#with open(video_path, "rb") as video_file:
#    video_data = video_file.read()

# 发送通知，并附带影片数据
#response = requests.post(url, headers=headers, data=data, files={"videoFile": video_data})
#print(response.text)
