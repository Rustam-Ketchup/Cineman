import axios from 'axios';

const API_PATH = 'http://localhost:5000/api';
const MY_GOOD_PLATFORMS_MOCK = [
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
    platform: 'PLATFORM_NAME',
    price: 'FILM_PRICE'
  },
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
    platform: 'PLATFORM_NAME',
    price: 'FILM_PRICE'
  },
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
    platform: 'PLATFORM_NAME',
    price: 'FILM_PRICE'
  },
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
    platform: 'PLATFORM_NAME',
    price: 'FILM_PRICE'
  },
];

const actions = {
  clearFilm({commit}: {commit: any}) {
    commit('selectFilm', '')
  },
  selectingFilm({commit}: {commit: any}, filmName: string) {
    commit('selectFilm', filmName);

    axios.post(`${API_PATH}/get-serch-results`, {
      film: filmName,
    })
      .then((response) => {
        // commit('setPlatforms', response.data);
        commit('setPlatforms', MY_GOOD_PLATFORMS_MOCK);
      })
      .catch((err) => {
        // console.log('Error when loading cinema-platforms!', err);
        commit('setPlatforms', MY_GOOD_PLATFORMS_MOCK);
      })
  }
};

export default actions
