#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_states.message_state import MessageState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.GripperEnable import VacuumGripperControlState
from ariac_flexbe_states.detect_first_part_camera_ariac_state import DetectFirstPartCameraAriacState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_support_flexbe_states.equal_state import EqualState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 29 2020
@author: Wouter
'''
class OppakkenSM(Behavior):
	'''
	Oppakken van de onderdelen van de conveyer
	'''


	def __init__(self):
		super(OppakkenSM, self).__init__()
		self.name = 'Oppakken'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1552 y:671, x:1127 y:251
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part', 'pose', 'move_group_prefix', 'move_group_right_arm', 'move_group_left_arm', 'action_topic', 'camera_frame', 'camera_topic', 'poweroff', 'ref_frame', 'move_group_gantry', 'robot_name', 'config_name_Left_Home', 'config_name_Right_Home', 'arm_idL', 'arm_idR', 'config_name_gantry_Pre_Conv_RA', 'config_name_gantry_Pre_Conv_LA', 'config_name_RA_pre', 'config_name_LA_pre'], output_keys=['offset_var_left', 'offset_var_right', 'offset_gasket', 'offset_piston'])
		_state_machine.userdata.part = ''
		_state_machine.userdata.pose = ''
		_state_machine.userdata.tool_link_right = 'right_ee_link'
		_state_machine.userdata.tool_link_left = 'left_ee_link'
		_state_machine.userdata.offset_piston = 0.02
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.move_group_prefix = ''
		_state_machine.userdata.move_group_left_arm = ''
		_state_machine.userdata.move_group_right_arm = ''
		_state_machine.userdata.action_topic = ''
		_state_machine.userdata.camera_frame = ''
		_state_machine.userdata.camera_topic = ''
		_state_machine.userdata.poweroff = 0
		_state_machine.userdata.ref_frame = ''
		_state_machine.userdata.config_name_gantry_Pre_Conv_RA = ''
		_state_machine.userdata.move_group_gantry = ''
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.arm_idL = ''
		_state_machine.userdata.config_name_Left_Home = ''
		_state_machine.userdata.config_name_Right_Home = ''
		_state_machine.userdata.arm_idR = ''
		_state_machine.userdata.config_name_gantry_Pre_Conv_LA = ''
		_state_machine.userdata.poweron = 100
		_state_machine.userdata.part_set = 'gasket_part_blue'
		_state_machine.userdata.offset_gasket = 0.035
		_state_machine.userdata.offset_var = 0
		_state_machine.userdata.offset_var_left = 0
		_state_machine.userdata.offset_var_right = 0
		_state_machine.userdata.config_name_LA_pre = ''
		_state_machine.userdata.config_name_RA_pre = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:257 y:421, x:130 y:360
		_sm_setten_voor_right_0 = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['arm_idR', 'move_group_right_arm', 'config_name_Right_Home', 'tool_link_right', 'config_name_gantry_Pre_Conv_RA', 'config_name_RA_pre'], output_keys=['arm_id_var', 'move_group_var', 'config_name_var', 'tool_link_var', 'config_name_gantry_var', 'config_name_pre_var'])

		with _sm_setten_voor_right_0:
			# x:30 y:40
			OperatableStateMachine.add('Set arm id',
										ReplaceState(),
										transitions={'done': 'Set config name'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'arm_idR', 'result': 'arm_id_var'})

			# x:30 y:117
			OperatableStateMachine.add('Set config name',
										ReplaceState(),
										transitions={'done': 'Set toollink'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_Right_Home', 'result': 'config_name_var'})

			# x:30 y:194
			OperatableStateMachine.add('Set toollink',
										ReplaceState(),
										transitions={'done': 'Set move group'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'tool_link_right', 'result': 'tool_link_var'})

			# x:30 y:271
			OperatableStateMachine.add('Set move group',
										ReplaceState(),
										transitions={'done': 'Set config name_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'move_group_right_arm', 'result': 'move_group_var'})

			# x:230 y:266
			OperatableStateMachine.add('Set config name_2',
										ReplaceState(),
										transitions={'done': 'set config pre pick'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_gantry_Pre_Conv_RA', 'result': 'config_name_gantry_var'})

			# x:233 y:344
			OperatableStateMachine.add('laat zien',
										MessageState(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'move_group_var'})

			# x:438 y:268
			OperatableStateMachine.add('set config pre pick',
										ReplaceState(),
										transitions={'done': 'laat zien'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_RA_pre', 'result': 'config_name_pre_var'})


		# x:627 y:357, x:130 y:360
		_sm_setten_voor_left_1 = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['arm_idL', 'move_group_left_arm', 'config_name_Left_Home', 'tool_link_left', 'config_name_gantry_Pre_Conv_LA', 'config_name_LA_pre'], output_keys=['arm_id_var', 'move_group_var', 'config_name_var', 'tool_link_var', 'config_name_gantry_var', 'config_name_pre_var'])

		with _sm_setten_voor_left_1:
			# x:30 y:40
			OperatableStateMachine.add('Set arm id',
										ReplaceState(),
										transitions={'done': 'Set config name'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'arm_idL', 'result': 'arm_id_var'})

			# x:30 y:117
			OperatableStateMachine.add('Set config name',
										ReplaceState(),
										transitions={'done': 'Set toollink'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_Left_Home', 'result': 'config_name_var'})

			# x:30 y:194
			OperatableStateMachine.add('Set toollink',
										ReplaceState(),
										transitions={'done': 'Set move group'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'tool_link_left', 'result': 'tool_link_var'})

			# x:30 y:271
			OperatableStateMachine.add('Set move group',
										ReplaceState(),
										transitions={'done': 'Set config name_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'move_group_left_arm', 'result': 'move_group_var'})

			# x:209 y:266
			OperatableStateMachine.add('Set config name_2',
										ReplaceState(),
										transitions={'done': 'set config name pre pick'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_gantry_Pre_Conv_LA', 'result': 'config_name_gantry_var'})

			# x:397 y:386
			OperatableStateMachine.add('laat zien',
										MessageState(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'move_group_var'})

			# x:383 y:274
			OperatableStateMachine.add('set config name pre pick',
										ReplaceState(),
										transitions={'done': 'laat zien'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_LA_pre', 'result': 'config_name_pre_var'})



		with _state_machine:
			# x:52 y:265
			OperatableStateMachine.add('Setten voor Left',
										_sm_setten_voor_left_1,
										transitions={'finished': 'Detect_part', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'arm_idL': 'arm_idL', 'move_group_left_arm': 'move_group_left_arm', 'config_name_Left_Home': 'config_name_Left_Home', 'tool_link_left': 'tool_link_left', 'config_name_gantry_Pre_Conv_LA': 'config_name_gantry_Pre_Conv_LA', 'config_name_LA_pre': 'config_name_LA_pre', 'arm_id_var': 'arm_id_var', 'move_group_var': 'move_group_var', 'config_name_var': 'config_name_var', 'tool_link_var': 'tool_link_var', 'config_name_gantry_var': 'config_name_gantry_var', 'config_name_pre_var': 'config_name_pre_var'})

			# x:190 y:143
			OperatableStateMachine.add('retrycamera',
										WaitState(wait_time=0.5),
										transitions={'done': 'Detect_part'},
										autonomy={'done': Autonomy.Off})

			# x:874 y:6
			OperatableStateMachine.add('Move_gantry_Precon',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Move arm pre pick', 'planning_failed': 'retry_2', 'control_failed': 'retry_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_gantry_var', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:677 y:8
			OperatableStateMachine.add('Stop conveyer',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'Move_gantry_Precon', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'poweroff'})

			# x:1406 y:5
			OperatableStateMachine.add('computeleft',
										ComputeGraspAriacState(joint_names=['left_shoulder_pan_joint', 'left_shoulder_lift_joint', 'left_elbow_joint', 'left_wrist_1_joint', 'left_wrist_2_joint', 'left_wrist_3_joint']),
										transitions={'continue': 'move to pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_var', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_var', 'pose': 'pose', 'offset': 'offset_var', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1661 y:116
			OperatableStateMachine.add('Gripperon',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'Move arm pre pick_2', 'failed': 'Rightrobot?', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id_var'})

			# x:1674 y:302
			OperatableStateMachine.add('Move to transpos',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Rightrobot end', 'planning_failed': 'retry_3', 'control_failed': 'Rightrobot end', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_var', 'move_group': 'move_group_var', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1911 y:11
			OperatableStateMachine.add('retry',
										WaitState(wait_time=0.1),
										transitions={'done': 'move to pick'},
										autonomy={'done': Autonomy.Off})

			# x:1870 y:336
			OperatableStateMachine.add('retry_3',
										WaitState(wait_time=0.1),
										transitions={'done': 'Move to transpos'},
										autonomy={'done': Autonomy.Off})

			# x:119 y:35
			OperatableStateMachine.add('Detect_part',
										DetectFirstPartCameraAriacState(part_list=['piston_rod_part_red', 'gasket_part_blue'], time_out=5),
										transitions={'continue': 'Gasket?', 'failed': 'retrycamera', 'not_found': 'retrycamera'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'pose'})

			# x:1668 y:9
			OperatableStateMachine.add('move to pick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'Gripperon', 'planning_failed': 'retry', 'control_failed': 'Gripperon'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group_var', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:346 y:387
			OperatableStateMachine.add('start conveyer',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'Detect_part', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'poweron'})

			# x:1142 y:5
			OperatableStateMachine.add('Rightrobot?',
										EqualState(),
										transitions={'true': 'computeright', 'false': 'computeleft'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'move_group_right_arm', 'value_b': 'move_group_var'})

			# x:1399 y:67
			OperatableStateMachine.add('computeright',
										ComputeGraspAriacState(joint_names=['right_shoulder_pan_joint', 'right_shoulder_lift_joint', 'right_elbow_joint', 'right_wrist_1_joint', 'right_wrist_2_joint', 'right_wrist_3_joint']),
										transitions={'continue': 'move to pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_var', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_var', 'pose': 'pose', 'offset': 'offset_var', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1576 y:390
			OperatableStateMachine.add('Rightrobot end',
										EqualState(),
										transitions={'true': 'offset Right', 'false': 'offset Left'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'move_group_right_arm', 'value_b': 'move_group_var'})

			# x:1086 y:371
			OperatableStateMachine.add('Setten voor Right',
										_sm_setten_voor_right_0,
										transitions={'finished': 'start conveyer', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'arm_idR': 'arm_idR', 'move_group_right_arm': 'move_group_right_arm', 'config_name_Right_Home': 'config_name_Right_Home', 'tool_link_right': 'tool_link_right', 'config_name_gantry_Pre_Conv_RA': 'config_name_gantry_Pre_Conv_RA', 'config_name_RA_pre': 'config_name_RA_pre', 'arm_id_var': 'arm_id_var', 'move_group_var': 'move_group_var', 'config_name_var': 'config_name_var', 'tool_link_var': 'tool_link_var', 'config_name_gantry_var': 'config_name_gantry_var', 'config_name_pre_var': 'config_name_pre_var'})

			# x:837 y:91
			OperatableStateMachine.add('retry_2',
										WaitState(wait_time=0.2),
										transitions={'done': 'Move_gantry_Precon'},
										autonomy={'done': Autonomy.Off})

			# x:357 y:18
			OperatableStateMachine.add('Gasket?',
										EqualState(),
										transitions={'true': 'offset gasket', 'false': 'Offset piston'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_set', 'value_b': 'part'})

			# x:521 y:10
			OperatableStateMachine.add('Offset piston',
										ReplaceState(),
										transitions={'done': 'Stop conveyer'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_piston', 'result': 'offset_var'})

			# x:518 y:81
			OperatableStateMachine.add('offset gasket',
										ReplaceState(),
										transitions={'done': 'Stop conveyer'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_gasket', 'result': 'offset_var'})

			# x:1470 y:524
			OperatableStateMachine.add('offset Right',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_var', 'result': 'offset_var_right'})

			# x:1303 y:372
			OperatableStateMachine.add('offset Left',
										ReplaceState(),
										transitions={'done': 'Setten voor Right'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_var', 'result': 'offset_var_left'})

			# x:1096 y:67
			OperatableStateMachine.add('Move arm pre pick',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Rightrobot?', 'planning_failed': 'retry_2', 'control_failed': 'retry_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_pre_var', 'move_group': 'move_group_var', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1669 y:201
			OperatableStateMachine.add('Move arm pre pick_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Move to transpos', 'planning_failed': 'retry_4', 'control_failed': 'Move to transpos', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_pre_var', 'move_group': 'move_group_var', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1902 y:197
			OperatableStateMachine.add('retry_4',
										WaitState(wait_time=0.1),
										transitions={'done': 'Move arm pre pick_2'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
