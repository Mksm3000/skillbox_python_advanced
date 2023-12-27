"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
import re
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(a=1, b=10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


def search(data: dict[int, BinaryTreeNode]) -> int:
    leaves = set()
    champion = -1

    for key, value in data.items():
        # print(key, value.left, value.right)

        if value.left is not None:
            leaves.add(value.left.val)
        if value.right is not None:
            leaves.add(value.right.val)

    print(leaves)

    for key in data.keys():
        if key not in leaves:
            champion = key

    return champion


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    # Генерируем само дерево (словарь)
    tree: dict[int, BinaryTreeNode] = {}
    # Создаем паттерн по которому будем доставать нужно значение
    pattern: str = r"\d+"

    # идем циклом по логам
    with open(path_to_log_file) as log:
        for line in log.readlines():

            # Получаем нужные значения из строк лога, по которым будем создавать узлы и если есть ветку
            values: list[int] = list(map(int, re.findall(pattern, line)))

            # Проверяем на наличие INFO - это по логам и есть корень от которого будут идти следующие ветки
            if "INFO" in line and values[0] not in tree:
                tree[values[0]] = BinaryTreeNode(val=values[0])

            #  Создаем для левой части
            elif "left" in line:
                left = BinaryTreeNode(val=values[1])
                tree[values[1]] = left
                tree[values[0]].left = tree[values[1]]

            # Создаем для правой части
            elif "right" in line:
                right = BinaryTreeNode(val=values[1])
                tree[values[1]] = right
                tree[values[0]].right = tree[values[1]]

    bingo = search(tree)
    return BinaryTreeNode(bingo)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_4.txt",
        filemode='w'
    )

    root = get_tree(7)
    walk(root)

    result = restore_tree('walk_log_4.txt')
    print(result)
