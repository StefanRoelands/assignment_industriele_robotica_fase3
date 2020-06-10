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
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_states.GripperEnable import VacuumGripperControlState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.compute_drop_bins import ComputeDropBinsState
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Jun 02 2020
@author: Wouter De Saegher, Stefan Roelands
'''
class DroppenSM(Behavior):
	'''
	Droppen van de parts in de juiste bin
	'''


	def __init__(self):
		super(DroppenSM, self).__init__()
		self.name = 'Droppen'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1089 y:770, x:1143 y:423, x:1266 y:674
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed', 'end'], input_keys=['move_group_prefix', 'move_group_right_arm', 'move_group_left_arm', 'action_topic', 'camera_frame', 'camera_topic', 'ref_frame', 'move_group_gantry', 'robot_name', 'offset_var_left', 'offset_var_right', 'offset_gasket', 'offset_piston', 'arm_idL', 'arm_idR', 'config_name_Right_Home', 'config_name_Left_Home', 'config_name_RA_pre', 'config_name_LA_pre'])
		_state_machine.userdata.move_group_prefix = ''
		_state_machine.userdata.move_group_right_arm = ''
		_state_machine.userdata.move_group_left_arm = ''
		_state_machine.userdata.action_topic = ''
		_state_machine.userdata.camera_frame = '/ariac/logical_camera_0'
		_state_machine.userdata.camera_topic = 'logical_camera_0_frame'
		_state_machine.userdata.ref_frame = ''
		_state_machine.userdata.move_group_gantry = ''
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.offset_var_left = 0
		_state_machine.userdata.offset_var_right = 0
		_state_machine.userdata.offset_gasket = 0
		_state_machine.userdata.offset_piston = 0
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.tool_link_left = 'left_ee_link'
		_state_machine.userdata.tool_link_right = 'right_ee_link'
		_state_machine.userdata.arm_idL = ''
		_state_machine.userdata.arm_idR = ''
		_state_machine.userdata.config_name_Right_Home = ''
		_state_machine.userdata.config_name_Left_Home = ''
		_state_machine.userdata.pose = ''
		_state_machine.userdata.bin_id = ''
		_state_machine.userdata.bin1 = 'bin1'
		_state_machine.userdata.bin2 = 'bin2'
		_state_machine.userdata.offset_id = 0
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.config_name_R_bin1 = 'Gantry_PreGrasp_R_bin1'
		_state_machine.userdata.config_name_L_bin1 = 'Gantry_PreGrasp_L_bin1'
		_state_machine.userdata.config_name_bin1_var = ''
		_state_machine.userdata.config_name_RA_pre = ''
		_state_machine.userdata.config_name_LA_pre = ''
		_state_machine.userdata.offsetx_bin1 = 0
		_state_machine.userdata.offsety_bin1 = 0
		_state_machine.userdata.offsetx_set = 0.33418
		_state_machine.userdata.offsety_set = 0.1827866667
		_state_machine.userdata.plus1 = 1
		_state_machine.userdata.xproduct_bin1 = 0
		_state_machine.userdata.yproduct_bin1 = 0
		_state_machine.userdata.drie = 3
		_state_machine.userdata.twee = 2
		_state_machine.userdata.zero = 0
		_state_machine.userdata.offsety_bin2 = 0
		_state_machine.userdata.offsetx_bin2 = 0
		_state_machine.userdata.yproduct_bin2 = 0
		_state_machine.userdata.xproduct_bin2 = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:1623 y:384, x:886 y:382, x:1759 y:258
		_sm_offset_verschuiven_0 = OperatableStateMachine(outcomes=['finished', 'failed', 'end'], input_keys=['bin_id', 'bin1', 'zero', 'twee', 'drie', 'bin2', 'offsetx_set', 'offsety_set', 'plus1', 'offsetx_bin1', 'offsety_bin2', 'offsetx_bin2', 'offsety_bin1', 'xproduct_bin1', 'yproduct_bin1', 'xproduct_bin2', 'yproduct_bin2'], output_keys=['offsety_bin2', 'offsetx_bin2', 'offsety_bin1', 'offsetx_bin1'])

		with _sm_offset_verschuiven_0:
			# x:146 y:40
			OperatableStateMachine.add('bin1 vergelijk',
										EqualState(),
										transitions={'true': 'set offsetyyy', 'false': 'set offsetyy'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin1', 'value_b': 'bin_id'})

			# x:610 y:50
			OperatableStateMachine.add('x producten tellen',
										AddNumericState(),
										transitions={'done': '3 products x bin?'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'xproduct_bin1', 'value_b': 'plus1', 'result': 'xproduct_bin1'})

			# x:818 y:45
			OperatableStateMachine.add('3 products x bin?',
										EqualState(),
										transitions={'true': 'set offsety', 'false': 'finished'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'xproduct_bin1', 'value_b': 'drie'})

			# x:1069 y:54
			OperatableStateMachine.add('set offsety',
										ReplaceState(),
										transitions={'done': 'set offsety back to zero'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offsetx_set', 'result': 'offsety_bin1'})

			# x:1263 y:51
			OperatableStateMachine.add('set offsety back to zero',
										ReplaceState(),
										transitions={'done': '2 products x?'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero', 'result': 'offsety_bin1'})

			# x:1471 y:55
			OperatableStateMachine.add('2 products x?',
										EqualState(),
										transitions={'true': 'st offsetx back to zero', 'false': 'finished'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'twee', 'value_b': 'xproduct_bin1'})

			# x:389 y:38
			OperatableStateMachine.add('set offsetyyy',
										AddNumericState(),
										transitions={'done': 'x producten tellen'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'offsety_set', 'value_b': 'offsetx_bin1', 'result': 'offsetx_bin1'})

			# x:610 y:161
			OperatableStateMachine.add('y producten tellen_2',
										AddNumericState(),
										transitions={'done': '3 products y bin2?'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'yproduct_bin2', 'value_b': 'plus1', 'result': 'yproduct_bin2'})

			# x:818 y:152
			OperatableStateMachine.add('3 products y bin2?',
										EqualState(),
										transitions={'true': 'set offsety_2', 'false': 'finished'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'yproduct_bin2', 'value_b': 'drie'})

			# x:1066 y:165
			OperatableStateMachine.add('set offsety_2',
										ReplaceState(),
										transitions={'done': 'set offsety back to zero_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offsetx_set', 'result': 'offsetx_bin2'})

			# x:1263 y:176
			OperatableStateMachine.add('set offsety back to zero_2',
										ReplaceState(),
										transitions={'done': '2 products x bin2?'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero', 'result': 'offsety_bin2'})

			# x:1472 y:149
			OperatableStateMachine.add('2 products x bin2?',
										EqualState(),
										transitions={'true': 'set offsetx back to zero bin2', 'false': 'finished'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'twee', 'value_b': 'xproduct_bin2'})

			# x:389 y:152
			OperatableStateMachine.add('set offsetyy',
										AddNumericState(),
										transitions={'done': 'y producten tellen_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'offsety_set', 'value_b': 'offsety_bin2', 'result': 'offsety_bin2'})

			# x:1651 y:50
			OperatableStateMachine.add('st offsetx back to zero',
										ReplaceState(),
										transitions={'done': 'end'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero', 'result': 'offsetx_bin1'})

			# x:1653 y:146
			OperatableStateMachine.add('set offsetx back to zero bin2',
										ReplaceState(),
										transitions={'done': 'end'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero', 'result': 'offsetx_bin2'})


		# x:30 y:401, x:130 y:401
		_sm_setten_voor_right_1 = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['arm_idR', 'move_group_right_arm', 'config_name_Right_Home', 'tool_link_right', 'config_name_RA_pre', 'offset_var_right'], output_keys=['arm_id_var', 'move_group_var', 'config_name_var', 'tool_link_var', 'config_name_pre_var', 'offset_id'])

		with _sm_setten_voor_right_1:
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
										remapping={'value': 'offset_var_right', 'result': 'offset_id'})

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


		# x:30 y:401
		_sm_setten_voor_left_2 = OperatableStateMachine(outcomes=['finished'], input_keys=['arm_idL', 'move_group_left_arm', 'config_name_Left_Home', 'tool_link_left', 'config_name_LA_pre', 'offset_var_left'], output_keys=['arm_id_var', 'move_group_var', 'config_name_var', 'tool_link_var', 'config_name_pre_var', 'offset_id'])

		with _sm_setten_voor_left_2:
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
										transitions={'done': 'Set offset'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'move_group_left_arm', 'result': 'move_group_var'})

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

			# x:209 y:266
			OperatableStateMachine.add('Set offset',
										ReplaceState(),
										transitions={'done': 'set config name pre pick'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_var_left', 'result': 'offset_id'})



		with _state_machine:
			# x:97 y:17
			OperatableStateMachine.add('Setten voor Left',
										_sm_setten_voor_left_2,
										transitions={'finished': 'Left product'},
										autonomy={'finished': Autonomy.Inherit},
										remapping={'arm_idL': 'arm_idL', 'move_group_left_arm': 'move_group_left_arm', 'config_name_Left_Home': 'config_name_Left_Home', 'tool_link_left': 'tool_link_left', 'config_name_LA_pre': 'config_name_LA_pre', 'offset_var_left': 'offset_var_left', 'arm_id_var': 'arm_id_var', 'move_group_var': 'move_group_var', 'config_name_var': 'config_name_var', 'tool_link_var': 'tool_link_var', 'config_name_pre_var': 'config_name_pre_var', 'offset_id': 'offset_id'})

			# x:190 y:708
			OperatableStateMachine.add('Setten voor Right',
										_sm_setten_voor_right_1,
										transitions={'finished': 'Right product', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'arm_idR': 'arm_idR', 'move_group_right_arm': 'move_group_right_arm', 'config_name_Right_Home': 'config_name_Right_Home', 'tool_link_right': 'tool_link_right', 'config_name_RA_pre': 'config_name_RA_pre', 'offset_var_right': 'offset_var_right', 'arm_id_var': 'arm_id_var', 'move_group_var': 'move_group_var', 'config_name_var': 'config_name_var', 'tool_link_var': 'tool_link_var', 'config_name_pre_var': 'config_name_pre_var', 'offset_id': 'offset_id'})

			# x:77 y:172
			OperatableStateMachine.add('Left product',
										EqualState(),
										transitions={'true': 'bin1', 'false': 'bin2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'offset_gasket', 'value_b': 'offset_id'})

			# x:311 y:29
			OperatableStateMachine.add('bin1',
										ReplaceState(),
										transitions={'done': 'Zie bin1_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'bin1', 'result': 'bin_id'})

			# x:300 y:252
			OperatableStateMachine.add('bin2',
										ReplaceState(),
										transitions={'done': 'Zie bin1_2_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'bin2', 'result': 'bin_id'})

			# x:116 y:534
			OperatableStateMachine.add('Right product',
										EqualState(),
										transitions={'true': 'bin1_2', 'false': 'bin2_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'offset_gasket', 'value_b': 'offset_id'})

			# x:1673 y:531
			OperatableStateMachine.add('turn off vacuum',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'Move to home', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id_var'})

			# x:299 y:610
			OperatableStateMachine.add('bin1_2',
										ReplaceState(),
										transitions={'done': 'Zie bin1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'bin1', 'result': 'bin_id'})

			# x:294 y:377
			OperatableStateMachine.add('bin2_2',
										ReplaceState(),
										transitions={'done': 'Zie bin2_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'bin2', 'result': 'bin_id'})

			# x:731 y:21
			OperatableStateMachine.add('gantry bin pose',
										ReplaceState(),
										transitions={'done': 'Move to bin'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_L_bin1', 'result': 'config_name_bin1_var'})

			# x:722 y:342
			OperatableStateMachine.add('gantry bin pose_2',
										ReplaceState(),
										transitions={'done': 'Move to bin'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_R_bin1', 'result': 'config_name_bin1_var'})

			# x:1691 y:675
			OperatableStateMachine.add('Move to home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Offset verschuiven', 'planning_failed': 'retry_4', 'control_failed': 'retry_4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_var', 'move_group': 'move_group_var', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:987 y:701
			OperatableStateMachine.add('Right robot end',
										EqualState(),
										transitions={'true': 'finished', 'false': 'Setten voor Right'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'move_group_right_arm', 'value_b': 'move_group_var'})

			# x:954 y:146
			OperatableStateMachine.add('retry',
										WaitState(wait_time=0.1),
										transitions={'done': 'Move to bin'},
										autonomy={'done': Autonomy.Off})

			# x:1578 y:610
			OperatableStateMachine.add('retry_4',
										WaitState(wait_time=0.1),
										transitions={'done': 'Move to home'},
										autonomy={'done': Autonomy.Off})

			# x:956 y:21
			OperatableStateMachine.add('Move to bin',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Check for bin', 'planning_failed': 'retry', 'control_failed': 'retry', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin1_var', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1691 y:248
			OperatableStateMachine.add('Computebin right',
										ComputeDropBinsState(joint_names=['right_shoulder_pan_joint', 'right_shoulder_lift_joint', 'right_elbow_joint', 'right_wrist_1_joint', 'right_wrist_2_joint', 'right_wrist_3_joint']),
										transitions={'continue': 'Move to drop', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_var', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_var', 'pose': 'pose', 'offset': 'offset_id', 'rotation': 'rotation', 'offsety': 'offsety', 'offsetx': 'offsetx', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1550 y:336
			OperatableStateMachine.add('Computebin left',
										ComputeDropBinsState(joint_names=['left_shoulder_pan_joint', 'left_shoulder_lift_joint', 'left_elbow_joint', 'left_wrist_1_joint', 'left_wrist_2_joint', 'left_wrist_3_joint']),
										transitions={'continue': 'Move to drop', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_var', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_var', 'pose': 'pose', 'offset': 'offset_id', 'rotation': 'rotation', 'offsety': 'offsety', 'offsetx': 'offsetx', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:516 y:599
			OperatableStateMachine.add('Zie bin1',
										GetObjectPoseState(object_frame='bin1_frame', ref_frame='world'),
										transitions={'continue': 'gantry bin pose_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'pose'})

			# x:529 y:34
			OperatableStateMachine.add('Zie bin1_2',
										GetObjectPoseState(object_frame='bin1_frame', ref_frame='world'),
										transitions={'continue': 'gantry bin pose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'pose'})

			# x:534 y:239
			OperatableStateMachine.add('Zie bin1_2_2',
										GetObjectPoseState(object_frame='bin2_frame', ref_frame='world'),
										transitions={'continue': 'gantry bin pose_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'pose'})

			# x:523 y:373
			OperatableStateMachine.add('Zie bin2_2',
										GetObjectPoseState(object_frame='bin2_frame', ref_frame='world'),
										transitions={'continue': 'gantry bin pose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'pose'})

			# x:1668 y:30
			OperatableStateMachine.add('Right robot end_2',
										EqualState(),
										transitions={'true': 'Computebin right', 'false': 'Computebin left'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'move_group_right_arm', 'value_b': 'move_group_var'})

			# x:1657 y:420
			OperatableStateMachine.add('Move to drop',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'turn off vacuum', 'planning_failed': 'failed', 'control_failed': 'turn off vacuum'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group_var', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1428 y:672
			OperatableStateMachine.add('Offset verschuiven',
										_sm_offset_verschuiven_0,
										transitions={'finished': 'Right robot end', 'failed': 'failed', 'end': 'end'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'end': Autonomy.Inherit},
										remapping={'bin_id': 'bin_id', 'bin1': 'bin1', 'zero': 'zero', 'twee': 'twee', 'drie': 'drie', 'bin2': 'bin2', 'offsetx_set': 'offsetx_set', 'offsety_set': 'offsety_set', 'plus1': 'plus1', 'offsetx_bin1': 'offsetx_bin1', 'offsety_bin2': 'offsety_bin2', 'offsetx_bin2': 'offsetx_bin2', 'offsety_bin1': 'offsety_bin1', 'xproduct_bin1': 'xproduct_bin1', 'yproduct_bin1': 'yproduct_bin1', 'xproduct_bin2': 'xproduct_bin2', 'yproduct_bin2': 'yproduct_bin2'})

			# x:1156 y:3
			OperatableStateMachine.add('Check for bin',
										EqualState(),
										transitions={'true': 'set offset voor bin 1', 'false': 'set offset voor bin 2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin1', 'value_b': 'bin_id'})

			# x:1406 y:0
			OperatableStateMachine.add('set offset voor bin 1',
										ReplaceState(),
										transitions={'done': 'set offset voor y bin 1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offsetx_bin1', 'result': 'offsetx'})

			# x:1441 y:64
			OperatableStateMachine.add('set offset voor y bin 1',
										ReplaceState(),
										transitions={'done': 'Right robot end_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offsety_bin1', 'result': 'offsety'})

			# x:1236 y:110
			OperatableStateMachine.add('set offset voor bin 2',
										ReplaceState(),
										transitions={'done': 'set offset voor y bin 2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offsetx_bin2', 'result': 'offsetx'})

			# x:1425 y:141
			OperatableStateMachine.add('set offset voor y bin 2',
										ReplaceState(),
										transitions={'done': 'Right robot end_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offsety_bin2', 'result': 'offsety'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
