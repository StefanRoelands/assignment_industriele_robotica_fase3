#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue May 26 2020
@author: Stefan Roelands, Wouter de Saegher
'''
class Move_to_HomeSM(Behavior):
	'''
	Robots en gantry naar Home bewegen
	'''


	def __init__(self):
		super(Move_to_HomeSM, self).__init__()
		self.name = 'Move_to_Home'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:805 y:349, x:467 y:416
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.config_name_gantry = 'Gantry_Home'
		_state_machine.userdata.move_group_gantry = 'Gantry'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.move_group_right_arm = 'Right_Arm'
		_state_machine.userdata.config_name_left_arm = 'Left_Home'
		_state_machine.userdata.config_name_right_arm = 'Right_Home'
		_state_machine.userdata.move_group_left_arm = 'Left_Arm'
		_state_machine.userdata.config_name_PreSide = 'Gantry_Pre_Side'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:164 y:146
			OperatableStateMachine.add('Move_left_arm_home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Move_right_arm_home', 'planning_failed': 'Retry', 'control_failed': 'Retry', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_left_arm', 'move_group': 'move_group_left_arm', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:201 y:38
			OperatableStateMachine.add('Retry',
										WaitState(wait_time=0.3),
										transitions={'done': 'Move_left_arm_home'},
										autonomy={'done': Autonomy.Off})

			# x:332 y:148
			OperatableStateMachine.add('Move_right_arm_home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Move_gantry_home', 'planning_failed': 'Retry_2', 'control_failed': 'Retry_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_right_arm', 'move_group': 'move_group_right_arm', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:362 y:37
			OperatableStateMachine.add('Retry_2',
										WaitState(wait_time=0.3),
										transitions={'done': 'Move_right_arm_home'},
										autonomy={'done': Autonomy.Off})

			# x:525 y:149
			OperatableStateMachine.add('Move_gantry_home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'Retry_3', 'control_failed': 'Retry_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_gantry', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:549 y:32
			OperatableStateMachine.add('Retry_3',
										WaitState(wait_time=0.3),
										transitions={'done': 'Move_gantry_home'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
