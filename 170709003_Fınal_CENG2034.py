'''
Osman Batuhan Şahin
'''
import os
import requests
import signal
import uuid
from multiprocessing import Pool
import hashlib




"""
n = os.fork()
if (n == 0):
    print("Child process id is : ", os.getpid())
if (n > 0):
    print("parent : ", os.getpid())
    os.kill(os.getpid(), signal.SIGSTOP)
print("pid is", os.getpid())
"""
arr = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg","https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg","http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]

array1 = ["1","2","3","4","5"]
unique = []
not_unique = []
seen = set()
hashlist = []

'''
def downloadf(url):
        filename = None
        r = requests.get(url, allow_redirects = True)
        h = hashlib.sha256(r.content).hexdigest()
        file = filename if filename else str(uuid.uuid4())
        open(file, 'wb').write(r.content)
        hashlist.append(h)
'''
def downloadf(url,file_name = None):
	r = requests.get(url, allow_redirects = True)
	file = file_name if file_name else str(uuid.uuid4())
	open(file, 'wb').write(r.content) 
 
j = 0
n = os.fork()
if (n == 0):
    print("Child process id is :", os.getpid())

    for i in range(len(arr)):
        url = arr[i]
       
        downloadf(url, "foto"+array1[j])
        j = j+1

        
    os._exit(0)

os.wait()
print("Parent process id is :", os.getpid())

hashlist.append(hashlib.md5(open("foto1",'rb').read()).hexdigest())
hashlist.append(hashlib.md5(open("foto2",'rb').read()).hexdigest())
hashlist.append(hashlib.md5(open("foto3",'rb').read()).hexdigest())
hashlist.append(hashlib.md5(open("foto4",'rb').read()).hexdigest())
hashlist.append(hashlib.md5(open("foto5",'rb').read()).hexdigest())

print("Hashlist is: ",hashlist)
'''
def list_duplicates(x):
    for i in x:
        if i not in not_unique:
            not_unique.append(i)
    print(not_unique)
def check_duplicates(x):
    len(x) != len(set(x))
    print("There is duplicate")
'''
def is_duplicate(hashlist):
    for i in hashlist:
        if hashlist.count(i) == 2:
            print(i, "has a duplicate")
'''
is_duplicate(hashlist)
'''
with Pool(2) as p:
    (p.map(is_duplicate , hashlist))




"# ceng_2034_2020_final" 
