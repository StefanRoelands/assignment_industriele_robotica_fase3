#!/usr/bin/env python
import rospy
import sys
import rostopic

from flexbe_core import EventState
from nist_gear.msg import VacuumGripperState
from std_msgs.msg import String


class GripperControle(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= Active 			The gripper holds a product.
	<= Not_active 			The gripper doesn't hold a product.
	<= invalid_arm_id		Invalid arm id
	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(GripperControle, self).__init__(input_keys = ['arm_id'], outcomes = ['Active', 'Not_active', 'invalid_arm_id'])


	def execute(self, userdata):

		if userdata.arm_id == 'left':
			status = rospy.wait_for_message('/ariac/gantry/left_arm/gripper/state', VacuumGripperState)
			if status.attached == True:
				return 'Active'
			else:
				return 'Not_active'

		elif userdata.arm_id == 'right':
			status = rospy.wait_for_message('/ariac/gantry/right_arm/gripper/state', VacuumGripperState)
			if status.attached == True:
				return 'Active'
			else:
				return 'Not_active'
		

	def on_enter(self, userdata):
		# This method is called when the state becomes active, i.e. a transition from another state to this one is taken.
		# It is primarily used to start actions which are associated with this state.

		# The following code is just for illustrating how the behavior logger works.
		# Text logged by the behavior logger is sent to the operator and displayed in the GUI.
		pass # Nothing to do in this example.



	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.

		pass # Nothing to do in this example.


	def on_start(self):
		# This method is called when the behavior is started.
		# If possible, it is generally better to initialize used resources in the constructor
		# because if anything failed, the behavior would not even be started.

		# In this example, we use this event to set the correct start time.
		self._start_time = rospy.Time.now()
		

	def on_stop(self):
		# This method is called whenever the behavior stops execution, also if it is cancelled.
		# Use this event to clean up things like claimed resources.

		pass # Nothing to do in this example.
		
