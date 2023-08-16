import os
import redis
from dir import Dir
from myredis import RedisQueue

photos_dir = Dir("photos")

photos_dir.read()
photos = photos_dir.spisok_files

phot = RedisQueue('photo')
for photo in photos:
    razmer = os.path.getsize(photo)
    phot.put(razmer)


while True:
    c = phot.get()
    if c is not None:
        print(c.decode('utf-8'))
    else:
        break

a = 1
