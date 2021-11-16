import json, requests

class Getdata:  
    def gettocep(cep):
        api = "https://viacep.com.br/ws/"
        data = requests.get(str(api)+str(cep)+"/json/")
        data_dict = json.loads(data.text)
        dataf = f"""Cep: {data_dict['cep']}\n
        Logradouro: {data_dict['logradouro']}\n
        Complemento: {data_dict['complemento']}\n
        Bairro: {data_dict['bairro']}\n
        Localidade: {data_dict['localidade']}/{data_dict['uf']}\n
        DDD: {data_dict['ddd']}\n\n"""
        return dataf

    def gettoadress(input1, input2, input3):
        api = "https://viacep.com.br/ws/"
        uf = input1
        cidade = input2.replace(" ", "%20")
        bairro = input3.replace(" ", "+")
        data = requests.get(str(api)+str(uf)+"/"+str(cidade)+"/"+str(bairro)+"/json/")
        data = json.loads(data.text) 
        return data