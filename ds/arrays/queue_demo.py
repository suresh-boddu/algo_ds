from ds.arrays.queue import AQueue
from ds.arrays.queue import Queue


def list_queue_demo():
    print "Queue Demo using List\n"
    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)
    queue.insert(5)
    queue.display()

    print "Deleted: " + str(queue.delete())
    print "Deleted: " + str(queue.delete())
    print "Deleted: " + str(queue.delete())

    queue.insert(6)
    queue.insert(7)
    queue.insert(8)
    queue.display()

    print "Deleted: " + str(queue.delete())
    print "Deleted: " + str(queue.delete())

    queue.insert(9)
    queue.insert(10)
    queue.display()

    print queue.is_empty()


def array_queue_demo():
    print "Queue Demo using Array\n"
    queue = AQueue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)
    queue.insert(5)
    queue.display()

    print "Deleted: " + str(queue.delete())
    print "Deleted: " + str(queue.delete())
    print "Deleted: " + str(queue.delete())

    queue.insert(6)
    queue.insert(7)
    queue.insert(8)
    queue.display()

    print "Deleted: " + str(queue.delete())
    print "Deleted: " + str(queue.delete())

    queue.insert(9)
    queue.insert(10)
    queue.display()

    print queue.is_empty()

if __name__ == "__main__":
    list_queue_demo()
    array_queue_demo()