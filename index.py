#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/8/2

import sys
from dueros.Bot import Bot
reload(sys)
sys.setdefaultencoding('utf8')


class TestBot(Bot):

    def launchRequest(self):
        '''
        打开调用名
        '''
        self.wait_answer()
        return {
            'outputSpeech': r'欢迎进入'
        }

    def getTaxSlot(self):
        '''
        获取槽位及逻辑处理
        '''
        num = self.get_slots('sys.number')
        city = self.get_slots('sys.city')
        if num and not city:
            self.nlu.ask('sys.city')
            return {
                'reprompt': r'你所在的城市是那里呢',
                'outputSpeech': r'你所在的城市是那里呢'
            }

        if city and not num:
            self.nlu.ask('sys.number')
            return {
                'reprompt': r'你的税前工资是多少呢',
                'outputSpeech': r'你的税前工资是多少呢'
            }

        computeType = self.get_slots('compute_type')
        if not computeType:
            self.nlu.ask('compute_type')
            return {
                'outputSpeech': r'你要查询什么税种呢'
            }
        else:
            taxNum = self.computeType(num, city)
            return {
                'outputSpeech': r'你需要缴纳' + str(taxNum)
            }

    def computeType(self, num, city):
        '''
        调用接口计算个税
        '''
        return 100

    def __init__(self, data):
        super(TestBot, self).__init__(data)
        self.add_launch_handler(self.launchRequest)
        self.add_intent_handler('personal_income_tax.inquiry', self.getTaxSlot)


def handler(event, context):

    bot = TestBot(event)
    bot.set_private_key(priKey)
    result = bot.run()

    return result


priKey = '''-----BEGIN RSA PRIVATE KEY-----
    MIICXQIBAAKBgQDKoeRzRVf8WoRSDYYqUzThpYCr90jfdFwTSXHJ526K8C6TEwdT
    UA+CFPQPRUg9jrYgFcown+J2myzO8BRLynD+XHb9ilLb49Mqk2CvDt/yK32lgHv3
    QVx14Dpb6h8isjncSF965fxBxlHGbvPwnHkJ9etRIYdYV3QpYohFszH3wQIDAQAB
    AoGAFhKqkw/ztK6biWClw8iKkyX3LURjsMu5F/TBK3BFb2cYe7bv7lhjSBVGPL+c
    TfBU0IvvGXrhLXBb4jLu0w67Xhggwwfc86vlZ8eLcrmYVat7N6amiBmYsw20GViU
    UFmePbo1G2BXqMA43JxqbIQwOLZ03zdw6GHj6EVlx369IAECQQD4K2R3K8ah50Yz
    LhF7zbYPIPGbHw+crP13THiYIYkHKJWsQDr8SXoNQ96TQsInTXUAmF2gzs/AwdQg
    gjIJ/dmBAkEA0QarqdWXZYbse1XIrQgBYTdVH9fNyLs1e1sBmNxlo4QMm/Le5a5L
    XenorEjnpjw5YpEJFDS4ijUI3dSzylC+QQJARqcD6TGbUUioobWB4L9GD7SPVFxZ
    c3+EgcxRoO4bNuCFDA8VO/InP1ONMFuXLt1MbCj0ru1yFCyamc63NEUDAQJBALt7
    PjGgsKCRuj6NnOcGDSbDWIitKZhnwfqYkAApfsiBQkYGO0LLaDIeAWG2KoCB9/6e
    lAQZnYPpOcCubWyDq4ECQQCrRDf0gVjPtipnPPS/sGN8m1Ds4znDDChhRlw74MI5
    FydvHFumChPe1Dj2I/BWeG1gA4ymXV1tE9phskV3XZfq
    -----END RSA PRIVATE KEY-----'''

if __name__ == '__main__':
    pass