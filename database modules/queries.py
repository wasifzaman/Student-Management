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
		if 'currentdatabase' not in config['DB_SETTINGS']:	#false on start
			if not new_db:
				return {'state': 'error', 'code': 'D0000'}
			shutil.copy(os.path.abspath(os.pardir) + config['DB_SETTINGS']['templatepath'], new_db)
			if current:
				config['DB_SETTINGS']['currentdatabase'] = new_db
				with open(configfile, 'w') as configfile_:
					config.write(configfile_)
		if not os.path.exists(config['DB_SETTINGS']['currentdatabase']):
			return {'state': 'error', 'code': 'D0001'}
		self.conn = sqlite3.connect(config['DB_SETTINGS']['currentdatabase'])
		self.cur = self.conn.cursor()
		return {'state': 'success'}

	def insert_(self, data, to_table):
		sql_script = 'PRAGMA table_info(' + to_table + ')'
		table_columns = [row[1] for row in self.cur.execute(sql_script)]
		table_values = tuple([data[column_name] \
			if column_name in data else '' for \
			column_name in table_columns])
		value_fill = str(tuple(['?' for i in table_columns])).replace("'", '')
		return {'prefix': 'INSERT INTO ' + to_table + ' VALUES ' + value_fill, 'suffix': table_values}

	def add_student(self, table_data):
		sql_script = self.insert_(table_data, 'students')
		self.cur.execute(sql_script['prefix'], sql_script['suffix'])
		self.conn.commit()

	def add_table(self, table_name, table_data):
		for row in table_data:
			sql_script = self.insert_(row, table_name)
			self.cur.execute(sql_script['prefix'], sql_script['suffix'])
			self.conn.commit()

	def update_student(self, id, table_data):
		return

	def update_table(self, id, table_name, table_data):
		return

d = Database()
#d.create_open_database(new_db=os.path.abspath(os.pardir) + '\database\\test.db', current=True)
d.create_open_database()
#d.add_student({'id': '0'})
#d.add_table('payments', [{'id': '0', 'value': '500'}])
#d.add_table('guardians', [{'id': '0', 'first': 'John'}])