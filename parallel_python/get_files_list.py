
import ftplib
import psycopg2
import sys
from helper import DBConnector


try:
    db_conn=DBConnector('default')
    cur=db_conn.getCursor()
    cur.execute("CREATE TABLE files_list (id serial PRIMARY KEY, path varchar unique, insert_time timestamp);commit;")
    del db_conn 
except Exception,e:
    print "Unable create table:",e


db_conn=DBConnector('default')
curr=db_conn.getCursor()

ftp = ftplib.FTP("ftp.zakupki.gov.ru")
ftp.login("free", "free")

files = []

def ftp_walk(ftp):    
    print 'Path:', ftp.pwd()
    dirs = ftp.nlst()
    for item in (path for path in dirs if path not in ('.', '..')):
        try:
            ftp.cwd(item)
            print 'Changed to', ftp.pwd()
            try:
                ftp_walk(ftp)
            finally:
                ftp.cwd('..')
        except Exception, e:
            path=ftp.pwd() + '/'+str(item)
        try:
            curr.execute("INSERT into files_list (path) values (%s)", (path,))
        except Exception, e:
            print e
        finally:
            curr.execute("commit;")
            

ftp_walk(ftp)



