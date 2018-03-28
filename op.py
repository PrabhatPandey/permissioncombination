import time 
#time.sleep(5)
import itertools
from pprint import pprint
import subprocess

revoke = 'adb shell pm revoke com.media.sample '
grant = 'adb shell pm grant com.media.sample '

"List of permissions."

key_list = ["android.permission.INTERNET","android.permission.ACCESS_NETWORK_STATE","android.permission.ACCESS_COARSE_LOCATION","android.permission.ACCESS_FINE_LOCATION","android.permission.ACCESS_WIFI_STATE","android.permission.CHANGE_WIFI_STATE","android.permission.GET_ACCOUNTS","android.permission.READ_CONTACTS","android.permission.READ_EXTERNAL_STORAGE","android.permission.READ_PHONE_STATE","android.permission.WRITE_EXTERNAL_STORAGE","com.android.browser.permission.READ_HISTORY_BOOKMARKS"]


def if_revoked():
	return revoke

def if_granted():
	return grant

def executeThisCommand(cmd):
	s = subprocess.check_output(cmd.split())
	#time.sleep(90)
	print s.split('\r\n')


def execute_the_revoke_permission(permission):
	print "Revoke this permission " + permission
	cmd = if_revoked() + permission
	print cmd
	s = subprocess.check_output(cmd.split())
	print s.split('\r\n')

def execute_the_grant_permission(permission):
	print "Granted this permission "+ permission
	cmd = if_granted() + permission
	print cmd
	s = subprocess.check_output(cmd.split())
        print s.split('\r\n')
	time.sleep(1)
	
def revoke_all_permissions():
	for thispermission in key_list : 
		execute_the_revoke_permission(thispermission)
		time.sleep(1)


def runBannerTextTestCase(permission):
	cmd = 'adb shell am instrument -w -r -e debug false -e class net.media.sample.AdSdkInstrumentationTest#testIfTheURLIsNotNullAndItOpensUpTheDifferentActivityWhenWeClickOnIt com.media.sample.test/android.support.test.runner.AndroidJUnitRunner'
	print cmd
	print "Running this banner text case when this permissin is granted. ->"+permission
	executeThisCommand(cmd)
	print "Ran banner test to completion."
	


def runBannerVideoTestCase(permission):
	cmd = 'adb shell am instrument -w -r -e debug false -e class net.media.sample.AdSdkInstrumentationTest#testIfInTheBannerVideoAdCloseCallIsWorking com.media.sample.test/android.support.test.runner.AndroidJUnitRunner'
	print cmd
	print "Running this banner video case when this permissin is granted. ->"+permission
	executeThisCommand(cmd)
	print "Ran banner video case."

def runInterestialTextTestCase(permission):
	cmd = 'adb shell am instrument -w -r -e debug false -e class net.media.sample.AdSdkInstrumentationTest#testIfWeClickOnInterstitialAdItOpensInTheBrowser com.media.sample.test/android.support.test.runner.AndroidJUnitRunner'
	print cmd
	print "Running this interestial  text case when this permissin is granted. ->"+permission
	executeThisCommand(cmd)
	print "Ran interestial text case."
	
def runInterestialVideoTestCase(permission):
	cmd = 'adb shell am instrument -w -r -e debug false -e class net.media.sample.AdSdkInstrumentationTest#testIfInTheInterstitialVideoAdCloseCallIsWorking com.media.sample.test/android.support.test.runner.AndroidJUnitRunner'
	print cmd
	print "Running this Interestial Video  case when this permissin is granted. ->"+permission
	executeThisCommand(cmd)	
	print "Ran interestial video case."
	
	
def runRewardedVideoTestCase(permission):
	cmd = 'adb shell am instrument -w -r -e debug false -e class net.media.sample.AdSdkInstrumentationTest#testIfTheRewardedVideoIsLoadedCallBackIsWorkingInPortraitMode com.media.sample.test/android.support.test.runner.AndroidJUnitRunner'
	print cmd
	print "Running this Rewarded Video  case when this permissin is granted. ->"+permission
	executeThisCommand(cmd)	
	print "Ran interestial video case."


def installTheApplicationFile():
	print "Installing the application file."

def installTheTestCaseFile():
	"Print install the test app in the system too."


"""key_list = ["android.permission.INTERNET","android.permission.ACCESS_NETWORK_STATE","android.permission.ACCESS_COARSE_LOCATION","android.permission.ACCESS_FINE_LOCATION","android.permission.ACCESS_WIFI_STATE","android.permission.CHANGE_WIFI_STATE","android.permission.GET_ACCOUNTS","android.permission.READ_CONTACTS","android.permission.READ_EXTERNAL_STORAGE","android.permission.READ_PHONE_STATE","android.permission.WRITE_EXTERNAL_STORAGE","com.android.browser.permission.READ_HISTORY_BOOKMARKS"] 
"""


"""This function returns the combinations of these permissions.It will be used later"""
def permutationAndCombination():
	ip_vals = [True, False]
	all_possibilities = itertools.product(ip_vals, repeat=len(key_list))
	global_list = []
	for poss in all_possibilities:
        	local_dict = {}
        	for index,key in enumerate(key_list):
                	local_dict[key] = poss[index]
        	global_list.append(local_dict)
	pprint(global_list)
	pprint(len(global_list))
		

def main():
	for value in key_list : 
		print "Starting 4 test cases for this granted permission "+ value
		"This revoke permission can be replaced by installing the app again to default state."	
		revoke_all_permissions()
		execute_the_grant_permission(value)
		runBannerTextTestCase(value)
		runBannerVideoTestCase(value)
		runInterestialTextTestCase(value)
		runInterestialVideoTestCase(value)
		runRewardedVideoTestCase(value)
		print "Finished running all 4 tests for this granted permission : " + value

if __name__ =='__main__':
	main()


	
"""
for listOfCombinations in global_list :
	#print listOfCombinations 
	for items in listOfCombinations :
		print listOfCombinations[items] 
		print items , listOfCombinations[items]
		#print "Checking the command which needs to be executed"
		#print "Execute this"
		if listOfCombinations[items] :
			print "Will grant this permission "+ items
			execute_the_grant_permission(items);
		if not listOfCombinations[items]:
			print "Will revoke this permission "+ items
			execute_the_revoke_permission(items);
		#time.sleep(2)

"""
		
