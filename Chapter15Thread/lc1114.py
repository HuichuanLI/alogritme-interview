from time import sleep


# 单线程
class Foo:

    def __init__(self):
        self.t = 0


def first(self, printFirst: 'Callable[[], None]') -> None:
    printFirst()
    self.t = 1


def second(self, printSecond: 'Callable[[], None]') -> None:
    while self.t != 1:
        sleep(1e-3)
    printSecond()
    self.t = 2


def third(self, printThird: 'Callable[[], None]') -> None:
    while self.t != 2:
        sleep(1e-3)
    printThird()


# 使用Lock
import threading


class Foo:
    def __init__(self):
        self.l1 = threading.Lock()
        self.l1.acquire()
        self.l2 = threading.Lock()
        self.l2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.l1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.l1.acquire()
        printSecond()
        self.l2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.l2.acquire()
        printThird()


# 使用了Semaphore

import threading


class Foo:
    def __init__(self):
        self.l1 = threading.Semaphore(0)
        self.l2 = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.l1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.l1.acquire()
        printSecond()
        self.l2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.l2.acquire()
        printThird()


# queue 多线程的阻塞队列

import queue


class Foo:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.put(0)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.get()
        printSecond()
        self.q2.put(0)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.get()
        printThird()
