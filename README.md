# epl_fixtures_analysis
A program to analyse EPL fixtures for the 2021-22 season. Contains features like printing all fixtures for a club, printing clashes between big clubs and tabular comparison of fixtures for multiple EPL clubs.

**As of now, the program does not support multiple dates per gameweek, so all fixtures in a gameweek have been set to the same date in fixtures.txt. Do not depend on output for exact date and time of the match, which would be released by broadcasters only a month in advance. This program is meant to illustrate order of fixtures only.**  
  
**Note:All the outputs below, except for the picture, illustrate the program's output for the 20-21 season. For the 21-22 season, please refer to the picture or run the program on your local machine.**
## Usage  
For comparison of fixtures between the 'Big Six':  
```console
(venv) sriram@sriram-e490:~/work/epl_fixtures$ py fixtures.py 
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| Week Number |    Date    |         Arsenal          |         Chelsea          |     Manchester City      |    Manchester United     |    Tottenham Hotspur     |        Liverpool         |
+=============+============+==========================+==========================+==========================+==========================+==========================+==========================+
| 1           | 12-09-2020 | Fulham (A)               | Brighton (A)             | Aston Villa (H)          | Burnley (A)              | Everton (H)              | Leeds United (H)         |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 2           | 19-09-2020 | West Ham United (H)      | Liverpool (H)            | Wolverhampton (A)        | Crystal Palace (H)       | Southampton (A)          | Chelsea (A)              |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 3           | 26-09-2020 | Liverpool (A)            | West Bromwich Albion (A) | Leicester City (H)       | Brighton (A)             | Newcastle United (H)     | Arsenal (H)              |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 4           | 03-10-2020 | Sheffield United (H)     | Crystal Palace (H)       | Leeds United (A)         | Tottenham Hotspur (H)    | Manchester United (A)    | Aston Villa (A)          |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 5           | 17-10-2020 | Manchester City (A)      | Southampton (H)          | Arsenal (H)              | Newcastle United (A)     | West Ham United (H)      | Everton (A)              |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 6           | 24-10-2020 | Leicester City (H)       | Manchester United (A)    | West Ham United (A)      | Chelsea (H)              | Burnley (A)              | Sheffield United (H)     |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 7           | 31-10-2020 | Manchester United (A)    | Burnley (A)              | Sheffield United (A)     | Arsenal (H)              | Brighton (H)             | West Ham United (H)      |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 8           | 07-11-2020 | Aston Villa (H)          | Sheffield United (H)     | Liverpool (H)            | Everton (A)              | West Bromwich Albion (A) | Manchester City (A)      |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 9           | 21-11-2020 | Leeds United (A)         | Newcastle United (A)     | Tottenham Hotspur (A)    | West Bromwich Albion (H) | Manchester City (H)      | Leicester City (H)       |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 10          | 28-11-2020 | Wolverhampton (H)        | Tottenham Hotspur (H)    | Burnley (H)              | Southampton (A)          | Chelsea (A)              | Brighton (A)             |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 11          | 05-12-2020 | Tottenham Hotspur (A)    | Leeds United (H)         | Fulham (H)               | West Ham United (A)      | Arsenal (H)              | Wolverhampton (H)        |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 12          | 12-12-2020 | Burnley (H)              | Everton (A)              | Manchester United (A)    | Manchester City (H)      | Crystal Palace (A)       | Fulham (A)               |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 13          | 15-12-2020 | Southampton (H)          | Wolverhampton (A)        | West Bromwich Albion (H) | Sheffield United (A)     | Liverpool (A)            | Tottenham Hotspur (H)    |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 14          | 19-12-2020 | Everton (A)              | West Ham United (H)      | Southampton (A)          | Leeds United (H)         | Leicester City (H)       | Crystal Palace (A)       |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 15          | 26-12-2020 | Chelsea (H)              | Arsenal (A)              | Newcastle United (H)     | Leicester City (A)       | Wolverhampton (A)        | West Bromwich Albion (H) |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 16          | 28-12-2020 | Brighton (A)             | Aston Villa (H)          | Everton (A)              | Wolverhampton (H)        | Fulham (H)               | Newcastle United (A)     |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 17          | 02-01-2021 | West Bromwich Albion (A) | Manchester City (H)      | Chelsea (A)              | Aston Villa (H)          | Leeds United (H)         | Southampton (A)          |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 18          | 12-01-2021 | Crystal Palace (H)       | Leicester City (A)       | Brighton (H)             | Fulham (A)               | Aston Villa (A)          | Burnley (H)              |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 19          | 16-01-2021 | Newcastle United (H)     | Fulham (A)               | Crystal Palace (H)       | Liverpool (A)            | Sheffield United (A)     | Manchester United (H)    |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 20          | 26-01-2021 | Southampton (A)          | Wolverhampton (H)        | West Bromwich Albion (A) | Sheffield United (H)     | Liverpool (H)            | Tottenham Hotspur (A)    |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 21          | 30-01-2021 | Manchester United (H)    | Burnley (H)              | Sheffield United (H)     | Arsenal (A)              | Brighton (A)             | West Ham United (A)      |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 22          | 02-02-2021 | Wolverhampton (A)        | Tottenham Hotspur (A)    | Burnley (A)              | Southampton (H)          | Chelsea (H)              | Brighton (H)             |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 23          | 06-02-2021 | Aston Villa (A)          | Sheffield United (A)     | Liverpool (A)            | Everton (H)              | West Bromwich Albion (H) | Manchester City (H)      |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 24          | 13-02-2021 | Leeds United (H)         | Newcastle United (H)     | Tottenham Hotspur (H)    | West Bromwich Albion (A) | Manchester City (A)      | Leicester City (A)       |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 25          | 20-02-2021 | Manchester City (H)      | Southampton (A)          | Arsenal (A)              | Newcastle United (H)     | West Ham United (A)      | Everton (H)              |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 26          | 27-02-2021 | Leicester City (A)       | Manchester United (H)    | West Ham United (H)      | Chelsea (A)              | Burnley (H)              | Sheffield United (A)     |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 27          | 06-03-2021 | Burnley (A)              | Everton (H)              | Manchester United (H)    | Manchester City (A)      | Crystal Palace (H)       | Fulham (H)               |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 28          | 13-03-2021 | Tottenham Hotspur (H)    | Leeds United (A)         | Fulham (A)               | West Ham United (H)      | Arsenal (A)              | Wolverhampton (A)        |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 29          | 20-03-2021 | West Ham United (A)      | Liverpool (A)            | Wolverhampton (H)        | Crystal Palace (A)       | Southampton (H)          | Chelsea (H)              |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 30          | 03-04-2021 | Liverpool (H)            | West Bromwich Albion (H) | Leicester City (A)       | Brighton (H)             | Newcastle United (A)     | Arsenal (A)              |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 31          | 10-04-2021 | Sheffield United (A)     | Crystal Palace (A)       | Leeds United (H)         | Tottenham Hotspur (A)    | Manchester United (H)    | Aston Villa (H)          |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 32          | 17-04-2021 | Fulham (H)               | Brighton (H)             | Aston Villa (A)          | Burnley (H)              | Everton (A)              | Leeds United (A)         |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 33          | 24-04-2021 | Everton (H)              | West Ham United (A)      | Southampton (H)          | Leeds United (A)         | Fulham (A)               | Newcastle United (H)     |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 34          | 01-05-2021 | Newcastle United (A)     | Fulham (H)               | Crystal Palace (A)       | Liverpool (H)            | Sheffield United (H)     | Manchester United (A)    |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 35          | 08-05-2021 | West Bromwich Albion (H) | Manchester City (A)      | Chelsea (H)              | Aston Villa (A)          | Leeds United (A)         | Southampton (H)          |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 36          | 12-05-2021 | Chelsea (A)              | Arsenal (H)              | Newcastle United (A)     | Leicester City (H)       | Wolverhampton (H)        | West Bromwich Albion (A) |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 37          | 15-05-2021 | Crystal Palace (A)       | Leicester City (H)       | Brighton (A)             | Fulham (H)               | Aston Villa (H)          | Burnley (A)              |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+
| 38          | 23-05-2021 | Brighton (H)             | Aston Villa (A)          | Everton (H)              | Wolverhampton (A)        | Leicester City (A)       | Crystal Palace (H)       |
+-------------+------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+

```

In the program, this can be modified to show any teams' comparison or a list of matchdays, clashes between the 'Big Six', or to simply print the list of fixtures for any one team.  
The features are given below, along with how to use them:  
### Features  
#### 1. Tabular comparison  
This program can create a picture or pdf of comparison of fixtures, gameweek by gameweek for any set of matches for any teams between any two gameweeks. By default, fixtures for the big six for future matchweeks are shown. The current (or immediately successive) matchweek is calculated using the system's date using the get_current_matchday() function. The function header is:  
`def print_comparison(teams=['Arsenal','Chelsea','Manchester City','Manchester United','Tottenham Hotspur','Liverpool'],start = get_current_matchday(),end = 38): #end is inclusive`  
The teams to be compared can be passed as a list. For best results, do not take more than 8 teams otherwise the output will look too cluttered. 'start' is a number from 1 to 38, taken as current matchday by default and the end is the 38th (last) fixture by default. Run the following commands to capture table shown above into a pdf and image (output.pdf and image.png) :  
```console
(venv) sriram@sriram-e490:~/work/epl_fixtures$ py fixtures.py > output.txt
(venv) sriram@sriram-e490:~/work/epl_fixtures$ pango-view --font=mono -qo image.png output.txt
(venv) sriram@sriram-e490:~/work/epl_fixtures$ soffice --convert-to pdf output.txt
```  
The pdf looks cluttered since there are too many teams and it is limited to A4 size. However, the image looks good. For better results, try reducing the value of width parameter in [Texttable(200)](https://github.com/sriramcu/epl_fixtures_analysis/blob/3b41b6b9bf0c4da59a9522aea851b46d8457822a/fixtures.py#L111) from 200 to maybe 80.  

![alt text](https://github.com/sriramcu/epl_fixtures_analysis/blob/master/image.png)  


#### 2. Print Big Games
The print_big_games() function prints clashes between predefined big teams (in this case the Big Six and Leicester City) along with gameweek number and date. Can be changed by altering the [big_teams](https://github.com/sriramcu/epl_fixtures_analysis/blob/3b41b6b9bf0c4da59a9522aea851b46d8457822a/fixtures.py#L94) list.  
```console
(venv) sriram@sriram-e490:~/work/epl_fixtures$ py
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from fixtures import *
>>> print_big_games()
 1. 19-09-2020 	Chelsea v Liverpool

 2. 26-09-2020 	Liverpool v Arsenal

 3. 26-09-2020 	Manchester City v Leicester City

 4. 03-10-2020 	Manchester United v Tottenham Hotspur

 5. 17-10-2020 	Manchester City v Arsenal

 6. 24-10-2020 	Arsenal v Leicester City

 7. 24-10-2020 	Manchester United v Chelsea

 8. 31-10-2020 	Manchester United v Arsenal

 9. 07-11-2020 	Manchester City v Liverpool

10. 21-11-2020 	Liverpool v Leicester City

11. 21-11-2020 	Tottenham Hotspur v Manchester City

12. 28-11-2020 	Chelsea v Tottenham Hotspur

13. 05-12-2020 	Tottenham Hotspur v Arsenal

14. 12-12-2020 	Manchester United v Manchester City

15. 15-12-2020 	Liverpool v Tottenham Hotspur

16. 19-12-2020 	Tottenham Hotspur v Leicester City

17. 26-12-2020 	Arsenal v Chelsea

18. 26-12-2020 	Leicester City v Manchester United

19. 02-01-2021 	Chelsea v Manchester City

20. 12-01-2021 	Leicester City v Chelsea

21. 16-01-2021 	Liverpool v Manchester United

22. 26-01-2021 	Tottenham Hotspur v Liverpool

23. 30-01-2021 	Arsenal v Manchester United

24. 02-02-2021 	Tottenham Hotspur v Chelsea

25. 06-02-2021 	Liverpool v Manchester City

26. 13-02-2021 	Leicester City v Liverpool

27. 13-02-2021 	Manchester City v Tottenham Hotspur

28. 20-02-2021 	Arsenal v Manchester City

29. 27-02-2021 	Chelsea v Manchester United

30. 27-02-2021 	Leicester City v Arsenal

31. 06-03-2021 	Manchester City v Manchester United

32. 13-03-2021 	Arsenal v Tottenham Hotspur

33. 20-03-2021 	Liverpool v Chelsea

34. 03-04-2021 	Arsenal v Liverpool

35. 03-04-2021 	Leicester City v Manchester City

36. 10-04-2021 	Tottenham Hotspur v Manchester United

37. 01-05-2021 	Manchester United v Liverpool

38. 08-05-2021 	Manchester City v Chelsea

39. 12-05-2021 	Manchester United v Leicester City

40. 12-05-2021 	Chelsea v Arsenal

41. 15-05-2021 	Chelsea v Leicester City

42. 23-05-2021 	Leicester City v Tottenham Hotspur

```

#### 3. Print Matches  
The print_matches() function is a simple function to print the list and approx dates of matches for a given team between any two gameweek numbers (by default between current matchday and gameweek 38).  
```console
(venv) sriram@sriram-e490:~/work/epl_fixtures$ py
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> from fixtures import *
>>> print_matches('Arsenal')

 1. 12-09-2020 	Fulham v Arsenal

 2. 19-09-2020 	Arsenal v West Ham United

 3. 26-09-2020 	Liverpool v Arsenal

 4. 03-10-2020 	Arsenal v Sheffield United

 5. 17-10-2020 	Manchester City v Arsenal

 6. 24-10-2020 	Arsenal v Leicester City

 7. 31-10-2020 	Manchester United v Arsenal

 8. 07-11-2020 	Arsenal v Aston Villa

 9. 21-11-2020 	Leeds United v Arsenal

10. 28-11-2020 	Arsenal v Wolverhampton

11. 05-12-2020 	Tottenham Hotspur v Arsenal

12. 12-12-2020 	Arsenal v Burnley

13. 15-12-2020 	Arsenal v Southampton

14. 19-12-2020 	Everton v Arsenal

15. 26-12-2020 	Arsenal v Chelsea

16. 28-12-2020 	Brighton v Arsenal

17. 02-01-2021 	West Bromwich Albion v Arsenal

18. 12-01-2021 	Arsenal v Crystal Palace

19. 16-01-2021 	Arsenal v Newcastle United

20. 26-01-2021 	Southampton v Arsenal

21. 30-01-2021 	Arsenal v Manchester United

22. 02-02-2021 	Wolverhampton v Arsenal

23. 06-02-2021 	Aston Villa v Arsenal

24. 13-02-2021 	Arsenal v Leeds United

25. 20-02-2021 	Arsenal v Manchester City

26. 27-02-2021 	Leicester City v Arsenal

27. 06-03-2021 	Burnley v Arsenal

28. 13-03-2021 	Arsenal v Tottenham Hotspur

29. 20-03-2021 	West Ham United v Arsenal

30. 03-04-2021 	Arsenal v Liverpool

31. 10-04-2021 	Sheffield United v Arsenal

32. 17-04-2021 	Arsenal v Fulham

33. 24-04-2021 	Arsenal v Everton

34. 01-05-2021 	Newcastle United v Arsenal

35. 08-05-2021 	Arsenal v West Bromwich Albion

36. 12-05-2021 	Chelsea v Arsenal

37. 15-05-2021 	Crystal Palace v Arsenal

38. 23-05-2021 	Arsenal v Brighton

>>> 

```

#### 4. Print all dates and all teams
The print_all_dates() function prints all the tentative dates corresponding to gameweek numbers and all_teams() function returns a list of all 20 teams playing in the Premier League.  
```console
(venv) sriram@sriram-e490:~/work/epl_fixtures$ py
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from fixtures import *
>>> print_all_dates()
1. 12-09-2020 
2. 19-09-2020 
3. 26-09-2020 
4. 03-10-2020 
5. 17-10-2020 
6. 24-10-2020 
7. 31-10-2020 
8. 07-11-2020 
9. 21-11-2020 
10. 28-11-2020 
11. 05-12-2020 
12. 12-12-2020 
13. 15-12-2020 
14. 19-12-2020 
15. 26-12-2020 
16. 28-12-2020 
17. 02-01-2021 
18. 12-01-2021 
19. 16-01-2021 
20. 26-01-2021 
21. 30-01-2021 
22. 02-02-2021 
23. 06-02-2021 
24. 13-02-2021 
25. 20-02-2021 
26. 27-02-2021 
27. 06-03-2021 
28. 13-03-2021 
29. 20-03-2021 
30. 03-04-2021 
31. 10-04-2021 
32. 17-04-2021 
33. 24-04-2021 
34. 01-05-2021 
35. 08-05-2021 
36. 12-05-2021 
37. 15-05-2021 
38. 23-05-2021 
>>> print(all_teams())
['Arsenal', 'Aston Villa', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Sheffield United', 'Southampton', 'Tottenham Hotspur', 'West Bromwich Albion', 'West Ham United', 'Wolverhampton']
>>> 
```  








