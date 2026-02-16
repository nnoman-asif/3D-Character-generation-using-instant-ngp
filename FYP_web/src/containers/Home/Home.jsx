import React from 'react' 
import './Home.css'
//import logo from '../../assets/logo.png'
import video from '../../assets/displayingmodel.mp4'


const Home = () => {
  return (
    <div className='gpt3__header section__padding' id='home'>
      <div className='gpt3__header-content'>
        <h1 className='gradient__text'> Let's dive into the world of 3D character with 3C</h1>
        <p>A efficient tool that is designed to make a 3D character by using only single video saving time and effort for animators and artists.</p>
        
      </div>
      <div className='gpt3__header-image'>
      <video autoPlay loop muted >
            <source src={video} type="video/mp4"/>
          </video>
        </div>
    </div>
  )
}

export default Home
