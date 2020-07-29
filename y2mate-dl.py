#Example Used y2mate API

import requests, sys, os
from tqdm import tqdm

#os.system('clear')
try:
	os.mkdir('result')
except: pass

def downld(url,judul):
	r = requests.get(url, stream=True)
	total_size = int(r.headers.get('content-length', 0))
	print(f"\n# Downloading {judul}")
#	print(f"['{url}']")
	block_size = 1024
	t=tqdm(total=total_size, unit='iB', unit_scale=True)
	with open(f'result/{judul.replace("/",",")}','wb') as f:
		for data in r.iter_content(chunk_size=block_size):
			if data:
				t.update(len(data))
				f.write(data)
	t.close()
	print('\n[OK] File saved in result\n')

print("""
	[Y2MATE DOWNLOADER]
	     -noobie-
""")

base="https://nuubi.herokuapp.com"

url = input("[In] Youtube URL: ")
tipe = int(input("1. download MP3\n2. download MP4\n[In] Pilih: "))
if tipe == 1:
	tipe = 'mp3'
elif tipe == 2:
	tipe = 'mp4'
else:
	sys.exit("[!] Lihat pilihannya COK!!!!!!")

resu = requests.get(f"{base}/api/y2mate/check_reso/{tipe}?url={url}").json()['result']

n=1
for x,y in resu.items():
	if tipe == 'mp4':
		print(f"{n}. {x} | {y}")
	elif tipe == 'mp3':
		print(f"{n}. {x}")
	n+=1

if len(resu) == 0:
	sys.exit('[!] Tidak dapat menemukan video')

pil = int(input("[In] Pilih: "))
if tipe == 'mp3':
	qualy=list(resu.values())[pil-1]
elif tipe == 'mp4':
	qualy=list(resu.keys())[pil-1].split(' ')[0]

down = requests.get(f"{base}/api/y2mate/download/{tipe}?url={url}&quality={qualy}")
if down.json()['status'] == 'success':
	downld(down.json()['url'], down.json()['judul'])
else:
	print(f"Error: {down.text}")