'''
Jacques' testing file
'''

import login;
import subjects;
import getpass;

if __name__ == "__main__":
    m_sess = login.login();
    url = subjects.getSubjectsURL("Computer Science","Third Year");
    print(subjects.getSubjectsDict(url,m_sess));
