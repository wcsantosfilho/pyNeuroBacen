#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:39:00 2020
#PYNEUROREQUEST - Submit requests to Neurotech
@author: wcsantosfilho
"""

import json
import requests

def getNeuro(cpf):
    url =  ENV_URL
    objModel = """{
        "Submit": {
            "Id": "#@#cpfcnpj#@#",
            "Inputs": [
                {
                    "Name": ENV_NAME,
                    "Value": ENV_VALUE
                }, {
                    "Name": ENV_NAME,
                    "Value": ENV_VALUE 
                }
            ],
            "Policy": ENV_POLICY,
            "ResultingVariable": ENV_RESULTINGVARIABLE
        },
        "Authentication": {
            "Login": ENV_LOGIN,
            "Password": ENV_PASSWORD,
            "Properties": [{
                    "Key": "FILIAL_ID",
                    "Value": "0"
                }
            ]
        },
        "Properties": [{
                "Key": "USUARIO",
                "Value": ENV_CIA
            }
        ]
    }"""

    myobj = objModel.replace("#@#cpfcnpj#@#", cpf)

    y = json.loads(myobj)
    x = requests.post(url, data=myobj, headers = {"Content-Type": "application/json"}, timeout=50.0)

    outputfile = './responses/' + 'resp_' + cpf + '.json'
    g = open(outputfile, "wt")
    if ( x.status_code == 200):
        g.write(x.content)
    else:
        g.write(cpf)
        g.write(x.status_code)
    g.close
    return x.status_code

if __name__ == "__main__":
    listaCPFs = [ "123"]
    for cpf in listaCPFs:
        getNeuro(cpf)
