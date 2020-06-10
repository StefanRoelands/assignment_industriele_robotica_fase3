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
from ariac_logistics_flexbe_states.get_order_state import GetOrderState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_logistics_flexbe_states.get_products_from_shipment_state import GetProductsFromShipmentState
from ariac_logistics_flexbe_states.get_part_from_products_state import GetPartFromProductsState
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
from ariac_support_flexbe_states.get_item_from_list_state import GetItemFromListState
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_flexbe_behaviors.notify_shipment_ready_sm import Notify_shipment_readySM
from ariac_flexbe_behaviors.gripperchoice_sm import GripperChoiceSM
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from ariac_flexbe_states.message_state import MessageState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 28 2020
@author: Wouter de Saegher, Stefan Roelands
'''
class Main_programSM(Behavior):
	'''
	Hoofdprogramma van het verwerken van de orders voor de klant
	'''


	def __init__(self):
		super(Main_programSM, self).__init__()
		self.name = 'Main_program'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(Notify_shipment_readySM, 'Notify_shipment_ready')
		self.add_behavior(GripperChoiceSM, 'GripperChoice')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:650 y:25, x:929 y:416
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.products = []
		_state_machine.userdata.product_index = 0
		_state_machine.userdata.shipment_index = 0
		_state_machine.userdata.material_locations = []
		_state_machine.userdata.bin_index = 0
		_state_machine.userdata.order_id = ''
		_state_machine.userdata.shipments = []
		_state_machine.userdata.number_of_shipments = 0
		_state_machine.userdata.shipment_type = ''
		_state_machine.userdata.number_of_products = 0
		_state_machine.userdata.bin_id = ''
		_state_machine.userdata.old_order_id = ''
		_state_machine.userdata.one_value = 1
		_state_machine.userdata.zero_value = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:45 y:112
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'GetOrder'},
										autonomy={'continue': Autonomy.Off})

			# x:211 y:112
			OperatableStateMachine.add('GetOrder',
										GetOrderState(),
										transitions={'continue': 'ConveyorOff'},
										autonomy={'continue': Autonomy.Off},
										remapping={'order_id': 'order_id', 'shipments': 'shipments', 'number_of_shipments': 'number_of_shipments'})

			# x:424 y:113
			OperatableStateMachine.add('TestLastOrder',
										EqualState(),
										transitions={'true': 'EndAssignment', 'false': 'RememberOldOrder'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'order_id', 'value_b': 'old_order_id'})

			# x:650 y:114
			OperatableStateMachine.add('RememberOldOrder',
										ReplaceState(),
										transitions={'done': 'GetShipment'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'order_id', 'result': 'old_order_id'})

			# x:869 y:114
			OperatableStateMachine.add('GetShipment',
										GetProductsFromShipmentState(),
										transitions={'continue': 'GetPart', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'shipments': 'shipments', 'index': 'shipment_index', 'shipment_type': 'shipment_type', 'agv_id': 'agv_id', 'products': 'products', 'number_of_products': 'number_of_products'})

			# x:1122 y:115
			OperatableStateMachine.add('GetPart',
										GetPartFromProductsState(),
										transitions={'continue': 'MaterialLocation', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'products': 'products', 'index': 'product_index', 'type': 'part_type', 'pose': 'part_pose'})

			# x:1361 y:113
			OperatableStateMachine.add('MaterialLocation',
										GetMaterialLocationsState(),
										transitions={'continue': 'GetBin'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part_type', 'material_locations': 'material_locations'})

			# x:1361 y:235
			OperatableStateMachine.add('GetBin',
										GetItemFromListState(),
										transitions={'done': 'AGV_id', 'invalid_index': 'failed'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'material_locations', 'index': 'bin_index', 'item': 'bin_id'})

			# x:759 y:683
			OperatableStateMachine.add('IncrementShipmentIndex',
										AddNumericState(),
										transitions={'done': 'EndShipment'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'shipment_index', 'value_b': 'one_value', 'result': 'shipment_index'})

			# x:536 y:683
			OperatableStateMachine.add('EndShipment',
										EqualState(),
										transitions={'true': 'Notify_shipment_ready', 'false': 'GetShipment'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'shipment_index', 'value_b': 'number_of_shipments'})

			# x:446 y:6
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:206 y:680
			OperatableStateMachine.add('Notify_shipment_ready',
										self.use_behavior(Notify_shipment_readySM, 'Notify_shipment_ready'),
										transitions={'finished': 'ResetShipmentIndex', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'shipment_type': 'shipment_type', 'agv_id': 'agv_id'})

			# x:1357 y:675
			OperatableStateMachine.add('GripperChoice',
										self.use_behavior(GripperChoiceSM, 'GripperChoice'),
										transitions={'finished': 'IncrementShipmentIndex', 'failed': 'failed', 'false': 'GetPart'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'false': Autonomy.Inherit},
										remapping={'number_of_products': 'number_of_products', 'product_index': 'product_index', 'bin_id': 'bin_id', 'part_type': 'part_type', 'part_pose': 'part_pose', 'agv_id': 'agv_id'})

			# x:194 y:377
			OperatableStateMachine.add('ResetShipmentIndex',
										ReplaceState(),
										transitions={'done': 'GetOrder'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero_value', 'result': 'shipment_index'})

			# x:216 y:19
			OperatableStateMachine.add('ConveyorOff',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'TestLastOrder', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'zero_value'})

			# x:1384 y:446
			OperatableStateMachine.add('AGV_id',
										MessageState(),
										transitions={'continue': 'GripperChoice'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'agv_id'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
