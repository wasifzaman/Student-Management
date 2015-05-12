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

	def gen_insert_sql_script(self, data, to_table):
		table_columns = [row[1] for row in self.cur.execute('PRAGMA table_info(' + to_table + ')')]
		if table_columns[0] == 'num': table_columns.pop(0)
		table_values = str(tuple([data[column_name] \
			if column_name in data else '' for \
			column_name in table_columns]))
		value_fill = str(tuple([i for i in table_columns])).replace("'", '')
		return 'INSERT INTO ' + to_table + value_fill + 'VALUES' + table_values

	def gen_update_sql_script(self, id, data, to_table):
		table_columns = [row[1] for row in self.cur.execute('PRAGMA table_info(' + to_table + ')')]
		row = data['num'] if table_columns[0] == 'num' else False
		update_script = 'UPDATE ' + to_table + ' SET '
		for column, value in data.items():
			update_script += column + "='" + value + "', "
		update_script = update_script[:-2]
		update_script += " WHERE "
		update_script += ("num=" + "'" + row + "'") if row else ("id=" + "'" + id + "'")
		return update_script

	def add_student(self, table_data):
		sql_script = self.gen_insert_sql_script(table_data, 'students')
		self.cur.execute(sql_script)
		self.conn.commit()

	def add_to_table(self, table_name, table_data):
		for row in table_data:
			sql_script = self.gen_insert_sql_script(row, table_name)
			self.cur.execute(sql_script)
		self.conn.commit()

	def update_student(self, id, table_data):
		sql_script = self.gen_update_sql_script(id, table_data, 'students')
		self.cur.execute(sql_script)
		self.conn.commit()

	def update_table(self, id, table_name, table_data):
		for row in table_data:
			sql_script = self.gen_update_sql_script(id, row, table_name)
			self.cur.execute(sql_script)
		self.conn.commit()

	def set_check_in_interval(self, interval):
		return

d = Database()
#d.create_open_database(new_db=os.path.abspath(os.pardir) + '\database\\test.db', current=True)
d.create_open_database()
#d.add_student({'id': '0'})
#d.add_to_table('payments', [{'id': '0', 'value': '500'}, {'id': '0', 'value': '700'}])
#d.add_to_table('guardians', [{'id': '0', 'first': 'John'}])
#d.update_student('0', {'first': 'test'})
#d.update_table('0', 'guardians', [{'num': '1', 'last': 'Smith', 'city': 'New York'}])