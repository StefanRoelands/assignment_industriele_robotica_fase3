#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.gripper_controle_state import GripperControle
from ariac_flexbe_behaviors.selectorstateleft_sm import SelectorStateLeftSM
from ariac_flexbe_behaviors.selectorstateright_sm import SelectorStateRightSM
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_behaviors.agvselector_sm import AgvSelectorSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 29 2020
@author: Wouter de Saegher, Stefan Roelands
'''
class GripperChoiceSM(Behavior):
	'''
	Gripper keuze maken en plaatsen op de AGV
	'''


	def __init__(self):
		super(GripperChoiceSM, self).__init__()
		self.name = 'GripperChoice'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(SelectorStateLeftSM, 'SelectorStateLeft')
		self.add_behavior(SelectorStateRightSM, 'SelectorStateRight')
		self.add_behavior(AgvSelectorSM, 'AgvSelector')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:579 y:679, x:313 y:185, x:323 y:666
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed', 'false'], input_keys=['number_of_products', 'product_index', 'bin_id', 'part_type', 'part_pose', 'agv_id'], output_keys=['product_index'])
		_state_machine.userdata.number_of_products = 0
		_state_machine.userdata.product_index = 0
		_state_machine.userdata.one_value = 1
		_state_machine.userdata.bin_id = ''
		_state_machine.userdata.zero_value = 0
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.arm_id_right = 'right'
		_state_machine.userdata.arm_id_left = 'left'
		_state_machine.userdata.part_pose_right = []
		_state_machine.userdata.part_pose_left = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:49 y:41
			OperatableStateMachine.add('GripperControlLeft',
										GripperControle(),
										transitions={'Active': 'GripperControlRight', 'Not_active': 'SelectorStateLeft', 'invalid_arm_id': 'failed'},
										autonomy={'Active': Autonomy.Off, 'Not_active': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id_left'})

			# x:50 y:185
			OperatableStateMachine.add('SelectorStateLeft',
										self.use_behavior(SelectorStateLeftSM, 'SelectorStateLeft'),
										transitions={'finished': 'IncrementProductIndex', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin_id': 'bin_id', 'part_type': 'part_type', 'arm_id_left': 'arm_id_left', 'part_pose': 'part_pose', 'part_pose_left': 'part_pose_left'})

			# x:516 y:37
			OperatableStateMachine.add('GripperControlRight',
										GripperControle(),
										transitions={'Active': 'AgvSelector', 'Not_active': 'SelectorStateRight', 'invalid_arm_id': 'failed'},
										autonomy={'Active': Autonomy.Off, 'Not_active': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id_right'})

			# x:510 y:189
			OperatableStateMachine.add('SelectorStateRight',
										self.use_behavior(SelectorStateRightSM, 'SelectorStateRight'),
										transitions={'finished': 'IncrementProductIndex_2', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin_id': 'bin_id', 'part_type': 'part_type', 'arm_id_right': 'arm_id_right', 'part_pose': 'part_pose', 'part_pose_right': 'part_pose_right'})

			# x:49 y:302
			OperatableStateMachine.add('IncrementProductIndex',
										AddNumericState(),
										transitions={'done': 'EndProduct'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'one_value', 'result': 'product_index'})

			# x:49 y:398
			OperatableStateMachine.add('EndProduct',
										EqualState(),
										transitions={'true': 'AgvSelector', 'false': 'false'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'number_of_products'})

			# x:507 y:303
			OperatableStateMachine.add('IncrementProductIndex_2',
										AddNumericState(),
										transitions={'done': 'EndProduct_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'one_value', 'result': 'product_index'})

			# x:508 y:396
			OperatableStateMachine.add('EndProduct_2',
										EqualState(),
										transitions={'true': 'AgvSelector', 'false': 'false'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'number_of_products'})

			# x:509 y:478
			OperatableStateMachine.add('ResetProductIndex',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero_value', 'result': 'product_index'})

			# x:271 y:473
			OperatableStateMachine.add('EndProduct_3',
										EqualState(),
										transitions={'true': 'ResetProductIndex', 'false': 'false'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'number_of_products'})

			# x:267 y:347
			OperatableStateMachine.add('AgvSelector',
										self.use_behavior(AgvSelectorSM, 'AgvSelector'),
										transitions={'finished': 'EndProduct_3', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_pose_right': 'part_pose_right', 'part_pose_left': 'part_pose_left', 'agv_id': 'agv_id', 'arm_id_right': 'arm_id_right', 'arm_id_left': 'arm_id_left'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
