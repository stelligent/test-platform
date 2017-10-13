var AWS = require('aws-sdk');
AWS.config.update({region: 'us-east-1'});
const codepipeline = new AWS.CodePipeline();
const ssm = new AWS.SSM();
var iCodePipelineStack = "";

function getCodePipelineStack(callback) { 
    var params = {
        Name: 'CodePipelineStack', /* required */
        WithDecryption: false
    };
    ssm.getParameter(params, function(err, data) {
      if (err) console.log(err, err.stack); // an error occurred
      else iCodePipelineStack = data.Parameter['Value']; callback(); // successful response
    });
} 

exports.handler = function(event, context) {
  getCodePipelineStack(function() {
    console.log(iCodePipelineStack);
    var params = {
      name: iCodePipelineStack
    };
    codepipeline.startPipelineExecution(params, function(err, data) {
      if (err) console.log(err, err.stack); // an error occurred
      else     console.log(data);   // successful response
    });
  });
};