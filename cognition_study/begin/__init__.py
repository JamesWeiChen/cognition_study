from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'wait_start'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Player(BasePlayer):
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
class 等(Page):
    pass


class WaitStart(Page):
    form_model = None


page_sequence = [ WaitStart,Consent,等]