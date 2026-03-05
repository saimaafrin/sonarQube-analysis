def build_app_logger(name='app', logfile='app.log', debug=True):
# Importing the logging library
	import logging
	
	# Create a logger object
	logger = logging.getLogger(name)
	
	# Set the level of logger
	if debug:
		logger.setLevel(logging.DEBUG)
	else:
		logger.setLevel(logging.INFO)
	
	# Create a file handler which logs even debug messages
	fh = logging.FileHandler(logfile)
	fh.setLevel(logging.DEBUG)
	
	# Create a console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.ERROR)
	
	# Create formatter and add it to the handlers
(formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
fh.setFormatter(formatter)
ch.setFormatter(formatter)
	
	# Add the handlers to the logger
	logger.addHandler(fh)
	logger.addHandler(ch)
	
	return logger