import unittest
import status_checker

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

	def test_check_existence_of_stacks(self):
		existence = status_checker.check_existence_of_stacks(status_checker.stacks_to_be_checked)
		self.assertTrue(existence)
		# print existence

	def test_get_status_using_stack_names(self):
		status_of_stacks = status_checker.get_status_using_stack_names(status_checker.stacks_to_be_checked)
		self.assertTrue(type(status_of_stacks) is dict)
		self.assertIsNotNone(status_of_stacks)
		# print status_of_stacks

	def test_manipulate_results_data_for_humans(self):
		stacks_to_be_checked = status_checker.get_stacks_to_be_tested()
		raw_results = status_checker.get_status_using_stack_names(stacks_to_be_checked)
		human_friendly_results = status_checker.manipulate_results_data_for_humans(raw_results)
		self.assertTrue(type(human_friendly_results) is str)
		self.assertFalse(human_friendly_results == "")

if __name__ == '__main__':
    unittest.main()
