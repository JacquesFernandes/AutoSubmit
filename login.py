import requests;
import getpass;
#from bs4 import BeautifulSoup;

def getSession(username, password):
	login_data = {"username":username,"password":password};
	moodle_session = requests.Session();

	response = moodle_session.post("https://moodle.dbit.in/login/index.php",data=login_data,verify=False);
	#"verify=False" is used to deal with HTTPS certificate issue which moodle currently has, remove once the issue has been reolved...

	#bs = BeautifulSoup(response.content,"html.parser");
	#print(bs.prettify());
	if response.status_code == 200:
		print("Successful connection to site... [Received 200]");
		if response.url is "https://moodle.dbit.in/login/index.php":
			print("ERROR: Bad Login!");
			return(None);
		elif response.url == "https://moodle.dbit.in/":
			print("logged in as: "+username);
			return(moodle_session);



if __name__ == "__main__":
	m_sess = None;
	username = input("Username: ");
	password = getpass.getpass("Password: ");
	while m_sess is None:
		m_sess = getSession(username,password);
	print("Exiting");
