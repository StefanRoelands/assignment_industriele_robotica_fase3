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
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.GripperEnable import VacuumGripperControlState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue May 26 2020
@author: Stefan Roelands, Wouter de Saegher
'''
class ProgramBinsLeftSM(Behavior):
	'''
	Oppakken van de producten uit de bins met de linker arm
	'''


	def __init__(self):
		super(ProgramBinsLeftSM, self).__init__()
		self.name = 'ProgramBinsLeft'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1064 y:645, x:966 y:441
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['offset_part_left', 'PreGrasp', 'camera_topic', 'camera_frame', 'offset_part_left', 'part_type', 'arm_id_left', 'part_pose'], output_keys=['part_pose_left'])
		_state_machine.userdata.move_group_gantry = 'Gantry'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.move_group_right_arm = 'Right_Arm'
		_state_machine.userdata.config_name_left_arm = 'Left_Home'
		_state_machine.userdata.config_name_right_arm = 'Right_Home'
		_state_machine.userdata.move_group_left_arm = 'Left_Arm'
		_state_machine.userdata.config_name_PreSide = 'Gantry_Pre_Side'
		_state_machine.userdata.PreGrasp = ''
		_state_machine.userdata.camera_ref_frame = 'world'
		_state_machine.userdata.camera_topic = ''
		_state_machine.userdata.camera_frame = ''
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.offset_part_left = 0
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.tool_link_left = 'left_ee_link'
		_state_machine.userdata.arm_id_left = ''
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.part_pose_left = []

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
										transitions={'reached': 'PreSide', 'planning_failed': 'Retry_2', 'control_failed': 'Retry_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_right_arm', 'move_group': 'move_group_right_arm', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:362 y:37
			OperatableStateMachine.add('Retry_2',
										WaitState(wait_time=0.3),
										transitions={'done': 'Move_right_arm_home'},
										autonomy={'done': Autonomy.Off})

			# x:745 y:152
			OperatableStateMachine.add('PreSide',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'DetectPart', 'planning_failed': 'Retry_4', 'control_failed': 'Retry_4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PreSide', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:773 y:27
			OperatableStateMachine.add('Retry_4',
										WaitState(wait_time=0.3),
										transitions={'done': 'PreSide'},
										autonomy={'done': Autonomy.Off})

			# x:1111 y:151
			OperatableStateMachine.add('PreGrasp',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComputePick', 'planning_failed': 'Retry_5', 'control_failed': 'Retry_5', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'PreGrasp', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1129 y:33
			OperatableStateMachine.add('Retry_5',
										WaitState(wait_time=0.3),
										transitions={'done': 'PreGrasp'},
										autonomy={'done': Autonomy.Off})

			# x:1308 y:150
			OperatableStateMachine.add('ComputePick',
										ComputeGraspAriacState(joint_names=['left_shoulder_pan_joint', 'left_shoulder_lift_joint', 'left_elbow_joint', 'left_wrist_1_joint', 'left_wrist_2_joint', 'left_wrist_3_joint']),
										transitions={'continue': 'Move_to_pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_left_arm', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_left', 'pose': 'pose', 'offset': 'offset_part_left', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:918 y:149
			OperatableStateMachine.add('DetectPart',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'PreGrasp', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:1552 y:44
			OperatableStateMachine.add('Retry_6',
										WaitState(wait_time=0.3),
										transitions={'done': 'Move_to_pick'},
										autonomy={'done': Autonomy.Off})

			# x:1501 y:148
			OperatableStateMachine.add('Move_to_pick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperOn', 'planning_failed': 'Retry_6', 'control_failed': 'GripperOn'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group_left_arm', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1510 y:247
			OperatableStateMachine.add('GripperOn',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'Move_left_arm_home_2', 'failed': 'ComputePick', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id_left'})

			# x:1517 y:381
			OperatableStateMachine.add('Move_left_arm_home_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'PreSide_2', 'planning_failed': 'Retry_7', 'control_failed': 'Retry_7', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_left_arm', 'move_group': 'move_group_left_arm', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1729 y:398
			OperatableStateMachine.add('Retry_7',
										WaitState(wait_time=0.3),
										transitions={'done': 'Move_left_arm_home_2'},
										autonomy={'done': Autonomy.Off})

			# x:1525 y:496
			OperatableStateMachine.add('PreSide_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Pose', 'planning_failed': 'Retry_8', 'control_failed': 'Retry_8', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_PreSide', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1730 y:498
			OperatableStateMachine.add('Retry_8',
										WaitState(wait_time=0.3),
										transitions={'done': 'PreSide_2'},
										autonomy={'done': Autonomy.Off})

			# x:1252 y:599
			OperatableStateMachine.add('Pose',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'part_pose', 'result': 'part_pose_left'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
