# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:21:22 2020

@author: Alan Lin
"""
# 選項不能超過20字元,不能超過13個選項
# ['測試數量','1','2','3','4','5','6','7','8','9','10','11','12','13']
Qdict={'q1':['目前有沒有高血壓','沒有','有，沒有治療','有，不規則治療','有，規則治療'],
        'q2':['目前有沒有糖尿病','沒有','有，沒有治療','有，不規則治療','有，規則治療'],
        'q3':['目前有沒有高血脂','沒有','有，沒有治療','有，不規則治療','有，規則治療'],
        'q4':['目前是否有治療中的內外科疾病','沒有','有，請輸入:'],
        'q5':['曾看過精神科（身心科），被確診過任何精神心理疾病？','沒有','焦慮症(廣泛性焦慮症、恐慌症、懼曠症)','憂鬱症','躁鬱症','飲食疾患(如:暴食症、厭食症)','注意力缺乏/過動症','思覺失調症(精神分裂症)','強迫症','創傷後壓力症候群','其它(請輸入:)'],
        'q6':['曾被診斷過下列疾病？','沒有','過敏性鼻炎','鼻竇炎','氣喘','胃食道逆流','消化性潰瘍（胃潰瘍或十二指腸潰瘍）'],
        'a':['有以下呼吸道與其他相關身體症狀\na. 聲音沙啞或嗓音有問題','沒有症狀','輕微','中等','嚴重'],
        'b':['b. 想清喉嚨的症狀，有東西卡住或腫塊的感覺','沒有症狀','輕微','中等','嚴重'],
        'c':['c. 喉部有過多的黏液或鼻涕倒流','沒有症狀','輕微','中等','嚴重'],
        'd':['d. 吞嚥食物、液體或藥丸時有困難','沒有症狀','輕微','中等','嚴重'],
        'e':['e. 吸氣困難或陣發性的嗆到感','沒有症狀','輕微','中等','嚴重'],
        'f':['f. 胸口灼熱、疼痛或胃酸逆流上來的感覺','沒有症狀','輕微','中等','嚴重'],
        'q7':['有抽菸習慣？','沒有','一天超過兩包','一天約一包','一天半包以下','偶爾抽'],
        'q8':['有喝酒習慣？','沒有','天天喝','一週2~3次','每月2~4次','每月少於1次'],
        '1':['1:這兩週，你通常幾點上床準備睡覺？\n晚上10:00上床 請輸入: 2200(24時制4位數)','(例如: 2200)'],
         '2':['2:這兩週，你上床經過多久才睡著?\n過15分鐘睡著 請輸入: 15(分鐘)','(例如: 15)'],
         '3':['3:這兩週，你醒來後通常幾點下床?\n早上7:30下床 請輸入: 0730(24時制4位數)','(例如: 0730)'],
         '4':['4:這兩週，你實際每晚平均可以入睡幾小時？\n共睡覺6.5小時 請輸入: 6.5','(例如: 6.5)'],
         '5':['5:整體而言，您滿意這兩週的睡眠品質？','很滿意','滿意','還可以','不滿意','很不滿意'],
         '6A':['6A:睡眠是否出現下列困擾','無法在三十分鐘內入睡','無法維持睡眠，半夜會醒來','比你預計的時間早醒來','沒有以上困擾'],
            '6-1-a':['6-1-a:無法在三十分鐘內入睡','從未發生','每週不到一次','每週一兩次','每週三次以上'],
            '6-1-b':['6-1-b:關於無法在三十分鐘內入睡的嚴重程度，你的評估？','還算輕微','有些困擾','明顯影響','非常嚴重'],
            '6-2.1-a':['6-2.1-a:無法維持睡眠，半夜會醒來','從未發生','每週不到一次','每週一兩次','每週三次以上'],
            '6-2.1-b':['6-2.1-b:關於無法維持睡眠的嚴重程度，你的評估？','還算輕微','有些困擾','明顯影響','非常嚴重'],
            '6-2.2-a':['6-2.2-a:比你預計的時間早醒來(太早醒)','從未發生','每週不到一次','每週一兩次','每週三次以上'],
            '6-2.2-b':['6-2.2-b:關於太早醒的嚴重程度，你的評估？','還算輕微','有些困擾','明顯影響','非常嚴重'],
        '6B':['6B:接下來請你回想這兩週的睡眠期間是否受以下症狀干擾？','半夜要起來上廁所','覺得呼吸不順暢','大聲打鼾','咳嗽','發冷','燥熱','作惡夢','身上有疼痛','沒有以上困擾'], 
            '6-3':['6-3:這兩週中，半夜要起來上廁所的狀況','從未發生','每週不到一次','每週一兩次','每週三次以上'],
            '6-3-A':['6-3-A:請問您開始出現夜尿（一次以上）的情況大約有幾年了？','最近一年內','一到三年','三到五年','超過五年'],
            '6-3-B':['6-3-B:一般而言請問您因為需要小便的緣故一個晚上會醒來多少次？','大約一次','兩次','三次','四次以上'],
            '6-3-C':['6-3-C:請問您平時是否出現解尿困難的現象？','從未發生','偶而會','有時候會','大多數時間會'],
            '6-4':['6-4:這兩週中，呼吸不順暢對睡眠的干擾','從未發生','每週不到一次','每週一兩次','每週三次以上'],
            '6-5.1':['6-5.1:這兩週中，大聲打鼾對睡眠的干擾','從未發生','每週不到一次','每週一兩次','每週三次以上'],
            '6-5.2':['6-5.2:這兩週中，咳嗽對睡眠的干擾','從未發生','每週不到一次','每週一兩次','每週三次以上'],
            '6-5.2-A':['6-5.2-A:咳嗽對您睡眠的影響:','從未發生','偶而會','有時候會','大多數時間會','幾乎都會'],
            '6-5.2-B':['6-5.2-B:您會因咳嗽而中斷談話或接聽電話嗎？','從未發生','偶而會','有時候會','大多數時間會','幾乎都會'],
            '6-5.2-C':['6-5.2-C:在身體勞動或運動時，你的咳嗽症狀:','比較嚴重','比較輕微','不受影響'],
            '6-5.2-D':['6-5.2-D:您覺得能控制咳嗽的症狀嗎？','一直都能','多數時間能','有時候能','很少能','一點也無法'],
            '6-6':['6-6:這兩週中，覺得冷對睡眠的干擾','從未發生','每週不到一次','每週一兩次','每週三次以上'],
            '6-7':['6-7:這兩週中，覺得躁熱對睡眠的干擾','從未發生','每週不到一次','每週一兩次','每週三次以上'],
            '6-8':['6-8這兩週中，作惡夢對睡眠的干擾:','從未發生','每週不到一次','每週一兩次','每週三次以上'],
            '6-9':['6-9:這兩週中，身上有疼痛對睡眠的干擾','從未發生','每週不到一次','每週一兩次','每週三次以上'],        
        '7':['7:睡眠困擾是否會影響工作，日常生活、專注力、記憶力、情緒等功能','不會','輕微','有些','明顯','非常'], #qtag = 21
        '8':['8:他人是否有注意到您的生活品質因睡眠問題受到影響？','不會','輕微','有些','明顯','非常'],
        '9':['9:最近的睡眠問題是否令您擔心/困擾？','不會','輕微','有些','明顯','非常'],
        '10':['10:過去兩週來，您要打起精神來完成您應該做的事情對您有多少困擾？','不會','輕微','有些','明顯','非常'],
        '11_1':['11_1:過去兩週來，是否需要使用藥物(處方用藥或成藥)幫忙睡眠？','從未發生','每週不到一次','每週一兩次','每週三次以上'],
        '11_2':['11_2:過去兩週來，是否需要使用酒精或其他中藥或保健食品幫忙睡眠？','從未發生','每週不到一次','每週一兩次','每週三次以上'], 
            'DSM_5_1':['上述這些失眠或是需要用藥物或是酒精，物質助眠的現象\n已經持續___幾週？\n（一個月以上：亞急性失眠，三個月以上：慢性失眠），請輸入:','(例如: 12)'],
            'DSM_5_2':['以前發生過嗎？','是','否'],
        '12':['12:是否有任何人觀察到你在睡覺時呼吸停止或嗆到/喘氣','否','是'],
        '13':['13:過去兩週來，您是否曾在用餐、開車或社交場合打瞌睡而無法保持清醒?','從未發生','每週不到一次','每週一兩次','每週三次以上'],
        '13_1':['13_1:坐著閱讀時，會打瞌睡或睡著嗎？','從未','很少','一半以上','幾乎都會'],
        '13_2':['13_2:看電視時，會打瞌睡或睡著嗎？','從未','很少','一半以上','幾乎都會'],
        '13_3':['13_3:在公眾場合安靜坐著(如在戲院或會議中) ，會打瞌睡或睡著嗎？','從未','很少','一半以上','幾乎都會'],
        '13_4':['13_4:坐車連續超過一小時(不包含自己開車) ，會打瞌睡或睡著嗎？','從未','很少','一半以上','幾乎都會'],
        '13_5':['13_5:在下午躺下休息時 ，會打瞌睡或睡著嗎？','從未','很少','一半以上','幾乎都會'],
        '13_6':['13_6:坐著與人交談時，會打瞌睡或睡著嗎？','從未','很少','一半以上','幾乎都會'],
        '13_7':['13_7:沒有喝酒的情況下，在午餐後安靜坐著時，會打瞌睡或睡著嗎？','從未','很少','一半以上','幾乎都會'],
        '13_8':['13_8:開車/騎車中遇到交通問題而停下數分鐘時 ，會打瞌睡或睡著嗎？','我沒有自行開/騎車','從未','很少','一半以上','幾乎都會'],
        '14':['睡眠好壞與情緒狀態習習相關，接下來請您回想一下這兩週的情緒狀態～\n14:這兩週，你是否會感到緊張、不安或煩躁','從未','很少','一半以上','幾乎都會'],
        '15':['15:這兩週，你是否會無法停止或控制憂慮','從未','很少','一半以上','幾乎都會'],
        '16':['16:這兩週，你是否會對不同事情過度擔憂','從未','很少','一半以上','幾乎都會'],
        '17':['17:這兩週，你是否會身心難以放鬆','從未','很少','一半以上','幾乎都會'],
        '18':['18:這兩週，你是否會焦躁不安到難以安靜坐著','從未','很少','一半以上','幾乎都會'],
        '19':['19:這兩週，你是否會容易心煩或易怒','從未','很少','一半以上','幾乎都會'],
        '20':['20:這兩週，你是否會感到害怕，就像要發生可怕的事情','從未','很少','一半以上','幾乎都會'],
        '21':['21:這兩週，你是否會做事時提不起勁或沒有樂趣','從未','很少','一半以上','幾乎都會'],
        '22':['22:這兩週，你是否會感到心情低落、沮喪或絕望','從未','很少','一半以上','幾乎都會'],
        '23':['23:這兩週，你是否會入睡困難、睡不安穩或睡眠過多','從未','很少','一半以上','幾乎都會'],
        '24':['24:這兩週，你是否會感覺疲倦或沒有活力','從未','很少','一半以上','幾乎都會'],
        '25':['25:這兩週，你是否會食慾不振或吃太多','從未','很少','一半以上','幾乎都會'],
        '26':['26:這兩週，你是否會覺得自己很糟—或覺得自己很失敗，或讓自己或家人失望','從未','很少','一半以上','幾乎都會'],
        '27':['27:這兩週，你是否會對事物專注有困難，例如閱讀報紙或看電視時','從未','很少','一半以上','幾乎都會'],
        '28':['28:這兩週，你是否會動作或說話速度緩慢到別人已經察覺，或正好相反-煩躁或坐立不安、動來動去的情況更勝於平常','從未','很少','一半以上','幾乎都會'],
        '29':['29:這兩週，你是否會有不如死掉或用某種方式傷害自己的念頭','從未','很少','一半以上','幾乎都會'],
        'gender':['基本資料\n性別 :','女','男'], #qtag = 52
        'birthday':['生日 :\n請輸入: 西元/月/日:','(例如: 1960/1/1)'],
        'height':['身高 :\n請輸入: 公分 cm','(例如: 170)'],
        'weight':['體重 :\n請輸入: 公斤 kg','(例如: 50)'],
        'neck circumference':['頸圍(或襯衫頸圍) :\n請輸入: 吋(35公分 除 2.54 = 13.7吋)','(例如: 14)'],
        'education':['教育 :','未就學','小學','國中','高中','大專','研究所以上'],
        'Profession':['職業 :','學生','軍公教','服務業','金融業','資訊/科技','傳播/廣告/設計','藝文','自由業','醫療','製造業','農林漁牧','家管','其他(請輸入:)'],
        'marital':['婚姻狀況 :','未婚','同居','已婚','離婚','寡居'],
        'income':['您家庭最近一年每月平均總收入為多少元？','30,000元以下','30,001~60,000元','60,001~100,000元','100,000元以上'] 
        }