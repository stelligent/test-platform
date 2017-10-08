import boto3

stack_name = 'StackName'
stack_status = 'StackStatus'
failure_states = ['CREATE_FAILED', 'ROLLBACK_COMPLETE','ROLLBACK_IN_PROGRESS','UPDATE_ROLLBACK_FAILED','UPDATE_ROLLBACK_IN_PROGRESS','ROLLBACK_FAILED']
success_states = ['CREATE_COMPLETE','UPDATE_COMPLETE','UPDATE_COMPLETE_CLEANUP_IN_PROGRESS']

def get_all_stacks_info():
	client = boto3.client('cloudformation')
	# response is a dict
	response = client.list_stacks(
    	StackStatusFilter=[
        	'CREATE_IN_PROGRESS','CREATE_FAILED','CREATE_COMPLETE','ROLLBACK_IN_PROGRESS','ROLLBACK_FAILED','ROLLBACK_COMPLETE','UPDATE_IN_PROGRESS','UPDATE_COMPLETE_CLEANUP_IN_PROGRESS','UPDATE_COMPLETE','UPDATE_ROLLBACK_IN_PROGRESS','UPDATE_ROLLBACK_FAILED','UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS','UPDATE_ROLLBACK_COMPLETE','REVIEW_IN_PROGRESS',
    	]
	)
	return response

def get_all_stack_names():
	# print response['StackSummaries'][0]['StackName']
	list_of_stack_names = []
	response = get_all_stacks_info()
	for key in response['StackSummaries']:
		if stack_name in key:
			# print key[stack_name]
			# for one_stack in stacks_to_be_checked:
			# 	if key[stack_name] == one_stack:
			# 		print one_stack
			list_of_stack_names.append(key[stack_name])
	return list_of_stack_names

def get_stacks_to_be_tested():
	stacks_to_be_checked = []
	all_the_names = get_all_stack_names()
	for key in all_the_names:
		if "test-platform-" in key:
			stacks_to_be_checked.append(key)
	return stacks_to_be_checked

def delete_stacks():
	client = boto3.client('cloudformation')
	stacks_to_be_deleted = get_stacks_to_be_tested()
	for one_stack in stacks_to_be_deleted:
		response = client.delete_stack(
			StackName=one_stack
		)
	return

delete_stacks()