import sys
import logging

def error_message_detail(error: Exception, error_detail: sys):
    '''Extracts the error information including file name, line number and details from an exception.'''

    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    line_number = exc_tb.tb_lineno

    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"

    logging.error(error_message)

    return error_message

class MyException(Exception):
    '''Custom exception class that logs the error message when an exception is raised.'''
    
    def __init__(self, error: Exception, error_detail: sys):
        '''Initializes the custom exception with the error message.'''
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        '''Returns the error message when the exception is converted to a string.'''
        return self.error_message
    
