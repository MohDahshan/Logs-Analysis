# Logs Analysis

## requirements
* Python
* psycopg2
* Postgresql

## how to run

* load the data in the database
```sql
psql -d news -f newsdata.sql
```
* connect to the database
```sql
psql
\c news
```

### create views

```sql
create view log_day_view as select date(time), count(*) as requests from log group by date(time) order by requestes desc;
```

```sql
create view log_day_error_view as select date(time), count(*) as requests from log where status not like '%200%' group by date(time) order by requests desc;
```
