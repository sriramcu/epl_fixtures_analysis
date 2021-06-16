import collections
from texttable import Texttable
import datetime



def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el
            
def get_fixtures():
    f = open("fixtures.txt",'r')
    a = f.read()
    f.close()
    a = a.split('\n')
    a = [x for x in a if x is not '']
    
    fixtures = []

    dates = []
    for fx in a:
        if ' v ' in fx:
            fixture = [fx.split(' v ')[0].strip(),fx.split(' v ')[1].strip()]
            fixtures.append(fixture)
        else:
            dt = datetime.datetime.strptime(fx.strip(),"%A %d %B %Y").strftime("%d-%m-%Y")
            dates.append(dt)
        
    
    fixtures = [x for x in fixtures if len(x)>=2]

   
    return fixtures,dates
    

def all_teams():
    fixtures,dates = get_fixtures()
    teams = flatten(fixtures)
    teams = list(set(teams))
    teams = sorted(teams, key=str.lower)
    return teams
    

    
def print_all_dates():
    fixtures,dates = get_fixtures()
    ctr = 1
    for dt in dates:
        print(ctr,end = '. ')
        print(dt)
        print()
        ctr+=1

      
def get_current_matchday():
    fixtures,fake_dates = get_fixtures()
    dates = []
    for dt in fake_dates:
        dates.append(datetime.datetime.strptime(dt,'%d-%m-%Y'))
    
    n = datetime.datetime.now()
    n1 = datetime.datetime(2023,11,11,0,0,0,0) #debug with later date, output is 39 meaning season ended
    n2 = datetime.datetime(2020,11,11,0,0,0,0) #debug
    ctr = 1
    for dt in dates:
        if dt>=n:
            break
        ctr+=1
            
    return ctr #will be modified in future
    
    

def print_matches(team='Arsenal',start = get_current_matchday(), end = 38):  #end is inclusive
  
    fixtures,dates = get_fixtures()
    #print(fixtures)
    fixtures = [x for x in fixtures if team in x]
    fixtures = fixtures[start-1:end]
    ctr = start
    print()
    for fixture in fixtures:
        print('{:>2}'.format(ctr),end = '. ')
        print(dates[ctr-1])
        print('\t{} v {}'.format(fixture[0],fixture[1]))
        print()
        ctr+=1
     
     

def print_big_games():
    fixtures,dates = get_fixtures()
    big_teams = ['Arsenal','Chelsea','Man City','Man Utd','Spurs','Liverpool']
    big_fixtures = [x for x in fixtures if (x[0] in big_teams and x[1] in big_teams)]
    
    ctr = 1
    for fixture in big_fixtures:
        print('{:>2}'.format(ctr),end = '. ')
        i = fixtures.index(fixture)
        i = int(i/10)
        
        dt = dates[i]
        print(dt,end='')
        print('\t{} v {}'.format(fixture[0],fixture[1]))
        print()
        ctr+=1
        

def print_comparison(teams=['Arsenal','Chelsea','Man City','Man Utd','Spurs','Liverpool'],start = get_current_matchday(),end = 38): #end is inclusive
    t  = Texttable(200)  #max width of table
    header = ['Week Number','Date']
    header.extend(teams)
    
    fixtures,dates = get_fixtures()
    outputs_list = []
    
    for team in teams:
        outputs = [] #list of opponents with venue
        temp_fix = [x for x in fixtures if team in x]
        for fx in temp_fix:
            if fx[0] == team:
                outputs.append(fx[1]+' (H)')
            elif fx[1] == team:
                outputs.append(fx[0]+' (A)')
                
        outputs_list.append(outputs)
    
    rows = [header]
    l = end
    ctr = start
    
    while(ctr<=l):  
             
        row = []
        row.append('{:>2}'.format(ctr))
        dt = dates[ctr-1]
        print(ctr)

        row.append(dt)
        for output in outputs_list:
            row.append(output[ctr-1])
        rows.append(row)
        ctr+=1
        
    t.add_rows(rows)
    
    print(t.draw())
    
    

if __name__ == '__main__':

    print_comparison()
    

    
