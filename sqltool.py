import sqlite3

class database(object):
            def __init__(self, path):
                        self.path=path

            def connect_db(self,dbname):
                        self.dbcon=None
                        try:
                                   self.dbcon=sqlite3.connect(self.path+'\\'+dbname, isolation_level="DEFFRRED", check_same_thread=False)
                                   self.con=self.dbcon.cursor()
                        except:
                                    pass




if __name__=='__main__':
            db=database('D:\Python')
            db.connect_db('mydatabase.db')
