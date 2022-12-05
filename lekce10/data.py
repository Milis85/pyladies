import requests
import json
from datetime import date
import os
from random import randrange
import qrcode

DATA = 'https://data.kurzy.cz/json/meny/b[6].json'
KURZY = 'kurzy.json'
TEMPLATE = 'template.html'
ACCOUNT = '19-99970217/0100'
MY_IBAN = 'CZ4501000000190099970217'


class CurrencyError(Exception):
    '''Vytvoreni vlastni vyjimky u chybne zadane meny'''
    pass


class Invoice:

    def download(self, url=DATA, file=KURZY):
        '''Stazeni URL s kurzy a ulozeni do souboru'''
        r = requests.get(url)
        with open(file, 'w') as f:
            f.write(r.text)

    def exist_file(self, file=KURZY):
        '''Overeni existence souboru s daty z URL'''
        existing_file = os.path.exists(file)
        return existing_file

    def load_file(self, file=KURZY):
        '''Ulozeni dat do promenne'''
        with open(file, 'r') as f:
            self.kurzy = json.loads(f.read())

    def control_date(self):
        '''Kontrola aktualniho data s datem na kurzovnim listku'''
        date_kurzy = self.kurzy['den']
        today = date.today()
        today = today.strftime('%Y%m%d')
        return date_kurzy == today

    def correct_amount(self):
        '''zadana castka musi byt cislo, v pripade ze ne, program se ukonci'''
        if self.result < 0:
            raise ValueError('The amount must be positive number')

        try:
            self.result = float(self.result)
            return self.result
        except ValueError:
            exit()

    def calculate(self, amount, currency):
        try:
            amount = float(amount)
        except ValueError:
            raise Exception('Wrong amount')

        if currency == 'CZK':
            self.result = amount
        else:
            try:
                currency = self.kurzy['kurzy'][currency]['dev_stred']
            except KeyError:
                raise CurrencyError('Wrong currency')
            self.result = currency * amount

    def generate_invoice(self, item, template=TEMPLATE):
        '''Generuje fakturu'''
        today = date.today()
        today = today.strftime('%Y%m%d')
        uniq_nr = randrange(100)
        var_symbol = today + str(uniq_nr)
        img = qrcode.make(f'SPD*1.0*ACC:{MY_IBAN}*AM:{self.result}*CC:CZK*MSG:{item}*X-VS:{var_symbol}')
        img_qr = 'invoice' + var_symbol + '.png'
        img.save(img_qr)
        with open(template, 'r') as f_:
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


if __name__ == '__main__':
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
