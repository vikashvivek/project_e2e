import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename.co_filename
    error_message ="error occurred in python script name [{0}] in line no [{1}] with error message;[{2}]".format(file_name,exc_ab.tb_lineno,error)
    file_name,rec_tb.tb_lineno,str(error)
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

    if __name__ == '__main__':
        try:
            a=1/0
        except Exception as e:
            logging.info("Divide by zero")
            raise CustomException(e,sys)