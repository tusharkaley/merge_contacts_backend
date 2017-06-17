from django.core.cache import cache


def get_user_db(user_token):
	return cache.get(user_token)

