# UCF_TA2_AC

Player Profiler Analytic Component 

Purpose: Player Profiles on ‘potential’ in teamwork and in taskwork used to inform ASI about player features that may be predictive of performance related behaviors. 

## Software requirements
 * MQTT service
 * Python and required dependencies in `requirements.txt`
   * Install dependencies as `pip3 install --user -r requirements.txt`

## Inputs/Messages for subscription:
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


## Outputs:
- [Participant_Id, PlayerRole, TaskPotential_Category, TeamPotential_Category, PlayerProfile]

#### Bus message format
### TOPIC

`agent/PlayerProfiler/player_profile`

#### Message Fields

| Field Name | Type | Description
| --- | --- | ---|
| player-profile | string | Player Profile category represents the categorization of the player as high or low in task potential and in team potential in order to distinguish players as members of four distinct groups that may display differing tasking and teaming behaviors
| team-potential-category | string | Team potential category represents the categorization of the player as high or low in potential to successfully maintain awareness of their teammates and progress as well as to coordinate activities and resources effectively and efficiently
| task-potential-category | string | Task potential category represents the categorization of the player as high or low in potential to successfully complete mission related actions effectively and efficiently
| callsign | string | The callsign of the player
| participant_id | string | The HSR safe id of the player

Legal values for `player-profile` are `["LowTaskLowTeam", "LowTaskHighTeam", "HighTaskLowTeam", "HighTaskHighTeam"]`

Legal values for `team-potential-category` are `["LowTeam", "HighTeam"]`

Legal values for `task-potential-category` are `["LowTask", "HighTask"]`

For callsign and participant_id, see [client_info.md](../Trial/client_info.md)

#### Message Example

```json
{
  "data": {
    "player-profile": "HighTaskLowTeam",
    "team-potential-category": "LowTeam",
    "task-potential-category": "LowTask",
    "participant_id": "P000443",
    "callsign": "Green"
  }
}
```

## Frequency of Measurement

Player profile messages will be published at a single instance in response to survey responses being published on the message bus. 

## Generating Assessments and Potential Applications

Details regarding interpretation of the Player Profiler are contained in the "UCF Player Profile Analytic Component Guide" that can be accesssed at the following link: https://docs.google.com/document/d/1gagBvrZpWfpmJ8D-Fs7AkMkH_TbvpZO8v7_LeAbiWMs/edit

General, high-level interpretation may be guided by the following statements:

- Low Task, Low Team Potential ("player-profile": "LowTaskLowTeam",
    "team-potential-category": "LowTeam",
    "task-potential-category": "LowTask"): Profiles indicate reduced teaming potential and reduced task capabilities. Hypothesized that these players will exhibit fewer teamwork oriented behaviors in Minecraft and will be less successful in meeting Minecraft task objectives.

- High Task, Low Team Potential ("player-profile": "HighTaskLowTeam",
    "team-potential-category": "LowTeam",
    "task-potential-category": "HighTask"): Profiles indicate reduced teaming potential and increased task capabilities. Hypothesized that these players will exhibit fewer teamwork oriented behaviors in Minecraft and will be more successful in meeting Minecraft task objectives. 

- Low Task, High Team Potential  ("player-profile": "LowTaskHighTeam",
    "team-potential-category": "LowTeam",
    "task-potential-category": "HighTask"): Profiles indicate increased teaming potential and reduced task capabilities. Hypothesized that these players will exhibit more teamwork oriented behaviors in Minecraft and will be less successful in meeting Minecraft task objectives. 

- High Task, High Team Potential ("player-profile": "HighTaskHighTeam",
    "team-potential-category": "HighTeam",
    "task-potential-category": "HighTask"): Profiles indicate increased teaming potential and increased task capabilities. Hypothesized that these players will exhibit more teamwork oriented behaviors in Minecraft and will be more successful in meeting Minecraft task objectives.

## Component Process and Output Validation

Full details of validating evidence associated with the Player Profile are contained in the "UCF Player Profile Analytic Component Guide" that can be accesssed at the following link: https://docs.google.com/document/d/1gagBvrZpWfpmJ8D-Fs7AkMkH_TbvpZO8v7_LeAbiWMs/edit

In brief: In Study 2, we found that Player Profiles are predictive of performance behaviors. First, players higher on task potential generally break more rubble. Second, we see a numerical increase in scores as player profile potential increases.  Third, rubbler differences emerge dependent on rubble type.  Players who score high on teaming potential learn better over missions about breaking critical rubble, that is, rubble effective in serving needs of their team.  Players who score low on teaming potential decrease in rubbler effectiveness from M1 to M2 regardless of rubble type.

Expanding our scope to examine all player profile groupings in the context of players’ sequential missions, we find that profiles also predict improvement/learning and convergence of particular profile types towards improved task performance behaviors.

We emphasize that players with greater measured team potential tended to execute more exploration behaviors. This is important because knowledge gathering in this task is analogous to coverage of problem space necessary for effectively meeting objectives.  Here we look at “distance traveled” as form of exploration in problem environment. Findings:  Player Profiles are predictive of exploration. First, players higher on team potential are traveling more distances overall 1 (right bars versus left bars). Second, see a numerical difference for low team potential when considering task potential - high task potential does lead to more exploration behaviors. Results of a repeated measures ANOVA provide evidence of a main effect of PP team group on distance traveled1,  F(1, 170)=7.15, p<.01.

Role balancing is a prime example of the sort of behaviors that will not be demonstrated in Study 3, but were predicted by player profiles in Study 2. In that study, we found that role balancing was indicative of players coordinating to effectively meet objectives.  Here we looked at “longest time in a role” for players on a team. Although we cannot examine that metric in Study 3, we anticipate similar predictive value related to team coordination metrics such as balancing transportation efforts across players. 

Findings:  Player Profiles are predictive of role balancing depending on role type. First, players higher on team potential are more evenly distributing their time regardless of role (right set of blue/gold bars versus left bars). Second, there is an interaction in that low team profiles spend less time in searcher role relative to other roles.1 Searcher role is least fun - suggests those with higher team orientation profile are choosing to serve the team needs by performing exploration and increasing accessibility of victims. Results of a repeated measures ANOVA provide evidence of interaction effect of PP team group on time in roles1,  F(2, 169)=3.94, p<.05.


## Engg notes
 * See [Agent Readme](./agent-dev-README.md) to learn about how to run the agent.
