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
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_behaviors.programbinsleft_sm import ProgramBinsLeftSM
from ariac_flexbe_behaviors.programshelvesleft_sm import ProgramShelvesLeftSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 29 2020
@author: Wouter de Saegher, Stefan Roelands
'''
class SelectorStateLeftSM(Behavior):
	'''
	Selecteert de juiste variabelen bij het juiste pad
	'''


	def __init__(self):
		super(SelectorStateLeftSM, self).__init__()
		self.name = 'SelectorStateLeft'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(ProgramBinsLeftSM, 'ProgramBinsLeft')
		self.add_behavior(ProgramShelvesLeftSM, 'ProgramShelvesLeft')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1250 y:199, x:781 y:695
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['bin_id', 'part_type', 'arm_id_left', 'part_pose'], output_keys=['part_pose_left'])
		_state_machine.userdata.bin_id = ''
		_state_machine.userdata.bin14 = 'bin14'
		_state_machine.userdata.bin3 = 'bin3'
		_state_machine.userdata.shelf6 = 'shelf6'
		_state_machine.userdata.shelf3 = 'shelf3'
		_state_machine.userdata.camera_topic = ''
		_state_machine.userdata.camera_topic_bin14 = '/ariac/logical_camera_2'
		_state_machine.userdata.camera_topic_bin3 = '/ariac/logical_camera_1'
		_state_machine.userdata.camera_topic_shelf6 = '/ariac/logical_camera_6'
		_state_machine.userdata.camera_topic_shelf3 = '/ariac/logical_camera_5'
		_state_machine.userdata.camera_frame = ''
		_state_machine.userdata.camera_frame_bin14 = 'logical_camera_2_frame'
		_state_machine.userdata.camera_frame_bin3 = 'logical_camera_1_frame'
		_state_machine.userdata.camera_frame_shelf6 = 'logical_camera_6_frame'
		_state_machine.userdata.camera_frame_shelf3 = 'logical_camera_5_frame'
		_state_machine.userdata.offset_part_left = 0
		_state_machine.userdata.offset_pulley_red = 0.081
		_state_machine.userdata.offset_gear_red = 0.027
		_state_machine.userdata.offset_gear_blue = 0.027
		_state_machine.userdata.offset_gasket_red = 0.035
		_state_machine.userdata.PreGrasp = ''
		_state_machine.userdata.PreGrasp_bin14 = 'Gantry_PreGrasp_Left_bins_LA'
		_state_machine.userdata.PreGrasp_bin3 = 'Gantry_PreGrasp_Right_bins_LA'
		_state_machine.userdata.PreGrasp_shelf6 = 'Gantry_PreGrasp_shelves_RAR'
		_state_machine.userdata.PreGrasp_shelf3 = 'Gantry_PreGrasp_shelves_LAR'
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.arm_id_left = ''
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.part_pose_left = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('Binkeuze1',
										EqualState(),
										transitions={'true': 'Camera_topic1', 'false': 'Binkeuze2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_id', 'value_b': 'bin14'})

			# x:30 y:132
			OperatableStateMachine.add('Binkeuze2',
										EqualState(),
										transitions={'true': 'Camera_topic2', 'false': 'Shelfkeuze1'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_id', 'value_b': 'bin3'})

			# x:30 y:224
			OperatableStateMachine.add('Shelfkeuze1',
										EqualState(),
										transitions={'true': 'Camera_topic3', 'false': 'Shelfkeuze2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_id', 'value_b': 'shelf6'})

			# x:30 y:316
			OperatableStateMachine.add('Shelfkeuze2',
										EqualState(),
										transitions={'true': 'Camera_topic4', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_id', 'value_b': 'shelf3'})

			# x:203 y:37
			OperatableStateMachine.add('Camera_topic1',
										ReplaceState(),
										transitions={'done': 'Camera_frame1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic_bin14', 'result': 'camera_topic'})

			# x:201 y:134
			OperatableStateMachine.add('Camera_topic2',
										ReplaceState(),
										transitions={'done': 'Camera_frame2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic_bin3', 'result': 'camera_topic'})

			# x:202 y:225
			OperatableStateMachine.add('Camera_topic3',
										ReplaceState(),
										transitions={'done': 'Camera_frame3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic_shelf6', 'result': 'camera_topic'})

			# x:202 y:316
			OperatableStateMachine.add('Camera_topic4',
										ReplaceState(),
										transitions={'done': 'Camera_frame4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic_shelf3', 'result': 'camera_topic'})

			# x:369 y:39
			OperatableStateMachine.add('Camera_frame1',
										ReplaceState(),
										transitions={'done': 'Offset1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame_bin14', 'result': 'camera_frame'})

			# x:370 y:136
			OperatableStateMachine.add('Camera_frame2',
										ReplaceState(),
										transitions={'done': 'Offset2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame_bin3', 'result': 'camera_frame'})

			# x:370 y:226
			OperatableStateMachine.add('Camera_frame3',
										ReplaceState(),
										transitions={'done': 'Offset3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame_shelf6', 'result': 'camera_frame'})

			# x:371 y:317
			OperatableStateMachine.add('Camera_frame4',
										ReplaceState(),
										transitions={'done': 'Offset4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame_shelf3', 'result': 'camera_frame'})

			# x:539 y:39
			OperatableStateMachine.add('Offset1',
										ReplaceState(),
										transitions={'done': 'PreGrasp1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_gear_red', 'result': 'offset_part_left'})

			# x:539 y:135
			OperatableStateMachine.add('Offset2',
										ReplaceState(),
										transitions={'done': 'PreGrasp2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_pulley_red', 'result': 'offset_part_left'})

			# x:539 y:226
			OperatableStateMachine.add('Offset3',
										ReplaceState(),
										transitions={'done': 'PreGrasp3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_gasket_red', 'result': 'offset_part_left'})

			# x:539 y:318
			OperatableStateMachine.add('Offset4',
										ReplaceState(),
										transitions={'done': 'PreGrasp4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'offset_gear_blue', 'result': 'offset_part_left'})

			# x:710 y:40
			OperatableStateMachine.add('PreGrasp1',
										ReplaceState(),
										transitions={'done': 'ProgramBinsLeft'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PreGrasp_bin14', 'result': 'PreGrasp'})

			# x:709 y:135
			OperatableStateMachine.add('PreGrasp2',
										ReplaceState(),
										transitions={'done': 'ProgramBinsLeft'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PreGrasp_bin3', 'result': 'PreGrasp'})

			# x:710 y:227
			OperatableStateMachine.add('PreGrasp3',
										ReplaceState(),
										transitions={'done': 'ProgramShelvesLeft'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PreGrasp_shelf6', 'result': 'PreGrasp'})

			# x:709 y:317
			OperatableStateMachine.add('PreGrasp4',
										ReplaceState(),
										transitions={'done': 'ProgramShelvesLeft'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'PreGrasp_shelf3', 'result': 'PreGrasp'})

			# x:940 y:90
			OperatableStateMachine.add('ProgramBinsLeft',
										self.use_behavior(ProgramBinsLeftSM, 'ProgramBinsLeft'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'offset_part_left': 'offset_part_left', 'PreGrasp': 'PreGrasp', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'offset_part_left': 'offset_part_left', 'part_type': 'part_type', 'arm_id_left': 'arm_id_left', 'part_pose': 'part_pose', 'part_pose_left': 'part_pose_left'})

			# x:938 y:262
			OperatableStateMachine.add('ProgramShelvesLeft',
										self.use_behavior(ProgramShelvesLeftSM, 'ProgramShelvesLeft'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'offset_part_left': 'offset_part_left', 'PreGrasp': 'PreGrasp', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'offset_part_left': 'offset_part_left', 'part_type': 'part_type', 'arm_id_left': 'arm_id_left', 'part_pose': 'part_pose', 'part_pose_left': 'part_pose_left'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
