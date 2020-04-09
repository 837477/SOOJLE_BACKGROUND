import sys
#837477 Path
sys.path.insert(0,'./')
sys.path.insert(0,'../SOOJLE')
sys.path.insert(0,'../SJ_AI/src')
sys.path.insert(0,'../IML_Tokenizer/src')
sys.path.insert(0,'../SOOJLE/database')
sys.path.insert(0,'../SOOJLE/apps')
###########################################
#Ubuntu Path
sys.path.insert(0,'/home/iml/')
sys.path.insert(0,'/home/iml/SOOJLE/')
sys.path.insert(0,'/home/iml/SOOJLE/database')
sys.path.insert(0,'/home/iml/SOOJLE_Crawler/src/')
sys.path.insert(0,'/home/iml/SJ_AI/src')
sys.path.insert(0,'/home/iml/IML_Tokenizer/src/')
###################################################
from pymongo import *
from datetime import timedelta, datetime
###################################################
from db_management import *
from db_info import *
from variable import *
from global_func import get_default_day

#매 시간별 방문자 수 기록! 
def SJ_visitor_of_time():
	db_client = MongoClient('mongodb://%s:%s@%s' %(MONGODB_ID, MONGODB_PW, MONGODB_HOST))
	db = db_client["soojle"]

	time = datetime.now() - timedelta(minutes = 59)

	visitor_cnt = find_today_time_visitor(db, time)

	hour_visitor_obj = {}
	if datetime.now().hour == 0:
		hour_visitor_obj['time'] = 24
	else:	
		hour_visitor_obj['time'] = datetime.now().hour
	
	hour_visitor_obj['visitor'] = visitor_cnt

	push_today_time_visitor(db, hour_visitor_obj)

	if db_client is not None:
		db_client.close()

if __name__ == '__main__':
	FILE = open('/home/iml/log/background.log', 'a')
	
	try:
    	SJ_visitor_of_time()
		log_data = datetime.now() + "매 시간 방문자 캐싱 성공 :)"
    
	except:
		log_data = datetime.now() + "매 시간 방문자 캐싱 실패 :("

	FILE.write(log_data)

	FILE.close()
    