import login;
import json;
from bs4 import BeautifulSoup;

'''
FUNCTIONS
'''

'''
FUNC: getSubjectsURL
Input:
 - branch {"Computer Science","IT","EXTC","FIRST YEAR","Mechanical"}
 - year {"First Year","Second Year","Third Year","BE"}
Output:
 - url of that page
'''
def getSubjectsURL(branch,year):
    if branch not in ["Computer Science","IT","EXTC","FIRST YEAR","Mechanical"]:
        print("ERROR: invalid branch")
        return(None);
    if year not in ["First Year","Second Year","Third Year","BE"]:
        print("ERROR: Invalid year");
        return(None);
    categ_id_file = open("categoryid.txt","r");
    categ_dic = json.loads(categ_id_file.readline());
    subjects = categ_dic[branch];
    cid = subjects[year];# categoryid
    url="http://moodle.dbit.in/course/index.php?categoryid="+cid;
    return(url);

'''
FUNC: getSubjectsDict
Input:
 - url: url of the subjects page
 - sess: session object from main
Output:
 - Dictionary of {"subject":"url"}
'''
def getSubjectsDict(url,sess):
    response = sess.get(url);
    soup = BeautifulSoup(response.text,"lxml");
    links = soup.body.find_all("a");
    #print(links);
    result = dict();
    for link in links:
        #print(link["href"]);
        if "title" in link.attrs.keys():
            if notInCheck(link["title"],["Summary","Forum","View profile","Connaissance","Seminar","UGC INterview 15 - 16"]):
                #print(link["title"]+" :: "+link["href"]);
                result[link["title"]] = link["href"];
                #print("\n\n")
    return(result);

def notInCheck(text,ls):
    for s in ls:
        if text == s:
            #print(text+" == "+s);
            return(False);
    return(True);
