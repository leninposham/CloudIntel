# importing necessary modules
import importlib

 # declaring class for handling dynamic module imports

class lib_loader():
    def __init__(self, module_name,class_name):
        """
         Tries importing the module based on the full path value
         throws error when import fails
        """

        try:
            self.module = importlib.import_module(module_name)
            self.get_class_object = getattr(self.module,class_name)
        
        except:
            print("Failed to import the module {} from {}".format(class_name,module_name))