#!/usr/bin/python
# coding: utf-8

from bson.objectid import ObjectId
from pymongo import MongoClient

# client = MongoClient('mongodb://sa:eagle-sight@118.24.97.166:27017/device');
client = MongoClient('mongodb://eagle:Uvd7799nJ@192.168.100.240:20000/device');
db = client.device;
t = db.T_CloudMirrorFacilityLocation;
print("db count is = ", t.count_documents({}));
t.delete_many({"IMEI": "xiajunceshi"})
data = {"Pid": "2c9616b12d2a483dac725fb8389a9b70", "IMEI": "xiajunceshi", "ReportReason": 0, "Longitude": "104.153290",
        "Ltitude": "30.643254", "Radius": "", "AddressStr": "sccd", "Province": "四川省", "City": "cds", "District": "cfq",
        "Direction": "", "Remark": "", "CreateUser": "CloudMirror", "CreateDate": None, "UpdateUser": None,
        "UpdateDate": None, "RecordTime": None, "IsEnabled": 0}
# print([data,data,data])
# t.insert_many(data)
# print(t.find({"IMEI":"xiajunceshi"}))
# for x in t.find({"IMEI":"xiajunceshi"}):
#    print(x)
# post_id = t.insert_one(data).inserted_id;

# for num in range(1,20):
#    t.insert_one(data);

# count = 0
# while (count < 9):
#   print('The count is:', count)
#   post_id = t.insert_one(data).inserted_id;
#   count = count + 1

# print(t.count_documents({"IMEI":"xiajunceshi"}));
