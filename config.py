import os

# Flask configuration
env = os.environ.get('FLASK_ENV') or 'development'
DEBUG = env == 'development'

# Supabase configuration
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
