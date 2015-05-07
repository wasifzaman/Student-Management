import sqlite3
import datetime
import shutil
import configparser
import sys, os

sys.path.append(os.path.abspath(os.pardir) + '\database')

class Database:

	def create_open_database(self, new_db=False, current=False):
		config = configparser.ConfigParser()
		configfile = os.path.abspath(os.pardir) + '\database\db_config.ini'
		config.read(configfile)
		if not config['DB_SETTINGS']['currentdatabase']:	#false on start
			if not new_db:
				return False
			shutil.copy(os.path.abspath(os.pardir) + config['DB_SETTINGS']['templatepath'], new_db)
			if current:
				config['DB_SETTINGS']['currentdatabase'] = new_db
				with open(configfile, 'w') as configfile_:
					config.write(configfile_)
		if not os.path.exists(config['DB_SETTINGS']['currentdatabase']):
			return False
		self.conn = sqlite3.connect(config['DB_SETTINGS']['currentdatabase'])
		self.cur = self.conn.cursor()


d = Database()
#d.create_open_database(new_db=os.path.abspath(os.pardir) + '\database\\test.db', current=True)
d.create_open_database()