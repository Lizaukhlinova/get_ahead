from flattened_iterator import FlattenedIterator


def test_1():
    print("Test 1:")
    it1 = iter([1, 2, 3])
    it2 = iter([4, 5])
    it3 = iter([6, 7, 8])
    flat_iter = FlattenedIterator(it1, it2, it3)
    for i in flat_iter:
        print(i)
    print()


def test_2():
    print("Test 2:")
    it1= iter([1, 2, 3])
    it2 = iter([])
    it3 = iter([6, 7])
    flat_iter = FlattenedIterator(it1, it2, it3)
    for i in flat_iter:
        print(i)
    print()


if __name__ == '__main__':
    test_1()
    test_2()
