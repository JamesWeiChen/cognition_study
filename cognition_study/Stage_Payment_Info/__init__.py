from otree.api import *
import time # 🌟 幫妳補上時間套件，免得最後的報酬頁面報錯！

class C(BaseConstants):
    NAME_IN_URL = 'receipt'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Player(BasePlayer):
    年齡 = models.IntegerField(label='請問您今年幾歲?', min=13, max=125)
    性別 = models.StringField(
        choices=[['男', '男'], ['女', '女']],
        label='請問您的性別為？',
        widget=widgets.RadioSelect,
    )
    是否為學生 = models.StringField(
        choices=['是', '否'],
        label='請問您目前是否具有學生身分？',
        widget=widgets.RadioSelect,
    )
    年級 = models.StringField(
        choices=['大一', '大二', '大三', '大四', '大四以上(延畢)', '碩士', '博士', '其他'],
        label='請問您目前的年級為？',
        blank=True,
        widget=widgets.RadioSelect,
    )
    學院 = models.StringField(
        label='請問您就讀的學院為？（例如：社會科學院、理學院等）',
        blank=True,
    )
    科系 = models.StringField(
        label='請問您就讀的科系為？',
        blank=True,
    )
    政治傾向 = models.StringField(
        choices=['民主進步黨', '中國國民黨', '台灣民眾黨', '時代力量', '台灣基進', '中立', '其他'],
        label='請問您的政治傾向較接近以下何者？',
        widget=widgets.RadioSelect,
    )
    政治傾向_其他 = models.StringField(
        label='若您選擇「其他」，請在此註明您的政治傾向：',
        blank=True
    )
    關注社會議題時間 = models.StringField(
        choices=['幾乎沒有', '每週 1 到 3 小時', '每週 4 到 6 小時', '每週 7 到 10 小時', '每週 10 小時以上'],
        label='請問您平均每週大約花多少時間關注社會或政治議題（包含看新聞、社群媒體討論等）？',
        widget=widgets.RadioSelect,
    )
    關注校園議題時間 = models.StringField(
        choices=['幾乎沒有', '每週 1 到 3 小時', '每週 4 到 6 小時', '每週 7 到 10 小時', '每週 10 小時以上'],
        label='請問您平均每週大約花多少時間關注校園議題？',
        widget=widgets.RadioSelect,
    )

    total_payment = models.IntegerField(initial=150)
    
    # === 基本資料 ===
    name = models.StringField(label="您的名字")
    school = models.StringField(
        label="您的學校",
        choices=[
            ('國立臺灣大學', '國立臺灣大學'),
            ('國立政治大學', '國立政治大學'),
            ('國立臺北大學', '國立臺北大學'),
            ('國立臺灣師範大學', '國立臺灣師範大學'),
            ('國立臺北教育大學', '國立臺北教育大學'),
            ('國立臺灣科技大學', '國立臺灣科技大學'),
            ('國立成功大學', '國立成功大學'),
        ],
        widget=widgets.RadioSelectHorizontal,
        initial='國立臺灣大學',
    )
    student_id = models.StringField(label="您的學號")
    id_number = models.StringField(label="您的身份證字號", blank=True)
    address = models.StringField(label="您的戶籍地址（含鄰里，需與身分證一致）")
    is_foreign = models.StringField(
        label="您是否為外籍生？",
        choices=[('是', '是'), ('否', '否')],
        widget=widgets.RadioSelect
    )
    arc = models.StringField(label="居留證號碼", blank=True)
    passport = models.StringField(label="護照號碼", blank=True)
    nation = models.StringField(label="國籍", blank=True)
    stay = models.StringField(
        label="是否在台滿 183 天",
        choices=[('是', '是'), ('否', '否')],
        widget=widgets.RadioSelect,
        blank=True
    )

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Consent(Page):
    form_model = None

    @staticmethod
    def vars_for_template(player: Player):
        return {}


class WaitStart(Page):
    form_model = None


class 等(Page):
    pass

class 收據前一頁(Page):
    pass

class BasicInfo(Page):
    form_model = 'player'
    form_fields = [
        'name',
        'school',
        'student_id',
        'is_foreign',
        'id_number',
        'address',
        'arc',
        'passport',
        'nation',
        'stay'
    ]

    @staticmethod
    def error_message(player: Player, values):
        if values['is_foreign'] == '否':
            id_number = (values['id_number'] or '').strip()
            if not id_number:
                return '請填寫身份證字號'
            if len(id_number) != 10:
                return '身份證字號長度不正確'
            if not id_number[0].isalpha():
                return '身份證字號第 1 碼應為英文字母'
            if not id_number[1:9].isnumeric():
                return '身份證字號格式不正確'
        if values['is_foreign'] == '是':
            if not values['arc']:
                return '請填寫居留證號碼'
            if not values['passport']:
                return '請填寫護照號碼'
            if not values['nation']:
                return '請填寫國籍'
            if not values['stay']:
                return '請選擇是否在台滿 183 天'

class 人口背景調查(Page):
    form_model = 'player'
    form_fields = ['年齡', '性別', '是否為學生', '年級', '學院', '科系', '政治傾向', '政治傾向_其他', '關注社會議題時間', '關注校園議題時間']
    
    @staticmethod
    def error_message(player:Player, values):
        if values['政治傾向'] == '其他' and not values['政治傾向_其他']:
            return '請在下方欄位具體填寫您的政治傾向'
        if values['是否為學生'] == '是':
            if not values['年級'] or not values['學院'] or not values['科系']:
                return '請完整填寫您的年級、學院與科系'

class 報酬(Page):
    pass

# 🌟 這是我們新增的結算頁面！
class 測驗結果結算(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # 1. 抓出總金額 (剛剛在第一頁已經安全存好了)
        總金額 = player.total_payment
        
        # 2. 扣掉底薪 150，剩下的就是額外獎金
        額外獎金 = 總金額 - 150
        
        # 3. 獎金除以 10，就是答對的題數 (轉成整數 int 才不會有小數點)
        答對題數 = int(額外獎金 / 10)
        
        # 4. 把算好的這三個數字打包，準備傳給網頁顯示！
        return dict(
            答對題數 = 答對題數,
            額外獎金 = 額外獎金,
            總金額 = 總金額
        )

class 收據前等(Page):
    # 🌟 終極魔法搬家啦！放在真正的第一頁，只要一進這個 App 絕對會發動！
    @staticmethod
    def is_displayed(player: Player):
        # 把算好的錢從隨身包拿出來，更新 App 2 的資料庫！
        payment = player.participant.vars.get('total_payment', 150)
        
        player.total_payment = payment
        player.payoff = payment # 順便把 oTree 內建的 payoff 也更新
        
        return True # 回傳 True 表示這個頁面會正常顯示

page_sequence = [收據前等, 收據前一頁, BasicInfo, 等, 人口背景調查, 測驗結果結算, 報酬]