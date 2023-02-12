from katas.hash_table import hash_table


def test_homemade_hasher_1__within_array_len() -> None:
    # setup hash table and get hash function
    array_len = 10
    ht = hash_table[int](array_len)
    hasher = ht.hasher_homemade_1

    # hash a keys
    hashed_key_1 = hasher("5", array_len)
    hashed_key_2 = hasher("999999asfd;af", array_len)
    hashed_key_3 = hasher("0" * 100, array_len)
    hashed_key_4 = hasher("0" * 105, array_len)

    # check keys are within array_len
    assert hashed_key_1 <= array_len - 1
    assert hashed_key_2 <= array_len - 1
    assert hashed_key_3 == hashed_key_4


def test_homemade_hasher_2__within_array_len() -> None:
    # setup hash table and get hash function
    array_len = 10
    ht = hash_table[int](array_len)
    hasher = ht.hasher_homemade_2

    # hash a keys
    hashed_key_1 = hasher("5", array_len)
    hashed_key_2 = hasher("999999asfd;af", array_len)
    hashed_key_3 = hasher("0" * 100, array_len)
    hashed_key_4 = hasher("0" * 105, array_len)

    # check keys are within array_len
    assert hashed_key_1 <= array_len - 1
    assert hashed_key_2 <= array_len - 1
    assert hashed_key_3 != hashed_key_4


def test_hash_table__can_set_item() -> None:
    # setup hash table and get hash function
    array_len = 10
    ht = hash_table[int](array_len)

    # set items to hash table
    ht.set("pink", 100)
    ht.set("orange", 500)


def test_hash_table__can_get_item() -> None:
    # setup hash table and get hash function
    array_len = 10
    ht = hash_table[int](array_len)

    # set items to hash table
    ht.set("pink", 100)
    ht.set("orange", 500)

    # get item from hash table
    orange_tuple = ht.get("orange")
    pink_tuple = ht.get("pink")

    # check correct tuple retrieved
    assert orange_tuple == ("orange", 500)
    assert pink_tuple == ("pink", 100)


def test_find_item__found_key() -> None:
    # setup input items
    test_array = [("pink", 100), ("orange", 500)]
    find_item = hash_table[int]._find_item

    # perform find
    item_pair = find_item(test_array, "pink")

    # check item_pair value
    assert item_pair == ("pink", 100)


def test_find_item__found_none() -> None:
    # setup input items
    test_array = []
    find_item = hash_table[int]._find_item

    # perform find
    item_pair = find_item(test_array, "pink")

    # check item_pair value
    assert item_pair == None


def test_hash_table__keys() -> None:
    # setup input items
    ht = hash_table[int]()
    ht.set("a", 96)
    ht.set("b", 97)
    ht.set("c", 96)

    # perform find
    ht_keys = ht.keys()

    """
    [
        [("a", 96)],  hash 1
        [("b", 97)],  hash 2
        [("c", 96)]   hash 3
    ]
    """

    # check item_pair value
    assert set(ht_keys) == set(["a", "b", "c"])

def test_hash_table__values() -> None:
    # setup input items
    ht = hash_table[int]()
    ht.set("a", 96)
    ht.set("b", 97)
    ht.set("c", 96)

    # perform find
    ht_values = ht.values()

    # check item_pair value
    assert ht_values == [96, 97, 96]
