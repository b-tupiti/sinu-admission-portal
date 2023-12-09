from io import BytesIO
from b2sdk.v2 import B2Api
from abc import ABC, abstractmethod

class AbstractDownloadManager(ABC):
    """
    Abstract base class for downloading files from cloud storage.
    """
    
    def __init__(self, key_id, secret_key, bucket) -> None:
        self.key_id = key_id
        self.secret_key = secret_key
        self.bucket = bucket
        self.api = self._initiate_connection()
    
    @abstractmethod
    def _initiate_connection(self):
        pass
    
    @abstractmethod
    def download_file_of_instance_by_attribute(self, instance, file_attribute):
        pass



class BackBlazeDownloadManager(AbstractDownloadManager):
    """
    Download Manager for BackBlaze cloud storage.
    """
    
    def download_file_of_instance_by_attribute(self, instance, attribute):
        
        filename = getattr(instance, attribute).name
          
        file_info = self.api.get_file_info_by_name(
            self.bucket, 
            filename
        )
        
        buffer = BytesIO()
        self.api.download_file_by_id(file_info.id_).save(buffer)

        return filename, buffer
    
    
    def _initiate_connection(self):
        api = B2Api()
        api.authorize_account("production", self.key_id, self.secret_key)
        return api