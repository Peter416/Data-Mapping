import pandas as pd
import numpy as np
import ijson
from io import StringIO





def convert_excel_file_to_list(filename):
    """
    Takes in a file name.
    Outputs a list of pairs, containing every pair of "International" and "Philosophy" keywords
    """
    df = pd.read_csv(filename, header=0, keep_default_na=False)

    column_status = "Department"        # column that has International/Philosophy tag
    column_prefix_keyword = "Key word"  # column prefixes that contain keywords

    set_international = set()           # will contain all international keywords
    set_philosophy = set()              # will contain all philosophy keywords

    # get all column names for columns that represent keywords: e.g. Key word #1, Key word #2, ...
    keyword_columns = [x for x in df.columns.values if "Key word" in x]

    # loop through table
    for index, row in df.iterrows():

        # get the status: International studies or Philosophy
        status = row[column_status]

        # go through all key word columns and collect key words
        for kc in keyword_columns:

            # skip empty keywords
            if str(row[kc]).strip() == "_":
                continue

            # if keyword belongs to international studies, put it in that set
            if status == "International Studies":
                set_international.add(row[kc])
            # otherwise, put it in the philosophy set
            else:
                set_philosophy.add(row[kc])

    # for EACH international key word, go through all philosophy keywrods and put the two as a pair in the list
    list_pairs = [[i, j] for i in set_international for j in set_philosophy]

    # E.g. list_pairs[0] is the first pair, list_pairs[1] is the second pair, etc..
    # list_pairs[0][0] is the international keyword of the first pair
    # list_pairs[0][1] is the philosophy keyword of the first pair
    # etc...
    return list_pairs

data_lists = convert_excel_file_to_list("data.csv")

# print all pairs separated by a comma

for pair in data_lists:
   print ("{}, {}".format(pair[0], pair[1]))




# put data list in a formatted table

df = pd.DataFrame(data_lists)

df.columns = ["International", "Philosophy"]

column_names = sorted(list(set(df["International"])))
row_names = sorted(list(set(df["Philosophy"])))

print (len(column_names), len(row_names))

# ;limit
column_names = column_names
row_names = row_names


df = pd.DataFrame(columns=column_names, index=row_names)
df.head()

def load_json_2(filename):
    
    with open(filename, "r") as f:
        
        keywords = list()

        for line in f:
            
            stream = StringIO(line)

            parser = ijson.parse(stream)
            
            for prefix, event, value in parser:

                if (prefix, event) == ("keywords", "start_array"):
                    
                    keywords.append(list())  # create new list for article

                if (prefix, event) == ("keywords.item", "string"):
                    
                    keywords[-1].append(value)

    return keywords

keywords = load_json_2(r"C:\Users\peter\Desktop\aminer_papers_0\aminer_papers_1.txt")

print(keywords[0])      # print keywrods of first article

print(keywords[1])      # print keywords of second article

print ("done)")

# call load_json_2 and it will give you a list of all the keywords per article

# keywords is a list
# keywords[0] is the list of keywords for the first article
# keywords[1] is the list of keywords for the second article
# ...

# keywords[0][0] is the first keyword of the first article
# keywrods[0][1] is the second keyword of the first article
# etc...

count = 0
for i in data_lists:
    i = data_lists
    for j in range(len(i)):
        if i[j] in keywords:
            count = count + 1
            print(count)
            
check =  any(item in keywords for item in data_lists)
print(check)


def countX(keyword_list, keyword_pair):
    
    keyword_list = keywords from publications I want to search
    
    keyword_pair = keywords from International Studies and Philosophy
    
    count = 0                       # set count
    
    for kw in data_lists:
        
        if (kw == any(word in keywords for word in data_lists)):
            
            count = count + 1
            
    return count
  
countX(keywords, data_lists)

for k in data_lists:
    
    count = keywords.count(k)
    print(count)

count = 0
for item in data_lists:
    if item in keywords:
        count= count + 1
        print(count)

df.replace(np.nan, c, inplace=True)
df

# create loop that will go through the list of pairs and scrape google scholar for citations
    
def search_single_keyword(keyword):

    return scholarly.search_keyword(keyword)


def find_keyword_in_search_results(search_results, keyword):

    keyword_lowercase = keyword.lower()

    output = list()

    for record in search_results:

        interests_lowercase = [x.lower() for x in record.interests]

        if keyword_lowercase in interests_lowercase:
            output.append(record)

    return output


def number_of_searches_with_keywords(keyword1, keyword2):

    result = search_single_keyword(keyword1)

    result_combined = find_keyword_in_search_results(result, keyword2)

    return len(result_combined)

# loop through all columns

for keyword1, row in df.iterrows():

    result_kw1 = search_single_keyword(keyword1)
    
    for keyword2 in df.columns.values:

        result_combined = find_keyword_in_search_results(result_kw1, keyword2)
        num_combined = len(result_combined)
        
        # fill the table
        df.at[keyword1, keyword2] = num_combined
        sleep(randint(1,7))
        df.to_csv("results.csv", index=True)

df.head()

search_query = scholarly.search_pubs_query('Capitalism')
next(search_query)

author = next(search_query)
print(author)

print(author.citedby)

search_query2 = scholarly.search_keyword('Beirut')

print(next(search_query2))

# Print the titles of the author's publications
print([pub['citedby'] for pub in search_query])

# Take a closer look at the first publication
cited_by = search_query.publications[0].fill()
print(cited_by)


keyword1 = 'Dashboards'
keyword2 = 'Independence'

def search_single_keyword(keyword):

    return scholarly.search_keyword(keyword)

def find_keyword_in_search_results(search_results, keyword):

    keyword_lowercase = keyword.lower()

    output = list()

    for record in search_results:

        interests_lowercase = [x.lower() for x in record.interests]

        if keyword_lowercase in interests_lowercase:
            output.append(record)

    return output


def number_of_searches_with_keywords(keyword1, keyword2):

    result = search_single_keyword(keyword1)

    result_combined = find_keyword_in_search_results(result, keyword2)

    return len(result_combined)

# loop through all columns

for keyword1, row in df.iterrows():

    result_kw1 = search_single_keyword(keyword1)
    
    for keyword2 in df.columns.values:

        result_combined = find_keyword_in_search_results(result_kw1, keyword2)
        num_combined = len(result_combined)
        
        # fill the table
        df.at[keyword1, keyword2] = num_combined
        sleep(randint(1,5))
        df.to_csv("results.csv", index=True)
        break





