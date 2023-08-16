import os
from dir import Dir
from mypostgersql import Postgres
from myredis import RedisQueue
import threading


def write_redis(db_redis):
    photos_dir = Dir("photos")
    photos_dir.read()

    for photo in photos_dir.spisok_files:
        razmer = os.path.getsize(photo)
        db_redis.put(razmer)

    db_redis.finished = True


def write_postgres(db_postgres, db_redis):
    db_postgres.create_table()

    while True:

        photo_from_redis = db_redis.get()

        if photo_from_redis is not None:
            print(photo_from_redis.decode('utf-8'))
            photo = photo_from_redis.decode('utf-8')

            db_postgres.insert(photo)

        if photo_from_redis is None and db_redis.finished:
            break



redis_queue = RedisQueue("asd")
postgres_db = Postgres("Pictures")



# init threads
t1 = threading.Thread(target=write_redis, args=(redis_queue,))
t2 = threading.Thread(target=write_postgres, args=(postgres_db, redis_queue,))


# start threads
t1.start()
t2.start()


# join threads to the main thread
t1.join()
t2.join()

postgres_db.close_database()
