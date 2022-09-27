#Exercise 2: Working With JSON
import json
sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
#Access the nested “salary” key from the JSON-string above.
print(sampleJson["company"]["employee"]["payable"]["salary"])
#Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
sampleJson["company"]["employee"]["birth_date"]="06-07-2000"

myJson = 'myJson.json'
with open(myJson,'w') as objectJson:
    json.dump(sampleJson,objectJson,indent=2,sort_keys=True)
