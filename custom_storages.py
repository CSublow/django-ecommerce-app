from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION # Use STATICFILES_LOCATION from settings.py
    
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION # Use MEDIAFILES_LOCATION from settings.py