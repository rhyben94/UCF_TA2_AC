# Ref https://docs.google.com/presentation/d/1Z1QMkGs2D6fZSxsZO9CM2bFzGYzZaVbjTieoUenhQho/edit#slide=id.g117addec6ce_0_45
import math
import numbers
from pprint import pprint
from statistics import mean
import PlayerProfiler_Draft

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
Engineer_RubbleDestroyed_to_MovementRatio_LowerThreshold_List = [6 / 400, 8 / 600, 8 / 600, 8 / 300, 8 / 600]

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

max_index_180_timeout = 5

timeout_180_reset_list = set()


def get_list_mean(lst):
    if len(lst) > 0:
        return mean(lst)
    return 0


def compute_task_potential_factor(current_window, count_current_window, upper_threshold_list, lower_threshold_list):
    if count_current_window >= upper_threshold_list[current_window]:
        return 1
    elif count_current_window <= lower_threshold_list[current_window]:
        return -1
    else:
        return 0


def compute_state_average_current_window(task_potential_factors_list_cw,
                                         FactorCoefficients):
    factor_coef_1, factor_coef_2, factor_coef_3, factor_coef_4, factor_coef_5 = FactorCoefficients
    num = task_potential_factors_list_cw[0] * factor_coef_1 + \
          task_potential_factors_list_cw[1] * factor_coef_2 + \
          task_potential_factors_list_cw[2] * factor_coef_3 + \
          task_potential_factors_list_cw[3] * factor_coef_4 + \
          task_potential_factors_list_cw[4] * factor_coef_5
    den = factor_coef_1 + factor_coef_2 + factor_coef_3 + factor_coef_4 + factor_coef_5
    return num / den


# Step 2 functions
def init_from_player_profile(player_info, player_profile):
    # print('Player Info')
    # pprint(player_info)
    # print('Player Profile')
    # pprint(player_profile)

    # Step 1
    player_info['TaskPotential_Start'] = player_profile['task-potential-category']
    player_info['TeamPotential_Category'] = player_profile['team-potential-category']
    TaskPotential_Categorization_LastWindow = player_info['TaskPotential_Categorization_LastWindow']
    if not TaskPotential_Categorization_LastWindow:
        player_info['TaskPotential_Categorization_LastWindow'] = player_info['TaskPotential_Start']
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
        player_info['Medic_TriageSuccessful_Count_CurrentWindow'] += 1
        player_info['Medic_TriageSuccessful_Count_Total'] += 1
    timeout_180_reset_list.add('Medic_TriageSuccessful_Count_CurrentWindow')


def handle_rubble_destroyed(player_info, pid):
    role = player_info['role']
    callsign = player_info['callsign']
    by_engg = False
    if role != 'engineer':
        print(f'Warn: Rubble destroyed pid: {pid} {callsign} {role} by engineer? {by_engg}')
    else:
        player_info['Engineer_RubbleDestroyed_Count_CurrentWindow'] += 1
        player_info['Engineer_RubbleDestroyed_Count_Total'] += 1
    timeout_180_reset_list.add('Engineer_RubbleDestroyed_Count_CurrentWindow')


def handle_victim_evacuated(player_info, pid, dat):
    role = player_info['role']
    callsign = player_info['callsign']
    by_transporter = False
    victim_type = dat['type']
    if role == 'transporter':
        player_info['Transporter_Evacuations_Count_CurrentWindow'] += 1
        player_info['Transporter_Evacuations_Count_Total'] += 1

        if victim_type == 'victim_saved_c':
            player_info['Transporter_Evacuations_Critical_Count_CurrentWindow'] += 1
            player_info['Transporter_Evacuations_Critical_Count_Total'] += 1
        else:
            player_info['Transporter_Evacuations_Regular_Count_CurrentWindow'] += 1
            player_info['Transporter_Evacuations_Regular_Count_Total'] += 1
    # else:
    #     print(
    #         f'Check: Victim evacuated pid: {pid} {callsign} {role} victim_type {victim_type} by transporter? {by_transporter}')

    timeout_180_reset_list.add('Transporter_Evacuations_Count_CurrentWindow')
    timeout_180_reset_list.add('Transporter_Evacuations_Critical_Count_CurrentWindow')
    timeout_180_reset_list.add('Transporter_Evacuations_Regular_Count_CurrentWindow')


def handle_victim_picked_up(player_info, pid, dat):
    player_info['IsTransporting'] = True
    player_info['Transports_Initiated_Count_CurrentWindow'] += 1
    player_info['Transports_Initiated_Count_Total'] += 1
    player_info['Transport_Current_VictimID'] = dat['victim_id']
    player_info['Transport_Current_PickupLocation'] = [dat['victim_x'], dat['victim_z']]
    timeout_180_reset_list.add('Transports_Initiated_Count_CurrentWindow')


def handle_victim_placed(player_info, pid, dat):
    player_info['IsTransporting'] = False
    player_info['Transports_Completed_Count_CurrentWindow'] += 1
    player_info['Transports_Completed_Count_Total'] += 1
    player_info['Transport_Current_VictimID'] = None
    player_info['Transport_Current_DropoffLocation'] = [dat['victim_x'], dat['victim_z']]

    player_info['Transport_Distances_CurrentWindow_List'].append(player_info['Transport_Current_DistanceTranslated'])
    player_info['Transport_Current_DistanceTranslated'] = 0
    timeout_180_reset_list.add('Transports_Completed_Count_CurrentWindow')
    timeout_180_reset_list.add('Transport_Distances_CurrentWindow_List')


def handle_obs_state(player_info, pid, dat):
    mx = dat['motion_x']
    mz = dat['motion_z']
    player_info['Motion_CurrentWindow'] = player_info['Motion_CurrentWindow'] + \
                                          math.sqrt(math.pow(mx, 2) + math.pow(mz, 2))

    if player_info['IsTransporting']:
        player_info['Transport_Current_DistanceTranslated'] = player_info['Transport_Current_DistanceTranslated'] + \
                                                              math.sqrt(math.pow(mx, 2) + math.pow(mz, 2))
    timeout_180_reset_list.add('Motion_CurrentWindow')


# Step 3 functions

def do_step_3_seq_3(TaskPotential_Factors_CurrentWindow,
                    FactorCoefficients,
                    TaskPotential_StateAverage_LastWindow
                    ):
    print('TaskPotential_Factors_CurrentWindow', TaskPotential_Factors_CurrentWindow)
    TaskPotential_StateAverage_CurrentWindow = compute_state_average_current_window(TaskPotential_Factors_CurrentWindow,
                                                                                    FactorCoefficients)

    TaskPotential_StateAverage_Delta = TaskPotential_StateAverage_CurrentWindow - TaskPotential_StateAverage_LastWindow
    return {'TaskPotential_StateAverage_CurrentWindow': TaskPotential_StateAverage_CurrentWindow}

def do_step_3_seq_4(current_window,
                    player_info,
                    TaskPotential_StateAverages_List,
                    TaskPotential_RealTime_Factors_Coefficient,
                    TaskPotential_RecategorizationThresholds_High_List,
                    TaskPotential_RecategorizationThresholds_Low_List):
    TaskPotential_BaseModifier = player_info['TaskPotential_BaseModifier']
    TaskPotential_Calculation = TaskPotential_BaseModifier + sum(
        TaskPotential_StateAverages_List) * TaskPotential_RealTime_Factors_Coefficient

    TaskPotential_Categorization_LastWindow = player_info['TaskPotential_Categorization_LastWindow']
    if TaskPotential_Calculation >= TaskPotential_RecategorizationThresholds_High_List[current_window]:
        TaskPotential_Categorization_CurrentWindow = 'HighTask'
    elif TaskPotential_Calculation <= TaskPotential_RecategorizationThresholds_Low_List[current_window]:
        TaskPotential_Categorization_CurrentWindow = 'LowTask'
    else:
        TaskPotential_Categorization_CurrentWindow = TaskPotential_Categorization_LastWindow

    if TaskPotential_Categorization_CurrentWindow == TaskPotential_Categorization_LastWindow:
        TaskPotential_Changed = False
    else:
        TaskPotential_Changed = True
    return {'TaskPotential_Changed': TaskPotential_Changed,
            'TaskPotential_Categorization_CurrentWindow': TaskPotential_Categorization_CurrentWindow
            }

def update_medic_180(player_info, current_window):
    print(f'update medic 180 index: {current_window}')
    # pprint(player_info)
    # print()
    # step 3 Seq 1
    Motion_CurrentWindow = player_info['Motion_CurrentWindow']
    Medic_TriageSuccessful_Count_CurrentWindow = player_info['Medic_TriageSuccessful_Count_CurrentWindow']
    Transports_Completed_Count_CurrentWindow = player_info['Transports_Completed_Count_CurrentWindow']

    Medic_TriageSuccessful_to_Movement_ratio_CurrentWindow = Medic_TriageSuccessful_Count_CurrentWindow / Motion_CurrentWindow
    # player_info[
    #     'Medic_TriageSuccessful_to_Movement_ratio_CurrentWindow'] = Medic_TriageSuccessful_to_Movement_ratio_CurrentWindow

    Transport_Distance_Average_CurrentWindow = get_list_mean(player_info['Transport_Distances_CurrentWindow_List'])
    # player_info['Transport_Distance_Average_CurrentWindow'] = Transport_Distance_Average_CurrentWindow

    Medic_TriageSuccessful_to_Transports_ratio_CurrentWindow = 0
    if Transports_Completed_Count_CurrentWindow > 0:
        Medic_TriageSuccessful_to_Transports_ratio_CurrentWindow = Medic_TriageSuccessful_Count_CurrentWindow / Transports_Completed_Count_CurrentWindow
    # player_info[
    #     'Medic_TriageSuccessful_to_Transports_ratio_CurrentWindow'] = Medic_TriageSuccessful_to_Transports_ratio_CurrentWindow

    #     Step 3, seq 2
    TaskPotential_Factor_1_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Medic_TriageSuccessful_Count_CurrentWindow,
                                                                         Medic_TriageSuccessful_UpperThreshold_List,
                                                                         Medic_TriageSuccessful_LowerThreshold_List)

    # player_info['TaskPotential_Factor_1_CurrentWindow'] = TaskPotential_Factor_1_CurrentWindow
    if 'TaskPotential_Factor_1_list' not in player_info:
        player_info['TaskPotential_Factor_1_list'] = []
    # player_info['TaskPotential_Factor_1_list'].append(TaskPotential_Factor_1_CurrentWindow)

    TaskPotential_Factor_2_CurrentWindow = \
        compute_task_potential_factor(current_window,
                                      Medic_TriageSuccessful_to_Movement_ratio_CurrentWindow,
                                      Medic_TriageSuccessful_to_MovementRatio_UpperThreshold_List,
                                      Medic_TriageSuccessful_to_MovementRatio_LowerThreshold_List)

    # player_info['TaskPotential_Factor_2_CurrentWindow'] = TaskPotential_Factor_2_CurrentWindow
    if 'TaskPotential_Factor_2_list' not in player_info:
        player_info['TaskPotential_Factor_2_list'] = []
    # player_info['TaskPotential_Factor_2_list'].append(TaskPotential_Factor_2_CurrentWindow)

    TaskPotential_Factor_3_CurrentWindow = 0
    if Transport_Distance_Average_CurrentWindow > 0:
        TaskPotential_Factor_3_CurrentWindow = compute_task_potential_factor(current_window,
                                                                             100 / Transport_Distance_Average_CurrentWindow,
                                                                             Medic_Transport_Distance_Average_UpperThreshold_List,
                                                                             Medic_Transport_Distance_Average_LowerThreshold_List)
    # player_info['TaskPotential_Factor_3_CurrentWindow'] = TaskPotential_Factor_3_CurrentWindow
    if 'TaskPotential_Factor_3_list' not in player_info:
        player_info['TaskPotential_Factor_3_list'] = []
    # player_info['TaskPotential_Factor_3_list'].append(TaskPotential_Factor_3_CurrentWindow)

    TaskPotential_Factor_4_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Transports_Completed_Count_CurrentWindow,
                                                                         Medic_Transports_Completed_Count_UpperThreshold_List,
                                                                         Medic_Transports_Completed_Count_LowerThreshold_List)
    # player_info['TaskPotential_Factor_4_CurrentWindow'] = TaskPotential_Factor_4_CurrentWindow
    if 'TaskPotential_Factor_4_list' not in player_info:
        player_info['TaskPotential_Factor_4_list'] = []
    # player_info['TaskPotential_Factor_4_list'].append(TaskPotential_Factor_4_CurrentWindow)

    TaskPotential_Factor_5_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Medic_TriageSuccessful_to_Transports_ratio_CurrentWindow,
                                                                         Medic_TriageSuccessful_to_Transports_ratio_UpperThreshold_List,
                                                                         Medic_TriageSuccessful_to_Transports_ratio_LowerThreshold_List)

    # player_info['TaskPotential_Factor_5_CurrentWindow'] = TaskPotential_Factor_5_CurrentWindow
    if 'TaskPotential_Factor_5_list' not in player_info:
        player_info['TaskPotential_Factor_5_list'] = []
    # player_info['TaskPotential_Factor_5_list'].append(TaskPotential_Factor_5_CurrentWindow)

    # seq 3
    TaskPotential_Factors_CurrentWindow = [TaskPotential_Factor_1_CurrentWindow,
                                           TaskPotential_Factor_2_CurrentWindow,
                                           TaskPotential_Factor_3_CurrentWindow,
                                           TaskPotential_Factor_4_CurrentWindow,
                                           TaskPotential_Factor_5_CurrentWindow]
    FactorCoefficients = [Medic_FactorCoefficient_1,
                          Medic_FactorCoefficient_2,
                          Medic_FactorCoefficient_3,
                          Medic_FactorCoefficient_4,
                          Medic_FactorCoefficient_5]
    TaskPotential_Factors_List = player_info['TaskPotential_Factors_List']
    TaskPotential_Factors_List.append(TaskPotential_Factors_CurrentWindow)
    TaskPotential_StateAverage_LastWindow = player_info['TaskPotential_StateAverage_LastWindow']
    seq_3_result = do_step_3_seq_3(TaskPotential_Factors_CurrentWindow, FactorCoefficients, TaskPotential_StateAverage_LastWindow)
    TaskPotential_StateAverage_CurrentWindow = seq_3_result['TaskPotential_StateAverage_CurrentWindow']
    TaskPotential_StateAverages_List = player_info['TaskPotential_StateAverages_List']
    TaskPotential_StateAverages_List.append(TaskPotential_StateAverage_CurrentWindow)

    # seq 4
    seq_4_result = do_step_3_seq_4(current_window,
                                   player_info,
                                   TaskPotential_StateAverages_List,
                                   Medic_TaskPotential_RealTime_Factors_Coefficient,
                                   Medic_TaskPotential_RecategorizationThresholds_High_List,
                                   Medic_TaskPotential_RecategorizationThresholds_Low_List
                                   )
    print('seq_4_result')
    pprint(seq_4_result)
    TaskPotential_Categorization_CurrentWindow = seq_4_result['TaskPotential_Categorization_CurrentWindow']
    TaskPotential_Changed = seq_4_result['TaskPotential_Changed']
    TeamPotential_Category = player_info['TeamPotential_Category']
    PlayerProfiler_Draft.make_player_profile(TaskPotential_Categorization_CurrentWindow, TeamPotential_Category)
    # print('update medic 180 after state', current_window)
    # pprint(player_info)
    # print()
    reset_vars_step_3_seq_5(player_info)
    return {'TaskPotential_Changed': TaskPotential_Changed,
            'TaskPotential_Category': TaskPotential_Categorization_CurrentWindow,
            'TaskPotential_StateAverages_List': TaskPotential_StateAverages_List,
            'TaskPotential_Factors_List': TaskPotential_Factors_List
            }

def update_engg_180(player_info, current_window):
    print(f'update engg 180 index: {current_window}')
    # pprint(player_info)
    # print()
    # step 3 seq 1
    Motion_CurrentWindow = player_info['Motion_CurrentWindow']
    Engineer_RubbleDestroyed_Count_CurrentWindow = player_info['Engineer_RubbleDestroyed_Count_CurrentWindow']
    Transports_Completed_Count_CurrentWindow = player_info['Transports_Completed_Count_CurrentWindow']

    Engineer_RubbleDestroyed_to_Movement_ratio_CurrentWindow = Engineer_RubbleDestroyed_Count_CurrentWindow / Motion_CurrentWindow
    Transport_Distance_Average_CurrentWindow = get_list_mean(player_info['Transport_Distances_CurrentWindow_List'])

    Engineer_Rubble_to_Transports_ratio_CurrentWindow = 0
    if Transports_Completed_Count_CurrentWindow > 0:
        Engineer_Rubble_to_Transports_ratio_CurrentWindow = Engineer_RubbleDestroyed_Count_CurrentWindow / Transports_Completed_Count_CurrentWindow

    # Seq 2
    TaskPotential_Factor_1_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Engineer_RubbleDestroyed_Count_CurrentWindow,
                                                                         Engineer_RubbleDestroyed_Count_UpperThreshold_List,
                                                                         Engineer_RubbleDestroyed_Count_LowerThreshold_List)

    TaskPotential_Factor_2_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Engineer_RubbleDestroyed_to_Movement_ratio_CurrentWindow,
                                                                         Engineer_RubbleDestroyed_to_MovementRatio_UpperThreshold_List,
                                                                         Engineer_RubbleDestroyed_to_MovementRatio_LowerThreshold_List)

    TaskPotential_Factor_3_CurrentWindow = 0
    if Transport_Distance_Average_CurrentWindow > 0:
        TaskPotential_Factor_3_CurrentWindow = compute_task_potential_factor(current_window,
                                                                             100 / Transport_Distance_Average_CurrentWindow,
                                                                             Engineer_Transport_Distance_Average_UpperThreshold_List,
                                                                             Engineer_Transport_Distance_Average_LowerThreshold_List)

    TaskPotential_Factor_4_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Transports_Completed_Count_CurrentWindow,
                                                                         Engineer_Transports_Completed_Count_UpperThreshold_List,
                                                                         Engineer_Transports_Completed_Count_LowerThreshold_List)

    TaskPotential_Factor_5_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Engineer_Rubble_to_Transports_ratio_CurrentWindow,
                                                                         Engineer_Rubble_to_Transports_ratio_UpperThreshold_List,
                                                                         Engineer_Rubble_to_Transports_ratio_LowerThreshold_List)
    # seq 3
    TaskPotential_Factors_CurrentWindow = [TaskPotential_Factor_1_CurrentWindow,
                                           TaskPotential_Factor_2_CurrentWindow,
                                           TaskPotential_Factor_3_CurrentWindow,
                                           TaskPotential_Factor_4_CurrentWindow,
                                           TaskPotential_Factor_5_CurrentWindow]
    FactorCoefficients = [Engineer_FactorCoefficient_1,
                          Engineer_FactorCoefficient_2,
                          Engineer_FactorCoefficient_3,
                          Engineer_FactorCoefficient_4,
                          Engineer_FactorCoefficient_5]
    TaskPotential_Factors_List = player_info['TaskPotential_Factors_List']
    TaskPotential_Factors_List.append(TaskPotential_Factors_CurrentWindow)
    TaskPotential_StateAverage_LastWindow = player_info['TaskPotential_StateAverage_LastWindow']
    seq_3_result = do_step_3_seq_3(TaskPotential_Factors_CurrentWindow, FactorCoefficients, TaskPotential_StateAverage_LastWindow)
    TaskPotential_StateAverage_CurrentWindow = seq_3_result['TaskPotential_StateAverage_CurrentWindow']
    TaskPotential_StateAverages_List = player_info['TaskPotential_StateAverages_List']
    TaskPotential_StateAverages_List.append(TaskPotential_StateAverage_CurrentWindow)

    # seq 4
    seq_4_result = do_step_3_seq_4(current_window,
                                   player_info,
                                   TaskPotential_StateAverages_List,
                                   Engineer_TaskPotential_RealTime_Factors_Coefficient,
                                   Engineer_TaskPotential_RecategorizationThresholds_High_List,
                                   Engineer_TaskPotential_RecategorizationThresholds_Low_List
                                   )
    TaskPotential_Categorization_CurrentWindow = seq_4_result['TaskPotential_Categorization_CurrentWindow']
    TaskPotential_Changed = seq_4_result['TaskPotential_Changed']
    TeamPotential_Category = player_info['TeamPotential_Category']
    PlayerProfiler_Draft.make_player_profile(TaskPotential_Categorization_CurrentWindow, TeamPotential_Category)
    # print('update engg 180 after state', current_window)
    # pprint(player_info)
    # print()
    reset_vars_step_3_seq_5(player_info)
    return {'TaskPotential_Changed': TaskPotential_Changed,
            'TaskPotential_Category': TaskPotential_Categorization_CurrentWindow,
            'TaskPotential_StateAverages_List': TaskPotential_StateAverages_List,
            'TaskPotential_Factors_List': TaskPotential_Factors_List
            }

# TODO print to stdout, vars in seq 1 and seq 2
def update_transporter_180(player_info, current_window):
    print(f'update transporter 180 index: {current_window}')
    # pprint(player_info)
    # print()
    # seq 1
    Transports_Completed_Count_CurrentWindow = player_info['Transports_Completed_Count_CurrentWindow']
    Transporter_Evacuations_Count_CurrentWindow = player_info['Transporter_Evacuations_Count_CurrentWindow']

    Transport_Distance_Average_CurrentWindow = get_list_mean(player_info['Transport_Distances_CurrentWindow_List'])
    Transporter_Transport_to_Evacuation_ratio_CurrentWindow = 0
    if Transporter_Evacuations_Count_CurrentWindow > 0:
        Transporter_Transport_to_Evacuation_ratio_CurrentWindow = Transports_Completed_Count_CurrentWindow / Transporter_Evacuations_Count_CurrentWindow

    print('Transport_Distances_CurrentWindow_List', player_info['Transport_Distances_CurrentWindow_List'])
    print('Transport_Distance_Average_CurrentWindow', Transport_Distance_Average_CurrentWindow)

    print('Transports_Completed_Count_CurrentWindow', Transports_Completed_Count_CurrentWindow)
    print('Transporter_Evacuations_Count_CurrentWindow', Transporter_Evacuations_Count_CurrentWindow)
    print('Transport_Distance_Average_CurrentWindow', Transport_Distance_Average_CurrentWindow)
    # seq 2
    Transporter_Evacuations_Regular_Count_CurrentWindow = player_info[
        'Transporter_Evacuations_Regular_Count_CurrentWindow']
    TaskPotential_Factor_1_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Transporter_Evacuations_Regular_Count_CurrentWindow,
                                                                         Transporter_Evacuations_Regular_Count_UpperThreshold_List,
                                                                         Transporter_Evacuations_Regular_Count_LowerThreshold_List)

    Transporter_Evacuations_Critical_Count_CurrentWindow = player_info[
        'Transporter_Evacuations_Critical_Count_CurrentWindow']
    TaskPotential_Factor_2_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Transporter_Evacuations_Critical_Count_CurrentWindow,
                                                                         Transporter_Evacuations_Critical_Count_UpperThreshold_List,
                                                                         Transporter_Evacuations_Critical_Count_LowerThreshold_List)

    TaskPotential_Factor_3_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Transport_Distance_Average_CurrentWindow / 100,
                                                                         Transporter_Transport_Distance_Average_UpperThreshold_List,
                                                                         Transporter_Transport_Distance_Average_LowerThreshold_List)

    TaskPotential_Factor_4_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Transports_Completed_Count_CurrentWindow,
                                                                         Transporter_Transports_Completed_Count_UpperThreshold_List,
                                                                         Transporter_Transports_Completed_Count_LowerThreshold_List)

    TaskPotential_Factor_5_CurrentWindow = compute_task_potential_factor(current_window,
                                                                         Transporter_Transport_to_Evacuation_ratio_CurrentWindow,
                                                                         Transporter_Transport_to_Evacuation_ratio_UpperThreshold_List,
                                                                         Transporter_Transport_to_Evacuation_ratio_LowerThreshold_List)

    # seq 3
    TaskPotential_Factors_CurrentWindow = [TaskPotential_Factor_1_CurrentWindow,
                                           TaskPotential_Factor_2_CurrentWindow,
                                           TaskPotential_Factor_3_CurrentWindow,
                                           TaskPotential_Factor_4_CurrentWindow,
                                           TaskPotential_Factor_5_CurrentWindow]
    FactorCoefficients = [Transporter_FactorCoefficient_1,
                          Transporter_FactorCoefficient_2,
                          Transporter_FactorCoefficient_3,
                          Transporter_FactorCoefficient_4,
                          Transporter_FactorCoefficient_5]
    TaskPotential_Factors_List = player_info['TaskPotential_Factors_List']
    TaskPotential_Factors_List.append(TaskPotential_Factors_CurrentWindow)
    TaskPotential_StateAverage_LastWindow = player_info['TaskPotential_StateAverage_LastWindow']
    seq_3_result = do_step_3_seq_3(TaskPotential_Factors_CurrentWindow, FactorCoefficients, TaskPotential_StateAverage_LastWindow)
    TaskPotential_StateAverage_CurrentWindow = seq_3_result['TaskPotential_StateAverage_CurrentWindow']
    TaskPotential_StateAverages_List = player_info['TaskPotential_StateAverages_List']
    TaskPotential_StateAverages_List.append(TaskPotential_StateAverage_CurrentWindow)

    # seq 4
    seq_4_result = do_step_3_seq_4(current_window,
                                   player_info,
                                   TaskPotential_StateAverages_List,
                                   Transporter_TaskPotential_RealTime_Factors_Coefficient,
                                   Transporter_TaskPotential_RecategorizationThresholds_High_List,
                                   Transporter_TaskPotential_RecategorizationThresholds_Low_List
                                   )
    TaskPotential_Categorization_CurrentWindow = seq_4_result['TaskPotential_Categorization_CurrentWindow']
    TaskPotential_Changed = seq_4_result['TaskPotential_Changed']
    TeamPotential_Category = player_info['TeamPotential_Category']
    PlayerProfiler_Draft.make_player_profile(TaskPotential_Categorization_CurrentWindow, TeamPotential_Category)
    # print('update transporter 180 after state', current_window)
    # pprint(player_info)
    # print()
    reset_vars_step_3_seq_5(player_info)
    return {'TaskPotential_Changed': TaskPotential_Changed,
            'TaskPotential_Category': TaskPotential_Categorization_CurrentWindow,
            'TaskPotential_StateAverages_List': TaskPotential_StateAverages_List,
            'TaskPotential_Factors_List': TaskPotential_Factors_List
            }


def reset_vars_step_3_seq_5(player_info):
    for var in timeout_180_reset_list:
        if var in player_info:
            val = player_info[var]
            # print(f'{type(val)} {var} = {val}')
            if isinstance(val, numbers.Number):
                player_info[var] = 0
            if isinstance(val, list):
                player_info[var] = []
            print(f'set {var}: {val} => {player_info[var]}')
        else:
            print('Check: timeout 180 reset var not in player_info')


def handle_180_sec_timeout(player_infos, factor):
    for pi in player_infos:
        role = pi['role']
        if role == 'medic':
            ret = update_medic_180(pi, factor)
            pi['update_180'] = ret
        elif role == 'engineer':
            ret = update_engg_180(pi, factor)
            pi['update_180'] = ret
        elif role == 'transporter':
            ret = update_transporter_180(pi, factor)
            pi['update_180'] = ret
        else:
            print('Unknown role for player: ', role)