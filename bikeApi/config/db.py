import os
db_config = {
  'user': os.getenv("DB_USER"),
  'password':  os.getenv("DB_PASSWORD"),
  'host':  os.getenv("DB_HOST"),
  'database': os.getenv("DB_DATABASE"),
  'raise_on_warnings': True
}