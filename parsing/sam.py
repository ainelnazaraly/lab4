import json

with open ('sample_data.json') as file: 
    data=json.load(file)
    print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
i=1
for item in data['imdata']: 
    l1=item["l1PhysIf"]
    att=l1["attributes"]
    
    while i<4:
        print(att["dn"], "                            ", att["speed"], " ", att["mtu"])
        i+=1