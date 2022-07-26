from io import StringIO
import sys

class Calculator:

    def __init__(self,*errors):
        self.errors=errors
        
    def __enter__(self):
        return self

    def __exit__(self,error_type,error,error_traceback_message):
        self.error= error
        return isinstance(error, self.errors)
        

