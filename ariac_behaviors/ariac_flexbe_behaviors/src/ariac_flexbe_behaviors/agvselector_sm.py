#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_behaviors.droponagv_sm import DropOnAGVSM
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_behaviors.droponagv2_sm import DropOnAGV2SM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 29 2020
@author: Wouter de Saegher, Stefan Roelands
'''
class AgvSelectorSM(Behavior):
	'''
	Kiezen van de juiste AGV en de PreDrops
	'''


	def __init__(self):
		super(AgvSelectorSM, self).__init__()
		self.name = 'AgvSelector'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(DropOnAGVSM, 'DropOnAGV')
		self.add_behavior(DropOnAGV2SM, 'DropOnAGV2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1009 y:150, x:524 y:560
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_pose_right', 'part_pose_left', 'agv_id', 'arm_id_right', 'arm_id_left'])
		_state_machine.userdata.part_pose_right = []
		_state_machine.userdata.part_pose_left = []
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.agv1 = 'agv1'
		_state_machine.userdata.agv2 = 'agv2'
		_state_machine.userdata.PreDropleft = ''
		_state_machine.userdata.PreDropright = ''
		_state_machine.userdata.PreDroprightAgv1 = 'Gantry_Predrop_AGV_1RA'
		_state_machine.userdata.PreDropleftAgv2 = 'Gantry_Predrop_AGV_2LA'
		_state_machine.userdata.PreDroprightAgv2 = 'Gantry_Predrop_AGV_2RA'
		_state_machine.userdata.PreDropleftAgv1 = 'Gantry_Predrop_AGV_1LA'
		_state_machine.userdata.arm_id_right = ''
		_state_machine.userdata.arm_id_left = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:97 y:71
			OperatableStateMachine.add('AGVChoice1',
										EqualState(),
										transitions={'true': 'PreDropleft', 'false': 'AGVChoice2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_id', 'value_b': 'agv1'})

			# x:728 y:69
			OperatableStateMachine.add('DropOnAGV',
										self.use_behavior(DropOnAGVSM, 'DropOnAGV'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_pose_right': 'part_pose_right', 'part_pose_left': 'part_pose_left', 'PreDropright': 'PreDropright', 'PreDropleft': 'PreDropleft', 'arm_id_right': 'arm_id_right', 'arm_id_left': 'arm_id_left'})

			# x:97 y:163
			OperatableStateMachine.add('AGVChoice2',
										EqualState(),
										transitions={'true': 'PreDropleft_2', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_id', 'value_b': 'agv2'})

			# x:287 y:70
			OperatableStateMachine.add('PreDropleft',
										ReplaceState(),
										transitions={'done': 'PreDropright'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PreDropleftAgv1', 'result': 'PreDropleft'})

			# x:475 y:71
			OperatableStateMachine.add('PreDropright',
										ReplaceState(),
										transitions={'done': 'DropOnAGV'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PreDroprightAgv1', 'result': 'PreDropright'})

			# x:287 y:164
			OperatableStateMachine.add('PreDropleft_2',
										ReplaceState(),
										transitions={'done': 'PreDropright_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PreDropleftAgv2', 'result': 'PreDropleft'})

			# x:475 y:163
			OperatableStateMachine.add('PreDropright_2',
										ReplaceState(),
										transitions={'done': 'DropOnAGV2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PreDroprightAgv2', 'result': 'PreDropright'})

			# x:726 y:164
			OperatableStateMachine.add('DropOnAGV2',
										self.use_behavior(DropOnAGV2SM, 'DropOnAGV2'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_pose_right': 'part_pose_right', 'part_pose_left': 'part_pose_left', 'PreDropright': 'PreDropright', 'PreDropleft': 'PreDropleft', 'arm_id_right': 'arm_id_right', 'arm_id_left': 'arm_id_left'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
