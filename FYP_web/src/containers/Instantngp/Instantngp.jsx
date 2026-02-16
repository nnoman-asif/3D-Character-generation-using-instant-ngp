import React from 'react'
import './instantngp.css'
import { Feature } from '../../components'
import nvidia from '../../assets/nvidia.png'

const featuresData = [
  {
  title:"What is Instant ngp?",
  text:"A framework that allows a neural network to learn representations of gigapixel images, 3D objects, and NeRFs in seconds."
} ,
{
  title:"What is NeRF?",
  text:"A neural radiance field (NeRF) is a fully-connected neural network that can generate novel views of complex 3D scenes, based on a partial set of 2D images. It is trained to use a rendering loss to reproduce input views of a scene."
} ,
{
  title:"Benefits of Instant ngp",
  text:"Based on NeRF's work, Instant NGP significantly shortens training and rendering time, reducing training time to within a minute, and making real-time rendering easily achievable."
},
{
  title:"How does it work?",
  text:"Instant-NGP proposes a trainable hash-based encoding. The idea is to map coordinates to trainable feature vectors which can be optimized in the standard flow of NeRF training."
} 
]




const Instantngp = () => {
  return (
    <div className='gpt3__features section__padding' id='ngp'>
      <div className='gpt3__features-heading'>
        <h1 className='gradient__text'> Instant NGP</h1>
        <p><img src={nvidia} alt='nvidia.png'></img>
          <a href='https://developer.nvidia.com/blog/getting-started-with-nvidia-instant-nerfs/'>Instant-NGP</a>
        </p>
      </div>
      <div className='gpt3__features-container'>
        {featuresData.map((item,index) => (
          <Feature title={item.title} text={item.text} key={item.title + index}/>
        ))}
      </div>
    </div>
  )
}

export default Instantngp
