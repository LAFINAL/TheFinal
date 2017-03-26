import json
import requests

def melon_search(q):

	url = "http://www.melon.com/search/keyword/index.json"

	params = {
	'jscallback': 'jQuery19106575063241004029_1480227335295',
	'query': q,
	}
	# ? 뒷부분이 url requests의 prameter임. 
	response = requests.get(url, params = params).text

	json_string = response.replace(params['jscallback'] + '(','').replace(');','')
	result_dict = json.loads(json_string)
	if 'SONGCONTENTS' not in result_dict:
		print('not found')
		pass
	else:
		for song in result_dict['SONGCONTENTS']:	
			print('''{SONGNAME} {ALBUMNAME} {ARTISTNAME}
			- http://www.melon.com/song/detail.htm?songId={SONGID}'''.format(**song))
		#print(song['SONGNAME'], song['ALBUMNAME'], song['ARTISTNAME'])
	#print(result_dict)

if __name__ == '__main__':
	line = input()
	melon_search(line)