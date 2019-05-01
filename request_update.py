import requests
import csv

API_ENDPOINT = 'http://192.168.1.18:8000/api/users/login/'
def csv_f():
    fobj = open('API_Login_Test_Execution_Status.csv','w')
    fobj.write('UserName'+','+'Password'+','+'Status_code'+','+'Status_Message'+'\n')
    with open('reister_API.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if 'phone' not in row:
                print(row)
                status_code,status_msg = register_Apicall(API_ENDPOINT,row[3], row[4])
                
                fobj.write(row[3]+','+row[4]+','+str(status_code)+','+status_msg+'\n')
        fobj.close()
        print(f'Processed {line_count} lines.')

def register_Apicall(API_ENDPOINT,fname,lname):

    data = {'first_name': fname,'last_name': lname}
    print(data)
    r = requests.post(url=API_ENDPOINT, data=data)
    pastebin_url = r.status_code
    pastebin_msg = r.text
    print("The pastebin URL is:%s" %pastebin_url)
    print("The pastebin Msg is:%s" %pastebin_msg)
    return pastebin_url,pastebin_msg

csv_f()