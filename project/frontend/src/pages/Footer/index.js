import React from 'react'
import { dataNav, links } from '.././data'
import { Link } from 'react-router-dom'

function Footer() {
  return (
    <footer>
      <div className='footer-container'>
        <div className='footer-logo'>
          <Link to='/'>
            <h1>logo</h1>
          </Link>
        </div>
        <div className='footer-trademark'>
          <p> {new Date().getFullYear()} ODTÜ Ori. All rights reserved.</p>
        </div>
        <div className='footer-navs'>
          {dataNav.map((navItem, index) => {
            return (
              <div key={index} className='footer-nav'>
                <Link to={navItem.page}>{navItem.page}</Link>
              </div>
            )
          })}
        </div>
        <div className='footer-links'>
          {links.map((link, index) => {
            return (
              <div key={index} className='footer-link'>
                <a href={link.url} target='_blank' rel='noreferrer'>
                  {link.icon}
                </a>
              </div>
            )
          })}
        </div>
      </div>
    </footer>
  )
}

export default Footer
