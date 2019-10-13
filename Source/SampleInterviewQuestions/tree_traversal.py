from queue import Queue


def depth_first_search(root):
    if root is None:
        return ''
    elif not all(root.children):
        return root
    else:
        children = root.children
        path = ''

        for child in children:
            path += depth_first_search(child) + ' '

        return path + root.name


def breadth_first_search(root):
    path = ''
    queue = Queue()

    if root is None:
        return path

    while True:
        if queue.empty():
            node = root
        else:
            node = queue.get()
            path += ' '

        path += node.name

        for child in node.children:
            queue.put(child)

        if queue.empty():
            break

    return path
