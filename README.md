# Results
[STATUS LIST OF INTERNAL PROJECTS](http://test-platform-internal-projects.s3-website-us-east-1.amazonaws.com/)

# Test Platform
1. Runs and tests internal projects' cloudformation templates to see if those projects are working and up-to-date.
1. Outputs results [here](http://test-platform-internal-projects.s3-website-us-east-1.amazonaws.com/)
1. Once the Test Platform pipeline is launched, it will run once a day from then on. 
1. Test Platform creates a Lambda function that is AUTOMATICALLY run once a day which creates all the CloudFormation stacks.
1. The cfn stacks (internal projects' cfn stacks) that get automatically created are also automatically deleted.

# !WARNING!
When this pipeline is created (by following all of the directions below), AWS resources will be created once a day due to the automatic Lambda function. Those resources will automatically be deleted right after creation.

# Setup
PREPPING TEST-PLATFORM BEFORE LAUNCH (one time only):  
The following is typically configured one time per AWS account. The following examples assume AWS region `us-east-1`

1. You must create an s3 bucket in your account with the name: 'test-platform-internal-projects'
(This is where the results of the projects will be posted.)
1. Create a *Secure String* parameter named `GitHubToken` in [Parameter Store](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Parameters:) The value should be a github token with ‘repo’ and ‘admin:repo_hook’ permissions.
1. Modify the [buildspec-cfnstacks.yml](./buildspec-cfnstacks.yml) to obtain the values of the parameters you defined in Parameter Store. Then change the following variables to match your information.

	  EMAIL_ADDRESS: "YOUR EMAIL ADDRESS"  
    S3_BUCKET_BEANSTALK: "YOUR BUCKET NAME" # Create an S3 bucket in us-east-1  
    GITHUB_USER: "YOUR GITHUB USERNAME" # Modify to the name of the user that forked the GitHub repo  
    EC2_KEY_PAIR_NAME: "YOUR EC2 KEY PAIR NAME" # https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:sort=keyName

# Launch Stack

[![Launch CFN stack](https://s3.amazonaws.com/www.devopsessentialsaws.com/img/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Estelligent-test-platform%7Cturl%7Ehttps://s3.amazonaws.com/stelligent-public/cloudformation-templates/github/test-platform/pipeline.yml)

# Configure Solution

1. Name the stack & provide an email for the sns messaging
1. Once the CloudFormation stack is successful, select the checkbox next to the stack and click the <strong>Outputs</strong> tab. 
1. From Outputs, click on the **PipelineUrl** output. The Source action will be in a failed state.
1. From the CodePipeline Source action, click on the CodeCommit provider and copy the **git clone** statement provided by CodeCommit
1. Paste the command in your Terminal
1. From this 'test-platform repo' which you've also cloned locally, copy all the files to your locally cloned CodeCommit git repo
1. In your locally cloned CodeCommmit git repo, from your Terminal, type `git add .`
1. From your Terminal, type `git commit -am "add new files"`
1. From your Terminal, type `git push`
1. Go back to your pipeline in CodePipeline and see the changes flow through the pipeline
1. Once the pipeline is complete, go to your CloudFormation stacks to see the CloudFormation stacks being generated
1. You're finished! Test-Platform will now run once a day and update the list of statuses. To view them, go into the s3 bucket that you created earlier, 'test-platform-internal-projects', and view the site.

# Resources

1. The CloudFormation template is available [here](https://s3.amazonaws.com/www.devopsessentialsaws.com/samples/test-platform/pipeline.yml).


# STATUS CHECKER - Running it Manually (Why would you want to do this though?)
1. Checks the status of cfn stacks, whether they have been created successfully, failed, or are 'in progress'.

You can view the results [here](http://test-platform-internal-projects.s3-website-us-east-1.amazonaws.com/)
The s3 bucket the results are put into is a variable in buildspec-status-checker.yml.

To manually run just the status checker locally:

First install boto3
1. `pip install boto3`
1. IF you are on a mac and run into an error while trying to install boto3
1. Try this command instead:
1. `sudo pip install --ignore-installed six boto3`

After boto3 is installed:
1. Open status_checker.py
1. Change the string inside the first function, get_stacks_to_be_tested(), to the name or part of the name of the cfn stack(s) you want to check. It's currently "test-platform-"
1. From command line, run:
1. `python status-checker.py`
1. This will create a file called index.html
1. Open index.html to view results
