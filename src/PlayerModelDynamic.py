# Ref https://docs.google.com/presentation/d/1Z1QMkGs2D6fZSxsZO9CM2bFzGYzZaVbjTieoUenhQho/edit#slide=id.g117addec6ce_0_45
import math
from pprint import pprint

role_lookup = {'Red': 'medic',
               'Blue': 'engineer',
               'Green': 'transporter'}

TaskPotential_LowModifier = 0
TaskPotential_HighModifier = 3

Medic_TaskPotential_RecategorizationThresholds_High_List = [4, 4, 4, 5, 5]
Medic_TaskPotential_RecategorizationThresholds_Low_List = [-1, 0, 1, 1, 2]

Engineer_TaskPotential_RecategorizationThresholds_High_List = [4, 4, 4, 5, 5]
Engineer_TaskPotential_RecategorizationThresholds_Low_List = [-1, 0, 1, 1, 2]

Transporter_TaskPotential_RecategorizationThresholds_High_List = [4, 4, 4, 5, 5]
Transporter_TaskPotential_RecategorizationThresholds_Low_List = [-1, 0, 1, 1, 2]

Medic_TaskPotential_RealTime_Factors_Coefficient = 1
Engineer_TaskPotential_RealTime_Factors_Coefficient = 1
Transporter_TaskPotential_RealTime_Factors_Coefficient = 1

Medic_FactorCoefficient_1 = 5
Medic_FactorCoefficient_2 = 10
Medic_FactorCoefficient_3 = 1
Medic_FactorCoefficient_4 = 2
Medic_FactorCoefficient_5 = 10

Engineer_FactorCoefficient_1 = 10
Engineer_FactorCoefficient_2 = 3
Engineer_FactorCoefficient_3 = 6
Engineer_FactorCoefficient_4 = 2
Engineer_FactorCoefficient_5 = 6

Transporter_FactorCoefficient_1 = 5
Transporter_FactorCoefficient_2 = 10
Transporter_FactorCoefficient_3 = 3
Transporter_FactorCoefficient_4 = 2
Transporter_FactorCoefficient_5 = 2

Medic_TriageSuccessful_UpperThreshold_List = [2, 3, 4, 5, 5]
Medic_TriageSuccessful_LowerThreshold_List = [0, 1, 1, 1, 1]

Medic_TriageSuccessful_to_MovementRatio_UpperThreshold_List = [2 / 300, 2 / 300, 3 / 300, 3 / 300, 4 / 300]
Medic_TriageSuccessful_to_MovementRatio_LowerThreshold_List = [2 / 600, 2 / 600, 3 / 700, 3 / 700, 4 / 800]

Medic_Transport_Distance_Average_UpperThreshold_List = [.5, .5, .5, .5, .5]
Medic_Transport_Distance_Average_LowerThreshold_List = [.1, .1, .1, .1, .1]

Medic_TriageSuccessful_to_Transports_ratio_UpperThreshold_List = [1.75, 1.75, 2, 2, 2]
Medic_TriageSuccessful_to_Transports_ratio_LowerThreshold_List = [.75, .75, .75, .75, .75]

Medic_Transports_Completed_Count_UpperThreshold_List = [2, 2, 2, 2, 2]
Medic_Transports_Completed_Count_LowerThreshold_List = [0, 0, 0, 0, 0]

Engineer_RubbleDestroyed_Count_UpperThreshold_List = [4, 8, 8, 8, 8]
Engineer_RubbleDestroyed_Count_LowerThreshold_List = [0, 2, 2, 2, 2]

Engineer_RubbleDestroyed_to_MovementRatio_UpperThreshold_List = [6 / 300, 8 / 300, 8 / 300, 8 / 300, 8 / 300]
Engineer_RubbleDestroyedMovementRatio_LowerThreshold_List = [6 / 400, 8 / 600, 8 / 600, 8 / 300, 8 / 600]

Engineer_Transport_Distance_Average_UpperThreshold_List = [.5, .5, .5, .5, .5]
Engineer_Transport_Distance_Average_LowerThreshold_List = [.1, .1, .1, .1, .1]

Engineer_Transports_Completed_Count_UpperThreshold_List = [3, 3, 3, 3, 3]
Engineer_Transports_Completed_Count_LowerThreshold_List = [0, 1, 1, 1, 1]

Engineer_Rubble_to_Transports_ratio_UpperThreshold_List = [3, 3, 4, 4, 4]
Engineer_Rubble_to_Transports_ratio_LowerThreshold_List = [1, 1, .75, .75, .75]

Transporter_Evacuations_Regular_Count_UpperThreshold_List = [3, 3, 4, 4, 4]
Transporter_Evacuations_Regular_Count_LowerThreshold_List = [0, 1, 1, 1, 1]

Transporter_Evacuations_Critical_Count_UpperThreshold_List = [1, 1, 2, 2, 2]
Transporter_Evacuations_Critical_Count_LowerThreshold_List = [0, 0, 1, 1, 1]

Transporter_Transport_Distance_Average_UpperThreshold_List = [4, 6, 6, 6, 6]
Transporter_Transport_Distance_Average_LowerThreshold_List = [1, 1, 1, 1, 1]

Transporter_Transport_to_Evacuation_ratio_UpperThreshold_List = [.5, .5, 1, 1, 1]
Transporter_Transport_to_Evacuation_ratio_LowerThreshold_List = [.1, .1, .1, .1, .1]

Transporter_Transports_Completed_Count_UpperThreshold_List = [4, 4, 6, 6, 6]
Transporter_Transports_Completed_Count_LowerThreshold_List = [1, 1, 1, 1, 1]


def init_from_player_profile(player_info, player_profile):
    # print('Player Info')
    # pprint(player_info)
    # print('Player Profile')
    # pprint(player_profile)

    # Step 1
    player_info['TaskPotential_Start'] = player_profile['task-potential-category']

    # Step 2
    if player_info['TaskPotential_Start'] == 'HighTask':
        player_info['TaskPotential_BaseModifier'] = TaskPotential_HighModifier
    else:
        player_info['TaskPotential_BaseModifier'] = TaskPotential_LowModifier


def handle_triage_event(player_info, pid, triage):
    role = player_info['role']
    callsign = player_info['callsign']
    tstate = triage['triage_state']
    by_medic = False
    if role != 'medic':
        print(f'Warn: Triage pid: {pid} {callsign} {role} {tstate} by medic? {by_medic}')
    if role == 'medic' and tstate == 'SUCCESSFUL':
        if 'Medic_TriageSuccessful_Count_CurrentWindow' not in player_info:
            player_info['Medic_TriageSuccessful_Count_CurrentWindow'] = 0
        if 'Medic_TriageSuccessful_Count_Total' not in player_info:
            player_info['Medic_TriageSuccessful_Count_Total'] = 0

        player_info['Medic_TriageSuccessful_Count_CurrentWindow'] += 1
        player_info['Medic_TriageSuccessful_Count_Total'] += 1


def handle_rubble_destroyed(player_info, pid):
    role = player_info['role']
    callsign = player_info['callsign']
    by_engg = False
    if role != 'engineer':
        print(f'Warn: Rubble destroyed pid: {pid} {callsign} {role} by engineer? {by_engg}')
    else:
        if 'Engineer_RubbleDestroyed_Count_CurrentWindow' not in player_info:
            player_info['Engineer_RubbleDestroyed_Count_CurrentWindow'] = 0
        if 'Engineer_RubbleDestroyed_Count_Total' not in player_info:
            player_info['Engineer_RubbleDestroyed_Count_Total'] = 0

        player_info['Engineer_RubbleDestroyed_Count_CurrentWindow'] += 1
        player_info['Engineer_RubbleDestroyed_Count_Total'] += 1


def handle_victim_evacuated(player_info, pid, dat):
    role = player_info['role']
    callsign = player_info['callsign']
    by_transporter = False
    victim_type = dat['type']
    if role != 'transporter':
        print(
            f'Check: Victim evacuated pid: {pid} {callsign} {role} victim_type {victim_type} by transporter? {by_transporter}')
    else:
        if 'Transporter_Evacuations_Count_CurrentWindow' not in player_info:
            player_info['Transporter_Evacuations_Count_CurrentWindow'] = 0
        if 'Transporter_Evacuations_Count_Total' not in player_info:
            player_info['Transporter_Evacuations_Count_Total'] = 0

        if 'Transporter_Evacuations_Critical_Count_CurrentWindow' not in player_info:
            player_info['Transporter_Evacuations_Critical_Count_CurrentWindow'] = 0
        if 'Transporter_Evacuations_Critical_Count_Total' not in player_info:
            player_info['Transporter_Evacuations_Critical_Count_Total'] = 0

        if 'Transporter_Evacuations_Regular_Count_CurrentWindow' not in player_info:
            player_info['Transporter_Evacuations_Regular_Count_CurrentWindow'] = 0
        if 'Transporter_Evacuations_Regular_Count_Total' not in player_info:
            player_info['Transporter_Evacuations_Regular_Count_Total'] = 0

        player_info['Transporter_Evacuations_Count_CurrentWindow'] += 1
        player_info['Transporter_Evacuations_Count_Total'] += 1

        if victim_type == 'victim_saved_c':
            player_info['Transporter_Evacuations_Critical_Count_CurrentWindow'] += 1
            player_info['Transporter_Evacuations_Critical_Count_Total'] += 1
        else:
            player_info['Transporter_Evacuations_Regular_Count_CurrentWindow'] += 1
            player_info['Transporter_Evacuations_Regular_Count_Total'] += 1


def handle_victim_picked_up(player_info, pid, dat):
    if 'Transports_Initiated_Count_CurrentWindow' not in player_info:
        player_info['Transports_Initiated_Count_CurrentWindow'] = 0
    if 'Transports_Initiated_Count_Total' not in player_info:
        player_info['Transports_Initiated_Count_Total'] = 0

    player_info['IsTransporting'] = True
    player_info['Transports_Initiated_Count_CurrentWindow'] += 1
    player_info['Transports_Initiated_Count_Total'] += 1
    player_info['Transport_Current_VictimID'] = dat['victim_id']
    player_info['Transport_Current_PickupLocation'] = [dat['victim_x'], dat['victim_z']]


def handle_victim_placed(player_info, pid, dat):
    if 'Transports_Completed_Count_CurrentWindow' not in player_info:
        player_info['Transports_Completed_Count_CurrentWindow'] = 0
    if 'Transports_Completed_Count_Total' not in player_info:
        player_info['Transports_Completed_Count_Total'] = 0
    if 'Transport_Distances_CurrentWindow_List' not in player_info:
        player_info['Transport_Distances_CurrentWindow_List'] = []

    player_info['IsTransporting'] = False
    player_info['Transports_Completed_Count_CurrentWindow'] += 1
    player_info['Transports_Completed_Count_Total'] += 1
    player_info['Transport_Current_VictimID'] = []
    player_info['Transport_Current_DropoffLocation'] = [dat['victim_x'], dat['victim_z']]

    player_info['Transport_Distances_CurrentWindow_List'].append(player_info['Transport_Current_DistanceTranslated'])
    player_info['Transport_Current_DistanceTranslated'] = 0


def handle_obs_state(player_info, pid, dat):
    if 'Motion_CurrentWindow' not in player_info:
        player_info['Motion_CurrentWindow'] = 0
    if 'Transport_Current_DistanceTranslated' not in player_info:
        player_info['Transport_Current_DistanceTranslated'] = 0
    if 'IsTransporting' not in player_info:
        player_info['IsTransporting'] = False

    mx = dat['motion_x']
    mz = dat['motion_z']
    player_info['Motion_CurrentWindow'] = player_info['Motion_CurrentWindow'] + \
                                          math.sqrt(math.pow(mx, 2) + math.pow(mz, 2))

    if player_info['IsTransporting']:
        player_info['Transport_Current_DistanceTranslated'] = player_info['Transport_Current_DistanceTranslated'] + \
                                                              math.sqrt(math.pow(mx, 2) + math.pow(mz, 2))
