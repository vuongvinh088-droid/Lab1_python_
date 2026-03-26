import json
with open("test.json","r") as f:
    data= json.load(f)
    for k in data["sv2"]:
        print(k,":",data["sv2"][k])