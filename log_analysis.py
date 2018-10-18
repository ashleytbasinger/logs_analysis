#! /usr/bin/env python
import psycopg2

DBNAME = "news"


def run_query(query):
    db = psycopg2.connect('dbname=' + DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    db.close()
    return rows


def get_top_articles():
    query = """
        SELECT
            articles.title,
            COUNT(*) AS views
        FROM
            articles
            JOIN log ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY
            articles.title
        ORDER BY
            views DESC
        LIMIT 3;
    """
    top_articles = run_query(query)
    print('\nTOP THREE ARTICLES BY PAGE VIEWS:\n')
    count = 1
    for i in top_articles:
        title = i[0]
        views = '" | ' + str(i[1]) + " views"
        print(title + views)
        count += 1


def get_top_authors():
    query = """
        SELECT
            authors.name,
            COUNT(*) AS views
        FROM
            authors
            JOIN articles ON authors.id = articles.author
            JOIN log ON log.path like concat('/article/%', articles.slug)
        GROUP BY
            authors.name
        ORDER BY
            views DESC
        LIMIT 3;
    """
    top_authors = run_query(query)
    print('\nTOP THREE AUTHORS BY VIEWS:\n')
    count = 1
    for i in top_authors:
        print(i[0] + ' | ' + str(i[1]) + " views")
        count += 1


def get_error_days():
    query = """
        SELECT
            total.day,
            ROUND(((errors.error_requests*1.0) / total.requests), 3) AS error_percent
        FROM (
          SELECT
            date_trunc('day', time) "day",
            count(*) AS error_requests
          FROM
            log
          WHERE
            status LIKE '404%'
          GROUP BY
            day
        ) AS errors
        JOIN (
          SELECT
            date_trunc('day', time) "day",
            count(*) AS requests
          FROM
            log
          GROUP BY
            day
          ) AS total
        ON total.day = errors.day
        WHERE
            (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY
            error_percent DESC;
    """
    error_days = run_query(query)
    print('\nDAYS WITH MORE THAN 1% ERRORS:\n')
    for i in error_days:
        date = i[0].strftime('%b %d %y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " | " + errors)

print('Your results are...\n')
get_top_articles()
get_top_authors()
get_error_days()
