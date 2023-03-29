from multiprocessing import Pool, Process, Pipe


def f(i, k):
    j = 0
    for j in range(i, k):
        print(j)
        j = j + 1


if __name__ == '__main__':
    # p = Process(target=f, args=(10000, 50000,))
    t = Process(target=f, args=(0, 100000,))
    # p.start()
    t.start()
    t.join()
    # p.join()
