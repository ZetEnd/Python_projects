# узел бинарного дерева
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# ф-ия для обхода дерева по
# центрированному алгоритму
def print_inorder(root):

	if root:

		# рекурсивно возвращаемся к левому поддереву
		print_inorder(root.left)

		# выводим данные узла
		print(root.val),

		# рекурсивно возвращаемся к правому поддереву
		print_inorder(root.right)

# ф-ия для обхода дерева по
# обратному алгоритму
def print_postorder(root):

	if root:

		# рекурсивно возвращаемся к левому поддереву
		print_postorder(root.left)

		# рекурсивно возвращаемся к правому поддереву
		print_postorder(root.right)

		# выводим данные узла
		print(root.val),

# ф-ия для обхода дерева по
# прямому алгоритму
def print_preorder(root):

	if root:

		# сначала выводим данные
		print(root.val),

		# рекурсивно возвращаемся к левому поддереву
		print_preorder(root.left)

		# рекурсивно возвращаемся к правому поддереву
		print_preorder(root.right)


# запускаем шайтан-код
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Обход по прямому алгоритму:")
print_preorder(root)
# Обход по прямому алгоритму:
# 1
# 2
# 4
# 5
# 3

print("\nОбход по центрированному алгоритму:")
print_inorder(root)
# Обход по центрированному алгоритму:
# 4
# 2
# 5
# 1
# 3

print("\nОбход по обратному алгоритму:")
print_postorder(root)
# Обход по обратному алгоритму:
# 4
# 5
# 2
# 3
# 1
