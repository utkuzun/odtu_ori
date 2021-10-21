import React, { useContext, createContext, useReducer, useState } from 'react'
import reducer from './reducer'
const axios = require('axios').default

const url = `${process.env.REACT_APP_DEV_URL}`

const AppContext = createContext()

const initialState = {
  user: {
    firstName: '',
    lastName: '',
    email: '',
    club: {},
    isAdmin: false,
    isDirector: false,
    isAuth: false,
  },
  clubs: [],
  categories: [],
  competitions: [],
  athletes: [],
}

const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState)

  const fetchChoices = () => {
    try {
      function getClubs() {
        return axios.get(url + 'api/clubs')
      }

      function getCategories() {
        return axios.get(url + 'api/categories')
      }

      Promise.all([getClubs(), getCategories()]).then(function (results) {
        const data1 = results[0].data
        const data2 = results[1].data
        dispatch({ type: 'SET_CLUBS', payload: data1.clubs })
        dispatch({ type: 'SET_CATEGORIES', payload: data2.categories })
      })
    } catch (error) {
      console.log(error)
    }
  }

  return (
    <AppContext.Provider value={{ state, dispatch, fetchChoices, url }}>
      {children}
    </AppContext.Provider>
  )
}

export const useGlobalContext = () => {
  return useContext(AppContext)
}

export { AppProvider }
