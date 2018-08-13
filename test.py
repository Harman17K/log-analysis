#!/usr/bin/env python
import psycopg2  # psycopg2 is imported


query1 = """Select title,count(*) from articles inner join
    log on log.path=concat('/article/',articles.slug) group by articles.title
    order by count(*) desc limit 3;"""

# query1 is the set of commands used to evaluate the top 3 articles using
# the log and articles table.

query2 = """select authors.name,count(*) from authors
    inner join articles on articles.author = authors.id
    inner join log on log.path=concat('/article/',articles.slug)
    group by authors.name order by count(*) desc;"""

# query2 includes the set of commands that evaluates the views per author
# using the fields required from the join of all the 3 tables.

query3 = """select incorrect.a_date,(incorrect.dilusion/negative.grand)
    from incorrect,negative where (negative.a_date = incorrect.a_date)
    and (incorrect.dilusion/negative.grand >1);"""

# query3 involves the use of 'incorrect' and 'negative' views
# to extract the percent error by dividing
# the 'total error per day' by 'total error per day'

news = psycopg2.connect(database="news")  # database is conected with python
cur = news.cursor()  # allows to execute the commands in news database
output = "{} : {}"


def Soln(commands):  # this function evalutes a given query and fetches result
    cur.execute(commands)
    return cur.fetchall()


print("Best articles of all time are:")
result1 = Soln(query1)  # value of query1 is stored in result1
for i in range(0, 3):
    print(output.format(result1[i][0], result1[i][1]))  # output is printed

print(" ***** ")
print("Authors and their article views:")
result2 = Soln(query2)  # value of query2 is stored in result2
for i in range(0, 4):  # for loop used so as to print the name of authors,views
    print(output.format(result2[i][0], result2[i][1]))  # output is printed
print(" ***** ")
result3 = Soln(query3)   # value of query3 is stored in result3
print("The date with percentage error greater than 1%:")
print("{} : {}%".format(result3[0][0], result3[0][1]))


print(" ***** ")
news.close()
