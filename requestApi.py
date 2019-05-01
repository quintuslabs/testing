import requests
import csv

postdata = {"first_name: Jacob","last_name:moran","phone:8983457823","email:j.moran@yahoo.in","password:jacob@1234"}
API_ENDPOINT  = ('http://192.168.1.18:8000/api/users/register/')
def csv_f():

    with open('reister_API.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if 'first_name' not in row:
                print(row)
                register_Apicall(API_ENDPOINT,row[0],row[1],row[2],row[3],row[4])
            print(f'Processed {line_count} lines.')

def register_Apicall(API_ENDPOINT,fname,lname,phone,email,password):

    """Api Request post
    api/users/register
    function taking user input"""
    data = {'first_name': fname,'last_name':lname,'phone':phone,'email':email,'password':password}

#    r = requests.post(url=API_ENDPOINT , data=data)
#    pastebin_url = r.status_code

    print("The pastebin URL is:%s"%pastebin_url)


#register_Apicall(API_ENDPOINT,fname,lname,phone,email,password)
csv_f()
