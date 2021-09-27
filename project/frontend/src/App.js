import logo from './logo.svg'
import './App.css'
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom'
import './css/main.css'

import Navbar from './pages/Nav'
import Home from './pages/Home'
import About from './pages/About'
import Registiration from './pages/Registiration'
import Footer from './pages/Footer'
import Contacts from './pages/Contacts'

function App() {
  return (
    <main>
      <Navbar />
      <Switch>
        <Route exact path='/'>
          <Home />
        </Route>
        <Route exact path='/register'>
          <Registiration />
        </Route>
        <Route exact path='/contacts'>
          <Contacts />
        </Route>
        <Route exact path='/about'>
          <About />
        </Route>
      </Switch>
      <Footer />
    </main>
  )
}

export default App
