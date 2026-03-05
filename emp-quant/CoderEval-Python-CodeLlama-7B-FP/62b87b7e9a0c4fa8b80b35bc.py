def _update_context(self, context):
	"""
	Update *context* with the properties of this graph.

*context.error* is appended with indices of errors.
Example subcontext for a graph with fields "E,t,error_E_low":
{"error": {"x_low": {"index": 2}}}.
Note that error names are called "x", "y" and "z"
(this corresponds to first three coordinates,
if they are present), which allows to simplify plotting.
Existing values are not removed
from *context.value* and its subcontexts.

Called on "destruction" of the graph (for example,
in :class:`.ToCSV`). By destruction we mean conversion
to another structure (like text) in the flow.
The graph object is not really destroyed in this process.
	"""
	if self.error:
		for name in self.error:
			if name not in context.error:
				context.error[name] = {}
			context.error[name]["index"] = self.index

	if self.value:
		for name in self.value:
			if name not in context.value:
				context.value[name] = {}
			context.value[name]["index"] = self.index

	if self.value_error:
		for name in self.value_error:
			if name not in context.value_error:
				context.value_error[name] = {}
			context.value_error[name]["index"] = self.index

	if self.value_error_low:
		for name in self.value_error_low:
			if name not in context.value_error_low:
				context.value_error_low[name] = {}
			context.value_error_low[name]["index"] = self.index

	if self.value_error_high:
		for name in self.value_error_high:
			if name not in context.value_error_high:
				context.value_error_high[name] = {}
			context.value_error_high[name]["index"] = self.index

	if self.value_error_low_low:
		for name in self.value_error_low_low:
			if name not in context.value_error_low_low:
				context.value_error_low_low[name] = {}
			context.value_error_low_low[name]["index"] = self.index

	if self.value_error_low_high:
		for name in self.value_error_low_high:
			if name not in context.value_error_low_high:
				context.value_error_low_high[name] = {}
			context.value_