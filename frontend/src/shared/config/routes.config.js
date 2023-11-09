export const appRoutes = {
	database: {
		path: 'database',
		goto() {
			return '/database'
		}
	},
	base: {
		path: '/',
		goto() {
			return '/'
		}
	}
}