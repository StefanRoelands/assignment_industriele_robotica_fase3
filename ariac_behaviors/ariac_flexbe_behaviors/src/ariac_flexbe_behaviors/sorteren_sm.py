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
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from flexbe_states.wait_state import WaitState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from ariac_flexbe_behaviors.oppakken_sm import OppakkenSM
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
		self.add_behavior(OppakkenSM, 'Oppakken')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1648 y:487, x:394 y:242
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.config_name_gantry_Pre_Conv = 'Gantry_PreGrasp_Conv_LA'
		_state_machine.userdata.move_group_gantry = 'Gantry'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.poweroff = 0
		_state_machine.userdata.config_name_gantry_Pre_Grasp_bin = 'Gantry_PreGrasp_Right_bins_2'
		_state_machine.userdata.Partsaantal = 0
		_state_machine.userdata.Partsvast = 6
		_state_machine.userdata.Plus1 = 1
		_state_machine.userdata.poweron = 100
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.camera_topic = '/ariac/logical_camera_4'
		_state_machine.userdata.camera_frame = 'logical_camera_4_frame'
		_state_machine.userdata.part = ''
		_state_machine.userdata.pose = ''
		_state_machine.userdata.move_group_right_arm = 'Right_Arm'
		_state_machine.userdata.move_group_left_arm = 'Left_Arm'
		_state_machine.userdata.arm_idL = 'left'
		_state_machine.userdata.arm_idR = 'right'
		_state_machine.userdata.config_name_Left_Home = ''
		_state_machine.userdata.config_name_Right_Home = ''

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
										transitions={'finished': 'Oppakken', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'config_name_PreSide': 'config_name_PreSide', 'config_name_right_arm': 'config_name_right_arm', 'config_name_left_arm': 'config_name_left_arm', 'config_name_gantry': 'config_name_gantry'})

			# x:1040 y:126
			OperatableStateMachine.add('Move to pre side',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Hier moet een behavior om te plaatsen', 'planning_failed': 'retry_2', 'control_failed': 'retry_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_gantry_Pre_Grasp_bin', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1034 y:271
			OperatableStateMachine.add('retry_2',
										WaitState(wait_time=0.2),
										transitions={'done': 'Move to pre side'},
										autonomy={'done': Autonomy.Off})

			# x:1278 y:109
			OperatableStateMachine.add('Hier moet een behavior om te plaatsen',
										WaitState(wait_time=2),
										transitions={'done': 'increase'},
										autonomy={'done': Autonomy.Off})

			# x:977 y:473
			OperatableStateMachine.add('6 parts?',
										EqualState(),
										transitions={'true': 'finished', 'false': 'Start conveyer'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'Partsvast', 'value_b': 'Partsaantal'})

			# x:1233 y:370
			OperatableStateMachine.add('increase',
										AddNumericState(),
										transitions={'done': '6 parts?'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'Plus1', 'value_b': 'Partsaantal', 'result': 'Partsaantal'})

			# x:682 y:223
			OperatableStateMachine.add('Start conveyer',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'Oppakken', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'poweron'})

			# x:1009 y:31
			OperatableStateMachine.add('Oppakken',
										self.use_behavior(OppakkenSM, 'Oppakken'),
										transitions={'finished': 'Move to pre side', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part': 'part', 'pose': 'pose', 'move_group_prefix': 'move_group_prefix', 'move_group_right_arm': 'move_group_right_arm', 'move_group_left_arm': 'move_group_left_arm', 'action_topic': 'action_topic', 'camera_frame': 'camera_frame', 'camera_topic': 'camera_topic', 'poweroff': 'poweroff', 'ref_frame': 'ref_frame', 'config_name_gantry_Pre_Conv': 'config_name_gantry_Pre_Conv', 'move_group_gantry': 'move_group_gantry', 'robot_name': 'robot_name', 'config_name_Left_Home': 'config_name_Left_Home', 'config_name_Right_Home': 'config_name_Right_Home', 'arm_idL': 'arm_idL', 'arm_idR': 'arm_idR'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
