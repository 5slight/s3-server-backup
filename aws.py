import config as cfg
import minio
import os
from datetime import datetime, date

def __timestamp():
    n = datetime.now()
    return n.strftime(cfg.DATE_FORMAT)

def __is_weekly():
    today = date.today()
    d = today.isoweekday()
    return d == cfg.WEEKLY_DAY

def __get_s3():
    return minio.Minio('s3.amazonaws.com',
                access_key=cfg.AWS_ACCESS,
                secret_key=cfg.AWS_SECRET)

def push():
    s3 = __get_s3()
    fn = cfg.TMP_DIR + cfg.TMP_FILE_NAME
    stat = os.stat(fn)

    prefix = ''
    if __is_weekly():
        prefix = cfg.WEEKLY_PREFIX
    else:
        prefix = cfg.NIGHTLY_PREFIX

    s3path = cfg.AWS_BUCKET_FOLDER + prefix + __timestamp() + '.tar.gz'

    with open(fn, 'rb') as f:
        s3.put_object(cfg.AWS_BUCKET, s3path, f, stat.st_size)

def __list_objects(s3, prefix, ret):
    objs = s3.list_objects(cfg.AWS_BUCKET,
                           cfg.AWS_BUCKET_FOLDER + prefix, False)

    sobjs = sorted(objs, lambda o: o.last_modified, reverse=True)
    return sobjs[ret: ]

def __remove_objs(s3, objs):
    objs = list(map(lambda o: o.object_name, objs))
    s3.remove_objects(cfg.AWS_BUCKET, objs)

def retention():
    s3 = __get_s3()
    objs = None

    if __is_weekly():
        objs = __list_objects(s3, cfg.WEEKLY_PREFIX, cfg.RETENTION_WEEKLY)
    else:
        objs =__list_objects(s3, cfg.WEEKLY_PREFIX, cfg.RETENTION_NIGHTLY)

    __remove_objs(s3, objs)
