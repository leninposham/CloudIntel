# importing necessary modules

from django.core.files.base import ContentFile
from django.conf import settings

# declaing the class which saves the call back function 

class CallBackSaver:
    """
    This class is used to save the callback function defined by the user on web interface
    
    """
    def __init__(self, function_text):
        self.__function_text = function_text
        self.CALLBACK_FUNCTION_DIR = getattr(settings, "CALLBACK_FUNCTION_DIR", None)
    
    def save(self, file_name):

        # for testing
        print(self.__function_text)
        try:
            # open a new file
            file = open(self.CALLBACK_FUNCTION_DIR+file_name, 'W+')
            file.write(self.__function_text)
            file.close()
            return True
        
        except:
            print("could not save the callback function")
