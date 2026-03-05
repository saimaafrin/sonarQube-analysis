def dehydrate_timedelta(value):
return {
		'days': value.days,
		'seconds': value.seconds,
		'microseconds': value.microseconds
	}