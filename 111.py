import requests

url = "https://notify-api.line.me/api/notify"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

data = {
    "message": "New file uploaded from GitHub!"
}

# 获取 GitHub 文件的原始链接（raw link）
github_raw_url = "https://github.com/vulc8/test_1_line"

response = requests.get(github_raw_url)
if response.status_code == 200:
    file_data = response.content

    # 发送通知，并附带文件数据
    response = requests.post(url, headers=headers, data=data, files={"file": file_data})
    print(response.text)
else:
    print("Failed to fetch file from GitHub.")
