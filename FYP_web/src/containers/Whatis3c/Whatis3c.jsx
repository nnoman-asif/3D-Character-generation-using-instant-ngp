import React from 'react'
import './Whatis3c.css'
import { Feature } from '../../components'

const Whatis3c = () => {
  return (
    <div className='gpt3__whatgpt3 section__margin' id="wgpt3">
      <div className='gpt3__whatgpt3-feature'>
        <Feature title='What is 3C?' text="This application allows the user to create a 3D character that is important inside gaming engines such as Unreal Engine. User can rig the character and then use it inside gaming engines."/>
      </div>
      <div className='gpt3__whatgpt3-heading'>
        <h1 className='gradient__text'> An Application to revolutionize creation of 3D characters</h1>
        <p>Making it easy for animators and creators to generate a 3D character that can be rigged and imported inside gaming engines.</p>
      </div>
      <div className='gpt3__whatgpt3-container'>
        <Feature title="Easy to Download" text="Just click Download"/>
        <Feature title="Easy to use" text="Easy to use with guide available at website"/>
        <Feature title="Requirements" text="Just one 360 video"/>
      </div>
    </div>
  )
}

export default Whatis3c
