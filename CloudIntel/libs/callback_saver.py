# importing necessary modules

from django.core.files.base import ContentFile
from django.conf import settings
from django.shortcuts import render
import os

# declaing the class which saves the call back function 

class CallBackSaver:
    """
    This class is used to save the callback function defined by the user on web interface
    
    """
    def __init__(self, function_text, request):
        self.__function_text = function_text
        self.CALLBACK_FUNCTION_DIR = getattr(settings, "CALLBACK_FUNCTION_DIR", None)
        self.CALLBACK_TEMPLATE_DIR = getattr(settings, "CALLBACK_TEMPLATE_DIR", None)
        filepath = os.path.join(self.CALLBACK_TEMPLATE_DIR,"callback_template.txt")
        lines= self.__function_text.splitlines()
        rend = render(request,"callback_template.txt",{"class_name":"sample","lines":lines})
        self.__function_text=rend.content
        print(rend.content)
        print(type(rend.content))
    
    def save(self, file_name):

        # for testing
        print(self.__function_text)
        try:
            # open a new file
            fileloc= os.path.join(self.CALLBACK_FUNCTION_DIR,file_name)
            file = open(fileloc, 'wb+')
            file.write(self.__function_text)
            file.close()

            return True
        
        except Exception as e:
            print(e)
            print("could not save the callback function")
