# Module Imports
import mariadb
import sys
from memory_profiler import profile

def update_progress(progress):
    barLength = 40 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), round(progress*100,2), status)
    sys.stdout.write(text)
    sys.stdout.flush()

class DB:
    def __init__(self) -> None:

        try:
            self.conn = mariadb.connect(
                user="varnit",
                password="action128",
                host="localhost",
                # port=8886,
                database="employees"
            )
            self.cur = self.conn.cursor()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def get_data(self):
        self.cur.execute("SELECT table_name FROM information_schema.tables;")
        rows = self.cur.fetchall()
        for table in rows:
            try:
                self.cur.execute(f"SELECT COUNT(*) FROM {table[0]}")
                row_count = self.cur.fetchall()[0][0]
                self.cur.execute(f"SELECT count(*) FROM information_schema.columns WHERE table_name = '{table[0]}';")
                column_count = self.cur.fetchall()[0][0]
                print(table[0],row_count,column_count)
            except:
                pass


    # @profile
    def get_salaries(self):
        self.cur.execute("SELECT * FROM employees")
        while True:
            row = self.cur.fetchone()
            if row:
                yield row
            else:
                break

    @profile
    def get_without_generator(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        length = len(rows)
        count = 0
        for row in rows:
            count += 1
            update_progress(count/length)


        

            

@profile
def call_gen():
    D = DB()
    count = 0
    length = 300024
    for row in D.get_salaries():
        count += 1
        update_progress(count/length)

if __name__ == '__main__':
    D = DB()
    D.get_without_generator()
    call_gen()


'''
Console Output.

For without Generator.

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    67     21.4 MiB     21.4 MiB           1       @profile
    68                                             def get_without_generator(self):
    69     21.4 MiB      0.0 MiB           1           self.cur.execute("SELECT * FROM employees")
    70    116.0 MiB     94.5 MiB           1           rows = self.cur.fetchall()
    71    116.0 MiB      0.0 MiB           1           length = len(rows)
    72    116.0 MiB      0.0 MiB           1           count = 0
    73    116.0 MiB      0.0 MiB      300025           for row in rows:
    74    116.0 MiB      0.0 MiB      300024               count += 1
    75    116.0 MiB      0.0 MiB      300024               update_progress(count/length)


With Generator.

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    82     24.9 MiB     24.9 MiB           1   @profile
    83                                         def call_gen():
    84     24.9 MiB      0.0 MiB           1       D = DB()
    85     24.9 MiB      0.0 MiB           1       count = 0
    86     24.9 MiB      0.0 MiB           1       length = 300024
    87     24.9 MiB      0.0 MiB      300025       for row in D.get_salaries():
    88     24.9 MiB      0.0 MiB      300024           count += 1
    89     24.9 MiB      0.0 MiB      300024           update_progress(count/length)

'''
