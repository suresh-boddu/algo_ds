from ds.arrays.stack import AStack
from ds.arrays.stack import Stack


def list_stack_demo():
    print "Stack Demo using List\n"
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.display()

    print "Deleted: " + str(stack.pop())
    print "Deleted: " + str(stack.pop())
    print "Deleted: " + str(stack.pop())

    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.display()

    print "Deleted: " + str(stack.pop())
    print "Deleted: " + str(stack.pop())

    stack.push(9)
    stack.push(10)

    print stack.is_empty()


def array_stack_demo():
    print "Stack Demo using Array\n"
    stack = AStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.display()

    print "Deleted: " + str(stack.pop())
    print "Deleted: " + str(stack.pop())
    print "Deleted: " + str(stack.pop())

    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.display()

    print "Deleted: " + str(stack.pop())
    print "Deleted: " + str(stack.pop())

    stack.push(9)
    stack.push(10)

    print stack.is_empty()


if __name__ == "__main__":
    list_stack_demo()
    array_stack_demo()