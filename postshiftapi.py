import requests
import json
class Api(object):
    def ReturnContent(self, response):
        return json.loads(response.content.decode('utf-8'))
    def CreateNew(self):
        return Api.ReturnContent(0, requests.get('https://post-shift.ru/api.php?action=new&type=json'))
    def GetList(self, key):
        return Api.ReturnContent(0, 'https://post-shift.ru/api.php?action=getlist&key=' + key + '&type=json')
    def GetText(self, key, mID):
        return Api.ReturnContent(0, 'https://post-shift.ru/api.php?action=getmail&key='+ key+'&id='+mID + '&type=json')
    def GetLiveTime(self, key):
        return Api.ReturnContent(0, 'https://post-shift.ru/api.php?action=livetime&key='+ key + '&type=json')
    def UpdateLiveTime(self, key):
        return Api.ReturnContent(0, 'https://post-shift.ru/api.php?action=update&key='+ key + '&type=json')
    def DeleteMail(self, key):
        return Api.ReturnContent(0, 'https://post-shift.ru/api.php?action=delete&key='+ key + '&type=json')
    def ClearMail(self, key):
        return Api.ReturnContent(0, 'https://post-shift.ru/api.php?action=clear&key='+ key + '&type=json')