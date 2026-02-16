import React from 'react';
import './Working.css';
import workingvideo from '../../assets/working.mp4'

const Working = () => {
  return (
    <div className='video-container'>
      <video controls >
            <source src={workingvideo} type="video/mp4"/>
          </video>
    </div>
  );
};

export default Working;
