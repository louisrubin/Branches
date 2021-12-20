from django.core.exceptions import PermissionDenied

class AdminRequiredMixins():
	"""docstring for AdminRequiredMixins"""
	def dispatch (self, request, *args, **kwars):
		if not request.user.es_administrador:
			if not request.user.is_superuser:
				raise PermissionDenied
		return super(AdminRequiredMixins, self).dispatch(request, *args, **kwars)
		
class WriterRequiredMixins():
	def dispatch (self, request, *args, **kwars):
		if not request.user.writer:
			if not request.user.es_administrador:
				if not request.user.is_superuser:
					raise PermissionDenied
		return super(WriterRequiredMixins, self).dispatch(request, *args, **kwars)
