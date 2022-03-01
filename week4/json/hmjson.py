import json
cnt = 0
print("Interface Status")
print("================================================================================")
print("DN                                                 ", end = '')
print("Description           ", end = '')
print("Speed    ", end = '')
print("MTU")
print("-------------------------------------------------- --------------------  ------  ------")
js = open('sample-date.json')
data = json.load(js)
for i in data['imdata']:
    print(i['l1PhysIf']['attributes']['dn'], end = '                              ')
    for j in data['imdata']:
        print(j['l1PhysIf']['attributes']['fecMode'], end = '   ')
        break
    for i in data['imdata']:
        print(i['l1PhysIf']['attributes']['mtu'])
        break
    cnt = cnt + 1
    if(cnt == 3):
        break
