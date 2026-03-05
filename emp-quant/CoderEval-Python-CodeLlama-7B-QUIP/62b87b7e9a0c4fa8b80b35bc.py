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
	context.update(self.context)
	context.update({"error": {}})
	for name in self.error_names:
		context["error"][name] = {"index": self.error_names.index(name)}
	context["error"]["error_E_low"] = {"index": self.error_names.index("error_E_low")}
	context["error"]["error_E_high"] = {"index": self.error_names.index("error_E_high")}
	context["error"]["error_E_low_high"] = {"index": self.error_names.index("error_E_low_high")}
	context["error"]["error_E_low_low"] = {"index": self.error_names.index("error_E_low_low")}
	context["error"]["error_E_high_high"] = {"index": self.error_names.index("error_E_high_high")}
	context["error"]["error_E_low_low_low"] = {"index": self.error_names.index("error_E_low_low_low")}
	context["error"]["error_E_high_high_high"] = {"index": self.error_names.index("error_E_high_high_high")}
	context["error"]["error_E_low_low_low_low"] = {"index": self.error_names.index("error_E_low_low_low_low")}
	context["error"]["error_E_high_high_high_high"] = {"index": self.error_names.index("error_E_high_high_high_high")}
	context["error"]["error_E_low_low_low_low_low"] = {"index": self.error_names.index("error_E_low_low_low_low_low")}
	context["error"]["error_E_high_high_high_high_high"] = {"index": self.error_names.index("error_E_high_high_high_high_high")}
	context["error"]["error_E_low_low_low_low_low_low