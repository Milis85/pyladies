
import piskvorky

def test_vyhra_x():
    assert piskvorky.vyhodnot('xxx-----------------') == 'x'

def test_vyhra_o():
    assert piskvorky.vyhodnot('---ooo--------------') == 'o'

def test_remiza():
    assert piskvorky.vyhodnot('ooxxooxxooxxooxxooxx') == '!'
    assert piskvorky.vyhodnot('xoxoxoxoxoxoxoxoxoxo') == '!'

def test_prazdne_pole():
    assert piskvorky.vyhodnot('---------------------') == '-'
    assert piskvorky.vyhodnot('x---------o----------') == '-'

def test_tah():
    assert piskvorky.tah('--------------------', 5, 'x') == '-----x--------------'
    assert piskvorky.tah('--------------------', 1, 'o') == '-o------------------'

