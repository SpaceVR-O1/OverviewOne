
__author__ = "Steve Alvarado"
__email__ = "alvarado@tethers.com"
__status__ = "Development"
__company__ = "Tethers Unlimited, Inc."
__date__ = "Late Updated: 5/27/15"

class ExecuteSettings(object):
	"""
	Author: S. Alvarado (4/2/15)
	Description: this class contains the SwiftRadioInterface settings for executing commands.
				 Because a SwiftRadioInterface object can have multiple connections, these are stored
				 in a dynamic classes with appropriate value checking for each setting.
	"""
	def __init__(self):
		"""
		Author: S. Alvarado (4/2/15)
		Description: class constructor function
		"""
		# Class attributes (PRIVATE)
		self.__return_rpc_error = False # return rpc error code
		self.__timeout = 4 				# time, in seconds, to wait for radio acknowledgment before timeout
		self.__fail_retries = 2 		# A failed command will be reattempted up to fail_retries.
		self.__fail_exception = False 	# throw a python exception if a command fails to execute
		self.__fail_rpc_error = True	# non-zero RPC CMDERR codes will be treated as a error condition.
		self.__endianess = "little"   	# raw byte Endianess

		# Range and bound conditions for each attribute (PRIVATE)
		self.__return_rpc_error_choices = (False, True)
		self.__timeout_range = (0, 3600) 			# 0 secs to 1 hr
		self.__fail_retries_range = (0, 100)
		self.__fail_exception_choices = (False, True)
		self.__fail_rpc_error_choices = (False, True)
		self.__endianess_syntax_choices = ("little", "big")

	# GETTERS AND SETTERS

	# return_rpc_error attribute
	@property
	def return_rpc_error(self):
		return self.__return_rpc_error
	@return_rpc_error.setter
	def return_rpc_error(self, value):
		# error check value
		self._check_choice(value, self.__return_rpc_error_choices, "return_rpc_error")
		self.__return_rpc_error = value

	# endianess attribute
	@property
	def endianess(self):
		return self.__endianess
	@endianess.setter
	def endianess(self, value):
		# error check value
		self._check_choice(value, self.__endianess_choices, "endianess")
		self.__endianess = value

	# timeout attribute
	@property
	def timeout(self):
		return self.__timeout
	@timeout.setter
	def timeout(self, value):
		# error check value
		self._check_range(value, self.__timeout_range, "timeout")
		self.__timeout = value

	# fail_retries attribute
	@property
	def fail_retries(self):
		return self.__fail_retries
	@fail_retries.setter
	def fail_retries(self, value):
		self._check_range(value, self.__fail_retries_range, "fail_retries")
		self.__fail_retries = value

	# fail_exception attribute
	@property
	def fail_exception(self):
		return self.__fail_exception
	@fail_exception.setter
	def fail_exception(self, value):
		self._check_choice(value, self.__fail_exception_choices, "fail_exception")
		self.__fail_exception = value

	# fail_rpc_error attribute
	@property
	def fail_rpc_error(self):
		return self.__fail_rpc_error
	@fail_rpc_error.setter
	def fail_rpc_error(self, value):
		self._check_choice(value, self.__fail_rpc_error_choices, "fail_rpc_error")
		self.__fail_rpc_error = value

	def _check_range(self, val, valrange, name):
		"""
		Author: S. Alvarado (4/2/15)
		Description: check the range of the variable attempting to be set.
		Parameters: val - value being error checked.
					valrange - acceptable range for this value.
					name - name of the variable.
		Return: 1 - variable is valid and was successfully set
				OR
				A Python exception will be thrown if the given value is deemed invalid (outside the given range)
		"""
		if val < valrange[0]:
			raise SwiftRadioSettingsError("ExecuteSettings: invalid {} value '{}'. value less than minimum value {}.".format(name, val, valrange[0]))
		elif val > valrange[1]:
			raise SwiftRadioSettingsError("ExecuteSettings: invalid {} value '{}'. value greater than maximum value {}.".format(name, val, valrange[1]))
		return 1

	def _check_choice(self, val, choices, name):
		"""
		Author: S. Alvarado (4/2/15)
		Description: check the range of the variable attempting to be set.
		Parameters: val - value being error checked.
					choices - valid choices for this variable
					name - name of the variable
		Return: 1 - variable is valid and was successfully set
				OR
				A Python exception will be thrown if the given value is deemed invalid.
		"""
		if val not in choices:
			raise SwiftRadioSettingsError("ExecuteSettings: invalid {} value '{}'. valid choices = {}".format(name, val, choices))
		return 1
class SwiftRadioSettingsError(RuntimeError):
	pass

if __name__ == '__main__':
	exe_settings = ExecuteCommandSettings()

	# print default values
	print exe_settings.return_rpc_error
	print exe_settings.fail_retry
	print exe_settings.fail_retries
	print exe_settings.fail_exception
	print exe_settings.fail_rpc_error
	print exe_settings.timeout
	print exe_settings.cmdline_syntax
	print exe_settings.auto_throttle
	print exe_settings.transid

	# test each property
	exe_settings.return_rpc_error = True
	exe_settings.fail_retry = True
	exe_settings.fail_retries = 4
	exe_settings.fail_exception = True
	exe_settings.fail_rpc_error = True
	exe_settings.timeout = 15
	exe_settings.cmdline_syntax = False
	exe_settings.auto_throttle = False
	exe_settings.transid = 0xABCD

	print exe_settings.return_rpc_error
	print exe_settings.fail_retry
	print exe_settings.fail_retries
	print exe_settings.fail_exception
	print exe_settings.fail_rpc_error
	print exe_settings.timeout
	print exe_settings.cmdline_syntax
	print exe_settings.auto_throttle
	print exe_settings.transid