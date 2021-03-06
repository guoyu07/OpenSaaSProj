# -*- coding: utf-8 -*-
from collections import OrderedDict
import urlparse


define_page = OrderedDict([
    ('http://cuidelong.m.nicaifu.com', (u'首页', )),
    ('https://m.nicaifu.com', (u'首页', )),
    ('http://xingxing.m.nicaifu.com', (u'首页', )),
    ('http://xingxing.m.nicaifu.com/index/home', (u'首页', )),
    ('https://m.nicaifu.com/index', (u'首页', )),
    ('https://m.nicaifu.com/index/home', (u'首页', )),
    ('https://wx.nicaifu.com', (u'首页', )),
    ('https://m.nicaifu.com/safe', (u'首页', )),
    ('https://m.nicaifu.com/safeios', (u'首页', )),
    ('https://wx.nicaifu.com/index', (u'首页', )),
    ('https://wx.nicaifu.com/index/home', (u'首页', )),
    ('https://m.nicaifu.com/index/weishi_home', (u'首页', )),
    ('http://cuidelong.m.nicaifu.com/login', (u'登录流程', )),
    ('http://m.nicaifu.com/login', (u'登录流程', )),
    ('http://xingxing.m.nicaifu.com/login', (u'登录流程', )),
    ('https://m.nicaifu.com/login', (u'登录流程', )),
    ('https://wx.nicaifu.com/login', (u'登录流程', )),
    ('http://xingxing.m.nicaifu.com/login/check_pass', (u'登录流程', )),
    ('https://m.nicaifu.com/login/check_pass', (u'登录流程', )),
    ('https://m.nicaifu.com/login/set_pass', (u'登录流程', )),
    ('http://cuidelong.m.nicaifu.com/ucenter', (u'个人中心页', )),
    ('http://xingxing.m.nicaifu.com/ucenter', (u'个人中心页', )),
    ('https://m.nicaifu.com/ucenter', (u'个人中心页', )),
    ('https://wx.nicaifu.com/ucenter', (u'个人中心页', )),
    ('http://xingxing.m.nicaifu.com/user/accountsecurity/v2', (u'个人中心设置', )),
    ('https://m.nicaifu.com/user/accountsecurity/v2', (u'个人中心设置', )),
    ('https://m.nicaifu.com/user/accountsecurity/address', (u'个人中心设置', )),
    ('https://wx.nicaifu.com/user/accountsecurity/address', (u'个人中心设置', )),
    ('https://wx.nicaifu.com/user/accountsecurity/v2', (u'个人中心设置', )),
    ('https://m.nicaifu.com/user/accountsecurity/safe_guard', (u'个人中心设置', )),
    ('https://wx.nicaifu.com/user/accountsecurity/safe_guard', (u'个人中心设置', )),
    ('https://m.nicaifu.com/ucenter/member_level_explain', (u'积分会员页', )),
    ('https://m.nicaifu.com/ucenter/member_light', (u'积分会员页', )),
    ('https://m.nicaifu.com/ucenter/member_score', (u'积分会员页', )),
    ('https://m.nicaifu.com/ucenter/member_score_explain', (u'积分会员页', )),
    ('https://m.nicaifu.com/ucenter/member_score_record', (u'积分会员页', )),
    ('https://m.nicaifu.com/ucenter/member_vip', (u'积分会员页', )),
    ('https://m.nicaifu.com/ucenter/member_xhb', (u'积分会员页', )),
    ('https://m.nicaifu.com/ucenter/vipintro', (u'积分会员页', )),
    ('https://m.nicaifu.com/ucenter/member_points', (u'积分会员页', )),
    ('https://wx.nicaifu.com/ucenter/member_birth', (u'积分会员页', )),
    ('https://wx.nicaifu.com/ucenter/member_help', (u'积分会员页', )),
    ('https://wx.nicaifu.com/ucenter/member_level_explain', (u'积分会员页', )),
    ('https://wx.nicaifu.com/ucenter/member_light', (u'积分会员页', )),
    ('https://wx.nicaifu.com/ucenter/member_points', (u'积分会员页', )),
    ('https://wx.nicaifu.com/ucenter/member_score', (u'积分会员页', )),
    ('https://wx.nicaifu.com/ucenter/member_score_explain', (u'积分会员页', )),
    ('https://wx.nicaifu.com/ucenter/member_score_record', (u'积分会员页', )),
    ('https://wx.nicaifu.com/ucenter/member_vip', (u'积分会员页', )),
    ('https://wx.nicaifu.com/ucenter/member_xhb', (u'积分会员页', )),
    ('https://m.nicaifu.com/user/award', (u'个人中心查红包', )),
    ('https://m.nicaifu.com/user/award/friendcode', (u'个人中心查红包', )),
    ('https://m.nicaifu.com/user/award/index', (u'个人中心查红包', )),
    ('https://wx.nicaifu.com/user/award', (u'个人中心查红包', )),
    ('https://wx.nicaifu.com/user/award/friendcode', (u'个人中心查红包', )),
    ('https://wx.nicaifu.com/user/award/index', (u'个人中心查红包', )),
    ('https://m.nicaifu.com/user/dingqi', (u'个人中心进定期类产品页', )),
    ('https://m.nicaifu.com/user/dingqi/gs', (u'个人中心进定期类产品页', )),
    ('https://m.nicaifu.com/user/dingqi/order_detail', (u'个人中心进定期类产品页', )),
    ('https://m.nicaifu.com/user/dingcunv2', (u'个人中心进活期类产品页', )),
    ('https://m.nicaifu.com/user/dingcunv2/detail', (u'个人中心进活期类产品页', )),
    ('https://m.nicaifu.com/user/huoqibao/tx', (u'个人中心进活期类产品页', )),
    ('https://wx.nicaifu.com/user/huoqibao/tx', (u'个人中心进活期类产品页', )),
    ('https://m.nicaifu.com/user/dingqi/order_list', (u'个人中心进定期类产品页', )),
    ('https://m.nicaifu.com/user/fund', (u'个人中心进基金类产品页', )),
    ('https://m.nicaifu.com/user/fund/detail', (u'个人中心进基金类产品页', )),
    ('https://m.nicaifu.com/user/fund/hold_detail', (u'个人中心进基金类产品页', )),
    ('https://m.nicaifu.com/user/fund/order_detail', (u'个人中心进基金类产品页', )),
    ('https://m.nicaifu.com/user/fund/redeem', (u'个人中心进基金类产品页', )),
    ('https://m.nicaifu.com/user/ins', (u'个人中心进保险类产品页', )),
    ('https://m.nicaifu.com/user/ins/xiaobai', (u'个人中心进保险类产品页', )),
    ('https://m.nicaifu.com/user/ins/xiaobai_detail', (u'个人中心进保险类产品页', )),
    ('https://m.nicaifu.com/user/ins/interest', (u'个人中心进保险类产品页', )),
    ('https://m.nicaifu.com/user/passwd/index', (u'密码设置页', )),
    ('https://m.nicaifu.com/user/passwd/reset', (u'密码设置页', )),
    ('https://m.nicaifu.com/user/paypwd/reset_paypwd', (u'密码设置页', )),
    ('https://wx.nicaifu.com/user/passwd/index', (u'密码设置页', )),
    ('https://wx.nicaifu.com/user/paypwd/reset_paypwd', (u'密码设置页', )),
    ('http://xingxing.m.nicaifu.com/user/bankcard', (u'个人中心银行卡', )),
    ('https://m.nicaifu.com/user/bankcard', (u'个人中心银行卡', )),
    ('https://wx.nicaifu.com/user/bankcard', (u'个人中心银行卡', )),
    ('https://m.nicaifu.com/user/bankcard/bind_withdraw_card', (u'个人中心银行卡', )),
    ('https://wx.nicaifu.com/user/bankcard/bind_withdraw_card', (u'个人中心银行卡', )),
    ('http://cuidelong.m.nicaifu.com/user/verify', (u'实名认证', )),
    ('https://m.nicaifu.com/user/verify', (u'实名认证', )),
    ('https://wx.nicaifu.com/user/verify', (u'实名认证', )),
    ('https://m.nicaifu.com/MessageCenter/index', (u'消息中心页', )),
    ('https://wx.nicaifu.com/MessageCenter/index', (u'消息中心页', )),
    ('https://m.nicaifu.com/ucenter/account_detail', (u'个人中心资产明细', )),
    ('https://wx.nicaifu.com/ucenter/account_detail', (u'个人中心资产明细', )),
    ('https://m.nicaifu.com/user/trade/v2', (u'个人中心资产明细', )),
    ('https://wx.nicaifu.com/user/trade/v2', (u'个人中心资产明细', )),
    ('https://m.nicaifu.com/dq', (u'定期产品页', )),
    ('https://m.nicaifu.com/dq/help', (u'定期产品页', )),
    ('https://m.nicaifu.com/dq/index', (u'定期产品页', )),
    ('https://m.nicaifu.com/dq/more', (u'定期产品页', )),
    ('https://m.nicaifu.com/dq/p2p_info', (u'定期产品页', )),
    ('https://m.nicaifu.com/dq/success', (u'定期产品页', )),
    ('https://wx.nicaifu.com/dq', (u'定期产品页', )),
    ('https://wx.nicaifu.com/dq/index', (u'定期产品页', )),
    ('https://m.nicaifu.com/hq', (u'活期产品页', )),
    ('https://m.nicaifu.com/hq/rank', (u'活期产品页', )),
    ('https://m.nicaifu.com/hq/success', (u'活期产品页', )),
    ('https://wx.nicaifu.com/hq', (u'活期产品页', )),
    ('https://wx.nicaifu.com/hq/rank', (u'活期产品页', )),
    ('https://m.nicaifu.com/fund', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/caiqi', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/detail', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/dt_detail', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/dt_list', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/dt_plan', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/dt_success', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/fund_gushou', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/fund_hot', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/fund_list', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/fund_new', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/fund_search', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/fund_themes', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/index_v3', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/news_list', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/optional', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/risk', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/success', (u'基金产品页', )),
    ('https://m.nicaifu.com/funds/huodong/qst', (u'基金产品页', )),
    ('https://m.nicaifu.com/funds/huodong/riddle', (u'基金产品页', )),
    ('https://wx.nicaifu.com/fund/detail', (u'基金产品页', )),
    ('https://wx.nicaifu.com/fund/dt_list', (u'基金产品页', )),
    ('https://wx.nicaifu.com/fund/dt_plan', (u'基金产品页', )),
    ('https://wx.nicaifu.com/fund/dt_success', (u'基金产品页', )),
    ('https://wx.nicaifu.com/fund/fund_list', (u'基金产品页', )),
    ('https://wx.nicaifu.com/fund/fund_search', (u'基金产品页', )),
    ('https://wx.nicaifu.com/fund/index_v3', (u'基金产品页', )),
    ('https://wx.nicaifu.com/fund/news_list', (u'基金产品页', )),
    ('https://wx.nicaifu.com/fund/risk', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/fund_themes_detail', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/hot_infor_detail', (u'基金产品页', )),
    ('https://m.nicaifu.com/fund/index_tty', (u'基金产品页', )),
    ('https://m.nicaifu.com/funds/huodong/hd', (u'基金产品页', )),
    ('https://wx.nicaifu.com/fund/hot_infor_detail', (u'基金产品页', )),
    ('https://m.nicaifu.com/ins/buy', (u'保险产品页', )),
    ('https://m.nicaifu.com/ins/detail', (u'保险产品页', )),
    ('https://m.nicaifu.com/ins/help', (u'保险产品页', )),
    ('https://m.nicaifu.com/ins/pay', (u'保险产品页', )),
    ('https://m.nicaifu.com/ins/success', (u'保险产品页', )),
    ('https://wx.nicaifu.com/ins/detail', (u'保险产品页', )),
    ('https://wx.nicaifu.com/ins/help', (u'保险产品页', )),
    ('https://m.nicaifu.com/ins/amount', (u'保险产品页', )),
    ('https://m.nicaifu.com/ins/xiaobai_buy', (u'保险产品页', )),
    ('https://wx.nicaifu.com/ins/amount', (u'保险产品页', )),
    ('https://m.nicaifu.com/trans', (u'转让产品页', )),
    ('https://m.nicaifu.com/trans/detail', (u'转让产品页', )),
    ('https://m.nicaifu.com/trans/success', (u'转让产品页', )),
    ('https://wx.nicaifu.com/trans', (u'转让产品页', )),
    ('https://wx.nicaifu.com/trans/detail', (u'转让产品页', )),
    ('https://m.nicaifu.com/trans/apply_option', (u'转让产品页', )),
    ('https://m.nicaifu.com/trans/apply_succ', (u'转让产品页', )),
    ('https://m.nicaifu.com/dc/detail', (u'其他类产品详情页', )),
    ('https://m.nicaifu.com/plus/detail', (u'其他类产品详情页', )),
    ('https://wx.nicaifu.com/plus/detail', (u'其他类产品详情页', )),
    ('https://m.nicaifu.com/dc/help', (u'其他类产品详情页', )),
    ('https://m.nicaifu.com/gushou/help', (u'其他类产品详情页', )),
    ('https://m.nicaifu.com/pay/newVersionBuy', (u'其他类付款页', )),
    ('https://m.nicaifu.com/pay/pay_wait', (u'其他类付款页', )),
    ('https://m.nicaifu.com/pay/success', (u'其他类付款页', )),
    ('https://wx.nicaifu.com/pay/newVersionBuy', (u'其他类付款页', )),
    ('https://wx.nicaifu.com/pay/pay_wait', (u'其他类付款页', )),
    ('https://wx.nicaifu.com/pay/success', (u'其他类付款页', )),
    ('https://m.nicaifu.com/pay/gs_buy', (u'其他类付款页', )),
    ('https://m.nicaifu.com/payV2/buy', (u'其他类付款页', )),
    ('https://wx.nicaifu.com/pay/gs_buy', (u'其他类付款页', )),
    ('https://wx.nicaifu.com/payV2/buy', (u'其他类付款页', )),
    ('http://m.nicaifu.com/huodong/promo/new_guide', (u'红包活动', )),
    ('https://m.nicaifu.com/huodong/promo/ad_for_vip', (u'红包活动', )),
    ('https://m.nicaifu.com/huodong/promo/bongive', (u'红包活动', )),
    ('https://m.nicaifu.com/huodong/promo/browser360', (u'红包活动', )),
    ('https://m.nicaifu.com/huodong/promo/new_guide', (u'红包活动', )),
    ('https://m.nicaifu.com/huodong/promo/new_guide#/xinshoubiao', (u'红包活动', )),
    ('https://m.nicaifu.com/huodong/promo/wswallet', (u'红包活动', )),
    ('https://m.nicaifu.com/huodong/fuli', (u'红包活动', )),
    ('https://m.nicaifu.com/huodong/fuli/use_list', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/fund/dcfund', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/fund/dt', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/fund/funds', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/fund/funds_buy', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/fund/funds_success', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/fund/goddess_festival', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/fund/gold_cattle', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/fund/invest_guide', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/mall/EeIvO3kdHoc', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/prize/AEUEDgjRmwY', (u'基金活动', )),
    ('https://wx.nicaifu.com/huodong/fund/goddess_festival', (u'基金活动', )),
    ('https://m.nicaifu.com/huodong/tiyanjin/sj360_detail', (u'体验金活动', )),
    ('https://m.nicaifu.com/huodong/tiyanjin/sj360_ucenter', (u'体验金活动', )),
    ('https://wx.nicaifu.com/huodong/tiyanjin/sj360_detail', (u'体验金活动', )),
    ('https://wx.nicaifu.com/huodong/tiyanjin/sj360_ucenter', (u'体验金活动', )),
    ('https://m.nicaifu.com/huodong/dream', (u'dream活动', )),
    ('https://m.nicaifu.com/huodong/dream/dq_ad', (u'dream活动', )),
    ('https://m.nicaifu.com/huodong/dream/dq_cash', (u'dream活动', )),
    ('https://m.nicaifu.com/huodong/dream/dq_cash_v2', (u'dream活动', )),
    ('https://m.nicaifu.com/huodong/dream/dqshouji', (u'dream活动', )),
    ('https://m.nicaifu.com/huodong/dream/new_year_2017_1', (u'dream活动', )),
    ('https://m.nicaifu.com/huodong/dream/remove_red_envelopes', (u'dream活动', )),
    ('https://m.nicaifu.com/huodong/dream/ringshow', (u'dream活动', )),
    ('https://wx.nicaifu.com/huodong/dream/dq_cash', (u'dream活动', )),
    ('https://wx.nicaifu.com/huodong/dream/dq_cash_v2', (u'dream活动', )),
    ('https://m.nicaifu.com/huodong/dream/lottery_ms', (u'dream活动', )),
    ('https://m.nicaifu.com/huodong/dream/lottery_ms_v2', (u'dream活动', )),
    ('http://xingxing.m.nicaifu.com/wx/wa', (u'挖宝', )),
    ('https://m.nicaifu.com/wx/wa', (u'挖宝', )),
    ('https://wx.nicaifu.com/wx/wa', (u'挖宝', )),
    ('https://m.nicaifu.com/help/bank_faq', (u'帮助页', )),
    ('https://m.nicaifu.com/help/faq', (u'帮助页', )),
    ('https://m.nicaifu.com/help/pact', (u'帮助页', )),
    ('https://m.nicaifu.com/help/pact_yeepay', (u'帮助页', )),
    ('https://wx.nicaifu.com/help/bank_faq', (u'帮助页', )),
    ('https://wx.nicaifu.com/help/faq', (u'帮助页', )),
    ('https://wx.nicaifu.com/help/pact', (u'帮助页', )),
    ('https://wx.nicaifu.com/help/pact_yeepay', (u'帮助页', )),
    ('http://cuidelong.m.nicaifu.com/bill/buy', (u'话费充值流程', )),
    ('http://cuidelong.m.nicaifu.com/bill/orderdetail', (u'话费充值流程', )),
    ('http://cuidelong.m.nicaifu.com/bill/success', (u'话费充值流程', )),
    ('https://m.nicaifu.com/bill/buy', (u'话费充值流程', )),
    ('https://m.nicaifu.com/bill/orderdetail', (u'话费充值流程', )),
    ('https://m.nicaifu.com/bill/orderlist', (u'话费充值流程', )),
    ('https://m.nicaifu.com/bill/ques', (u'话费充值流程', )),
    ('https://m.nicaifu.com/bill/xieyi', (u'话费充值流程', )),
    ('http://cuidelong.m.nicaifu.com/flow/buy', (u'流量充值页', )),
    ('http://cuidelong.m.nicaifu.com/flow/orderdetail', (u'流量充值页', )),
    ('http://cuidelong.m.nicaifu.com/flow/orderlist', (u'流量充值页', )),
    ('http://cuidelong.m.nicaifu.com/flow/success', (u'流量充值页', )),
    ('http://xingxing.m.nicaifu.com/flow/wswallet', (u'流量充值页', )),
    ('https://m.nicaifu.com/flow/buy', (u'流量充值页', )),
    ('https://m.nicaifu.com/flow/orderdetail', (u'流量充值页', )),
    ('https://m.nicaifu.com/flow/orderlist', (u'流量充值页', )),
    ('https://m.nicaifu.com/flow/success', (u'流量充值页', )),
    ('https://m.nicaifu.com/topic/ability', (u'介绍页', )),
    ('https://m.nicaifu.com/topic/guidedown', (u'介绍页', )),
    ('https://m.nicaifu.com/topic/trainticket', (u'介绍页', )),
    ('https://wx.nicaifu.com/topic/guidedown', (u'介绍页', )),
    ('https://m.nicaifu.com/reg/check_idcard', (u'身份证验证页', )),
    ('https://wx.nicaifu.com/reg/check_idcard', (u'身份证验证页', ))
     ])


parse_path = OrderedDict()
define_path = OrderedDict()
map(lambda (index, (uri, item)): parse_path.setdefault(urlparse.urlparse(uri).path, [item[0], ]), enumerate(define_page.iteritems()))
map(lambda (index, (uri_path, item)): define_path.setdefault(uri_path, [item[0], index]), enumerate(parse_path.iteritems()))
import json
print json.dumps(define_path)
