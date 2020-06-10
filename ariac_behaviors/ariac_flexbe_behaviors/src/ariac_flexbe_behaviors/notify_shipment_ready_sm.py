#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.notify_shipment_ready_state import NotifyShipmentReadyState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.get_agv_status_state import GetAgvStatusState
from ariac_support_flexbe_states.equal_state import EqualState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 29 2020
@author: Wouter de Saegher, Stefan Roelands
'''
class Notify_shipment_readySM(Behavior):
	'''
	Notifies the agv the shipment is ready
This is a part of the ariac_example.
	'''


	def __init__(self):
		super(Notify_shipment_readySM, self).__init__()
		self.name = 'Notify_shipment_ready'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:637 y:218, x:137 y:252
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['shipment_type', 'agv_id'])
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.shipment_type = ''
		_state_machine.userdata.succes = 0
		_state_machine.userdata.agv_state = ''
		_state_machine.userdata.agv_ready_state = 'ready_to_deliver'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:77 y:40
			OperatableStateMachine.add('NotifyShipmentReady',
										NotifyShipmentReadyState(),
										transitions={'continue': 'Wait', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'shipment_type': 'shipment_type', 'success': 'success', 'message': 'message'})

			# x:296 y:38
			OperatableStateMachine.add('Wait',
										WaitState(wait_time=1),
										transitions={'done': 'GetAgvState'},
										autonomy={'done': Autonomy.Off})

			# x:452 y:39
			OperatableStateMachine.add('GetAgvState',
										GetAgvStatusState(),
										transitions={'continue': 'AgvReady', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'agv_state': 'agv_state'})

			# x:380 y:192
			OperatableStateMachine.add('AgvReady',
										EqualState(),
										transitions={'true': 'finished', 'false': 'Wait'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_state', 'value_b': 'agv_ready_state'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
