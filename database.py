import config as cfg
import subprocess

def dump():
    fn = cfg.TMP_DIR + cfg.DB_FILENAME
    command = [
        'mysqldump',
        '-u', cfg.DB_USER,
        ('--password=%s' % cfg.DB_PASS),
        '--single-transaction',
        cfg.DB_NAME,
        '>', fn
    ]

    subprocess.call(' '.join(command), shell=True)
