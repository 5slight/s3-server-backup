#! /usr/bin/python2
import logging as l
import os

import config as cfg
import tar
import database as db
import aws

def cleanup():
    os.remove(cfg.TMP_DIR + cfg.DB_FILENAME)
    os.remove(cfg.TMP_DIR + cfg.TMP_FILE_NAME)

l.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%I:%M:%S',
                    level=l.INFO)

l.info('Starting database dump...')
db.dump()
l.info('Database dump complete!')

l.info('Creating archive...')
tar.open_tar()

tar.add_directories()
tar.add_db()

tar.close_tar()
l.info('Archive created!')

l.info('Pushing archive to S3...')
aws.push()
l.info ('Archive pushed to S3!')

l.info('Removing old backups...')
aws.retention()
l.info('Old backups removed!')

l.info('Cleaning up temporary files...')
cleanup()
l.info('Temporary files removed!')
