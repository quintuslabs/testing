import requests
import csv

API_ENDPOINT = 'http://192.168.1.18:8000/api/users/2/update/'
token = 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Ijg5ODM0NTc4MjMiLCJleHAiOjE1NTYxNTk2MDgsIm9yaWdfaWF0IjoxNTU2MTA3NzY4fQ.bebRNhDRRKtxPTAoV0VI_Q7CLZQcMshRHzEmFNVXU_I'
def csv_f():
    fobj = open('API_Login_Test_Execution_Status.csv', 'w')
    fobj.write('UserName' + ',' + 'Password' + ',' + 'Status_code' + ',' + 'Status_Message' + '\n')
    with open('reister_API.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if 'phone' not in row:
                print(row)

def register_Apicall(API_ENDPOINT,fname,lname):
    data = {'first_name': fname,'last_name': lname}
    print(data)
    #r = requests.put(url=API_ENDPOINT, data=data)
    r = requests.put(url=API_ENDPOINT, headers={'authorization':token}, data=data)
    pastebin_url = r.status_code
    pastebin_msg = r.text
    print("The pastebin URL is:%s" %pastebin_url)
    print("The pastebin Msg is:%s" %pastebin_msg)
    return pastebin_url,pastebin_msg

register_Apicall(API_ENDPOINT,'bgcbv','hgbc')
csv_f()