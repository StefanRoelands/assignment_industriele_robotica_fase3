#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_flexbe_behaviors.move_to_home_sm import Move_to_HomeSM
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 28 2020
@author: Wouter de Saegher, Stefan Roelands
'''
class SorterenSM(Behavior):
	'''
	Het sorteren van binnenkomende producten
	'''


	def __init__(self):
		super(SorterenSM, self).__init__()
		self.name = 'Sorteren'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(Move_to_HomeSM, 'Move_to_Home')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1222 y:168, x:482 y:174
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.config_name_gantry_Pre_Conv = 'Gantry_PreGrasp_Conv'
		_state_machine.userdata.move_group = 'Gantry'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.poweroff = 0
		_state_machine.userdata.config_name_gantry_Pre_side = 'Gantry_PreGrasp_Right_bins_2'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('Start',
										StartAssignment(),
										transitions={'continue': 'Move_to_Home'},
										autonomy={'continue': Autonomy.Off})

			# x:213 y:41
			OperatableStateMachine.add('Move_to_Home',
										self.use_behavior(Move_to_HomeSM, 'Move_to_Home'),
										transitions={'finished': 'Camera moet hier', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:624 y:35
			OperatableStateMachine.add('Stop conveyer',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'Move_gantry_Precon', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'poweroff'})

			# x:429 y:37
			OperatableStateMachine.add('Camera moet hier',
										WaitState(wait_time=1),
										transitions={'done': 'Stop conveyer'},
										autonomy={'done': Autonomy.Off})

			# x:849 y:44
			OperatableStateMachine.add('Move_gantry_Precon',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Hier moet Compute pick en move to pick etc ', 'planning_failed': 'retry', 'control_failed': 'retry', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_gantry_Pre_Conv', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:884 y:172
			OperatableStateMachine.add('retry',
										WaitState(wait_time=0.2),
										transitions={'done': 'Move_gantry_Precon'},
										autonomy={'done': Autonomy.Off})

			# x:1019 y:41
			OperatableStateMachine.add('Hier moet Compute pick en move to pick etc ',
										WaitState(wait_time=2),
										transitions={'done': 'Move to pre side'},
										autonomy={'done': Autonomy.Off})

			# x:1040 y:126
			OperatableStateMachine.add('Move to pre side',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'retry_2', 'control_failed': 'retry_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_gantry_Pre_side', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1034 y:271
			OperatableStateMachine.add('retry_2',
										WaitState(wait_time=0.2),
										transitions={'done': 'Move to pre side'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
