import * as getsRequests from './gets'
import * as postsRequests from './posts'


export const login = {
	...getsRequest,
	...postsRequests
}