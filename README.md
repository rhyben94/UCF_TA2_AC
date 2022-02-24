# UCF_TA2_AC

Player Profiler Analytic Component 

Purpose: Player Profiles on ‘potential’ in teamwork and in taskwork used to inform ASI about player features that may be predictive of performance related behaviors. 

#### Software requirements
 * MQTT service
 * Python and required dependencies in `requirements.txt`
   * Install dependencies as `pip3 install --user -r requirements.txt`

Inputs/Messages for subscription:
- Survey items
  - SBSOD_1 = {"ImportId":"QID13_1"}
  - SBSOD_2 = {"ImportId":"QID13_2"}
  - SBSOD_3 = {"ImportId":"QID13_3"}
  - SBSOD_4 = {"ImportId":"QID13_4"}
  - SBSOD_5 = {"ImportId":"QID13_5"}
  - SBSOD_6 = {"ImportId":"QID13_6"}
  - SBSOD_7 = {"ImportId":"QID13_7"}
  - SBSOD_8 = {"ImportId":"QID13_8"}
  - SBSOD_9 = {"ImportId":"QID13_9"}
  - SBSOD_10 = {"ImportId":"QID13_10"}
  - SBSOD_11 = {"ImportId":"QID13_11"}
  - SBSOD_12 = {"ImportId":"QID13_12"}
  - SBSOD_13 = {"ImportId":"QID13_13"}
  - SBSOD_14 = {"ImportId":"QID13_14"}
  - SBSOD_15 = {"ImportId":"QID13_15"}
  - VGEM_1 = {"ImportId":"QID867_1"}
  - VGEM_2 = {"ImportId":"QID867_2"}
  - VGEM_3 = {"ImportId":"QID867_4"}
  - VGEM_4 = {"ImportId":"QID868_1"}
  - VGEM_5 = {"ImportId":"QID868_3"}
  - VGEM_6 = {"ImportId":"QID868_5"}
  - VGEM_7 = {"ImportId":"QID868_6"}
  - VGEM_8 = {"ImportId":"QID872_1"}
  - VGEM_9 = {"ImportId":"QID872_2"}
  - VGEM_10 = {"ImportId":"QID872_3"}
  - VGEM_11 = {"ImportId":"QID872_4"}
  - VGEM_12 = {"ImportId":"QID872_5"}
  - VGEM_13 = {"ImportId":"QID872_6"}
  - VGEM_14 = {"ImportId":"QID872_7"}
  - VGEM_15 = {"ImportId":"QID872_8"}
  - PsychologicalCollectivism_1 = {"ImportId":"QID830_1"}
  - PsychologicalCollectivism_2 = {"ImportId":"QID830_2"}
  - PsychologicalCollectivism_3 = {"ImportId":"QID830_3"}
  - PsychologicalCollectivism_4 = {"ImportId":"QID830_4"}
  - PsychologicalCollectivism_5 = {"ImportId":"QID830_5"}
  - PsychologicalCollectivism_6 = {"ImportId":"QID830_6"}
  - PsychologicalCollectivism_7 = {"ImportId":"QID830_7"}
  - PsychologicalCollectivism_8 = {"ImportId":"QID830_8"}
  - PsychologicalCollectivism_9 = {"ImportId":"QID830_9"}
  - PsychologicalCollectivism_10 = {"ImportId":"QID830_10"}
  - PsychologicalCollectivism_11 = {"ImportId":"QID830_11"}
  - PsychologicalCollectivism_12 = {"ImportId":"QID830_12"}
  - PsychologicalCollectivism_13 = {"ImportId":"QID830_13"}
  - PsychologicalCollectivism_14 = {"ImportId":"QID830_14"}
  - PsychologicalCollectivism_15 = {"ImportId":"QID830_15"}
  - SociableDominance_1 = {"ImportId":"QID832_9"}
  - SociableDominance_2 = {"ImportId":"QID832_16"}
  - SociableDominance_3 = {"ImportId":"QID832_17"}
  - SociableDominance_4 = {"ImportId":"QID832_18"}
  - SociableDominance_5 = {"ImportId":"QID832_19"}
  - SociableDominance_6 = {"ImportId":"QID832_20"}
  - SociableDominance_7 = {"ImportId":"QID832_21"}
  - SociableDominance_8 = {"ImportId":"QID832_22"}
  - SociableDominance_9 = {"ImportId":"QID832_23"}
  - SociableDominance_10 = {"ImportId":"QID832_24"}
  - SociableDominance_11 = {"ImportId":"QID832_25"}
  - SociableDominance_12 = {"ImportId":"QID832_26"}
  - SociableDominance_13 = {"ImportId":"QID832_27"}
  - SociableDominance_14 = {"ImportId":"QID832_28"}
  - SociableDominance_15 = {"ImportId":"QID832_29"}
  - RMET_1 = {"ImportId":"QID751"}
  - RMET_2 = {"ImportId":"QID753"}
  - RMET_3 = {"ImportId":"QID755"}
  - RMET_4 = {"ImportId":"QID757"}
  - RMET_5 = {"ImportId":"QID759"}
  - RMET_6 = {"ImportId":"QID761"}
  - RMET_7 = {"ImportId":"QID763"}
  - RMET_8 = {"ImportId":"QID765"}
  - RMET_9 = {"ImportId":"QID767"}
  - RMET_10 = {"ImportId":"QID769"}
  - RMET_11 = {"ImportId":"QID771"}
  - RMET_12 = {"ImportId":"QID773"}
  - RMET_13 = {"ImportId":"QID775"}
  - RMET_14 = {"ImportId":"QID777"}
  - RMET_15 = {"ImportId":"QID779"}
  - RMET_16 = {"ImportId":"QID781"}
  - RMET_17 = {"ImportId":"QID783"}
  - RMET_18 = {"ImportId":"QID785"}
  - RMET_19 = {"ImportId":"QID787"}
  - RMET_20 = {"ImportId":"QID789"}
  - RMET_21 = {"ImportId":"QID791"}
  - RMET_22 = {"ImportId":"QID793"}
  - RMET_23 = {"ImportId":"QID795"}
  - RMET_24 = {"ImportId":"QID797"}
  - RMET_25 = {"ImportId":"QID799"}
  - RMET_26 = {"ImportId":"QID801"}
  - RMET_27 = {"ImportId":"QID803"}
  - RMET_28 = {"ImportId":"QID805"}
  - RMET_29 = {"ImportId":"QID807"}
  - RMET_30 = {"ImportId":"QID809"}
  - RMET_31 = {"ImportId":"QID811"}
  - RMET_32 = {"ImportId":"QID813"}
  - RMET_33 = {"ImportId":"QID815"}
  - RMET_34 = {"ImportId":"QID817"}
  - RMET_35 = {"ImportId":"QID819"}
  - RMET_36 = {"ImportId":"QID821"}


Outputs:
- [Participant_Id, PlayerRole, TaskPotential_Category, TeamPotential_Category, PlayerProfile]

#### Engg notes
 * See [Agent Readme](./agent-dev-README.md) to learn about how to run the agent.
