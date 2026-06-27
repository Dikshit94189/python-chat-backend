# print("Settings.py loaded")

# # This imports the function that reads the .env file.
# from dotenv import load_dotenv

# # Python stores environment variables inside the operating system.
# import os

# # Load .env file
# load_dotenv()

# # DB URL 
# DATABASE_URL = os.getenv("DATABASE_URL")

# # JWT SETTINGS
# JWT_SECRET = os.getenv("JWT_SECRET")
# JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

from dotenv import load_dotenv
import os

print("Settings.py loaded")

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

print("DATABASE_URL =", DATABASE_URL)
print("JWT_SECRET =", JWT_SECRET)
print("JWT_ALGORITHM =", JWT_ALGORITHM)