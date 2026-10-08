from otree.api import *
import random
import time

class C(BaseConstants):
    NAME_IN_URL = 'policy_cognition'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    論點列表 = [
        "並非持有多戶房屋者皆為炒房，一概徵收高稅率有失公平。部分房產屬於繼承取得或民眾投入畢生積蓄準備養老之用，必須予以區分。",
        "住宅雖具備投資獲利資本財性質，但核心功能乃滿足居住需求消費財。當民生必需品出現嚴重囤積空置情形時，政府應積極介入抑制。",
        "房屋稅賦極易轉嫁給消費者來承受，學術研究指出其轉嫁幅度往往極高。缺乏配套強行課稅恐致租金上漲，引發房價愈打愈高的怪象。",
        "台灣的房市問題具備了特殊性，高房價卻伴隨高空屋率並非單純經濟學能解釋，而是市場將房屋當作炒作工具而非居住之外部效應。"
    ]
    景觀論點列表 = [
        "台灣老舊危險建築眾多，降低都更門檻能加速淘汰具公安疑慮之危樓保障居民生命財產安全，並避免都市更新因少數人杯葛而停滯。",
        "適度下修同意比例有助大面積推動老屋重建計畫，不僅能提升整體居住安全與生活品質，更能優化土地利用效率帶動周邊經濟發展。",
        "房屋與土地本屬私有財產，貿然下修門檻恐將導致多數暴力。強迫少數不同意戶參與改建，將嚴重侵犯憲法所保障的財產與居住自由。",
        "降低門檻極易使建商掌握主導權，迫使經濟弱勢原住戶搬離其熟悉生活圈。若缺乏完善的安置配套，將引發社會迫遷爭議與階級不公。"
    ]
    論點列表2 = [
        "大學成績通膨極其嚴重，導致優等評價失去原有的鑑別度。限制比例能恢復成績客觀評估功能，讓表現卓越學生獲得應有肯定與區隔。",
        "嚴格限制高分比例容易引發學生間的惡性競爭破壞同儕合作學習氛圍。評量應以學生達到學習目標為準而非強迫進行相對的比較。",
        "給分過於浮濫會削弱學術標準公信力，讓外界難以評估學生的真實能力。透過合理比例限制，可以有效維護學校教學品質與文憑價值。",
        "每門課程性質與學生組成皆不同，硬性規定給分比例顯得相當不合常理。部分進階課程學生已具備專業，強制壓低分數對其極為不公。"
    ]
    景觀論點列表2 = [
        "現代社會極需跨領域優秀人才，增加探索學分能大幅降低學業壓力。鼓勵學生勇敢跨出舒適圈去嘗試不同學科，有助拓展多元的思維。",
        "大幅放寬探索學分恐導致部分學生修課態度變得散漫而抱持及格就好心態。此舉不僅浪費寶貴教育資源亦無法確保跨域學習成效。",
        "許多學生選系時並不清楚自身志向，給予更多探索空間能讓他們有機會發掘真正熱愛的領域，減少未來因學非所用所產生適應問題。",
        "畢業的總學分固定不變，過度增加探索學分比例，勢必會擠壓到本科專業的訓練時間，恐致學生核心領域競爭力下滑影響其職涯發展。"
    ]
    九階選項 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    import random
    
    treatments_1 = [
        ('失調組', '動機性推理組'),
        ('失調組', '中性推理組'),
        ('中性組', '動機性推理組'),
        ('中性組', '中性推理組')
    ]
    
    random.shuffle(treatments_1)
    
    for player in subsession.get_players():
        config = subsession.session.config
        idx = (player.id_in_subsession - 1) % 4
        t1, r1 = treatments_1[idx]
        
        player.失調組別 = config.get('dissonance_1', t1)
        player.推理組別 = config.get('reasoning_1', r1)

        論點順序 = [1, 2, 3, 4]
        random.shuffle(論點順序)
        player.participant.vars['論點順序'] = 論點順序
        
        政見列表 = ['完全廢除景觀法', '建立更嚴格的景觀法']
        random.shuffle(政見列表)
        player.候選人A_景觀法政見 = 政見列表[0]
        player.候選人B_景觀法政見 = 政見列表[1]

class Group(BaseGroup):
    pass

def 囤房稅後續選擇_choices(player):
    低稅率, 高稅率 = get_tax_rates(player)
    第一個選項 = [低稅率, f'候選人A（主張囤房稅率：{低稅率}%）']
    第二個選項 = [高稅率, f'候選人B（主張囤房稅率：{高稅率}%）']
    return [第一個選項, 第二個選項]

def 景觀法後續選擇_choices(player):
    低門檻, 高門檻 = get_renewal_rates(player)
    第一個選項 = [低門檻, f'候選人A（主張：{低門檻}%居民同意即可都更）']
    第二個選項 = [高門檻, f'候選人B（主張：{高門檻}%居民同意即可都更）']
    return [第一個選項, 第二個選項]

def A加後續選擇_choices(player):
    低比例, 高比例 = get_a_plus_rates(player)
    第一個選項 = [低比例, f'候選人A（主張將 A+ 比例控管在 {低比例}% 以內）']
    第二個選項 = [高比例, f'候選人B（主張將 A+ 比例控管在 {高比例}% 以內）']
    return [第一個選項, 第二個選項]

def 探索學分後續選擇_choices(player):
    低學分, 高學分 = get_credit(player)
    第一個選項 = [低學分, f'候選人A（主張探索學分上限為 {低學分} 學分）']
    第二個選項 = [高學分, f'候選人B（主張探索學分上限為 {高學分} 學分）']
    return [第一個選項, 第二個選項]

class Player(BasePlayer):
    囤房稅錯誤次數 = models.IntegerField(initial=0)
    景觀法錯誤次數 = models.IntegerField(initial=0)
    A加錯誤次數 = models.IntegerField(initial=0)
    探索學分錯誤次數 = models.IntegerField(initial=0)
    前測囤房稅錯誤次數 = models.IntegerField(initial=0)
    前測景觀法錯誤次數 = models.IntegerField(initial=0)
    前測A加錯誤次數 = models.IntegerField(initial=0)
    前測探索學分錯誤次數 = models.IntegerField(initial=0)

    前測囤房稅測驗結果 = models.IntegerField(blank=True, null=True)
    前測景觀法測驗結果 = models.IntegerField(blank=True, null=True)
    前測探索學分測驗結果 = models.IntegerField(blank=True, null=True)
    前測A加測驗結果 = models.IntegerField(blank=True, null=True)

    囤房稅測驗結果 = models.IntegerField(blank=True, null=True)
    景觀法測驗結果 = models.IntegerField(blank=True, null=True)
    探索學分測驗結果 = models.IntegerField(blank=True, null=True) 
    A加測驗結果 = models.IntegerField(blank=True, null=True)

    總實驗時間 = models.FloatField(blank=True, null=True)
    失調組別 = models.StringField()
    推理組別 = models.StringField()
    
    
    初始囤房稅 = models.FloatField(label='',min=0)
    最終囤房稅 = models.FloatField(label='',min=0)
    初始景觀同意門檻 = models.FloatField(label='',min=0, max=100)
    最終景觀同意門檻 = models.FloatField(label='',min=0, max=100)

    初始A加比例 = models.FloatField(label='',min=0, max=100)
    最終A加比例 = models.FloatField(label='',min=0, max=100)
    初始探索學分 = models.IntegerField(label='',min=0)
    最終探索學分 = models.IntegerField(label='',min=0)

    初始囤房稅態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終囤房稅態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    初始囤房稅重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終囤房稅重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    
    初始景觀法態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終景觀法態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    初始景觀法重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終景觀法重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)

    初始A加限制態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終A加限制態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    初始A加限制重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終A加限制重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)

    初始探索學分態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終探索學分態度 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    初始探索學分重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    最終探索學分重要性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)

    囤房稅後續選擇 = models.FloatField(
        label='現在有兩位候選人正在競選T市市長\n請想像自己身為 T市公民，選擇你支持的候選人\n＊注意：這不是真實的選舉，您無需考量現實法規的上下限。',
        widget=widgets.RadioSelect
    )
    景觀法後續選擇 = models.FloatField(
        label='現在有兩位候選人正在競選T市市長\n請想像自己身為 T市公民，選擇你支持的候選人\n＊注意：這不是真實的選舉，您無需考量現實法規的上下限。',
        widget=widgets.RadioSelect
    )
    候選人A_景觀法政見 = models.StringField()
    候選人B_景觀法政見 = models.StringField()
    辯護文章 = models.LongStringField(label='')
    景觀法文章 = models.LongStringField(label='')
    A加後續選擇 = models.FloatField(
        label='現在有兩位候選人正在競選T校學生會會長\n請想像自己身為 T校學生，選擇你支持的候選人\n＊注意：這不是真實的選舉，您無需考量現實規章的上下限。',
        widget=widgets.RadioSelect
    )
    探索學分後續選擇 = models.FloatField(
        label='現在有兩位候選人正在競選T校學生會會長\n請想像自己身為 T校學生，選擇你支持的候選人\n＊注意：這不是真實的選舉，您無需考量現實規章的上下限。',
        widget=widgets.RadioSelect
    )
    候選人A_景觀法政見 = models.StringField()
    候選人B_景觀法政見 = models.StringField()
    A加文章 = models.LongStringField(label='')
    探索學分文章 = models.LongStringField(label='')
    
    論點1_說服力 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點1_邏輯性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點2_說服力 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點2_邏輯性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點3_說服力 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點3_邏輯性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點4_說服力 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點4_邏輯性 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點1_說服力2 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點1_邏輯性2 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點2_說服力2 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點2_邏輯性2 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點3_說服力2 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點3_邏輯性2 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點4_說服力2 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    論點4_邏輯性2 = models.IntegerField(choices=C.九階選項, widget=widgets.RadioSelectHorizontal)
    前測時間 = models.FloatField(blank=True, initial=0)
    看政見時間 = models.FloatField(blank=True, initial=0)
    寫作時間 = models.FloatField(blank=True, initial=0)
    看政見時間2 = models.FloatField(blank=True, initial=0)
    寫作時間2 = models.FloatField(blank=True, initial=0)
    論點1時間 = models.FloatField(blank=True, initial=0)
    論點2時間 = models.FloatField(blank=True, initial=0)
    論點3時間 = models.FloatField(blank=True, initial=0)
    論點4時間 = models.FloatField(blank=True, initial=0)
    論點1時間2 = models.FloatField(blank=True, initial=0)
    論點2時間2 = models.FloatField(blank=True, initial=0)
    論點3時間2 = models.FloatField(blank=True, initial=0)
    論點4時間2 = models.FloatField(blank=True, initial=0)
    後測時間 = models.FloatField(blank=True, initial=0)
    選擇理由1 = models.LongStringField(label='')
    選擇理由2 = models.LongStringField(label='')

class 前測(Page):
    form_model = 'player'
    form_fields = [
        '初始囤房稅', '初始囤房稅態度', '初始囤房稅重要性',
        '初始景觀同意門檻', '初始景觀法態度', '初始景觀法重要性',
        '初始A加比例', '初始A加限制態度', '初始A加限制重要性',
        '初始探索學分', '初始探索學分態度', '初始探索學分重要性','前測囤房稅測驗結果',
        '前測景觀法測驗結果',
        '前測探索學分測驗結果',
        '前測囤房稅錯誤次數', '前測景觀法錯誤次數', '前測A加錯誤次數', '前測探索學分錯誤次數',
        '前測A加測驗結果','前測時間'
    ]
class 後測(Page):
    form_model = 'player'
    form_fields = [
        '最終囤房稅', '最終囤房稅態度', '最終囤房稅重要性',
        '最終景觀同意門檻', '最終景觀法態度', '最終景觀法重要性',
        '最終A加比例', '最終A加限制態度', '最終A加限制重要性',
        '最終探索學分', '最終探索學分態度', '最終探索學分重要性','後測時間'
    ]

    @staticmethod
    def vars_for_template(player: Player):
        import time
        if 'start_time' in player.participant.vars:
            total_seconds = time.time() - player.participant.vars['start_time']
            player.總實驗時間 = total_seconds / 60  # 換算成分鐘存起來

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        正確題數 = 0
        
        if player.field_maybe_none('囤房稅測驗結果') == 1: 正確題數 += 1
        if player.field_maybe_none('景觀法測驗結果') == 1: 正確題數 += 1
        if player.field_maybe_none('探索學分測驗結果') == 1: 正確題數 += 1
        if player.field_maybe_none('A加測驗結果') == 1: 正確題數 += 1
  
        if player.field_maybe_none('前測囤房稅測驗結果') == 1: 正確題數 += 1
        if player.field_maybe_none('前測景觀法測驗結果') == 1: 正確題數 += 1
        if player.field_maybe_none('前測探索學分測驗結果') == 1: 正確題數 += 1
        if player.field_maybe_none('前測A加測驗結果') == 1: 正確題數 += 1

        總金額 = 150 + (正確題數 * 10)
 
        player.participant.vars['total_payment'] = 總金額
        player.payoff = 總金額

def get_tax_rates(player):
    if player.初始囤房稅 < 3.8:
        稅率一 = player.初始囤房稅 * (3/4)
        稅率二 = player.初始囤房稅 * (3/2)
    elif player.初始囤房稅 > 3.8:
        稅率一 = player.初始囤房稅 * (1/2)
        稅率二 = player.初始囤房稅 * (5/4)
    else:
        稅率一 = player.初始囤房稅 * (3/4)
        稅率二 = player.初始囤房稅 * (3/2)
            
    低稅率 = round(min(稅率一, 稅率二), 2)
    高稅率 = round(max(稅率一, 稅率二), 2)
    return 低稅率, 高稅率

def get_renewal_rates(player):
    if player.初始景觀同意門檻 < 90:
        門檻一 = player.初始景觀同意門檻 + ((100 - player.初始景觀同意門檻) * (0.5))
        門檻二 = player.初始景觀同意門檻 - ((100 - player.初始景觀同意門檻) * (0.25))
    elif player.初始景觀同意門檻 > 90:
        門檻一 = player.初始景觀同意門檻 + ((100 - player.初始景觀同意門檻) * (0.25))
        門檻二 = player.初始景觀同意門檻 - ((100 - player.初始景觀同意門檻) * (0.5))
    else:
        門檻一 = player.初始景觀同意門檻 + ((100 - player.初始景觀同意門檻) * (0.5))
        門檻二 = player.初始景觀同意門檻 - ((100 - player.初始景觀同意門檻) * (0.25))

    if 門檻二 < 0:
        門檻二 = 0  
    低門檻 = round(min(門檻一, 門檻二), 2)
    高門檻 = round(max(門檻一, 門檻二), 2)
    return 低門檻, 高門檻

def get_credit(player):
    if player.初始探索學分 < 6:
        學分一 = player.初始探索學分 * (3/4)
        學分二 = player.初始探索學分 * (3/2)
    elif player.初始探索學分 > 6:
        學分一 = player.初始探索學分 * (1/2)
        學分二 = player.初始探索學分 * (5/4)
    else:
       
        學分一 = player.初始探索學分 * (3/4)
        學分二 = player.初始探索學分 * (3/2)
 

    低學分 = int(round(min(學分一, 學分二)))
    高學分 = int(round(max(學分一, 學分二)))
    return 低學分, 高學分

def get_a_plus_rates(player):
    if player.初始A加比例 < 31:
        比例一 = player.初始A加比例 + ((player.初始A加比例) * (0.5))
        比例二 = player.初始A加比例 - ((player.初始A加比例) * (0.25))
    elif player.初始A加比例 > 31:
        比例一 = player.初始A加比例 + ((player.初始A加比例) * (0.25))
        比例二 = player.初始A加比例 - ((player.初始A加比例) * (0.5))
    else:

        比例一 = player.初始A加比例 + ((player.初始A加比例) * (0.5))
        比例二 = player.初始A加比例 - ((player.初始A加比例) * (0.25))
        
    if 比例一 > 100:
        比例一 = 100
    低比例 = round(min(比例一, 比例二), 2)
    高比例 = round(max(比例一, 比例二), 2)
    return 低比例, 高比例


# =========================================================
# 囤房稅區塊
# =========================================================
class 選舉情境介紹(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'

class 候選人政見(Page):
    form_model = 'player'
    form_fields = ['看政見時間']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
    @staticmethod
    def vars_for_template(player: Player):
        低稅率, 高稅率 = get_tax_rates(player)
        return dict(候選人A_稅率=低稅率, 候選人B_稅率=高稅率)

class 候選人測驗(Page):
    form_model = 'player'
    form_fields = ['囤房稅測驗結果','囤房稅錯誤次數']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
    @staticmethod
    def vars_for_template(player: Player):
        低稅率, 高稅率 = get_tax_rates(player)
        return dict(候選人A_稅率=低稅率, 候選人B_稅率=高稅率)

class 投票選擇(Page):
    form_model = 'player'
    form_fields = ['囤房稅後續選擇','選擇理由1']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
    @staticmethod
    def vars_for_template(player: Player):
        低稅率, 高稅率 = get_tax_rates(player)
        return dict(候選人A_稅率=低稅率, 候選人B_稅率=高稅率)
    

# =========================================================
# 景觀法區塊
# =========================================================
class 景觀法選舉情境介紹(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'

class 景觀法候選人政見(Page):
    form_model = 'player'
    form_fields = ['看政見時間']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
    @staticmethod
    def vars_for_template(player: Player):
        低門檻, 高門檻 = get_renewal_rates(player)
        return dict(候選人A_門檻=低門檻, 候選人B_門檻=高門檻)

class 景觀法候選人測驗(Page):
    form_model = 'player'
    form_fields = ['景觀法測驗結果','景觀法錯誤次數']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
    @staticmethod
    def vars_for_template(player: Player):
        低門檻, 高門檻 = get_renewal_rates(player)
        return dict(候選人A_門檻=低門檻, 候選人B_門檻=高門檻)

class 景觀法投票選擇(Page):
    form_model = 'player'
    form_fields = ['景觀法後續選擇','選擇理由1']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
    @staticmethod
    def vars_for_template(player: Player):
        低門檻, 高門檻 = get_renewal_rates(player)
        return dict(候選人A_門檻=低門檻, 候選人B_門檻=高門檻)


# =========================================================
# A加區塊
# =========================================================
class A加選舉情境介紹(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'

class A加候選人政見(Page):
    form_model = 'player'
    form_fields = ['看政見時間2']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
    @staticmethod
    def vars_for_template(player: Player):
        低比例, 高比例 = get_a_plus_rates(player)
        return dict(候選人A_比例=低比例, 候選人B_比例=高比例)

class A加候選人測驗(Page):
    form_model = 'player'
    form_fields = ['A加測驗結果','A加錯誤次數']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
    @staticmethod
    def vars_for_template(player: Player):
        低比例, 高比例 = get_a_plus_rates(player)
        return dict(候選人A_比例=低比例, 候選人B_比例=高比例)

class A加投票選擇(Page):
    form_model = 'player'
    form_fields = ['A加後續選擇','選擇理由2']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
    @staticmethod
    def vars_for_template(player: Player):
        低比例, 高比例 = get_a_plus_rates(player)
        return dict(候選人A_比例=低比例, 候選人B_比例=高比例)


# =========================================================
# 探索學分區塊
# =========================================================
class 探索學分選舉情境介紹(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'

class 探索學分候選人政見(Page):
    form_model = 'player'
    form_fields = ['看政見時間2']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
    @staticmethod
    def vars_for_template(player: Player):
        低學分, 高學分 = get_credit(player)
        return dict(候選人A_學分=低學分, 候選人B_學分=高學分)

class 探索學分候選人測驗(Page):
    form_model = 'player'
    form_fields = ['探索學分測驗結果', '探索學分錯誤次數']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
    @staticmethod
    def vars_for_template(player: Player):
        低學分, 高學分 = get_credit(player)
        return dict(候選人A_學分=低學分, 候選人B_學分=高學分)

class 探索學分投票選擇(Page):
    form_model = 'player'
    form_fields = ['探索學分後續選擇', '選擇理由2']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
    @staticmethod
    def vars_for_template(player: Player):
        低學分, 高學分 = get_credit(player)
        return dict(候選人A_學分=低學分, 候選人B_學分=高學分)
    

class 階段等(Page):
    pass
   
class 囤房稅介紹(Page):
    pass

class 景觀法介紹(Page):
    pass

class A加限制介紹(Page):
    pass

class 探索學分介紹(Page):
    pass

class 第一階段介紹(Page):
    @staticmethod
    def vars_for_template(player: Player):
        if 'start_time' not in player.participant.vars:
            player.participant.vars['start_time'] = time.time()

class 第四階段介紹(Page):
    pass

class 模擬選舉說明(Page):
    pass

class 囤房稅選項頁面(Page):
    form_model = 'player'
    form_fields = ['囤房稅後續選擇']
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'

class 囤房稅寫作(Page):
    form_model = 'player'
    form_fields = ['辯護文章','寫作時間']
    timeout_seconds = 600
    
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
        
    @staticmethod
    def vars_for_template(player: Player):
        低稅率, 高稅率 = get_tax_rates(player)
        
        if player.囤房稅後續選擇 == 低稅率:
            支持的候選人 = "候選人A"
        else:
            支持的候選人 = "候選人B"
            
        return dict(
            選擇的稅率=player.囤房稅後續選擇,
            支持的候選人=支持的候選人
        )

    @staticmethod
    def error_message(player: Player, values):
        if len(values['辯護文章']) < 70:
            return '您的辯護文章字數不足，請至少輸入70個字！'

class 景觀法寫作(Page):
    form_model = 'player'
    form_fields = ['景觀法文章','寫作時間']
    timeout_seconds = 600
    
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
        
    @staticmethod
    def vars_for_template(player: Player):
        低門檻, 高門檻 = get_renewal_rates(player)
        
        if player.景觀法後續選擇 == 低門檻:
            支持的候選人 = "候選人A"
            支持的政見 = f"{低門檻}%同意門檻"
        else:
            支持的候選人 = "候選人B"
            支持的政見 = f"{高門檻}%同意門檻"
            
        return dict(
            支持的政見=支持的政見,
            支持的候選人=支持的候選人
        )
    @staticmethod
    def error_message(player: Player, values):
        if len(values['景觀法文章']) < 70:
            return '您的辯護文章字數不足，請至少輸入70個字！'

class A加寫作(Page):
    form_model = 'player'
    form_fields = ['A加文章','寫作時間2']
    timeout_seconds = 600
    
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '失調組'
        
    @staticmethod
    def vars_for_template(player: Player):
        低比例, 高比例 = get_a_plus_rates(player)
        
        if player.A加後續選擇 == 低比例:
            支持的候選人 = "候選人A"
            支持的政見 = f"{低比例}% A+ 比例"
        else:
            支持的候選人 = "候選人B"
            支持的政見 = f"{高比例}% A+ 比例"
            
        return dict(
            支持的政見=支持的政見,
            支持的候選人=支持的候選人
        )
    @staticmethod
    def error_message(player: Player, values):
        if len(values['A加文章']) < 70:
            return '您的辯護文章字數不足，請至少輸入70個字！'

class 探索學分寫作(Page):
    form_model = 'player'
    form_fields = ['探索學分文章','寫作時間2']
    timeout_seconds = 600
    
    @staticmethod
    def is_displayed(player: Player):
        return player.失調組別 == '中性組'
        
    @staticmethod
    def vars_for_template(player: Player):
        低學分, 高學分 = get_credit(player)
        
        if player.探索學分後續選擇 == 低學分:
            支持的候選人 = "候選人A"
            支持的政見 = f"{低學分}"
        else:
            支持的候選人 = "候選人B"
            支持的政見 = f"{高學分}"
            
        return dict(
            支持的政見=支持的政見,
            支持的候選人=支持的候選人
        )
    @staticmethod
    def error_message(player: Player, values):
        if len(values['探索學分文章']) < 70:
            return '您的辯護文章字數不足，請至少輸入70個字！'

class 動機性推理介紹(Page):
   pass

class 論點頁面一(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性', '論點1時間']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return dict(論點內容=C.論點列表[編號-1], 計時小抄='論點1時間')

class 論點頁面二(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性', '論點2時間']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return dict(論點內容=C.論點列表[編號-1], 計時小抄='論點2時間')

class 論點頁面三(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性', '論點3時間']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return dict(論點內容=C.論點列表[編號-1], 計時小抄='論點3時間')

class 論點頁面四(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性', '論點4時間']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return dict(論點內容=C.論點列表[編號-1], 計時小抄='論點4時間')
    
class 景觀論點頁面一(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性', '論點1時間']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return dict(論點內容=C.景觀論點列表[編號-1], 計時小抄='論點1時間')

class 景觀論點頁面二(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性', '論點2時間']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return dict(論點內容=C.景觀論點列表[編號-1], 計時小抄='論點2時間')

class 景觀論點頁面三(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性', '論點3時間']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return dict(論點內容=C.景觀論點列表[編號-1], 計時小抄='論點3時間')

class 景觀論點頁面四(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return [f'論點{編號}_說服力', f'論點{編號}_邏輯性', '論點4時間']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return dict(論點內容=C.景觀論點列表[編號-1], 計時小抄='論點4時間')
    
class 論點頁面一2(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分2.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return [f'論點{編號}_說服力2', f'論點{編號}_邏輯性2', '論點1時間2']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return dict(論點內容=C.論點列表2[編號-1], 計時小抄='論點1時間2')

class 論點頁面二2(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分2.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return [f'論點{編號}_說服力2', f'論點{編號}_邏輯性2', '論點2時間2']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return dict(論點內容=C.論點列表2[編號-1], 計時小抄='論點2時間2')

class 論點頁面三2(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分2.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return [f'論點{編號}_說服力2', f'論點{編號}_邏輯性2', '論點3時間2']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return dict(論點內容=C.論點列表2[編號-1], 計時小抄='論點3時間2')

class 論點頁面四2(Page):
    form_model = 'player'
    template_name = 'policy_exp/論點評分2.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '動機性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return [f'論點{編號}_說服力2', f'論點{編號}_邏輯性2', '論點4時間2']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return dict(論點內容=C.論點列表2[編號-1], 計時小抄='論點4時間2')
    
class 景觀論點頁面一2(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分2.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return [f'論點{編號}_說服力2', f'論點{編號}_邏輯性2', '論點1時間2']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][0]
        return dict(論點內容=C.景觀論點列表2[編號-1], 計時小抄='論點1時間2')

class 景觀論點頁面二2(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分2.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return [f'論點{編號}_說服力2', f'論點{編號}_邏輯性2', '論點2時間2']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][1]
        return dict(論點內容=C.景觀論點列表2[編號-1], 計時小抄='論點2時間2')

class 景觀論點頁面三2(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分2.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return [f'論點{編號}_說服力2', f'論點{編號}_邏輯性2', '論點3時間2']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][2]
        return dict(論點內容=C.景觀論點列表2[編號-1], 計時小抄='論點3時間2')

class 景觀論點頁面四2(Page):
    form_model = 'player'
    template_name = 'policy_exp/景觀論點評分2.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.推理組別 == '中性推理組'
    @staticmethod
    def get_form_fields(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return [f'論點{編號}_說服力2', f'論點{編號}_邏輯性2', '論點4時間2']
    @staticmethod
    def vars_for_template(player: Player):
        編號 = player.participant.vars['論點順序'][3]
        return dict(論點內容=C.景觀論點列表2[編號-1], 計時小抄='論點4時間2')



page_sequence = [
    第一階段介紹,前測,階段等,
    模擬選舉說明,選舉情境介紹,候選人政見,候選人測驗,投票選擇,囤房稅寫作, 
    景觀法選舉情境介紹,景觀法候選人政見,景觀法候選人測驗,景觀法投票選擇,景觀法寫作, 
    A加選舉情境介紹,A加候選人政見,A加候選人測驗,A加投票選擇,A加寫作,
    探索學分選舉情境介紹,探索學分候選人政見,探索學分候選人測驗,探索學分投票選擇,探索學分寫作,階段等,
    動機性推理介紹,論點頁面一,論點頁面二,論點頁面三,論點頁面四,
    景觀論點頁面一,景觀論點頁面二,景觀論點頁面三,景觀論點頁面四, 
    論點頁面一2,論點頁面二2,論點頁面三2,論點頁面四2,
    景觀論點頁面一2,景觀論點頁面二2,景觀論點頁面三2,景觀論點頁面四2,階段等,
    第四階段介紹,後測
]
