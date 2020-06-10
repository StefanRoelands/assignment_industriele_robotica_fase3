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
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from ariac_flexbe_behaviors.oppakken_sm import OppakkenSM
from ariac_flexbe_behaviors.droppen_sm import DroppenSM
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
		self.add_behavior(DroppenSM, 'Droppen')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1648 y:487, x:394 y:242
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.config_name_gantry_Pre_Conv_LA = 'Gantry_PreGrasp_Conv_LA'
		_state_machine.userdata.move_group_gantry = 'Gantry'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.poweroff = 0
		_state_machine.userdata.Partsaantal = 0
		_state_machine.userdata.Partsvast = 3
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
		_state_machine.userdata.config_name_gantry_Pre_Conv_RA = 'Gantry_PreGrasp_Conv_RA'
		_state_machine.userdata.config_name_RA_pre = 'config_name_RA_pre'
		_state_machine.userdata.config_name_LA_pre = 'config_name_LA_pre'

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
										remapping={'arm_idL': 'arm_idL', 'arm_idR': 'arm_idR', 'config_name_PreSide': 'config_name_PreSide', 'config_name_Right_Home': 'config_name_Right_Home', 'config_name_Left_Home': 'config_name_Left_Home', 'config_name_gantry': 'config_name_gantry'})

			# x:977 y:473
			OperatableStateMachine.add('3 parts?',
										EqualState(),
										transitions={'true': 'finished', 'false': 'Start conveyer'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'Partsvast', 'value_b': 'Partsaantal'})

			# x:1233 y:370
			OperatableStateMachine.add('increase',
										AddNumericState(),
										transitions={'done': '3 parts?'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'Plus1', 'value_b': 'Partsaantal', 'result': 'Partsaantal'})

			# x:601 y:399
			OperatableStateMachine.add('Start conveyer',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'Oppakken', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'poweron'})

			# x:823 y:35
			OperatableStateMachine.add('Oppakken',
										self.use_behavior(OppakkenSM, 'Oppakken'),
										transitions={'finished': 'Droppen', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part': 'part', 'pose': 'pose', 'move_group_prefix': 'move_group_prefix', 'move_group_right_arm': 'move_group_right_arm', 'move_group_left_arm': 'move_group_left_arm', 'action_topic': 'action_topic', 'camera_frame': 'camera_frame', 'camera_topic': 'camera_topic', 'poweroff': 'poweroff', 'ref_frame': 'ref_frame', 'move_group_gantry': 'move_group_gantry', 'robot_name': 'robot_name', 'config_name_Left_Home': 'config_name_Left_Home', 'config_name_Right_Home': 'config_name_Right_Home', 'arm_idL': 'arm_idL', 'arm_idR': 'arm_idR', 'config_name_gantry_Pre_Conv_RA': 'config_name_gantry_Pre_Conv_RA', 'config_name_gantry_Pre_Conv_LA': 'config_name_gantry_Pre_Conv_LA', 'config_name_RA_pre': 'config_name_RA_pre', 'config_name_LA_pre': 'config_name_LA_pre', 'offset_var_left': 'offset_var_left', 'offset_var_right': 'offset_var_right', 'offset_gasket': 'offset_gasket', 'offset_piston': 'offset_piston'})

			# x:1314 y:156
			OperatableStateMachine.add('Droppen',
										self.use_behavior(DroppenSM, 'Droppen'),
										transitions={'finished': 'increase', 'failed': 'failed', 'end': 'finished'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'end': Autonomy.Inherit},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group_right_arm': 'move_group_right_arm', 'move_group_left_arm': 'move_group_left_arm', 'action_topic': 'action_topic', 'camera_frame': 'camera_frame', 'camera_topic': 'camera_topic', 'ref_frame': 'ref_frame', 'move_group_gantry': 'move_group_gantry', 'robot_name': 'robot_name', 'offset_var_left': 'offset_var_left', 'offset_var_right': 'offset_var_right', 'offset_gasket': 'offset_gasket', 'offset_piston': 'offset_piston', 'arm_idL': 'arm_idL', 'arm_idR': 'arm_idR', 'config_name_Right_Home': 'config_name_Right_Home', 'config_name_Left_Home': 'config_name_Left_Home', 'config_name_RA_pre': 'config_name_RA_pre', 'config_name_LA_pre': 'config_name_LA_pre'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
