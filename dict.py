#creation
months = {}
months = { 1 : "January", 
     	2 : "February", 
    	3 : "March", 
        4 : "April", 
     	5 : "May", 
     	6 : "June", 
    	7 : "July",
        8 : "August",
     	9 : "September", 
    	10 : "October", 
        11 : "November",
    	12 : "December" } 
print "The dictionary contains the following keys: ", months.keys()
Output:
The dictionary contains the following keys:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12]


#accessing
#To get a value out of a dictionary, you must supply its key, you cannot provide the value and get the key
whichMonth = months[1]
print whichMonth
Output: January
#To delete an element from a dictionary, use del
del(months[5])
print months.keys()
Output:
[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
#add a new element
months[5] = "May"
print months.keys()
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#update an element
months[1] = "Jan"
print months
Output:
{1: 'Jan', 2: 'February', 3: 'March', 4: 'April', 5... }
#sorting
sortedkeys = months.keys()
print sortedkeys
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for key in months:
    print key, months[key]
Output:
1 January
2 February
3 March
4 April
5 May
6 June
7 July
8 August
9 September
10 October
11 November
12 December

for key, value in months.iteritems():
    print key, value

print "The entries in the dictionary are:"
for item in months.keys():
    print "months[ ", item, " ] = ", months[ item ]

customers = [{"uid":1,"name":"John"},
    {"uid":2,"name":"Smith"},
           {"uid":3,"name":"Andersson"},
            ]
print customers
Output:
[{'uid': 1, 'name': 'John'}, {'uid': 2, 'name': 'Smith'}, {'uid': 3, 'name':
'Andersson'}]
#Print the uid and name of each customer
for x in customer:
    print x["uid"], x["name"]
Output:
1 John
2 Smith
3 Andersson
#Modify an entry

#This will change the name of customer 2 from Smith to Charlie
customers[2]["name"]="charlie"
print customers
Output:
[{'uid': 1, 'name': 'John'}, {'uid': 2, 'name': 'Smith'}, {'uid': 3, 'name':
'charlie'}]
#Add a new field to each entry
for x in customers:
    x["password"]="123456" # any initial value

print customers
Output:
[{'password': '123456', 'uid': 1, 'name': 'John'}, {'password': '123456', 'uid':
2, 'name': 'Smith'}, {'password': '123456', 'uid': 3, 'name': 'Andersson'}]
#Delete a field
del customers[1]
print customers
Output:
[{'uid': 1, 'name': 'John'}, {'uid': 3, 'name': 'Andersson'}]
#Delete all fields
# This will delete id field of each entry.
for x in customers:
    del x["id"]
Output:
[{'name': 'John'}, {'name': 'Smith'}, {'name': 'Andersson'}]





import requests
def translate(word, lang_from = 'ru', lang_to = 'kk'):
	url = "https://sozdik.kz/translate/%s/%s/%s/" % (lang_from, lang_to, word)
	r = requests.get(url)
	data = r.json()
	translation = data['translation']
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(translation, "html.parser")
	l = soup.select("span a")
	result = []
	for item in l:
		result.append(item.text)
	return result

r = translate('ручка', lang_to='kk', lang_from = 'ru')
s = ",".join(r)
print(s)