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
	if self.error_E_low is not None:
		context.error["E"]["low"] = {"index": self.error_E_low}
	if self.error_E_high is not None:
		context.error["E"]["high"] = {"index": self.error_E_high}
	if self.error_t_low is not None:
		context.error["t"]["low"] = {"index": self.error_t_low}
	if self.error_t_high is not None:
		context.error["t"]["high"] = {"index": self.error_t_high}
	if self.error_E_low_E_high is not None:
		context.error["E"]["low"] = {"index": self.error_E_low}
		context.error["E"]["high"] = {"index": self.error_E_high}
	if self.error_t_low_t_high is not None:
		context.error["t"]["low"] = {"index": self.error_t_low}
		context.error["t"]["high"] = {"index": self.error_t_high}
	if self.error_E_low_E_high_t_low_t_high is not None:
		context.error["E"]["low"] = {"index": self.error_E_low}
		context.error["E"]["high"] = {"index": self.error_E_high}
		context.error["t"]["low"] = {"index": self.error_t_low}
		context.error["t"]["high"] = {"index": self.error_t_high}