################################################################################
# Main backup configuration
################################################################################

# Database config
DB_NAME           = ''
DB_USER           = ''
DB_PASS           = ''

# AWS S3 Config
AWS_ACCESS        = ''
AWS_SECRET        = ''
AWS_BUCKET        = ''
AWS_BUCKET_FOLDER = ''

# Dates
WEEKLY_DAY        = 3
DATE_FORMAT       = '%Y%m%d_%H%M'

# Retention - How many backups to keep
RETENTION_NIGHTLY = 2
RETENTION_WEEKLY  = 2

# Locations
TMP_DIR           = '/tmp/'
TMP_FILE_NAME     = 'backup.tar.gz'
DB_FILENAME       = 'database.sql'

NIGHTLY_PREFIX    = 'NIGHTLY'
WEEKLY_PREFIX     = 'WEEKLY'

DIRECTORIES       = [
    ''
]
