import os
import sys
import time
import datetime
import logging
from colorama import init
init()
from logging.handlers import RotatingFileHandler
import colorlog
FORMAT = '%(log_color)s%(asctime)s - %(name)s -  [%(levelname)-7s] - %(message)s'
FILE_FORMAT = '%(asctime)s - %(name)s -  [%(levelname)-7s] - %(message)s'

class Logger(object):

    def __init__(self):
        pass
    
    def setup_main_logger(self, name='canmops', console_loglevel=logging.INFO, logger_file=None):
        # Set color  
        streamhandler = colorlog.StreamHandler(sys.stderr)
        streamhandler.setLevel(console_loglevel)
        logger = logging.getLogger(name)
        formatter = self._setup_coloredlogs(logger)
        streamhandler.setFormatter(formatter)
        if not len(logger.handlers):
            # Add Logger level
            logger.setLevel(console_loglevel)
            self._add_success_level(logger)
            self._add_notice_level(logger)
            self._add_warning_level(logger)
            # Add logger file
            if logger_file:
                fh = self.setup_logfile(logger_file, console_loglevel=console_loglevel, format=formatter)
                self._add_logfiles_to(logger, fh)
            logger.propagate = False    
            logger.addHandler(streamhandler)    
        return logger

    def setup_file_logger(self, name='canmops', console_loglevel=logging.INFO, logger_file=None): 
        formatter = logging.Formatter(FILE_FORMAT)
        logger = logging.getLogger(name)
        logger.setLevel(console_loglevel)
        self._add_success_level(logger)
        self._add_warning_level(logger) 
        self._add_notice_level(logger)
        fh = self.setup_logfile(logger_file, console_loglevel=console_loglevel, format=formatter)
        self._add_logfiles_to(logger, fh)
        logger.propagate = False
        return logger
    
    def setup_logfile(self, filename, console_loglevel=logging.INFO, format=FORMAT):
        fh = RotatingFileHandler(filename + 'log', backupCount=10,
                                        maxBytes=10 * 1024 * 1024)
        fh.setLevel(console_loglevel)
        fh.setFormatter(format)
        return fh
    
    def _add_logfiles_to(self, logger, fh):
        fhs = [fh]
        for lg in logging.Logger.manager.loggerDict.values():
            if isinstance(lg, logging.Logger):
                for handler in lg.handlers[:]:
                    if isinstance(handler, logging.FileHandler):
                        fhs.append(handler)
        for fh in fhs:
            logger.addHandler(fh)
                
    def add_logfile_to_loggers(self, fh):
        # Add filehandler to all active loggers
        for lg in logging.Logger.manager.loggerDict.values():
            if isinstance(lg, logging.Logger):
                lg.addHandler(fh)
    
    def close_logfile(self, fh):
        # Remove filehandler from all active loggers
        for lg in logging.Logger.manager.loggerDict.values():
            if isinstance(lg, logging.Logger):
                lg.removeHandler(fh)
    
    def _setup_coloredlogs(self, logger):
        colors = {'DEBUG': 'green',
                  'INFO': 'green',
                  'SUCCESS': 'bold_green',
                  'NOTICE':'cyan',
                  'WARNING': 'white,bg_yellow',
                  'ERROR': 'white,bg_red',
                  'CRITICAL': 'bold_purple'}
        formatter = colorlog.ColoredFormatter(FORMAT, log_colors=colors) 
        return  formatter      
    
    def _add_success_level(self, logger):
        logging.SUCCESS = 45
        logging.addLevelName(logging.SUCCESS, 'SUCCESS')
        logger.success = lambda msg, *args, **kwargs: logger.log(logging.SUCCESS, msg, *args, **kwargs)
    
    def _add_notice_level(self, logger):
        logging.NOTICE = 25
        logging.addLevelName(logging.NOTICE, 'NOTICE')
        logger.notice = lambda msg, *args, **kwargs: logger.log(logging.NOTICE, msg, *args, **kwargs)
    
    def _add_warning_level(self, logger):
        logging.WARNING = 35
        logging.addLevelName(logging.WARNING, 'WARNING')
        logger.warning = lambda msg, *args, **kwargs: logger.log(logging.WARNING, msg, *args, **kwargs)
        
    def _reset_all_loggers(self):
        logging.root.handlers = []
    
if __name__ == "__main__":
    pass