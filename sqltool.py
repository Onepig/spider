# -*- coding: cp936 -*-
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
                        raise

        def initdatabase(self):
                """
                ��ʼ�����ݿ�
                table1:
                url ��ַ title �������� inurl ���������� outurl ���������� jumpnumber ��ת���� deep ��ζ���ڼ���������ȡ�������� response ����״̬��
                jumptype ��ת����
                """
                try:
                        sql1="""create table if not exists urls
                        (url text primary key, title, inurl integer default 0, outurl integer default 0, jumpnumber integer default 0, jumptype text default null, deep integer default 0, response integer default 0, jumpinfo text default null)
                        """
                        self.con.execute(sql1)
                except:
                        pass

        def insert_one(self, info, table):
                sql1 = "insert or ignore into '%s' "%table
                name = []
                value = []
                try:
                        for k, v in info.iteritems():
                                name.append("'%s'"%(str(k)))
                                value.append("'%s'"%(str(v)))
                except UnicodeEncodeError:
                        pass
                namestr=','.join(name)
                valuestr = ','.join(value)
                sql2 = "(%s) valuse(%s)"%(namestr, valuerstr)
                sql = sql1+sql2
                print "#######"+sql
                try:
                        self.con.execute(sql)
                        self.dbcon.commit()
                except sqlite3.IntegrityError:
                        pass
                except:
                        pass

                      
if __name__=='__main__':
            db=database('D:\Python')
            db.connect_db('mydatabase.db')
