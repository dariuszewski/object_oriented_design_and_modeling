from Queue import *

def test_shift():
    colors = Queue()
    colors.shift("Pthalo Blue")
    assert colors.count() == 1
    colors.shift("Ultramarine Blue")
    assert colors.count() == 2
test_shift()

def test_unshift():
    colors = Queue()
    colors.shift("Magenta")
    colors.shift("Alizarin")
    assert colors.unshift() == "Magenta"
    assert colors.unshift() == "Alizarin"
    assert colors.unshift() == None
test_unshift()

def test_first():
    colors = Queue()
    colors.shift("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Pthalo Green")
    assert colors.first() == "Cadmium Red Light"
test_first()
