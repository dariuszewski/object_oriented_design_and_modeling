from wizcoin import WizCoin, WizCoinException

def test_weight():
    purse = WizCoin(1,1,1)
    assert purse.weight > 49
    assert purse.weight('kilograms') > 0.004
test_weight()

def test_total():
    chest = WizCoin(100, 50, 10)
    assert chest.total == 50760
test_total()

def test_add():
    bag_of_galleons = WizCoin(1000, 0, 0)
    bag_of_knuts = WizCoin(0, 0, 1000)

    big_bag = bag_of_galleons + bag_of_knuts

    assert big_bag == WizCoin(1000, 0, 1000)

    big_bag += WizCoin(0, 1000, 0)

    assert big_bag == WizCoin(1000, 1000, 1000)
test_add()

def test_comparison():
    bag_of_galleons = WizCoin(1000, 0, 0)
    bag_of_knuts = WizCoin(0, 0, 1000)
    big_bag = bag_of_galleons + bag_of_knuts

    assert big_bag > bag_of_galleons

    assert bag_of_galleons != bag_of_knuts

    assert big_bag == big_bag
test_comparison()