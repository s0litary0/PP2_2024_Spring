import json

print("Interface Status\n================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

with open('sample-data.json') as file:
    json_dict = json.load(file)

layer1 = json_dict['imdata']

def info_print(layerN):
    print(layerN["dn"], end = "         ")
    print(layerN["descr"], end = "                     ")
    print(layerN["speed"], end = "   ")
    print(layerN["mtu"])
for x in layer1:
    layer2 = x["l1PhysIf"]
    layer3 = layer2["attributes"]
    if layer3["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/33]": 
        info_print(layer3)
    if layer3["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/34]":
        info_print(layer3)
    if layer3["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/35]":
        info_print(layer3)