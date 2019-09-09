import requests

r = requests.post("http://127.0.0.1:6201/", json={"test_A_files": "/home/xt/Documents/data/UGATIT/dataset/selfie2anime/testA/AB.jpg"})
print(r)
print(r.text)
