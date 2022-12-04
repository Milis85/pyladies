import requests
import json
from datetime import datetime, date
import os
from random import randint
import qrcode

DATA = 'https://data.kurzy.cz/json/meny/b[6].json'
KURZY = 'kurzy.json'
TEMPLATE = 'template.html'
ACCOUNT = '19-99970217/0100'
MY_IBAN = 'CZ4501000000190099970217'

class CurrencyError(Exception):
    pass

class Invoice:

    def download(self, url=DATA, file=KURZY):
        r = requests.get(url)
        #print(r.text)
        with open(file, 'w') as f:
            f.write(r.text)

    def exist_file(self, file=KURZY):
        existing_file = os.path.exists(file)
        return existing_file

    def load_file(self, file=KURZY):
        with open (file, 'r') as f:
            self.kurzy = json.loads(f.read())

    def control_date(self):
        date_kurzy = self.kurzy['den']
        today = date.today()
        today = today.strftime('%Y%m%d')
        return date_kurzy == today
    
    def correct_amount(self):
        '''zadana castka musi byt cislo, v pripade ze ne, program se ukonci'''
        if self.result < 0:
            raise Exception

        try:
            self.result = float(self.result)
            return self.amount
        except ValueError:
            exit()

    
    def calculate(self, amount, currency):
        try:
            amount = float(amount)
        except ValueError:
            raise Exception('Zadej castku v cislech')
            
        if currency == 'CZK':
            self.result = amount
        else:
            #print(self.kurzy)
            #print(currency)
            try:
                currency = self.kurzy['kurzy'][currency]['dev_stred']
            except KeyError:
                raise CurrencyError('Spatna mena')
            self.result = currency * amount


    def generate_invoice(self, item, template=TEMPLATE):
        
        today = date.today()
        today = today.strftime('%Y%m%d')
        var_symbol = today 
        img = qrcode.make(f'SPD*1.0*ACC:{MY_IBAN}*AM:{self.result}*CC:CZK*MSG:{item}*X-VS:{var_symbol}')
        img_qr = 'invoice' + var_symbol + '.png'
        img.save(img_qr)
        with open (template, 'r') as f_:
            template = f_.read()
            template = template.replace('KOLIK', str(self.result))
            template = template.replace('ZACO', item)
            template = template.replace('VSCISLO', var_symbol)
            template = template.replace('FC', var_symbol)
            template = template.replace('KAM', ACCOUNT)
            template = template.replace('KOD', img_qr)
        
        file_nr = ('invoice' + var_symbol + '.html')
        
        
        

        with open(file_nr, 'w') as fa:
            fa.write(template)


    
    
if __name__=='__main__':
    faktura = Invoice()
    if not faktura.exist_file():
        faktura.download()
    faktura.load_file()
    faktura.control_date()
    if not faktura.control_date():
        faktura.download()
    amount = input('Zadej castku: ')
    currency = (input('Zadej menu platby: ').upper())
    item = input('Zadej nazev polozky: ')
    faktura.calculate(amount, currency)
    faktura.correct_amount()

    
    print(faktura.result)
    faktura.generate_invoice(item)
    #print(faktura.kurzcastku,y['den'])
    #print(faktura.kurzy['kurzy']['AUD']['dev_stred'])
    #faktury.nacist
    #faktura.porovnrjdataum(jedno, druhy)

    


