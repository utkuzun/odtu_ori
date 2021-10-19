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

const deneme_clubs = [
  {
    city: 'Ankara',
    competitions: [],
    id: 3,
    name: 'METU MONT',
    short_name: 'METU MONT',
  },
  {
    city: 'Ankara',
    competitions: [],
    id: 4,
    name: 'Ankara AOSK',
    short_name: 'AOSK',
  },
  {
    city: 'İstanbul',
    competitions: [],
    id: 5,
    name: 'İstanbul İOG',
    short_name: 'İOG',
  },
  {
    city: 'Ankara',
    competitions: [],
    id: 6,
    name: 'Ferdi',
    short_name: 'Ferdi',
  },
]
const deneme_categories = [
  {
    name: 'Erkek Elit 21 yas',
    competitions: [
      {
        is_active: true,
        city: 'Ankara',
        name: 'METU OPEN',
        date: '2021-10-07T14:29:00',
        id: 2,
      },
    ],
    id: 2,
    short_name: 'E21',
  },
  {
    name: 'Kadın Elit 21 yas',
    competitions: [
      {
        is_active: true,
        city: 'Ankara',
        name: 'METU OPEN',
        date: '2021-10-07T14:29:00',
        id: 2,
      },
    ],
    id: 3,
    short_name: 'K21',
  },
  {
    name: 'Erkek Elit 20 yas',
    competitions: [
      {
        is_active: true,
        city: 'Ankara',
        name: 'METU OPEN',
        date: '2021-10-07T14:29:00',
        id: 2,
      },
    ],
    id: 4,
    short_name: 'E20',
  },
  {
    name: 'Kadın Elit 20 yas',
    competitions: [
      {
        is_active: true,
        city: 'Ankara',
        name: 'METU OPEN',
        date: '2021-10-07T14:29:00',
        id: 2,
      },
    ],
    id: 5,
    short_name: 'K20',
  },
  {
    name: 'Erkek Genç Yeni Başlayan',
    competitions: [],
    id: 6,
    short_name: 'EGYB',
  },
  {
    name: 'Erkek Elit 18 yas',
    competitions: [],
    id: 7,
    short_name: 'E18',
  },
  {
    name: 'Kadın Elit 18 yas',
    competitions: [],
    id: 8,
    short_name: 'K18',
  },
]
export { dataNav, links, deneme_clubs, deneme_categories }
