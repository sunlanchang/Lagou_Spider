import requests
import base64
password = "bipt184755"
en_pass = password.encode(encoding="utf-8")
encodestr = base64.b64encode(en_pass)
url = 'http://210.31.32.126/srun_portal_pc_succeed.php?ac_id=2&username=5120150752&ip=10.10.13.63&access_token=6df09905ec038c99e5e0313a431bd53b528317a595ef6be3795fb4d1d6c647aa'
params = {
    'ac_id': '2',
    'username': '5120150752',
    'ip': '10.10.13.63',
    'access_token': encodestr
}
res = requests.get(url, params=params)
# print(res.text)
print(params)
