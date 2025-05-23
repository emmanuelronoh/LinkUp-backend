import os
import django
from django.db import connection

# Set the correct settings module for your project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# This is now required in newer Django versions
django.setup()

try:
    with connection.cursor() as cursor:
        cursor.execute("DROP SCHEMA public CASCADE")
        cursor.execute("CREATE SCHEMA public")
        cursor.execute("GRANT ALL ON SCHEMA public TO linkup_u9i3_user")
        cursor.execute("GRANT ALL ON SCHEMA public TO public")
    print("Database reset successfully!")
except Exception as e:
    print(f"Error resetting database: {e}")