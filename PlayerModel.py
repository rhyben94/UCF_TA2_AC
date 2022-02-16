# Copyright 2022 Dynamic Object Language Labs Inc.
# DISTRIBUTION STATEMENT C: U.S. Government agencies and their contractors.
# Other requests shall be referred to DARPA’s Public Release Center via email at prc@darpa.mil.

from pprint import pprint

# player = {'sbsod': [f'SBSOD_{x}' for x in range(1, 16)]}
# vgem = {f'VGEM_{x}': 'QID8_' for x in range(1, 16)}
# pprint(vgem)
# PsychologicalCollectivism = {f'PsychologicalCollectivism_{x}': f'QID830_{x}' for x in range(1, 16)}
# pprint(PsychologicalCollectivism)
# SociableDominance = {f'SociableDominance_{x}': f'QID832_{x + 14}' for x in range(1, 16)}
# pprint(SociableDominance)
# rmet_qid = [x for x in range(751, 822, 2)]
# print(rmet_qid)
# rmet = {f'RMET_{x}': f'QID{rmet_qid[x - 1]}' for x in range(1, 37)}
# pprint(rmet)

# Required keys
# Created mappings using template code above and manually updated as needed.
player = {'sbsod':
              {'SBSOD_1': 'QID13_1',
               'SBSOD_2': 'QID13_2',
               'SBSOD_3': 'QID13_3',
               'SBSOD_4': 'QID13_4',
               'SBSOD_5': 'QID13_5',
               'SBSOD_6': 'QID13_6',
               'SBSOD_7': 'QID13_7',
               'SBSOD_8': 'QID13_8',
               'SBSOD_9': 'QID13_9',
               'SBSOD_10': 'QID13_10',
               'SBSOD_11': 'QID13_11',
               'SBSOD_12': 'QID13_12',
               'SBSOD_13': 'QID13_13',
               'SBSOD_14': 'QID13_14',
               'SBSOD_15': 'QID13_15'},

          'vgem': {'VGEM_1': 'QID867_1',
                   'VGEM_2': 'QID867_2',
                   'VGEM_3': 'QID867_4',

                   'VGEM_4': 'QID868_1',
                   'VGEM_5': 'QID868_3',
                   'VGEM_6': 'QID868_5',
                   'VGEM_7': 'QID868_6',

                   'VGEM_8': 'QID872_1',
                   'VGEM_9': 'QID872_2',
                   'VGEM_10': 'QID872_3',
                   'VGEM_11': 'QID872_4',
                   'VGEM_12': 'QID872_5',
                   'VGEM_13': 'QID872_6',
                   'VGEM_14': 'QID872_7',
                   'VGEM_15': 'QID872_8'},

          'psychologicalcollectivism': {'PsychologicalCollectivism_1': 'QID830_1',
                                        'PsychologicalCollectivism_2': 'QID830_2',
                                        'PsychologicalCollectivism_3': 'QID830_3',
                                        'PsychologicalCollectivism_4': 'QID830_4',
                                        'PsychologicalCollectivism_5': 'QID830_5',
                                        'PsychologicalCollectivism_6': 'QID830_6',
                                        'PsychologicalCollectivism_7': 'QID830_7',
                                        'PsychologicalCollectivism_8': 'QID830_8',
                                        'PsychologicalCollectivism_9': 'QID830_9',
                                        'PsychologicalCollectivism_10': 'QID830_10',
                                        'PsychologicalCollectivism_11': 'QID830_11',
                                        'PsychologicalCollectivism_12': 'QID830_12',
                                        'PsychologicalCollectivism_13': 'QID830_13',
                                        'PsychologicalCollectivism_14': 'QID830_14',
                                        'PsychologicalCollectivism_15': 'QID830_15', },

          'sociabledominance': {'SociableDominance_1': 'QID832_9',
                                'SociableDominance_2': 'QID832_16',
                                'SociableDominance_3': 'QID832_17',
                                'SociableDominance_4': 'QID832_18',
                                'SociableDominance_5': 'QID832_19',
                                'SociableDominance_6': 'QID832_20',
                                'SociableDominance_7': 'QID832_21',
                                'SociableDominance_8': 'QID832_22',
                                'SociableDominance_9': 'QID832_23',
                                'SociableDominance_10': 'QID832_24',
                                'SociableDominance_11': 'QID832_25',
                                'SociableDominance_12': 'QID832_26',
                                'SociableDominance_13': 'QID832_27',
                                'SociableDominance_14': 'QID832_28',
                                'SociableDominance_15': 'QID832_29'},
          'rmet': {'RMET_1': 'QID751',
                   'RMET_2': 'QID753',
                   'RMET_3': 'QID755',
                   'RMET_4': 'QID757',
                   'RMET_5': 'QID759',
                   'RMET_6': 'QID761',
                   'RMET_7': 'QID763',
                   'RMET_8': 'QID765',
                   'RMET_9': 'QID767',
                   'RMET_10': 'QID769',

                   'RMET_11': 'QID771',
                   'RMET_12': 'QID773',
                   'RMET_13': 'QID775',
                   'RMET_14': 'QID777',
                   'RMET_15': 'QID779',
                   'RMET_16': 'QID781',
                   'RMET_17': 'QID783',
                   'RMET_18': 'QID785',
                   'RMET_19': 'QID787',
                   'RMET_20': 'QID789',

                   'RMET_21': 'QID791',
                   'RMET_22': 'QID793',
                   'RMET_23': 'QID795',
                   'RMET_24': 'QID797',
                   'RMET_25': 'QID799',
                   'RMET_26': 'QID801',
                   'RMET_27': 'QID803',
                   'RMET_28': 'QID805',
                   'RMET_29': 'QID807',
                   'RMET_30': 'QID809',

                   'RMET_31': 'QID811',
                   'RMET_32': 'QID813',
                   'RMET_33': 'QID815',
                   'RMET_34': 'QID817',
                   'RMET_35': 'QID819',
                   'RMET_36': 'QID821'
                   }}


def get_required_qids():
    qid_set = set()
    for vals_parent in player.values():
        for val in vals_parent.values():
            qid_set.add(val)
    return qid_set


class PlayerState:
    def __init__(self):
        self.players = {}
        self.req_qid_set = get_required_qids()
        print('QID set', len(self.req_qid_set))

    def handle_survey_values(self, vals, exp_id, trial_id):
        participant_id = vals['participantid']
        print('for participant', participant_id)
        if participant_id not in self.players:
            self.players[participant_id] = {'experiment_id': exp_id,
                                            'trials': [],
                                            'qid': {}}

        if trial_id not in self.players[participant_id]['trials']:
            self.players[participant_id]['trials'].append(trial_id)

        collected = self.collect_qid_vals(participant_id, vals)
        have_all = self.have_all_qids(participant_id)

        if collected and have_all:
            print('Compute and publish player profile message')
        else:
            print('collected any:', collected, '\nhave all qids:', have_all)

        print()

    def collect_qid_vals(self, participant_id, vals):
        collected = False
        for k, v in vals.items():
            if k.startswith('QID') and k in self.req_qid_set:

                if k not in self.players[participant_id]['qid']:
                    collected = True
                    self.players[participant_id]['qid'][k] = v
                else:  # qud val update
                    old = self.players[participant_id]['qid'][k]
                    if old != v:
                        print('WARN: overriding previous QID',
                              self.players[participant_id]['experiment_id'],
                              self.players[participant_id]['trials'],
                              participant_id, k, 'old: ', old, 'new: ', v)
                        collected = True
                        self.players[participant_id]['qid'][k] = v
        return collected

    def have_all_qids(self, participant_id):
        have = set().union(self.players[participant_id]['qid'].keys())
        # print('qid expected, have', participant_id, len(self.req_qid_set), len(have))
        needed = self.req_qid_set - have
        # print('Needed qid', needed)
        if 0 == len(needed):
            return True
        return False


playerstate = PlayerState()

# def initPlayerState():
#     global playerstate
#     if playerstate is not None:
#         print('Player state is not None: Reiniting')
#     playerstate = PlayerState()
