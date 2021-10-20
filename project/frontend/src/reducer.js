const reducer = (state, action) => {
  if (action.type === 'TEST') {
    console.log('You are in test dispatch')
    console.log(state)
    return state
  }

  if (action.type === 'SET_CLUBS') {
    return { ...state, clubs: action.payload }
  }
  if (action.type === 'SET_CATEGORIES') {
    return { ...state, categories: action.payload }
  }

  throw new Error('no matching action type')
}

export default reducer
