import config as cfg
import subprocess

def __run(c): subprocess.call(' '.join(c), shell=True)

def __dump_mysql(fn):
    __run([
        'mysqldump',
        '-u', cfg.DB_USER,
        ('--password=%s' % cfg.DB_PASS),
        '--single-transaction',
        cfg.DB_NAME,
        '>', fn
    ])


def __dump_postgres(fn):
    __run([
        'pg_dump',
        ('--username=%s' % cfg.DB_USER),
        ('--password=%s' % cfg.DB_PASS),
        ('--dbname=%s' % cfg.DB_NAME)
    ])

def dump():
    fn = cfg.TMP_DIR + cfg.DB_FILENAME
    dbs = {
        "mysql": __dump_mysql,
        "postgres": __dump_postgres
    }
    f = dbs.get(cfg.DB_TYPE, lambda f: False)
    return f(fn)
