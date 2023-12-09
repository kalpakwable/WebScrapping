Line 1 to 4 : We imported some libraries,
		a) requests and BeautifulSoup for extracting the data from web
		b) sqllite3 for connecting to a sql server database
		c) matplotlib and wordcloud for performing analysis and displaying wordcloud


Line 9 to 30 : a) The code indicates the connection to the sql server database
	       b) Once the connection established, we created a table called news, with the column names we have extrated from web scrapping.


Line 34 to 50 : a) We tried to get the html source code for Category Science using GET() method.
		b) We wrote all the code in try catch block, in case a wrong URL, has been passed. then it should give error.
		c) raise_for_status() method is verifying the same.
		d) Once we got the whole HTML code of a webpage, we tried to find out a lable or tag which is required for getting the values mentioned in assignment.
		   Such as Date, Author, Time, Title and many more.
		e) When we found that tag, we tried to extract the values for our DB columns using some inbuilt functions such as (FIND(), FIND_ALL(), GET_TEXT())  				f) We also used some functions such as Split(), encode() to manipulate the data, inorder to get the required value.
		g) Similarly, we have perform this same activity for other categories to get there value and inserted all the values into our database.

Line 52 to 56 : a) We have executed the insert query for data storage into sql server database for every record.



 ###### OTHER TRY EXCEPT block have perform the extraction and storage of data for other categories #############


Line 152 to 165 : a) We have created a string with Title and a Body of the news.
		  b) Again, we have a list of some keywords which we need to display according to their frequency in above string.
		  c) We have used matplot library for dispplaying the word cloud of the keywords.



**************************************Thank You*************************************************