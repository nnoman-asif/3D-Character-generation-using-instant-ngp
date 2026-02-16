import React, {useState} from 'react'
import {RiMenu3Line, RiCloseLine} from 'react-icons/ri'
import logo from '../../assets/logo.png'
import app from '../../assets/3cApp.zip'
import { Link } from 'react-router-dom';
import './navbar.css'

const Menu = () => (
  <>
  <Link to='/'><p>Home</p></Link>
  <Link to='/What-is-3C'><p>What is 3C?</p></Link>
  <Link to='/Instant-ngp'><p>Instant Ngp</p></Link>
  <Link to='/Working'><p>Working</p></Link>
  <Link to='/About'><p>About</p></Link>
  </>
)

const Navbar = () => {
  const [toggleMenu,setToggleMenu] = useState(false);
  return (
    <div className='gpt3__navbar'>
      <div className='gpt3__navbar-links'>
        <div className='gpt3__navbar-links_logo'>
          <img id='logo_id' src={logo} alt="logo" />
        </div>
          <div className='gpt3__navbar-links_container'>
            <Menu/>
          </div>
      </div>
      { <div className='gpt3__navbar-sign'>
        <p>DOWNLOAD HERE</p>
        <a
        href={app}
        download="3C_App.zip"
        target="_blank"
        rel="noreferrer"
      >
        <button type='button'>DOWNLOAD</button>
        </a>
      </div> }
      <div className='gpt3__navbar-menu'>
        {toggleMenu
          ? <RiCloseLine color="#fff" size={27} onClick={() => setToggleMenu(false)} />
          : <RiMenu3Line color="#fff" size={27} onClick={() => setToggleMenu(true)} />
          
        }
        {toggleMenu && (
          <div className='gpt3__navbar-menu_container scale-up-center'>
            <div className='gpt3__navbar-menu_container-links'>
              <Menu/>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default Navbar