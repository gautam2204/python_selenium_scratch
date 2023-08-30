import logging

def log_my():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    #Create a file handler
    handler_warn = logging.FileHandler('reports/warning_log.txt')
    handler_warn.setLevel(logging.WARNING)
    
    handler_info = logging.FileHandler('reports/info_log.txt')
    handler_info.setLevel(logging.INFO)
    
    #create a logging format
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler_warn.setFormatter(formatter)
    handler_info.setFormatter(formatter)
    
    
    #add the handler to the logger
    
    logger.addHandler(handler_warn)
    logger.addHandler(handler_info)
    
    
    logger.info('Information')
    logger.warning('warning')
    logger.info("This is log info")
    
if __name__ == "__main__":
    log_my()