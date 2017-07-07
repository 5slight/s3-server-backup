import config as cfg
import tarfile
import os

__tf = None

def open_tar():
    global __tf
    fn = cfg.TMP_DIR + cfg.TMP_FILE_NAME
    flags = 'w:gz'
    __tf = tarfile.open(fn, flags)

def close_tar():
    global __tf
    __tf.close()

def __add_directory(p):
    global __tf
    n = os.path.basename(p)
    __tf.add(p, arcname=n)

def add_directories():
    for d in cfg.DIRECTORIES: __add_directory(d)

def add_db():
    global __tf
    n = cfg.DB_FILENAME
    p = cfg.TMP_DIR + n
    __tf.add(p, arcname=n)
