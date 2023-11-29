export const appRoutes = {
	login: {
		path: '/',
		goto() {
			return '/'
		}
	},
	regist: {
		path: '/register',
		goto() {
			return '/register'
		}
	},
	neuralNetwork: {
		path: '/neuralNetwork',
		goto() {
			return '/use-nn'
		}
	},
	history: {
		path: '/history',
		goto() {
			return '/history'
		}
	},
	changePassword: {
		path: '/change-password/',
		goto() {
			return '/change-password/'
		}
	}

}