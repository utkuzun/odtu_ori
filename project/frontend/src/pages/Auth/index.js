import React, { useState, useEffect } from 'react'
import { useGlobalContext } from '../../context'

function RegisterUser() {
  const [slide, setSlide] = useState(false)
  const { dispatch, fetchChoices, state } = useGlobalContext()

  const [registerUser, setRegisterUser] = useState({
    user: {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      password_rep: '',
    },
    athlete: {
      club: '',
      category: '',
      first_name: '',
      last_name: '',
      email: '',
      born: new Date(2000, 0, 0).toISOString().slice(0, 10),
      sex: '',
      si: 0,
    },
  })

  useEffect(() => {
    fetchChoices()
  }, [])

  const handleChangeUser = (e) => {
    const name = e.target.name
    const value = e.target.value

    if (name === 'first_name' || name === 'last_name' || name === 'email') {
      setRegisterUser({
        ...registerUser,
        user: {
          ...registerUser.user,
          [name]: value,
        },
        athlete: {
          ...registerUser.athlete,
          [name]: value,
        },
      })
    } else {
      setRegisterUser({
        ...registerUser,
        user: {
          ...registerUser.user,
          [name]: value,
        },
      })
    }
  }
  const handleChangeAthlete = (e) => {
    const name = e.target.name
    const value = e.target.value

    setRegisterUser({
      ...registerUser,
      athlete: {
        ...registerUser.athlete,
        [name]: value,
      },
    })
  }

  const toggleSlide = (e) => {
    e.preventDefault()
    setSlide(!slide)
  }

  return (
    <div className='container'>
      <section className='register-user'>
        <form className={`register-form ${slide && 'slide'}`}>
          <div className='part' id='user'>
            <div className='form-title'>
              <h2>Hesap oluşturun</h2>
            </div>
            <div className='form-control'>
              <label htmlFor='first_name'>Adınız</label>
              <input
                type='text'
                id='first_name'
                name='first_name'
                value={registerUser.user.first_name}
                className='form-input'
                onChange={handleChangeUser}
              />
            </div>
            <div className='form-control'>
              <label htmlFor='last_name'>Soyadınız</label>
              <input
                type='text'
                id='last_name'
                name='last_name'
                className='form-input'
                value={registerUser.user.last_name}
                onChange={handleChangeUser}
              />
            </div>
            <div className='form-control'>
              <label htmlFor='email'>E-mail adresi</label>
              <input
                type='email'
                id='email'
                name='email'
                className='form-input'
                value={registerUser.user.email}
                onChange={handleChangeUser}
              />
            </div>
            <div className='form-control'>
              <label htmlFor='password'>Şifre</label>
              <input
                type='password'
                id='password'
                name='password'
                value={registerUser.user.password}
                className='form-input'
                onChange={handleChangeUser}
              />
            </div>
            <div className='form-control'>
              <label htmlFor='password_rep'>Şifrenizi tekrar ediniz</label>
              <input
                type='password'
                id='password_rep'
                name='password_rep'
                value={registerUser.user.password_rep}
                className='form-input'
                onChange={handleChangeUser}
              />
            </div>
            <div className='btn-container'>
              <button className='btn' onClick={toggleSlide}>
                Sıradaki
              </button>
            </div>
          </div>

          {/* Athlete part form inputs */}

          <div className='part' id='athlete'>
            <div className='form-title'>
              <h2>Sporcu bilgilerinizi giriniz</h2>
            </div>
            <div className='form-control'>
              <label htmlFor='club'>Kulüp</label>
              <select
                name='club'
                id='club'
                value={registerUser.athlete.club}
                onChange={handleChangeAthlete}
                className='form-input'
              >
                {state.clubs.map((club) => {
                  return (
                    <option key={club.id} value={club.short_name}>
                      {club.name}
                    </option>
                  )
                })}
              </select>
            </div>
            <div className='form-control'>
              <label htmlFor='category'>Kategori</label>
              <select
                name='category'
                id='category'
                value={registerUser.athlete.category}
                onChange={handleChangeAthlete}
                className='form-input'
              >
                {state.categories.map((category) => {
                  return (
                    <option key={category.id} value={category.short_name}>
                      {category.short_name}
                    </option>
                  )
                })}
              </select>
            </div>
            <div className='form-control'>
              <label htmlFor='sex'>Cinsiyet</label>
              <input
                type='text'
                id='sex'
                name='sex'
                className='form-input'
                value={registerUser.athlete.sex}
                onChange={handleChangeAthlete}
              />
            </div>
            <div className='form-control'>
              <label htmlFor='si'>SI numarası</label>
              <input
                type='number'
                id='si'
                name='si'
                value={registerUser.athlete.si}
                className='form-input'
                onChange={handleChangeAthlete}
              />
            </div>
            <div className='form-control'>
              <label htmlFor='born'>Doğum Tarihi</label>
              <input
                type='date'
                id='born'
                name='born'
                value={registerUser.athlete.born}
                className='form-input'
                onChange={handleChangeAthlete}
              />
            </div>
            <div className='btn-container'>
              <button className='btn' onClick={toggleSlide}>
                Önceki
              </button>
              <button className='btn'>Kaydol</button>
            </div>
          </div>
        </form>
      </section>
    </div>
  )
}

export default RegisterUser
