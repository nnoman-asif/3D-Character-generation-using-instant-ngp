import React from 'react'
import {About, Working, Instantngp, Whatis3c,Home} from './containers'
import {Navbar} from './components'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'

const App = () => {
  return (
    <div className='App'>
      
      <Router>
        <Routes>
          <Route path="/" element={[<div className='gradient__bg'><Navbar/></div>,<div className='gradient__bg'><Home/></div>]} />
          <Route path="/What-is-3C" element={[<div className='gradient__bg'><Navbar/></div>,<Whatis3c/>]} />
          <Route path="/Instant-ngp" element={[<div className='gradient__bg'><Navbar/></div>,<Instantngp/>]}/>
          <Route path='/Working' element={[<div className='gradient__bg'><Navbar/></div>,<Working/>]}/>
          <Route path="/About" element={[<div className='gradient__bg'><Navbar/></div>,< About/>]}/>
        </Routes>
      </Router>
    </div>
  )
}

export default App;
 