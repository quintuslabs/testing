import requests
import csv

# postdata = {'symbol_name: fname','option_type:BuyCE','buy_price:200','target_price:100','achievement:75%'}
API_ENDPOINT = ('http://192.168.1.18:8000//api/options/create/')
def csv_f():
    fobj = open('API_Option_test_Exe.csv', 'w')
    fobj.write('symbol_name' + ',' + 'option_type' + ',' + 'Status_code' + ',' + 'Status_Message' + '\n')

    with open('Option.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if 'symbol_name' not in row:
                print(row)
                status_code, status_msg = option_Apicall(API_ENDPOINT, row[0], row[1], row[2], row[3], row[4])
                fobj.write(row[0] + ',' + row[1] + ',' + str(status_code) + ',' + str(status_msg) + '\n')
        fobj.close()



def option_Apicall(API_ENDPOINT, sym, opt, buy_pr, target_pr, achi):

    """Api Request options


    api/options/create/
    function taking user input"""
    data = {'symbol_name': sym, 'option_type': opt, 'buy_price': buy_pr, 'target_price': target_pr, 'achievement':achi}

    r = requests.post(url=API_ENDPOINT , data=data)
    pastebin_url = r.status_code
    pastebin_msg = r.text
    return pastebin_url, pastebin_msg


csv_f()
