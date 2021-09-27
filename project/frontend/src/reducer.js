const reducer = (state, action) => {
  if (action.type === 'TEST') {
    console.log('You are in test dispatch')
    console.log(state)
    return state
  }

  throw new Error('no matching action type')
}

export default reducer
