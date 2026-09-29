from os import environ

SESSION_CONFIGS = [
    dict(
        name='full_experiment',
        app_sequence=['begin', 'policy_exp','Stage_Payment_Info'],
        num_demo_participants=25,
        display_name='正式實驗:認知失調與動機性推理_隨機'
    ),

  
    dict(
        name='full_experiment_01',
        app_sequence=['begin', 'policy_exp','Stage_Payment_Info'],
        num_demo_participants=25,
        display_name='正式實驗:認知失調與動機性推理_A"B"',
        dissonance_1='中性組',
        reasoning_1='中性推理組',
     
    ),

  
    dict(
        name='full_experiment_02',
        app_sequence=['begin', 'policy_exp','Stage_Payment_Info'],
        num_demo_participants=25,
        display_name='正式實驗:認知失調與動機性推理_A"B',
        dissonance_1='中性組',
        reasoning_1='動機性推理組',
   
    ),

    dict(
        name='full_experiment_03',
        app_sequence=['begin', 'policy_exp','Stage_Payment_Info'],
        num_demo_participants=25,
        display_name='正式實驗:認知失調與動機性推理_AB"',
        dissonance_1='失調組',
        reasoning_1='中性推理組',
  
    ),

    dict(
        name='full_experiment_04',
        app_sequence=['begin', 'policy_exp','Stage_Payment_Info'],
        num_demo_participants=25,
        display_name='正式實驗:認知失調與動機性推理_AB',
        dissonance_1='失調組',
        reasoning_1='動機性推理組',
   
    ),


    dict(
        name='policy_exp_only',
        app_sequence=['policy_exp'],
        num_demo_participants=25,
        display_name='主實驗'
    ),
    

    dict(
        name='start',
        app_sequence=['Stage_Payment_Info'],
        num_demo_participants=25,
        display_name='開場'
    ),
    

]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = 'zh-hant'

REAL_WORLD_CURRENCY_CODE = 'TWD'
USE_POINTS = True
ROOMS = []

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
"""

SECRET_KEY = '6076730954186'

INSTALLED_APPS = ['otree']