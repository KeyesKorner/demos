import sys
import os
import time
import shutil

testRootDir = '/Users/mkeyes/Documents/Training/myCodeExamples'
dirDelimiter = '/'
# Create html formatted summary file
summaryFile = open(testRootDir + dirDelimiter + "AutoTestSummary.html","w")
resultFile = open(testRootDir + dirDelimiter + "result_file.txt", 'r')
titleTuple = ('suite','test case', 'result','failed step', 'comment')
listTuples = [titleTuple]
numberFail = 0
numberPass = 0
for line in resultFile:
	lineListCurr = line.split(':')
	# Retrieve number of passes and fails from the result_file.txt
	if lineListCurr[0] == 'Number Fail':
		numberFail = lineListCurr[1]
	elif lineListCurr[0] == 'Number Pass':
		numberPass = lineListCurr[1]
	lineTupleCurr = tuple(lineListCurr)
	listTuples.append(lineTupleCurr)
	
# Sort listTuples
outListTuples = sorted(listTuples)
	
# ***Create the HTML summary file***
summaryFile.write('<html>\n')
summaryFile.write('<body bgcolor="#E6E690">')
summaryFile.write('<font size=16>Example Automation Summary</font><br>')
summaryFile.write('<b>Sample test job</b><br><br>')
now = time.strftime("%c")
summaryFile.write(now + '<br><br>')
summaryFile.write('Number Pass: '+ numberPass + '<br>')
summaryFile.write('Number Fail: '+ numberFail + '<br><br>')

# Create table and make the magic happen
summaryFile.write('<table border="1" style="width:100%">')
summaryFile.write('<tr>')
summaryFile.write('<td><b>Suite</b></td>')
summaryFile.write('<td><b>Test Case</b></td>')
summaryFile.write('<td><b>Test Result</b></td>')
summaryFile.write('<td><b>Test Step on Fail</b></td>')
summaryFile.write('<td><b>Comment</b></td>')
summaryFile.write('</tr>')

# Write each test case as a tuple 
for outTuple in outListTuples:
	summaryFile.write('<tr>')
	if (len(outTuple) > 0) and (outTuple[0] != 'Number Pass') and (outTuple[0] != 'Number Fail') and (outTuple[0] != 'suite'):
		if len(outTuple) == 3:
			if outTuple[2].find('FAIL') >= 0:
				summaryFile.write('<td bgcolor="#FF0000">' + outTuple[0] + '</td>')
				summaryFile.write('<td bgcolor="#FF0000">' + outTuple[1] + '</td>')
				summaryFile.write('<td bgcolor="#FF0000">' + outTuple[2] + '</td>')
				summaryFile.write('<td bgcolor="#FF0000">-</td>')
				summaryFile.write('<td bgcolor="#FF0000">-</td>')
			else:
				summaryFile.write('<td>' + outTuple[0] + '</td>')
				summaryFile.write('<td>' + outTuple[1] + '</td>')
				summaryFile.write('<td>' + outTuple[2] + '</td>')
				summaryFile.write('<td>-</td>')
				summaryFile.write('<td>-</td>')
		elif len(outTuple) == 4:				
			summaryFile.write('<td>' + outTuple[0] + '</td>')
			summaryFile.write('<td>' + outTuple[1] + '</td>')
			summaryFile.write('<td>' + outTuple[2] + '</td>')
			summaryFile.write('<td>' + outTuple[3] + '</td>')
			summaryFile.write('<td>-</td>')
		elif len(outTuple) == 5:	
			summaryFile.write('<td>' + outTuple[0] + '</td>')
			summaryFile.write('<td>' + outTuple[1] + '</td>')
			summaryFile.write('<td>' + outTuple[2] + '</td>')
			summaryFile.write('<td>' + outTuple[3] + '</td>')
			summaryFile.write('<td>' + outTuple[4] + '</td>')			
	summaryFile.write('</tr>')
summaryFile.write('</table>')

# Wrap it up
summaryFile.write('</body>')
summaryFile.write('</html>\n')
summaryFile.close()
resultFile.close()	
