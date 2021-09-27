import React, { useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useGlobalContext } from '../.././context'

function Navbar() {
  const { user, dispatch } = useGlobalContext()

  // useEffect(() => {
  //   dispatch({ type: 'TEST' })
  // }, [])

  return (
    <nav>
      <div className='nav_center'>
        <div className='nav_headers'>
          <div className='logo'>
            <Link to='/' className='nav_logo'>
              <h1>ODTU Ori</h1>
            </Link>
          </div>
          <div className='toggle_menu'>
            <h1>X</h1>
          </div>
        </div>
        <ul className='nav_links'>
          <Link to='/' className='nav_link'>
            Anasayfa
          </Link>
          <Link to='/about' className='nav_link'>
            Hakkımızda
          </Link>
          <Link to='/register' className='nav_link'>
            Kayıt
          </Link>
          <Link to='/contacts' className='nav_link'>
            İletişim
          </Link>
        </ul>

        <ul className='nav_auth'>
          {!user.isAuth && (
            <Link to='login' className='btn login'>
              Giriş
            </Link>
          )}
          {!user.isAuth && (
            <Link to='register_user' className='btn register'>
              Kaydol
            </Link>
          )}
          {user.isAuth && (
            <Link to='logoff' className='btn logoff'>
              çıkış
            </Link>
          )}
        </ul>
      </div>
    </nav>
  )
}

export default Navbar
