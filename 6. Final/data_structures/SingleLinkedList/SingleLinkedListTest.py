from SingleLinkedList import *


def test_push():
    colors = SingleLinkedList()
    colors.push("Pthalo Blue")  
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors.push("Ultramarine Violet")
    assert colors.count() == 3
test_push()


def test_pop():
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None
test_pop()


def test_unshift():
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    colors.push("Azure")
    assert colors.unshift() == "Magenta"
    assert colors.unshift() == "Alizarin"
    assert colors.unshift() == "Azure"
    assert colors.unshift() == None
test_unshift()



def test_shift():
    colors = SingleLinkedList()
    colors.shift("Pthalo Blue")  
    assert colors.count() == 1
    colors.shift("Ultramarine Blue")
    assert colors.count() == 2
    colors.pop() == ("Pthalo Blue")
    assert colors.count() == 1
test_shift()


def test_remove():
    colors = SingleLinkedList()
    colors.push("Cobalt")
    colors.push("Cyan")
    colors.push("Nicel")
    colors.push("Perinione")
    assert colors.remove("Cobalt") == 0
    assert colors.remove("Perinione") == 2
    assert colors.remove("Nicel") == 1
    assert colors.remove("Cyan") == 0
test_remove()

def test_first():
    colors = SingleLinkedList()
    colors.push("Red")
    assert colors.first() == "Red"
    colors.push("Green")
    assert colors.first() == "Red"
test_first()

def test_last():
    colors = SingleLinkedList()
    colors.push("Red")
    assert colors.last() == "Red"
    colors.push("Green")
    assert colors.last() == "Green"
test_last()

def test_get():
    colors = SingleLinkedList()
    colors.push("White")
    assert colors.get(0) == "White"
    colors.push("Black")
    assert colors.get(0) == "White"
    assert colors.get(1) == "Black"
    colors.push("Yellow")
    assert colors.get(0) == "White"
    assert colors.get(1) == "Black"
    assert colors.get(2) == "Yellow"
    assert colors.pop() == "Yellow"
    assert colors.get(0) == "White"
    assert colors.get(1) == "Black"
    assert colors.get(2) == None
    colors.pop()
    colors.pop()
    assert colors.get(0) == None
test_get()