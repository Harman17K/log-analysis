LOG ANALYSIS 

PROJECT OUTLINE:
In this project we are provided with a database name 'news' and we have to extract information and answer the following question by the use of Postgre and Python:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

FILES ATTACHED:
1. test.py
2. README.txt
3. Final output.txt

PRIORLY REQUIRED:
1. Install Python
2. Install Vagrant
3. Install VirtualBox
4. Install Gitbash
5. Download newsdata.zip

EXECUTION PROCEDURE:
Running Virtual Machine:
1. Extract content from the zip file.
2. Then make sure you have vagrant installed in your computer.
3. Run the following commands:
	- Go to the vagrant folder on your computer using "cd /location"
	- Power the virtual machine using "vagrant up"
	- Then run "vagrant ssh"
	- Execute "psql -d news -f newsdata.sql"
	- Run "psql -d news"
	- Get the solutions using command "python test.py"
4. Formatted answers to all the questions in simple text will be seen.

ABOUT CODE:
-Code is written using python language.
-After we connected the database to the code, we can extract information from database.
-Using POSTGRESQL+PYTHON we extract the output from database.
-Then the final output is displayed there itself in the terminal.

VIEWS CREATED:
-create view incorrect as select date(time) as a_date,count(*)*100 as dilusion from log where status='404 NOT FOUND' group by date(time) order by date(time).  
-create view negative as select date(time) as a_date,count(*) as grand from log group by date(time) order by date(time).
	
VIEW EXPLAINATION: In this query we have to find the date with more than 1% error request . For that we have to first find the total requests that are made in a single day i.e grand and the no. of requests that are not processed in a single day i.e dilusion ,then on dividing the 'error request in one day*100' with 'total no. of requests'. We get the percentage error for each day.There is a VIEW named 'incorrect' in which the total error requests made in a day are calculated . Another VIEW named 'negative' in which total no. of requests made in a day are fed. Later on dividing the 'incorrect.dilusion' with 'negative.grand' , error requests(in %) for each day are obtained and the date having error request with more than 1% is displayed on the terminal portal .  

QUERIES CREATED:
Query1:- Select title,count(*) from articles inner join
    log on log.path=concat('/article/',articles.slug) group by articles.title
    order by count(*) desc limit 3;

Query2:- select authors.name,count(*) from authors
    inner join articles on articles.author = authors.id
    inner join log on log.path=articles.slug
    group by authors.name order by count(*) desc;

Query3:- select incorrect.a_date,(incorrect.dilusion/negative.grand)
    from incorrect,negative where (negative.a_date = incorrect.a_date)
    and (incorrect.dilusion/negative.grand >1);

QUERY EXPLAINATION: Query1 There was a provision given in last review that I can't update the existing database tables using 'update' command so I changed it with concat('/articles/') command in the query so that articles and log tables can be joined from common field. 
Now the tables articles and log are joined using the common field i.e.modified slug entries in articles table are like path in log table hence,the articles name can be ordered by count(*) i.e. views.

Query2 uses concat in slug field to join log and articles table, further more joined by authors table on the basis of their common field that is id in authors,author in articles. Now the authors' names can be displayed on the basis of views i.e count(*).

Query3 uses 'incorrect' and 'negative' views to display the percentage error per day  by dividing the 'dilusion' and 'grand' fields >1% as per each date.