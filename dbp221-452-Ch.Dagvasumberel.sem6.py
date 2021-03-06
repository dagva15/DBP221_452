#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[48]:


order_id=pd.Series(('CA-2016-152156',
'CA-2016-152156',
'CA-2016-138688',
'US-2015-108966',
'US-2015-108966',
'CA-2014-115812',
'CA-2014-115812',
'CA-2014-115812',
'CA-2014-115812',
'CA-2014-115812',
'CA-2014-115812',
'CA-2014-115812',
'CA-2017-114412',
'CA-2016-161389',
'US-2015-118983',
'US-2015-118983',
'CA-2014-105893',
'CA-2014-167164',
'CA-2014-143336',
'CA-2014-143336',
'CA-2014-143336',
'CA-2016-137330',
'CA-2016-137330',
'US-2017-156909',
'CA-2015-106320',
'CA-2016-121755',
'CA-2016-121755',
'US-2015-150630',
'US-2015-150630',
'US-2015-150630',
'US-2015-150630',
'US-2015-150630',
'US-2015-150630',
'US-2015-150630',
'CA-2017-107727',
'CA-2016-117590',
'CA-2016-117590',
'CA-2015-117415',
'CA-2015-117415',
'CA-2015-117415',
'CA-2015-117415',
'CA-2017-120999',
'CA-2016-101343',
'CA-2017-139619',
'CA-2016-118255',
'CA-2016-118255',
'CA-2014-146703',
'CA-2016-169194',
'CA-2016-169194',
'CA-2015-115742',
'CA-2015-115742',
'CA-2015-115742',
'CA-2015-115742',
'CA-2016-105816',
'CA-2016-105816',
'CA-2016-111682',
'CA-2016-111682',
'CA-2016-111682',
'CA-2016-111682',
'CA-2016-111682',
'CA-2016-111682',
'CA-2016-111682',
'CA-2015-135545',
'CA-2015-135545',
'CA-2015-135545',
'CA-2015-135545',
'US-2015-164175',
'CA-2014-106376',
'CA-2014-106376',
'CA-2016-119823',
'CA-2016-106075',
'CA-2017-114440',
'US-2015-134026',
'US-2015-134026',
'US-2015-134026',
'US-2017-118038',
'US-2017-118038',
'US-2017-118038',
'US-2014-147606',
'CA-2016-127208',
'CA-2016-127208',
'CA-2014-139451',
'CA-2014-139451',
'CA-2015-149734',
'US-2017-119662',
'CA-2017-140088',
'CA-2017-155558',
'CA-2017-155558',
'CA-2016-159695',
'CA-2016-109806',
'CA-2016-109806',
'CA-2016-109806',
'CA-2015-149587',
'CA-2015-149587',
'CA-2015-149587',
'US-2017-109484',
'CA-2017-161018',
'CA-2017-157833',
'CA-2016-149223',
'CA-2016-158568'))
order_id


# In[13]:


order_date=pd.Series(('08/11/2016',
'08/11/2016',
'12/06/2016',
'11/10/2015',
'11/10/2015',
'09/06/2014',
'09/06/2014',
'09/06/2014',
'09/06/2014',
'09/06/2014',
'09/06/2014',
'09/06/2014',
'15/04/2017',
'05/12/2016',
'22/11/2015',
'22/11/2015',
'11/11/2014',
'13/05/2014',
'27/08/2014',
'27/08/2014',
'27/08/2014',
'09/12/2016',
'09/12/2016',
'16/07/2017',
'25/09/2015',
'16/01/2016',
'16/01/2016',
'17/09/2015',
'17/09/2015',
'17/09/2015',
'17/09/2015',
'17/09/2015',
'17/09/2015',
'17/09/2015',
'19/10/2017',
'08/12/2016',
'08/12/2016',
'27/12/2015',
'27/12/2015',
'27/12/2015',
'27/12/2015',
'10/09/2017',
'17/07/2016',
'19/09/2017',
'11/03/2016',
'11/03/2016',
'20/10/2014',
'20/06/2016',
'20/06/2016',
'18/04/2015',
'18/04/2015',
'18/04/2015',
'18/04/2015',
'11/12/2016',
'11/12/2016',
'17/06/2016',
'17/06/2016',
'17/06/2016',
'17/06/2016',
'17/06/2016',
'17/06/2016',
'17/06/2016',
'24/11/2015',
'24/11/2015',
'24/11/2015',
'24/11/2015',
'30/04/2015',
'05/12/2014',
'05/12/2014',
'04/06/2016',
'18/09/2016',
'14/09/2017',
'26/04/2015',
'26/04/2015',
'26/04/2015',
'09/12/2017',
'09/12/2017',
'09/12/2017',
'26/11/2014',
'12/06/2016',
'12/06/2016',
'12/10/2014',
'12/10/2014',
'03/09/2015',
'13/11/2017',
'28/05/2017',
'26/10/2017',
'26/10/2017',
'05/04/2016',
'17/09/2016',
'17/09/2016',
'17/09/2016',
'31/01/2015',
'31/01/2015',
'31/01/2015',
'06/11/2017',
'09/11/2017',
'17/06/2017',
'06/09/2016',
'29/08/2016'))
order_date


# In[14]:


customer_id=pd.Series(('EB-13930',
'EB-13930',
'MO-17950',
'JO-15550',
'JO-15550',
'RH-19600',
'RH-19600',
'RH-19600',
'RH-19600',
'RH-19600',
'RH-19600',
'RH-19600',
'GB-14530',
'PW-19030',
'RB-19570',
'RB-19570',
'JS-15940',
'SB-20170',
'HL-15040',
'HL-15040',
'HL-15040',
'DK-13225',
'DK-13225',
'CV-12805',
'NS-18640',
'AF-10885',
'AF-10885',
'JK-15625',
'JK-15625',
'JK-15625',
'JK-15625',
'JK-15625',
'JK-15625',
'JK-15625',
'BC-11125',
'JS-15595',
'JS-15595',
'CS-12355',
'CS-12355',
'CS-12355',
'CS-12355',
'JK-15205',
'SC-20695',
'JD-15895',
'CC-12475',
'CC-12475',
'PM-19135',
'CR-12580',
'CR-12580',
'TB-21400',
'TB-21400',
'TB-21400',
'TB-21400',
'SR-20740',
'SR-20740',
'BB-10990',
'BB-10990',
'BB-10990',
'BB-10990',
'BB-10990',
'BB-10990',
'BB-10990',
'EB-13870',
'EB-13870',
'EB-13870',
'EB-13870',
'QJ-19255',
'RC-19825',
'RC-19825',
'RE-19450',
'RB-19645',
'DL-13315',
'JL-15130',
'JL-15130',
'JL-15130',
'BO-11425',
'BO-11425',
'BO-11425',
'CL-12565',
'LM-17065',
'LM-17065',
'JM-15535',
'JM-15535',
'RP-19855',
'AG-10525',
'GH-14410',
'TS-21205',
'TS-21205',
'AF-10885',
'FM-14380',
'FM-14380',
'FM-14380',
'NS-18640',
'NS-18640',
'NS-18640',
'JR-15700',
'AJ-10945',
'BM-11575',
'CV-12805',
'DK-12835'))
customer_id


# In[15]:


segment=pd.Series(('???????? ??????',
'???????? ??????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'??????????????????????',
'??????????????????????',
'????????????',
'????????????',
'????????????',
'????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'????????????',
'???????? ??????',
'??????????????????????',
'????????????'))
segment


# In[16]:


region=pd.Series(('????????????????',
'????????????????',
'??????-??????',
'????????????????',
'????????????????',
'??????-??????',
'??????-??????',
'??????-??????',
'??????-??????',
'??????-??????',
'??????-??????',
'??????-??????',
'????????????????',
'??????-??????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????-??????',
'??????-??????',
'??????-??????',
'??????-??????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????-??????',
'??????-??????',
'??????-??????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????-??????',
'????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????-??????',
'??????-??????',
'??????-??????',
'??????-??????',
'??????????????????',
'??????-??????',
'??????-??????',
'????????????????',
'??????????????????',
'??????????????????',
'????????????????',
'????????????????',
'????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'????????????????',
'????????????????',
'??????-??????',
'??????-??????',
'????????????????',
'??????????????????',
'????????????????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????-??????',
'??????-??????',
'??????-??????',
'??????????????????',
'??????????????????',
'??????????????????',
'??????-??????',
'??????????????????',
'??????-??????',
'??????????????????',
'??????????????????'))
region


# In[26]:


category=pd.Series(('??????????, ??????????????',
'OO ?????? ????????, ??????????????????',
'??????????, ??????????????',
'???????? ????????',
'?????????? ????',
'???????? ??????????',
'?????????? ??????????',
'?????????? ??????????',
'OO ?????? ????????, ??????????????????',
'?????????? ????',
'OO ?????? ????????, ??????????????????',
'?????????? ????',
'???????? ????????',
'????????, ???????????? ????????',
'?????????? ????',
'?????????? ????',
'?????????? ??????',
'??????????????',
'?????????? ????????????',
'??????????, ??????????????',
'?????????? ????',
'OO ?????? ????????, ??????????????????',
'???????? ????????',
'??????????????',
'?????? ????????',
'??????????, ??????????????, ????????',
'??????????, ??????????????',
'?????? ????????',
'?????????? ??????????',
'?????????? ????????????',
'?????????? ????',
'???????? ??????????',
'?????????? ????',
'??????????, ??????????????, ????????',
'?????????? ????',
'?????????? ????????',
'??????????????',
'???? ????????',
'?????????? ??????????',
'???????? ????????',
'??????????????',
'?????????? ??????????',
'??????????, ??????????????',
'?????????? ????',
'?????????? ????',
'?????????? ??????',
'?????????? ????????????',
'?????????? ??????????',
'??????????????',
'OO ?????? ????????, ??????????????????',
'?????????? ??????????',
'?????????? ????',
'?????????? ????',
'???????? ??????????',
'??????????????',
'OO ?????? ????????, ??????????????????',
'?????????? ????????',
'???????? ????????',
'OO ?????? ????????, ??????????????????',
'?????????????????? ????????????????????????, ???????????????? ??????',
'??????????, ??????????????',
'?????? ????????????',
'?????????? ??????',
'??????????, ??????????????',
'?????? ????????????',
'??????????, ??????????????',
'???????? ????????',
'???????? ????????',
'?????????? ????',
'??????????????',
'?????????? ??????????',
'?????????? ????????',
'?????????? ????',
'?????????????????? ????????????????????????, ???????????????? ??????',
'?????? ????????',
'??????????????',
'???????? ??????????',
'???????? ??????????',
'??????????, ??????????????',
'?????????? ????????',
'?????? ????????',
'?????????? ????',
'?????????????????? ????????????????????????, ???????????????? ??????',
'?????????? ????',
'??????????, ??????????????',
'?????????? ????',
'???????? ????????',
'?????????????????? ????????????????????????, ???????????????? ??????',
'?????????????????? ????????????????????????, ???????????????? ??????',
'??????????, ??????????????',
'?????? ????????',
'?????????? ????????????',
'??????????, ??????????????',
'???????? ????????',
'??????????????',
'???????????? ??????????????, ???????????????? ????????????',
'?????????? ????????',
'??????????, ??????????????, ????????',
'???????? ????????',
'?????????? ????????????'))
category


# In[27]:


product_name=pd.Series(('Shokolinsen 250 ????',
'???????????????? 00?????? ????????',
'?????????????? ???????????????? 230 ????',
'?????????????? ???????? 500 ????',
'Punch 450 ????',
'?????????????? ??????',
'?????????? ?????????? 400 ????',
'?????????? ?????? ??????????????????',
'Lady 20 ??',
'370 ???????? 370 ????',
'???????? ?????????? 30 ??',
'Pysio 300 ????',
'A vodka 0.5',
'?????????? ??????????????',
'Vita ?????????????? ???? 510 ????',
'???????? ???????????? 180 ????',
'Power 400 g',
'?????????????? ???? ?????????????? 80 ???? ????????????',
'???????? ???????????? ????????????',
'M&M 45 ????',
'?????????????? ???? 500 ????',
'?????????????? ???4',
'Solpro ?????????????? 3 ?? 67 %',
'???????????? 80 ????',
'???????????????? ???????????? 5 ?? ????????',
'???????????? ??????????',
'Akuku ?????????? 90 ????',
'???????????? ???????????????? Gilette',
'?????????????? ?????????? 250 ????',
'?????????? ???????????? ??????????????',
'?????????????? ?????????? 500 ????',
'?????????????? ??????',
'Arizona ?????????????? 680 ????',
'Jacobs ????????',
'?????????? ??????',
'?????? ???????? 55 ????',
'???????????? 65 ????',
'Colgate total 100 ????',
'?????????? ?????????????????? ?????????? 650 ????',
'?????????? 0.75 ??????????',
'???????????? 200 ????',
'???????? 1 ????',
'Mini cracker 350 ????',
'Arizona ?????????????? 680 ????',
'?????????? ?????????????? 330 ????',
'Tide 450 ???? ????????',
'Paldo king noodle 110 ????',
'?????????? 25 ????',
'Appetita ??????????',
'???????? ?????????? 100 ??',
'?????????? ?????? 1 ????',
'?????? ?????????? 1 ??',
'???????? ???????? 1.25 ????',
'????????????????',
'Appetita ???????????????? ????????????',
'???????????????? 00?????? ????????',
'Siesta ???????? 200 ????',
'?????????????? ?????????????? 400 ????',
'Selpak 2 ??????????????',
'Oleina ?????? 1 ??',
'?????????? ???? ?????????? 400 ????',
'Nivea ?????? 50 ????',
'?????? 100 ????',
'?????????? ??????????',
'Head & Shoulders 400 ????',
'?????????????? ?????????????? 6 ??',
'???????????? 2.5 ??',
'?????????????? 0.5',
'?????????????? ???? 500 ????',
'???????????? 50 ????',
'?????????????? ?????????? 5 ????',
'Lays ???????? 80 ????',
'???????? ???????????? 180 ????',
'???????????????????? ???????? 454 ????',
'?????????? 1 ??',
'Appetita ???????????????? ????????????',
'???????????? ?????????? 250 ????',
'????????????',
'?????????? ???? ???????????? ???????? 400 ????',
'Cocoro 100 ????',
'3?? ???????????? ????????????',
'???????????????? ???? ?????????????? 500 ????',
'?????????? ???????????? ??????',
'?????? ???????? 200 ????',
'?????????????????? ???????? 22 ????',
'?????? ?????????? 1 ??',
'?????????? 0.75 ??????????',
'?????????? ?????? ???????????? 190 ????',
'Bagro ?????????? ???????????????????? ?????????? 500 ????',
'???????????? ?????????? 50 ????',
'?????????? ?????? ??????????',
'?????? ???????? 110 ???? ????????????',
'Custard 6 ??',
'???????????????????? 0.5',
'?????????? ?????????? 180 ????',
'Hainich ??????????',
'Lays ???????? 80 ????',
'???????????????? 23 ????',
'?????????? 0.100',
'???????????? ???????????? 110 ????'))
product_name


# In[20]:


product_name=pd.Series(('Shokolinsen 250 ????',
'???????????????? 00?????? ????????',
'?????????????? ???????????????? 230 ????',
'?????????????? ???????? 500 ????',
'Punch 450 ????',
'?????????????? ??????',
'?????????? ?????????? 400 ????',
'?????????? ?????? ??????????????????',
'Lady 20 ??',
'370 ???????? 370 ????',
'???????? ?????????? 30 ??',
'Pysio 300 ????',
'A vodka 0.5',
'?????????? ??????????????',
'Vita ?????????????? ???? 510 ????',
'???????? ???????????? 180 ????',
'Power 400 g',
'?????????????? ???? ?????????????? 80 ???? ????????????',
'???????? ???????????? ????????????',
'M&M 45 ????',
'?????????????? ???? 500 ????',
'?????????????? ???4',
'Solpro ?????????????? 3 ?? 67 %',
'???????????? 80 ????',
'???????????????? ???????????? 5 ?? ????????',
'???????????? ??????????',
'Akuku ?????????? 90 ????',
'???????????? ???????????????? Gilette',
'?????????????? ?????????? 250 ????',
'?????????? ???????????? ??????????????',
'?????????????? ?????????? 500 ????',
'?????????????? ??????',
'Arizona ?????????????? 680 ????',
'Jacobs ????????',
'?????????? ??????',
'?????? ???????? 55 ????',
'???????????? 65 ????',
'Colgate total 100 ????',
'?????????? ?????????????????? ?????????? 650 ????',
'?????????? 0.75 ??????????',
'???????????? 200 ????',
'???????? 1 ????',
'Mini cracker 350 ????',
'Arizona ?????????????? 680 ????',
'?????????? ?????????????? 330 ????',
'Tide 450 ???? ????????',
'Paldo king noodle 110 ????',
'?????????? 25 ????',
'Appetita ??????????',
'???????? ?????????? 100 ??',
'?????????? ?????? 1 ????',
'?????? ?????????? 1 ??',
'???????? ???????? 1.25 ????',
'????????????????',
'Appetita ???????????????? ????????????',
'???????????????? 00?????? ????????',
'Siesta ???????? 200 ????',
'?????????????? ?????????????? 400 ????',
'Selpak 2 ??????????????',
'Oleina ?????? 1 ??',
'?????????? ???? ?????????? 400 ????',
'Nivea ?????? 50 ????',
'?????? 100 ????',
'?????????? ??????????',
'Head & Shoulders 400 ????',
'?????????????? ?????????????? 6 ??',
'???????????? 2.5 ??',
'?????????????? 0.5',
'?????????????? ???? 500 ????',
'???????????? 50 ????',
'?????????????? ?????????? 5 ????',
'Lays ???????? 80 ????',
'???????? ???????????? 180 ????',
'???????????????????? ???????? 454 ????',
'?????????? 1 ??',
'Appetita ???????????????? ????????????',
'???????????? ?????????? 250 ????',
'????????????',
'?????????? ???? ???????????? ???????? 400 ????',
'Cocoro 100 ????',
'3?? ???????????? ????????????',
'???????????????? ???? ?????????????? 500 ????',
'?????????? ???????????? ??????',
'?????? ???????? 200 ????',
'?????????????????? ???????? 22 ????',
'?????? ?????????? 1 ??',
'?????????? 0.75 ??????????',
'?????????? ?????? ???????????? 190 ????',
'Bagro ?????????? ???????????????????? ?????????? 500 ????',
'???????????? ?????????? 50 ????',
'?????????? ?????? ??????????',
'?????? ???????? 110 ???? ????????????',
'Custard 6 ??',
'???????????????????? 0.5',
'?????????? ?????????? 180 ????',
'Hainich ??????????',
'Lays ???????? 80 ????',
'???????????????? 23 ????',
'?????????? 0.100',
'???????????? ???????????? 110 ????'))
product_name


# In[21]:


price=pd.Series(('3300',
'500',
'3100',
'2800',
'1150',
'4000',
'750',
'2500',
'2200',
'850',
'2200',
'1700',
'9000',
'3000',
'1050',
'1100',
'1600',
'1200',
'1200',
'1000',
'450',
'1000',
'7700',
'2500',
'2500',
'2100',
'1500',
'550',
'1100',
'1200',
'1050',
'4000',
'2500',
'240',
'2600',
'1300',
'900',
'4400',
'2100',
'11500',
'1500',
'200',
'3500',
'2500',
'1250',
'4100',
'2200',
'45000',
'450',
'1400',
'2000',
'3200',
'1900',
'4500',
'350',
'400',
'2700',
'1700',
'4800',
'4200',
'5500',
'3300',
'900',
'1950',
'12000',
'2300',
'5700',
'7600',
'500',
'800',
'13200',
'2300',
'1100',
'3400',
'3000',
'350',
'2000',
'4000',
'3000',
'2300',
'1100',
'1050',
'3300',
'500',
'600',
'1600',
'11500',
'3500',
'2200',
'500',
'13000',
'2300',
'2300',
'12500',
'2750',
'3300',
'2300',
'500',
'2000',
'1800'))
price


# In[23]:


quantity=pd.Series(('2',
'3',
'2',
'5',
'2',
'7',
'4',
'6',
'3',
'5',
'9',
'4',
'3',
'3',
'5',
'3',
'6',
'2',
'2',
'3',
'4',
'7',
'7',
'2',
'3',
'2',
'3',
'7',
'2',
'3',
'2',
'6',
'6',
'2',
'3',
'7',
'5',
'9',
'3',
'3',
'4',
'4',
'2',
'2',
'2',
'2',
'4',
'3',
'2',
'6',
'6',
'2',
'1',
'7',
'5',
'6',
'5',
'5',
'2',
'2',
'4',
'1',
'2',
'6',
'3',
'4',
'5',
'8',
'4',
'2',
'1',
'3',
'8',
'2',
'1',
'3',
'3',
'3',
'5',
'1',
'3',
'5',
'1',
'7',
'3',
'2',
'1',
'2',
'7',
'3',
'2',
'1',
'2',
'3',
'2',
'1',
'7',
'3',
'6',
'7'))
quantity


# In[24]:


discount=pd.Series(('0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0,03',
'0,03',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0,03',
'0',
'0',
'0,03',
'0,03',
'0,03',
'0,03',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0,03',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0,03',
'0',
'0',
'0',
'0,03',
'0',
'0',
'0',
'0',
'0',
'0',
'0,03',
'0,03',
'0',
'0',
'0,03'))
discount


# In[25]:


sales=pd.Series(('6600',
'1500',
'6200',
'14000',
'2300',
'28000',
'3000',
'15000',
'6600',
'4250',
'19800',
'6800',
'27000',
'9000',
'5092,5',
'3201',
'9600',
'2400',
'2400',
'3000',
'1800',
'7000',
'53900',
'5000',
'7500',
'4200',
'4500',
'3850',
'2200',
'3600',
'2100',
'24000',
'15000',
'480',
'7566',
'9100',
'4500',
'38412',
'6111',
'33465',
'5820',
'800',
'7000',
'5000',
'2500',
'8200',
'8800',
'135000',
'900',
'8400',
'12000',
'6400',
'1900',
'31500',
'1750',
'2400',
'13500',
'8500',
'9600',
'8400',
'22000',
'3300',
'1800',
'11700',
'36000',
'9200',
'27645',
'60800',
'2000',
'1600',
'13200',
'6900',
'8800',
'6800',
'3000',
'1050',
'6000',
'12000',
'15000',
'2300',
'3300',
'5250',
'3300',
'3500',
'1746',
'3200',
'11500',
'7000',
'14938',
'1500',
'26000',
'2300',
'4600',
'37500',
'5500',
'3201',
'15617',
'1500',
'12000',
'12222'))
sales


# In[31]:


a=pd.DataFrame({'Order ID':order_id,'Order Date':order_date,'Customer ID':customer_id,'Segment':segment,'Region':region,'Category':category,'Product Name':product_name,'Price':price,'Quantity':quantity,'Discount':discount,"Sales":sales})
a


# In[32]:


import numpy as np


# In[ ]:





# In[37]:


order_id=(['CA-2016-152156',
'CA-2016-152156',
'CA-2016-138688',
'US-2015-108966',
'US-2015-108966',
'CA-2014-115812',
'CA-2014-115812',
'CA-2014-115812',
'CA-2014-115812',
'CA-2014-115812',
'CA-2014-115812',
'CA-2014-115812',
'CA-2017-114412',
'CA-2016-161389',
'US-2015-118983',
'US-2015-118983',
'CA-2014-105893',
'CA-2014-167164',
'CA-2014-143336',
'CA-2014-143336',
'CA-2014-143336',
'CA-2016-137330',
'CA-2016-137330',
'US-2017-156909',
'CA-2015-106320',
'CA-2016-121755',
'CA-2016-121755',
'US-2015-150630',
'US-2015-150630',
'US-2015-150630',
'US-2015-150630',
'US-2015-150630',
'US-2015-150630',
'US-2015-150630',
'CA-2017-107727',
'CA-2016-117590',
'CA-2016-117590',
'CA-2015-117415',
'CA-2015-117415',
'CA-2015-117415',
'CA-2015-117415',
'CA-2017-120999',
'CA-2016-101343',
'CA-2017-139619',
'CA-2016-118255',
'CA-2016-118255',
'CA-2014-146703',
'CA-2016-169194',
'CA-2016-169194',
'CA-2015-115742',
'CA-2015-115742',
'CA-2015-115742',
'CA-2015-115742',
'CA-2016-105816',
'CA-2016-105816',
'CA-2016-111682',
'CA-2016-111682',
'CA-2016-111682',
'CA-2016-111682',
'CA-2016-111682',
'CA-2016-111682',
'CA-2016-111682',
'CA-2015-135545',
'CA-2015-135545',
'CA-2015-135545',
'CA-2015-135545',
'US-2015-164175',
'CA-2014-106376',
'CA-2014-106376',
'CA-2016-119823',
'CA-2016-106075',
'CA-2017-114440',
'US-2015-134026',
'US-2015-134026',
'US-2015-134026',
'US-2017-118038',
'US-2017-118038',
'US-2017-118038',
'US-2014-147606',
'CA-2016-127208',
'CA-2016-127208',
'CA-2014-139451',
'CA-2014-139451',
'CA-2015-149734',
'US-2017-119662',
'CA-2017-140088',
'CA-2017-155558',
'CA-2017-155558',
'CA-2016-159695',
'CA-2016-109806',
'CA-2016-109806',
'CA-2016-109806',
'CA-2015-149587',
'CA-2015-149587',
'CA-2015-149587',
'US-2017-109484',
'CA-2017-161018',
'CA-2017-157833',
'CA-2016-149223',
'CA-2016-158568'
])
order_date=(['08/11/2016',
'08/11/2016',
'12/06/2016',
'11/10/2015',
'11/10/2015',
'09/06/2014',
'09/06/2014',
'09/06/2014',
'09/06/2014',
'09/06/2014',
'09/06/2014',
'09/06/2014',
'15/04/2017',
'05/12/2016',
'22/11/2015',
'22/11/2015',
'11/11/2014',
'13/05/2014',
'27/08/2014',
'27/08/2014',
'27/08/2014',
'09/12/2016',
'09/12/2016',
'16/07/2017',
'25/09/2015',
'16/01/2016',
'16/01/2016',
'17/09/2015',
'17/09/2015',
'17/09/2015',
'17/09/2015',
'17/09/2015',
'17/09/2015',
'17/09/2015',
'19/10/2017',
'08/12/2016',
'08/12/2016',
'27/12/2015',
'27/12/2015',
'27/12/2015',
'27/12/2015',
'10/09/2017',
'17/07/2016',
'19/09/2017',
'11/03/2016',
'11/03/2016',
'20/10/2014',
'20/06/2016',
'20/06/2016',
'18/04/2015',
'18/04/2015',
'18/04/2015',
'18/04/2015',
'11/12/2016',
'11/12/2016',
'17/06/2016',
'17/06/2016',
'17/06/2016',
'17/06/2016',
'17/06/2016',
'17/06/2016',
'17/06/2016',
'24/11/2015',
'24/11/2015',
'24/11/2015',
'24/11/2015',
'30/04/2015',
'05/12/2014',
'05/12/2014',
'04/06/2016',
'18/09/2016',
'14/09/2017',
'26/04/2015',
'26/04/2015',
'26/04/2015',
'09/12/2017',
'09/12/2017',
'09/12/2017',
'26/11/2014',
'12/06/2016',
'12/06/2016',
'12/10/2014',
'12/10/2014',
'03/09/2015',
'13/11/2017',
'28/05/2017',
'26/10/2017',
'26/10/2017',
'05/04/2016',
'17/09/2016',
'17/09/2016',
'17/09/2016',
'31/01/2015',
'31/01/2015',
'31/01/2015',
'06/11/2017',
'09/11/2017',
'17/06/2017',
'06/09/2016',
'29/08/2016'])
customer_id=(['EB-13930',
'EB-13930',
'MO-17950',
'JO-15550',
'JO-15550',
'RH-19600',
'RH-19600',
'RH-19600',
'RH-19600',
'RH-19600',
'RH-19600',
'RH-19600',
'GB-14530',
'PW-19030',
'RB-19570',
'RB-19570',
'JS-15940',
'SB-20170',
'HL-15040',
'HL-15040',
'HL-15040',
'DK-13225',
'DK-13225',
'CV-12805',
'NS-18640',
'AF-10885',
'AF-10885',
'JK-15625',
'JK-15625',
'JK-15625',
'JK-15625',
'JK-15625',
'JK-15625',
'JK-15625',
'BC-11125',
'JS-15595',
'JS-15595',
'CS-12355',
'CS-12355',
'CS-12355',
'CS-12355',
'JK-15205',
'SC-20695',
'JD-15895',
'CC-12475',
'CC-12475',
'PM-19135',
'CR-12580',
'CR-12580',
'TB-21400',
'TB-21400',
'TB-21400',
'TB-21400',
'SR-20740',
'SR-20740',
'BB-10990',
'BB-10990',
'BB-10990',
'BB-10990',
'BB-10990',
'BB-10990',
'BB-10990',
'EB-13870',
'EB-13870',
'EB-13870',
'EB-13870',
'QJ-19255',
'RC-19825',
'RC-19825',
'RE-19450',
'RB-19645',
'DL-13315',
'JL-15130',
'JL-15130',
'JL-15130',
'BO-11425',
'BO-11425',
'BO-11425',
'CL-12565',
'LM-17065',
'LM-17065',
'JM-15535',
'JM-15535',
'RP-19855',
'AG-10525',
'GH-14410',
'TS-21205',
'TS-21205',
'AF-10885',
'FM-14380',
'FM-14380',
'FM-14380',
'NS-18640',
'NS-18640',
'NS-18640',
'JR-15700',
'AJ-10945',
'BM-11575',
'CV-12805',
'DK-12835'
])
segment=(['???????? ??????',
'???????? ??????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'??????????????????????',
'??????????????????????',
'????????????',
'????????????',
'????????????',
'????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'????????????',
'???????? ??????',
'??????????????????????',
'????????????'
])
region=(['???????? ??????',
'???????? ??????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'??????????????????????',
'??????????????????????',
'????????????',
'????????????',
'????????????',
'????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'??????????????????????',
'????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'??????????????????????',
'??????????????????????',
'??????????????????????',
'???????? ??????',
'???????? ??????',
'???????? ??????',
'????????????',
'????????????',
'???????? ??????',
'??????????????????????',
'????????????'
])
category=(['??????????, ??????????????',
'OO ?????? ????????, ??????????????????',
'??????????, ??????????????',
'???????? ????????',
'?????????? ????',
'???????? ??????????',
'?????????? ??????????',
'?????????? ??????????',
'OO ?????? ????????, ??????????????????',
'?????????? ????',
'OO ?????? ????????, ??????????????????',
'?????????? ????',
'???????? ????????',
'????????, ???????????? ????????',
'?????????? ????',
'?????????? ????',
'?????????? ??????',
'??????????????',
'?????????? ????????????',
'??????????, ??????????????',
'?????????? ????',
'OO ?????? ????????, ??????????????????',
'???????? ????????',
'??????????????',
'?????? ????????',
'??????????, ??????????????, ????????',
'??????????, ??????????????',
'?????? ????????',
'?????????? ??????????',
'?????????? ????????????',
'?????????? ????',
'???????? ??????????',
'?????????? ????',
'??????????, ??????????????, ????????',
'?????????? ????',
'?????????? ????????',
'??????????????',
'???? ????????',
'?????????? ??????????',
'???????? ????????',
'??????????????',
'?????????? ??????????',
'??????????, ??????????????',
'?????????? ????',
'?????????? ????',
'?????????? ??????',
'?????????? ????????????',
'?????????? ??????????',
'??????????????',
'OO ?????? ????????, ??????????????????',
'?????????? ??????????',
'?????????? ????',
'?????????? ????',
'???????? ??????????',
'??????????????',
'OO ?????? ????????, ??????????????????',
'?????????? ????????',
'???????? ????????',
'OO ?????? ????????, ??????????????????',
'?????????????????? ????????????????????????, ???????????????? ??????',
'??????????, ??????????????',
'?????? ????????????',
'?????????? ??????',
'??????????, ??????????????',
'?????? ????????????',
'??????????, ??????????????',
'???????? ????????',
'???????? ????????',
'?????????? ????',
'??????????????',
'?????????? ??????????',
'?????????? ????????',
'?????????? ????',
'?????????????????? ????????????????????????, ???????????????? ??????',
'?????? ????????',
'??????????????',
'???????? ??????????',
'???????? ??????????',
'??????????, ??????????????',
'?????????? ????????',
'?????? ????????',
'?????????? ????',
'?????????????????? ????????????????????????, ???????????????? ??????',
'?????????? ????',
'??????????, ??????????????',
'?????????? ????',
'???????? ????????',
'?????????????????? ????????????????????????, ???????????????? ??????',
'?????????????????? ????????????????????????, ???????????????? ??????',
'??????????, ??????????????',
'?????? ????????',
'?????????? ????????????',
'??????????, ??????????????',
'???????? ????????',
'??????????????',
'???????????? ??????????????, ???????????????? ????????????',
'?????????? ????????',
'??????????, ??????????????, ????????',
'???????? ????????',
'?????????? ????????????'
])
p_name=(['Shokolinsen 250 ????',
'???????????????? 00?????? ????????',
'?????????????? ???????????????? 230 ????',
'?????????????? ???????? 500 ????',
'Punch 450 ????',
'?????????????? ??????',
'?????????? ?????????? 400 ????',
'?????????? ?????? ??????????????????',
'Lady 20 ??',
'370 ???????? 370 ????',
'???????? ?????????? 30 ??',
'Pysio 300 ????',
'A vodka 0.5',
'?????????? ??????????????',
'Vita ?????????????? ???? 510 ????',
'???????? ???????????? 180 ????',
'Power 400 g',
'?????????????? ???? ?????????????? 80 ???? ????????????',
'???????? ???????????? ????????????',
'M&M 45 ????',
'?????????????? ???? 500 ????',
'?????????????? ???4',
'Solpro ?????????????? 3 ?? 67 %',
'???????????? 80 ????',
'???????????????? ???????????? 5 ?? ????????',
'???????????? ??????????',
'Akuku ?????????? 90 ????',
'???????????? ???????????????? Gilette',
'?????????????? ?????????? 250 ????',
'?????????? ???????????? ??????????????',
'?????????????? ?????????? 500 ????',
'?????????????? ??????',
'Arizona ?????????????? 680 ????',
'Jacobs ????????',
'?????????? ??????',
'?????? ???????? 55 ????',
'???????????? 65 ????',
'Colgate total 100 ????',
'?????????? ?????????????????? ?????????? 650 ????',
'?????????? 0.75 ??????????',
'???????????? 200 ????',
'???????? 1 ????',
'Mini cracker 350 ????',
'Arizona ?????????????? 680 ????',
'?????????? ?????????????? 330 ????',
'Tide 450 ???? ????????',
'Paldo king noodle 110 ????',
'?????????? 25 ????',
'Appetita ??????????',
'???????? ?????????? 100 ??',
'?????????? ?????? 1 ????',
'?????? ?????????? 1 ??',
'???????? ???????? 1.25 ????',
'????????????????',
'Appetita ???????????????? ????????????',
'???????????????? 00?????? ????????',
'Siesta ???????? 200 ????',
'?????????????? ?????????????? 400 ????',
'Selpak 2 ??????????????',
'Oleina ?????? 1 ??',
'?????????? ???? ?????????? 400 ????',
'Nivea ?????? 50 ????',
'?????? 100 ????',
'?????????? ??????????',
'Head & Shoulders 400 ????',
'?????????????? ?????????????? 6 ??',
'???????????? 2.5 ??',
'?????????????? 0.5',
'?????????????? ???? 500 ????',
'???????????? 50 ????',
'?????????????? ?????????? 5 ????',
'Lays ???????? 80 ????',
'???????? ???????????? 180 ????',
'???????????????????? ???????? 454 ????',
'?????????? 1 ??',
'Appetita ???????????????? ????????????',
'???????????? ?????????? 250 ????',
'????????????',
'?????????? ???? ???????????? ???????? 400 ????',
'Cocoro 100 ????',
'3?? ???????????? ????????????',
'???????????????? ???? ?????????????? 500 ????',
'?????????? ???????????? ??????',
'?????? ???????? 200 ????',
'?????????????????? ???????? 22 ????',
'?????? ?????????? 1 ??',
'?????????? 0.75 ??????????',
'?????????? ?????? ???????????? 190 ????',
'Bagro ?????????? ???????????????????? ?????????? 500 ????',
'???????????? ?????????? 50 ????',
'?????????? ?????? ??????????',
'?????? ???????? 110 ???? ????????????',
'Custard 6 ??',
'???????????????????? 0.5',
'?????????? ?????????? 180 ????',
'Hainich ??????????',
'Lays ???????? 80 ????',
'???????????????? 23 ????',
'?????????? 0.100',
'???????????? ???????????? 110 ????'
])
price=(['3300',
'500',
'3100',
'2800',
'1150',
'4000',
'750',
'2500',
'2200',
'850',
'2200',
'1700',
'9000',
'3000',
'1050',
'1100',
'1600',
'1200',
'1200',
'1000',
'450',
'1000',
'7700',
'2500',
'2500',
'2100',
'1500',
'550',
'1100',
'1200',
'1050',
'4000',
'2500',
'240',
'2600',
'1300',
'900',
'4400',
'2100',
'11500',
'1500',
'200',
'3500',
'2500',
'1250',
'4100',
'2200',
'45000',
'450',
'1400',
'2000',
'3200',
'1900',
'4500',
'350',
'400',
'2700',
'1700',
'4800',
'4200',
'5500',
'3300',
'900',
'1950',
'12000',
'2300',
'5700',
'7600',
'500',
'800',
'13200',
'2300',
'1100',
'3400',
'3000',
'350',
'2000',
'4000',
'3000',
'2300',
'1100',
'1050',
'3300',
'500',
'600',
'1600',
'11500',
'3500',
'2200',
'500',
'13000',
'2300',
'2300',
'12500',
'2750',
'3300',
'2300',
'500',
'2000',
'1800'
])
quantity=(['2',
'3',
'2',
'5',
'2',
'7',
'4',
'6',
'3',
'5',
'9',
'4',
'3',
'3',
'5',
'3',
'6',
'2',
'2',
'3',
'4',
'7',
'7',
'2',
'3',
'2',
'3',
'7',
'2',
'3',
'2',
'6',
'6',
'2',
'3',
'7',
'5',
'9',
'3',
'3',
'4',
'4',
'2',
'2',
'2',
'2',
'4',
'3',
'2',
'6',
'6',
'2',
'1',
'7',
'5',
'6',
'5',
'5',
'2',
'2',
'4',
'1',
'2',
'6',
'3',
'4',
'5',
'8',
'4',
'2',
'1',
'3',
'8',
'2',
'1',
'3',
'3',
'3',
'5',
'1',
'3',
'5',
'1',
'7',
'3',
'2',
'1',
'2',
'7',
'3',
'2',
'1',
'2',
'3',
'2',
'1',
'7',
'3',
'6',
'7'
])
discount=(['0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0,03',
'0,03',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0,03',
'0',
'0',
'0,03',
'0,03',
'0,03',
'0,03',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0,03',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0,03',
'0',
'0',
'0',
'0,03',
'0',
'0',
'0',
'0',
'0',
'0',
'0,03',
'0,03',
'0',
'0',
'0,03'
])
sales=(['6600',
'1500',
'6200',
'14000',
'2300',
'28000',
'3000',
'15000',
'6600',
'4250',
'19800',
'6800',
'27000',
'9000',
'5092,5',
'3201',
'9600',
'2400',
'2400',
'3000',
'1800',
'7000',
'53900',
'5000',
'7500',
'4200',
'4500',
'3850',
'2200',
'3600',
'2100',
'24000',
'15000',
'480',
'7566',
'9100',
'4500',
'38412',
'6111',
'33465',
'5820',
'800',
'7000',
'5000',
'2500',
'8200',
'8800',
'135000',
'900',
'8400',
'12000',
'6400',
'1900',
'31500',
'1750',
'2400',
'13500',
'8500',
'9600',
'8400',
'22000',
'3300',
'1800',
'11700',
'36000',
'9200',
'27645',
'60800',
'2000',
'1600',
'13200',
'6900',
'8800',
'6800',
'3000',
'1050',
'6000',
'12000',
'15000',
'2300',
'3300',
'5250',
'3300',
'3500',
'1746',
'3200',
'11500',
'7000',
'14938',
'1500',
'26000',
'2300',
'4600',
'37500',
'5500',
'3201',
'15617',
'1500',
'12000',
'12222'
])
a=np.array([order_id,order_date,customer_id,segment,region,category,p_name,price,quantity,discount,sales])
a


# In[43]:


b=pd.DataFrame(a,index=['Order ID',
'Order Date',
'Customer ID',
'Segment',
'Region',
'Category',
'Product Name',
'Price',
'Quantity',
'Discount',
"Sales"],columns=['1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'10',
'11',
'12',
'13',
'14',
'15',
'16',
'17',
'18',
'19',
'20',
'21',
'22',
'23',
'24',
'25',
'26',
'27',
'28',
'29',
'30',
'31',
'32',
'33',
'34',
'35',
'36',
'37',
'38',
'39',
'40',
'41',
'42',
'43',
'44',
'45',
'46',
'47',
'48',
'49',
'50',
'51',
'52',
'53',
'54',
'55',
'56',
'57',
'58',
'59',
'60',
'61',
'62',
'63',
'64',
'65',
'66',
'67',
'68',
'69',
'70',
'71',
'72',
'73',
'74',
'75',
'76',
'77',
'78',
'79',
'80',
'81',
'82',
'83',
'84',
'85',
'86',
'87',
'88',
'89',
'90',
'91',
'92',
'93',
'94',
'95',
'96',
'97',
'98',
'99',
'100'])
b


# In[46]:


b.T


# In[49]:


order_id.to_numpy


# In[ ]:




