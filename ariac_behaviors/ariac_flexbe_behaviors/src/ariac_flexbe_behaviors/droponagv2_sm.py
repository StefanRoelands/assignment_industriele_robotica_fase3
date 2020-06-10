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
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.GripperEnable import VacuumGripperControlState
from ariac_flexbe_states.gripper_controle_state import GripperControle
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
from ariac_flexbe_states.compute_grasp_part_offset_ariac_state import ComputeGraspPartOffsetAriacState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 29 2020
@author: Wouter de Saegher, Stefan Roelands
'''
class DropOnAGV2SM(Behavior):
	'''
	Droppen van de producten op de juiste AGV
	'''


	def __init__(self):
		super(DropOnAGV2SM, self).__init__()
		self.name = 'DropOnAGV2'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:779 y:685, x:708 y:446
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_pose_right', 'part_pose_left', 'PreDropright', 'PreDropleft', 'arm_id_right', 'arm_id_left'])
		_state_machine.userdata.part_pose_right = []
		_state_machine.userdata.part_pose_left = []
		_state_machine.userdata.PreDropleft = ''
		_state_machine.userdata.PreDropright = ''
		_state_machine.userdata.value_b = 0
		_state_machine.userdata.value_a = 0
		_state_machine.userdata.arm_id_left = ''
		_state_machine.userdata.arm_id_right = ''
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.tool_link_right = 'right_ee_link'
		_state_machine.userdata.tool_link_left = 'left_ee_link'
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.move_group_left_arm = 'Left_Arm'
		_state_machine.userdata.move_group_right_arm = 'Right_Arm'
		_state_machine.userdata.config_name_right_arm = 'Right_Home'
		_state_machine.userdata.config_name_left_arm = 'Left_Home'
		_state_machine.userdata.move_group_prefix = '/ariac/gantry'
		_state_machine.userdata.move_group_gantry = 'Gantry'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.drop_offset = 0.145
		_state_machine.userdata.config_name_gantry = 'Gantry_Home'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:41 y:519
			OperatableStateMachine.add('GantryHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ArmHome_3', 'planning_failed': 'Retry_7', 'control_failed': 'Retry_7', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_gantry', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:216 y:127
			OperatableStateMachine.add('PreDropTray',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComputeDrop', 'planning_failed': 'Retry', 'control_failed': 'Retry', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'PreDropleft', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:237 y:8
			OperatableStateMachine.add('Retry',
										WaitState(wait_time=0.5),
										transitions={'done': 'PreDropTray'},
										autonomy={'done': Autonomy.Off})

			# x:603 y:127
			OperatableStateMachine.add('MoveToDrop',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperOff', 'planning_failed': 'Retry_2', 'control_failed': 'Retry_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group_left_arm', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:640 y:3
			OperatableStateMachine.add('Retry_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'MoveToDrop'},
										autonomy={'done': Autonomy.Off})

			# x:814 y:126
			OperatableStateMachine.add('GripperOff',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'ArmHome', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id_left'})

			# x:1028 y:124
			OperatableStateMachine.add('ArmHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GripperControl', 'planning_failed': 'Retry_3', 'control_failed': 'Retry_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_left_arm', 'move_group': 'move_group_left_arm', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1054 y:7
			OperatableStateMachine.add('Retry_3',
										WaitState(wait_time=0.5),
										transitions={'done': 'ArmHome'},
										autonomy={'done': Autonomy.Off})

			# x:1216 y:123
			OperatableStateMachine.add('GripperControl',
										GripperControle(),
										transitions={'Active': 'GetAGVPose_2', 'Not_active': 'GantryHome_2', 'invalid_arm_id': 'failed'},
										autonomy={'Active': Autonomy.Off, 'Not_active': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id_right'})

			# x:1436 y:124
			OperatableStateMachine.add('GetAGVPose_2',
										GetObjectPoseState(object_frame='kit_tray_2', ref_frame='world'),
										transitions={'continue': 'PreDropTray_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'agv_pose_right'})

			# x:1428 y:232
			OperatableStateMachine.add('PreDropTray_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComputeDrop_2', 'planning_failed': 'Retry_4', 'control_failed': 'Retry_4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'PreDropright', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1644 y:233
			OperatableStateMachine.add('Retry_4',
										WaitState(wait_time=0.5),
										transitions={'done': 'PreDropTray_2'},
										autonomy={'done': Autonomy.Off})

			# x:1398 y:447
			OperatableStateMachine.add('MoveToDrop_2',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperOff_2', 'planning_failed': 'Retry_5', 'control_failed': 'Retry_5'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group_right_arm', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1637 y:452
			OperatableStateMachine.add('Retry_5',
										WaitState(wait_time=0.5),
										transitions={'done': 'MoveToDrop_2'},
										autonomy={'done': Autonomy.Off})

			# x:1397 y:582
			OperatableStateMachine.add('GripperOff_2',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'ArmHome_2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id_right'})

			# x:1417 y:689
			OperatableStateMachine.add('ArmHome_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GantryHome_2', 'planning_failed': 'Retry_6', 'control_failed': 'Retry_6', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_right_arm', 'move_group': 'move_group_right_arm', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1634 y:689
			OperatableStateMachine.add('Retry_6',
										WaitState(wait_time=0.5),
										transitions={'done': 'ArmHome_2'},
										autonomy={'done': Autonomy.Off})

			# x:53 y:627
			OperatableStateMachine.add('Retry_7',
										WaitState(wait_time=0.5),
										transitions={'done': 'GantryHome'},
										autonomy={'done': Autonomy.Off})

			# x:51 y:128
			OperatableStateMachine.add('GetAGVPose',
										GetObjectPoseState(object_frame='kit_tray_2', ref_frame='world'),
										transitions={'continue': 'PreDropTray', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'agv_pose_left'})

			# x:381 y:129
			OperatableStateMachine.add('ComputeDrop',
										ComputeGraspPartOffsetAriacState(joint_names=['left_shoulder_pan_joint', 'left_shoulder_lift_joint', 'left_elbow_joint', 'left_wrist_1_joint', 'left_wrist_2_joint', 'left_wrist_3_joint']),
										transitions={'continue': 'MoveToDrop', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_left_arm', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_left', 'pose': 'agv_pose_left', 'offset': 'drop_offset', 'rotation': 'rotation', 'part_pose': 'part_pose_left', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1388 y:336
			OperatableStateMachine.add('ComputeDrop_2',
										ComputeGraspPartOffsetAriacState(joint_names=['right_shoulder_pan_joint', 'right_shoulder_lift_joint', 'right_elbow_joint', 'right_wrist_1_joint', 'right_wrist_2_joint', 'right_wrist_3_joint']),
										transitions={'continue': 'MoveToDrop_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group_right_arm', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link_right', 'pose': 'agv_pose_right', 'offset': 'drop_offset', 'rotation': 'rotation', 'part_pose': 'part_pose_right', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:42 y:393
			OperatableStateMachine.add('ArmHome_3',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ArmHome_2_2', 'planning_failed': 'Retry_3_2', 'control_failed': 'Retry_3_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_left_arm', 'move_group': 'move_group_left_arm', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:229 y:401
			OperatableStateMachine.add('Retry_3_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'ArmHome_3'},
										autonomy={'done': Autonomy.Off})

			# x:43 y:250
			OperatableStateMachine.add('ArmHome_2_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GetAGVPose', 'planning_failed': 'Retry_6_2', 'control_failed': 'Retry_6_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_right_arm', 'move_group': 'move_group_right_arm', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:229 y:269
			OperatableStateMachine.add('Retry_6_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'ArmHome_2_2'},
										autonomy={'done': Autonomy.Off})

			# x:985 y:660
			OperatableStateMachine.add('GantryHome_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'Retry_7_2', 'control_failed': 'Retry_7_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_gantry', 'move_group': 'move_group_gantry', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1006 y:777
			OperatableStateMachine.add('Retry_7_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'GantryHome_2'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
