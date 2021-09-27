import React, { useContext, createContext, useReducer } from 'react'
import App from './App'
import reducer from './reducer'

const url = `${process.env.REACT_APP_DEV_URL}`

const AppContext = createContext()

const initialState = {
  user: {
    firstName: '',
    lastName: '',
    isAdmin: false,
    isDirector: false,
    isAuth: false,
  },
  clubs: [],
  categories: [],
  competitions: [],
  atheletes: [],
}

const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState)

  return (
    <AppContext.Provider value={{ ...state, dispatch }}>
      {children}
    </AppContext.Provider>
  )
}

export const useGlobalContext = () => {
  return useContext(AppContext)
}

export { AppProvider }
