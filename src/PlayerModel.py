# Copyright 2022 Dynamic Object Language Labs Inc.
# DISTRIBUTION STATEMENT C: U.S. Government agencies and their contractors.
# Other requests shall be referred to DARPA’s Public Release Center via email at prc@darpa.mil.
import sys
from pprint import pprint
import PlayerProfiler_Draft as player_profiler
import PlayerModelDynamic  as player_dynamic
import csv

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


#
def qid_defaults_from_csv(csv_f='player-profile-qid-defaults.csv'):
    qid_defaults = {}
    with open(csv_f) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pprint(row)
            qid = row['QID']
            val = float(row['Default Value'])
            qid_defaults[qid] = val

    pprint(qid_defaults)
    return qid_defaults


# qid_defaults_from_csv()
# qid_defaults created using qid_defaults_from_csv)_
qid_defaults = {'QID13_1': 5.502857143,
                'QID13_10': 3.508571429,
                'QID13_11': 3.281609195,
                'QID13_12': 2.350574713,
                'QID13_13': 3.482758621,
                'QID13_14': 4.457142857,
                'QID13_15': 2.754285714,
                'QID13_2': 3.44,
                'QID13_3': 5.098837209,
                'QID13_4': 5.402298851,
                'QID13_5': 4.165714286,
                'QID13_6': 3.782857143,
                'QID13_7': 4.908571429,
                'QID13_8': 2.534482759,
                'QID13_9': 5.218390805,
                'QID751': 3.0,
                'QID753': 2.0,
                'QID755': 3.0,
                'QID757': 2.0,
                'QID759': 2.0,
                'QID761': 2.0,
                'QID763': 2.0,
                'QID765': 1.0,
                'QID767': 4.0,
                'QID769': 1.0,
                'QID771': 2.0,
                'QID773': 3.0,
                'QID775': 2.0,
                'QID777': 1.0,
                'QID779': 1.0,
                'QID781': 2.0,
                'QID783': 2.0,
                'QID785': 1.0,
                'QID787': 2.0,
                'QID789': 2.0,
                'QID791': 2.0,
                'QID793': 1.0,
                'QID795': 4.0,
                'QID797': 1.0,
                'QID799': 4.0,
                'QID801': 3.0,
                'QID803': 2.0,
                'QID805': 1.0,
                'QID807': 1.0,
                'QID809': 2.0,
                'QID811': 2.0,
                'QID813': 1.0,
                'QID815': 4.0,
                'QID817': 3.0,
                'QID819': 2.0,
                'QID821': 3.0,
                'QID830_1': 3.508571429,
                'QID830_10': 4.017142857,
                'QID830_11': 4.354285714,
                'QID830_12': 4.494252874,
                'QID830_13': 3.542857143,
                'QID830_14': 3.634285714,
                'QID830_15': 3.417142857,
                'QID830_2': 3.622857143,
                'QID830_3': 3.451428571,
                'QID830_4': 3.497142857,
                'QID830_5': 3.551724138,
                'QID830_6': 3.88,
                'QID830_7': 4.28,
                'QID830_8': 4.274285714,
                'QID830_9': 4.195402299,
                'QID832_16': 3.417142857,
                'QID832_17': 3.534482759,
                'QID832_18': 3.811428571,
                'QID832_19': 3.337142857,
                'QID832_20': 3.24,
                'QID832_21': 3.925714286,
                'QID832_22': 3.683908046,
                'QID832_23': 3.068965517,
                'QID832_24': 3.108571429,
                'QID832_25': 2.645714286,
                'QID832_26': 1.885714286,
                'QID832_27': 1.6,
                'QID832_28': 2.794285714,
                'QID832_29': 1.874285714,
                'QID832_9': 3.925714286,
                'QID867_1': 14.09,
                'QID867_2': 11.58,
                'QID867_4': 8.08,
                'QID868_1': 7.0,
                'QID868_3': 7.0,
                'QID868_5': 7.0,
                'QID868_6': 6.0,
                'QID872_1': 74.29714286,
                'QID872_2': 70.40571429,
                'QID872_3': 76.94285714,
                'QID872_4': 80.41714286,
                'QID872_5': 79.94857143,
                'QID872_6': 77.48,
                'QID872_7': 92.85142857,
                'QID872_8': 80.44571429}

factor_windows = 180 * 1000  # every 180 seconds since the mission start,  we fire "end of 180 second loop" event

print('factor_windows = ', factor_windows)


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
        self.elapsed_time = -1  # -1 implies mission ended
        self.last_factor_window = -1
        # print('QID set', len(self.req_qid_set))

    def check_180_timeout(self):
        ret_data = False
        current_factor_window = (int)(self.elapsed_time / factor_windows)
        if current_factor_window != self.last_factor_window:
            if 0 < current_factor_window <= player_dynamic.max_index_180_timeout:
                print(
                    f'Handle 180 second timeout {self.last_factor_window} => {current_factor_window} @time {self.elapsed_time}')
                player_dynamic.handle_180_sec_timeout(self.players.values(), self.last_factor_window)
                ret_data = True
            self.last_factor_window = current_factor_window
        return ret_data

    def update_elapsed(self, elapsed_ms):
        if elapsed_ms == -1:
            # self.elapsed_time
            # print(f'update_elapsed given {elapsed_ms} => {self.elapsed_time}')
            return False
        if elapsed_ms > self.elapsed_time:
            self.elapsed_time = elapsed_ms
            return True
        delta = elapsed_ms - self.elapsed_time
        # for printing, tolerate delta of 30ms
        if abs(delta) > 30:
            print(f'Elapsed time not updated. prev {self.elapsed_time} => {elapsed_ms} {delta}')
        return False

    def handle_trial_start(self, client_info, exp_id, trial_id):
        print('Trial Start client info')
        pprint(client_info)
        for ci in client_info:
            participant_id = ci['participant_id']
            callsign = ci['callsign']
            role = None
            if callsign not in player_dynamic.role_lookup:
                print('Warn: We don\'t have role for call sign', callsign)
            else:
                role = player_dynamic.role_lookup[callsign]
            print(f'Got {participant_id}: {callsign} => {role}')
            if participant_id not in self.players:
                self.players[participant_id] = self.make_new_player(exp_id, trial_id)
            if trial_id not in self.players[participant_id]['trials']:
                self.players[participant_id]['trials'].append(trial_id)
            if 'callsign' in self.players[participant_id]:
                old = self.players[participant_id]['callsign']
                if old != callsign:
                    print(f'Player {participant_id} call sign changed: {old} -> {callsign}')
            self.players[participant_id]['callsign'] = callsign
            if 'role' in self.players[participant_id]:
                old = self.players['participant_id']['role']
                if old != role:
                    print(f'Player {participant_id} role changed: {old} -> {role}')
            self.players[participant_id]['role'] = role

    def make_new_player(self, exp_id, trial_id):
        return {'experiment_id': exp_id,
                'trials': [trial_id],
                'qid': {},
                'Motion_CurrentWindow': 0,
                'Transport_Current_DistanceTranslated': 0,
                'IsTransporting': False,
                'Medic_TriageSuccessful_Count_CurrentWindow': 0,
                'Medic_TriageSuccessful_Count_Total': 0,

                'Engineer_RubbleDestroyed_Count_CurrentWindow': 0,
                'Engineer_RubbleDestroyed_Count_Total': 0,

                'Transporter_Evacuations_Count_CurrentWindow': 0,
                'Transporter_Evacuations_Count_Total': 0,
                'Transporter_Evacuations_Critical_Count_CurrentWindow': 0,
                'Transporter_Evacuations_Critical_Count_Total': 0,
                'Transporter_Evacuations_Regular_Count_CurrentWindow': 0,
                'Transporter_Evacuations_Regular_Count_Total': 0,

                'Transports_Initiated_Count_CurrentWindow': 0,
                'Transports_Initiated_Count_Total': 0,
                'Transports_Completed_Count_CurrentWindow': 0,
                'Transports_Completed_Count_Total': 0,
                'Transport_Distances_CurrentWindow_List': [],
                'TaskPotential_StateAverages_List': [],
                'TaskPotential_Categorization_LastWindow': None,
                'TaskPotential_StateAverage_LastWindow': 0,
                'TaskPotential_Factors_List': []
                }

    def handle_survey_values(self, vals, exp_id, trial_id):
        participant_id = vals['participantid']
        print('\nsurvey for participant', participant_id)
        if participant_id not in self.players:
            print('Error: handle_survey_values participant_id not found:', participant_id)
            pprint(vals)
            self.players[participant_id] = self.make_new_player(exp_id, trial_id)

        if trial_id not in self.players[participant_id]['trials']:
            print('Error: handle_survey_values trial_id not found:', trial_id)
            pprint(vals)
            self.players[participant_id]['trials'].append(trial_id)

        added_defaults = self.add_default_qid_vals(vals)
        collected = self.collect_qid_vals(participant_id, added_defaults)
        have_all = self.have_all_qids(participant_id)

        player_profile = None
        if collected and have_all:
            print('Compute and publish player profile message')
            player_profile = self.compute_player_profile(participant_id)
            print('Publish Player Profile')
            pprint(player_profile)
        # else:
        #     print('not new data or enough data \n\tcollected any:', collected, '\n\thave all qid vals:', have_all)
        # print()
        return {'collected': collected, 'have_all': have_all, 'player_profile': player_profile}

    # for missing qid vals, we add defaults and return new map
    def add_default_qid_vals(self, vals):
        all_qid = {}
        added = {}
        for qid in self.req_qid_set:
            if qid not in vals:
                if qid in qid_defaults:
                    all_qid[qid] = qid_defaults[qid]
                    added[qid] = qid_defaults[qid]
                else:
                    print(f'Error: Required {qid} not found in vals and qid_defaults')
            else:
                all_qid[qid] = vals[qid]

        if len(added) > 0:
            print('Added missing qid vals from survey', len(added))
            pprint(added)
        return all_qid

    def handle_player_profile(self, player_profile):
        # pprint(player_profile)
        pid = player_profile['participant_id']
        if pid not in self.players:
            print(f'Error: handle_player_profile got {pid} but not found in players')
            pprint(player_profile)
            return
        player_dynamic.init_from_player_profile(self.players[pid], player_profile)

    def handle_event_triage(self, dat, exp_id, trial_id):
        # print(f'handle event triage {trial_id}')
        pid = dat['participant_id']
        if pid not in self.players:
            print(f'Error: handle_player_profile got {pid} but not found in players')
            pprint(dat)
            return
        player_dynamic.handle_triage_event(self.players[pid], pid, dat)

    def handle_rubble_destroyed(self, dat, exp_id, trial_id):
        # print(f'handle rubble destroyed {trial_id}')
        pid = dat['participant_id']
        if pid not in self.players:
            print(f'Error: handle_rubble_destroyed got {pid} but not found in players')
            pprint(dat)
            return
        player_dynamic.handle_rubble_destroyed(self.players[pid], pid)

    def handle_victim_evacuated(self, dat, exp_id, trial_id):
        # print(f'handle victim evacuated {trial_id}')
        pid = dat['participant_id']
        if pid not in self.players:
            print(f'Error: handle_victim_evacuated got {pid} but not found in players')
            pprint(dat)
            return
        player_dynamic.handle_victim_evacuated(self.players[pid], pid, dat)

    def handle_victim_picked_up(self, dat, exp_id, trial_id):
        # print(f'handle victim picked up {trial_id}')
        pid = dat['participant_id']
        if pid not in self.players:
            print(f'Error: handle_victim_picked_up got {pid} but not found in players')
            pprint(dat)
            return
        player_dynamic.handle_victim_picked_up(self.players[pid], pid, dat)

    def handle_victim_placed(self, dat, exp_id, trial_id):
        # print(f'handle victim placed {trial_id}')
        pid = dat['participant_id']
        if pid not in self.players:
            print(f'Error: handle_victim_placed got {pid} but not found in players')
            pprint(dat)
            return
        player_dynamic.handle_victim_placed(self.players[pid], pid, dat)

    def handle_obs_state(self, dat, exp_id, trial_id):
        # pprint(f'handle observation state {trial_id}')
        pid = dat['participant_id']
        if pid not in self.players:
            print(f'Error: handle_obs_state got {pid} but not found in players')
            pprint(dat)
            return
        player_dynamic.handle_obs_state(self.players[pid], pid, dat)

    def compute_player_profile(self, participant_id):
        converted = self.convert_quid_to_internal(participant_id)
        # pprint(converted)
        sbsod_score = player_profiler.get_SBSOD_SCORE(converted['sbsod'])
        vgem_score = player_profiler.get_vgem_score(converted['vgem'])
        sc_score = player_profiler.get_PsychologicalCollectivism_Score(converted['psychologicalcollectivism'])
        social_dominance_score = player_profiler.get_SociableDominance_Score(converted['sociabledominance'])
        rmet_score = player_profiler.get_rmet_score(converted['rmet'])
        print('sbsod score', sbsod_score)
        print('vgem score', vgem_score)
        print('psychological collectivism score', sc_score)
        print('sociable dominance score', social_dominance_score)
        print('rmet score', rmet_score)
        player_profile = player_profiler.compute_player_profile(sbsod_score, vgem_score, sc_score,
                                                                rmet_score, social_dominance_score)
        player_profile['participant_id'] = participant_id
        player_profile['callsign'] = 'not_available'
        player_profile['role'] = 'not_available'
        if 'callsign' in self.players[participant_id]:
            player_profile['callsign'] = self.players[participant_id]['callsign']
        if 'role' in self.players[participant_id]:
            player_profile['role'] = self.players[participant_id]['role']
        return player_profile

    def collect_qid_vals(self, participant_id, vals):
        # print('collect qid vals')
        # pprint(vals)
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
        needed = self.req_qid_set - have
        if 0 == len(needed):
            return True
        print('qid expected, have', participant_id, len(self.req_qid_set), len(have))
        print('Needed qid', needed)
        return False

    def convert_quid_to_internal(self, participant_id):
        converted = {}
        for k, vals in player.items():
            converted[k] = {}
            for k1, qid in vals.items():
                qval = self.players[participant_id]['qid'][qid]
                converted[k][k1] = qval
        return converted

    def print_player_state(self):
        for p in self.players.items():
            pprint(p)

    def handle_mission_state(self, msg):
        # pprint(msg)
        state = msg['data']['mission_state']
        elapsed = msg['data']['elapsed_milliseconds']
        print(f'Mission State {state} Elapsed ms {self.elapsed_time} => {elapsed}')
        self.elapsed_time = elapsed  # -1 implies mission ended


playerstate = PlayerState()

# def initPlayerState():
#     global playerstate
#     if playerstate is not None:
#         print('Player state is not None: Reiniting')
#     playerstate = PlayerState()
