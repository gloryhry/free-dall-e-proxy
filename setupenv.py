import os
import urllib.request

def download_file(url, filepath):
    # 下载文件
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"File downloaded successfully: {filepath}")
    except Exception as e:
        print(f"Failed to download the file: {e}")

def setupenv():
    # 提供一个默认值，如果环境变量不存在，则使用默认值
    url = os.getenv('ENV_URL', 'https://gist.githubusercontent.com/test/.env') # 由docker环境读取
    print(url)
    filename = os.path.join('data','.env')
    download_file(url, filename)

if __name__ == "__main__":
    setupenv()