import unittest
import status_checker


# a = status_checker.get_all_stacks_info()
# print a

class StatusCheckerTest(unittest.TestCase):
	def setUp():
		pass

# 	def tearDown(self):
# 		pass

	def test_get_all_stacks_info():
		response = status_checker.get_all_stacks_info()
		print response

# 	def test_get_all_stack_names():
# 		all_the_stacks = get_all_stack_names()
# 		for x in all_the_stacks:
# 			print x

# 	def test_get_status_using_stack_ids(stack_id):
# 		all_the_status = get_status_using_stack_ids(stack_id)
# 		print all_the_status

# 	def test_check_existence_of_stacks(stacks_to_be_checked):
# 		existence = check_existence_of_stacks(stacks_to_be_checked)
# 		print existence

# 	def test_get_status_using_stack_names(stacks_to_be_checked):
# 		status_of_stacks = get_status_using_stack_names(stacks_to_be_checked)
# 		print status_of_stacks

# test_get_all_stacks_info()
# test_get_all_stack_names()
# test_get_status_using_stack_ids(stack_id)
# test_get_status_using_stack_names(stacks_to_be_checked)
# test_check_existence_of_stacks(stacks_to_be_checked)


if __name__ == '__main__':
    unittest.main()
