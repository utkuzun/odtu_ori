import { FaFacebook, FaInstagram, FaTwitter } from 'react-icons/fa'

const dataNav = [
  {
    page: 'about',
    url: '/about',
    links: [
      { label: 'payment', icon: '', url: '' },
      { label: 'terminal', icon: '', url: '' },
      { label: 'connect', icon: '', url: '' },
    ],
  },
  {
    page: 'register',
    url: '/register',

    links: [
      { label: 'payment', icon: '', url: '' },
      { label: 'terminal', icon: '', url: '' },
      { label: 'connect', icon: '', url: '' },
    ],
  },
  {
    page: 'contacts',
    url: '/contacts',

    links: [
      { label: 'payment', icon: '', url: '' },
      { label: 'terminal', icon: '', url: '' },
      { label: 'connect', icon: '', url: '' },
    ],
  },
]

const links = [
  {
    name: 'facebook',
    url: 'https://www.facebook.com/odtuorienteering',
    icon: <FaFacebook />,
  },
  {
    name: 'instagram',
    url: 'https://www.instagram.com/odtuorienteering',
    icon: <FaInstagram />,
  },
  {
    name: 'twitter',
    url: 'https://www.twitter.com/odtu_o',
    icon: <FaTwitter />,
  },
]

export { dataNav, links }
