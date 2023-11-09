import { useRoutes } from 'react-router-dom'

import { appRoutes } from '@shared/config'

import {
	HistoryPage,
	NeuralNetworkPage,
	SignInPage,

} from '../components'
import { MainLayout } from './layouts'
import { WordDependenciesPage } from '../components/WordDependencies'
import { SearchPage } from '../components/Search'

export const GenerateRoutes = () => {
	return useRoutes([
		{
			path: appRoutes.base.path,
			element: <MainLayout />,
			children: [
				{
					index: true,
					element: <Home />
				},
				{
					path: appRoutes.history.path,
					element: <SignInPage />
				},
				{
					path: appRoutes.neuralNetwork.path,
					element: <NeuralNetworkPage />
				},
				{
					path: appRoutes.notesCreator.path,
					element: <NotesCreator />
				},
				{
					path: appRoutes.parseSentense.path,
					element: <TreeParserPage />
				}
			]
		}
	])
}
