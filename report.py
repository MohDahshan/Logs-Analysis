#!/usr/bin/python
import psycopg2


print('\n\n    				[REPORT]')
conn_string = "host='localhost' dbname='newsdb' user='dbuser' "\
              "password='dbpassword'"

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

cursor.execute('''SELECT title,count(*) as count
    FROM log,articles
    WHERE log.path LIKE concat('%', articles.slug)
    GROUP BY articles.title
    ORDER BY count DESC
    limit 3''')
result = cursor.fetchall()
print ("\n  the most popular three articles of all time:")
for x in result:
    title, views = x
    print("   " + str(result.index(x) + 1) + '- ' + title + '   ' + str(views))

cursor.execute('''SELECT authors.name,count(*) as count
    FROM log,articles
    JOIN authors ON authors.id = articles.author
    WHERE log.path LIKE concat('%', articles.slug)
    GROUP BY authors.name
    ORDER BY count DESC''')
result = cursor.fetchall()
print ("\n  the most popular article authors of all time:")
for x in result:
    author, views = x
    print("   "+str(result.index(x) + 1)+'- '+str(author)+'   '+str(views))

cursor.execute('''SELECT log_day_view.date,
    round(100.0 * log_day_error_view.requests / log_day_view.requests, 2)
    AS parcent
    FROM log_day_error_view
    JOIN log_day_view ON log_day_error_view.date = log_day_view.date
    WHERE round(100.0*log_day_error_view.requests/log_day_view.requests, 2) > 1
    ORDER BY parcent DESC''')
result = cursor.fetchall()
print ("\n  days had more than 1% of errors:")
for x in result:
    date, parcent = x
    print("   " + str(date) + '   ' + str(parcent) + ' %')

