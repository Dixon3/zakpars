There is number of utilites for zakupki.gov.ru.

Catalog structure:


How to parse data from server:

Download and install PostgreSQL database.
1)Create User zakupki/zakupki in following way. You may choose any username as you wish.
Please create database for this user as well.
[dmitry@project26-as01 zakpars]$ psql -U postgres
postgres=# CREATE USER zakupki WITH PASSWORD 'zakupki';
postgres=# create database zakupki owner zakupki encoding 'UTF-8' template template0;
CREATE DATABASE

2) Prepare database for data loading:

Please execute scripts in catalog in following sequence:
./sql/01create_files_list.sql
./sql/02create_logs.sql
./sql/create_contracts.sql
./sql/create_notifications.sql
./sql/create_protocols.sql

with command

psql -U zakupki < <script_name.sql>

Please check that there is not postgres errors in output.
If all goes smooth at the end you wil have postgres database with empty schema and ready for data load.

Data loading from FTP::

In directory parallel_python you can find some scripts for data loading from FTP to postgres.
There are 2 main scrtipts which you can use:
./parallel_python/get_files_list.py for fill table files list with actual file names on FTP server, you should re-run sctipt for update fileslist on ftp.

./parallel_python/parseFilesFromFtp.py this is parser file. It shuld be run after some date will be inserted in files_list table.

Database connection credentials are stored in:
./parellel_python/settings.py


If you have any question please contact with me by mail: dixon3@yandex.ru
