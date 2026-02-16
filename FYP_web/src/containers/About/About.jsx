import React from 'react'
import './About.css'
import linkedin from '../../assets/Linkedin.png'
import github from '../../assets/github.png'
import email from '../../assets/email.png'

const About = () => {
  return (
    <div className='gpt3__footer section__padding'>
      <div className='gpt3__footer-heading'>
        <h1 className='gradient__text'>About Us</h1>
      </div>
      <div className='gpt3__footer-details'>
        <p>
        We are a team of passionate graduates from FAST NUCES, dedicated to delivering excellence in our Final Year Project (FYP). Our mission is to revolutionize the process of creating 3D characters by leveraging the power of a single video.

At the core of our application is the goal to make 3D character creation accessible and effortless. We understand the challenges faced by creators, and our solution streamlines the process by utilizing a single video input. Our innovative technology analyzes the video data, extracting key features to generate a fully-fledged 3D character.

One of our primary objectives is to ensure compatibility with Unreal Engine, a leading game development platform. By focusing on Unreal Engine integration, we enable seamless implementation of the characters created using our application into virtual worlds and gaming experiences.

As graduates with a deep passion for computer graphics and a comprehensive understanding of the industry, we are driven to push boundaries and redefine possibilities. We believe that our application has the potential to transform the way 3D characters are brought to life, empowering creators and developers alike.
        </p>
      </div>
      <div className='gpt3__footer-heading-contact'>
        <h1 className='gradient__text'>Contact Us</h1>
      </div>
      <div className='gpt3__footer-links'>
        <div className='gpt3__footer-links_div'>
          <h4>Links</h4>
          <p><img src={linkedin} alt='Linkedin'></img>
          <a href='https://www.linkedin.com/in/noman-asif-682085270'>  Noman Asif, </a>
          </p>
          <p><img src={linkedin} alt='Linkedin'></img>
          <a href='https://www.linkedin.com/in/afaq-qureshi-a92463251/'>  Afaq Qureshi, </a>
          </p>
          <p><img src={linkedin} alt='Linkedin'></img>
          <a href='https://www.linkedin.com/in/faizan-satti-112a9b233/'>  Faizan Zubair.</a>
          </p>
          <p><img src={github} alt='Github'></img>
            <a href='https://github.com/nnoman-asif/3D-Character-generation-using-instant-ngp'> 3C Github</a>
          </p>
        </div>
        <div className='gpt3__footer-links_div'>
          <h4>Get in touch</h4>
          <p><img src={email} alt='Email'></img>
            <a href='mailto:i191880@nu.edu.pk'>  Noman Asif </a>
          </p>
          <p><img src={email} alt='Email'></img>
            <a href='mailto:i191775@nu.edu.pk'>  Afaq Qureshi </a>
          </p>
          <p><img src={email} alt='Email'></img>
            <a href='mailto:i191863@nu.edu.pk'>  Faizan Zubair</a>
          </p>
        </div>
      </div>
    </div>
  )
}

export default About
