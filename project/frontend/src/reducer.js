const reducer = (state, action) => {
  if (action.type === 'TEST') {
    console.log('You are in test dispatch')
    console.log(state)
    return state
  }

  if (action.type === 'FETCH_CHOICES') {
    console.log('Fetch func')
    return state
  }

  throw new Error('no matching action type')
}

export default reducer
