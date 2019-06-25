import requests
import json
class Api(object):
    def ReturnContent(self, res):
        return json.loads(res.content.decode('utf-8'))
    def CreateNew(self, name):
        if name is not None:
            return Api.ReturnContent(0, requests.get('https://post-shift.ru/api.php?action=new&name='+name+'&type=json'))
        else:
            return Api.ReturnContent(0, requests.get('https://post-shift.ru/api.php?action=new&type=json'))
    def GetList(self, key):
        return eval(requests.get('https://post-shift.ru/api.php?action=getlist&key=' + key + '&type=json').content.decode('utf-8'))
    def GetText(self, key, mID):
        return Api.ReturnContent(0, 'https://post-shift.ru/api.php?action=getmail&key='+ key+'&id='+mID + '&type=json')
    def GetLiveTime(self, key):
        return json.loads(requests.get('https://post-shift.ru/api.php?action=livetime&key='+ key + '&type=json').content.decode('utf-8'))
    def UpdateLiveTime(self, key):
        return requests.get('https://post-shift.ru/api.php?action=update&key='+ key + '&type=json')
    def DeleteMail(self, key):
        return requests.get('https://post-shift.ru/api.php?action=delete&key='+ key + '&type=json')
    def ClearMail(self, key):
        return Api.ReturnContent(0, 'https://post-shift.ru/api.php?action=clear&key='+ key + '&type=json')