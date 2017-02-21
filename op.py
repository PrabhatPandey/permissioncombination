import time 
#time.sleep(5)
import itertools
from pprint import pprint
import subprocess

revoke = 'adb shell pm revoke com.media.sample '
grant = 'adb shell pm grant com.media.sample '

def if_revoked():
	return revoke

def if_granted():
	return grant

def execute_the_revoke_permission(permission):
	print "Revoke this permission " + permission
	cmd = if_revoked() + permission
	print cmd
	#s = subprocess.check_output(cmd.split())
	#print s.split('\r\n')
	#print "--------------***------------------"

def execute_the_grant_permission(permission):
	print "Granted this permission "+ permission
	cmd = if_granted() + permission
	print cmd

key_list = ["android.permission.INTERNET","android.permission.ACCESS_NETWORK_STATE","android.permission.ACCESS_COARSE_LOCATION","android.permission.ACCESS_FINE_LOCATION","android.permission.ACCESS_WIFI_STATE","android.permission.CHANGE_WIFI_STATE","android.permission.GET_ACCOUNTS","android.permission.READ_CONTACTS","android.permission.READ_EXTERNAL_STORAGE","android.permission.READ_PHONE_STATE","android.permission.WRITE_EXTERNAL_STORAGE","com.android.browser.permission.READ_HISTORY_BOOKMARKS"] 
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
		
