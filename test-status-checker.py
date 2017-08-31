import unittest
import status_checker


# a = status_checker.get_all_stacks_info()
# print a

class StatusCheckerTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_get_all_stacks_info(self):
		response = status_checker.get_all_stacks_info()
		self.assertIsNotNone(response)
		# print response

	def test_get_all_stack_names(self):
		all_the_stacks = status_checker.get_all_stack_names()
		self.assertIsNotNone(all_the_stacks)
		for each_stack in all_the_stacks:
			self.assertIn(each_stack, all_the_stacks)
 			# print each_stack

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
