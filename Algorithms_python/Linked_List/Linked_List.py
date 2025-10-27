# Класс узла
class Node:
	# Инициализация объекта узел
	def __init__(self, data):
		self.data = data # присваиваем данные
		self.next = None # инициализируем
						# далее - null

# Класс связанного списка
class LinkedList:
	# Инициализация связанного списка
	# объект - список
	def __init__(self):
		self.head = None

# печатает содержимое связанного списка
	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next


# Исполнение начинается отсюда
if __name__=='__main__':

	# начнём с пустого списка
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)


	llist.head.next = second
	second.next = third

	llist.print_list()

	'''
	Создали три узла.
	Их имена: head, second и third

	llist.head	   second		   third
		|			 |				 |
		|			 |				 |
	+----+------+	 +----+------+	 +----+------+
	| 1 | None |	 | 2 | None |	 | 3 | None |
	+----+------+	 +----+------+	 +----+------+
	'''

	llist.head.next = second # связываем первый узел со вторым

	'''
	Первый узел ссылается на второй.
	Теперь они связаны.

	llist.head	   second		   third
		|			 |				 |
		|			 |				 |
	+----+------+	 +----+------+	 +----+------+
	| 1 | o-------->| 2 | null |	 | 3 | null |
	+----+------+	 +----+------+	 +----+------+
	'''

	second.next = third # связываем второй узел с третьим

	'''
    Второй узел ссылается на третий.
	Теперь они связаны.

	llist.head	 second			 third
		|			 |				 |
		|			 |				 |
	+----+------+	 +----+------+	 +----+------+
	| 1 | o-------->| 2 | o-------->| 3 | null |
	+----+------+	 +----+------+	 +----+------+
	'''