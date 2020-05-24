import axios from 'axios';

const API_KEY = '9063ae2a574c85c70476669d90a3a4a9';
const API_PATH = 'http://localhost:5000/api';
const API_FILM = 'https://api.themoviedb.org/3';
const MY_GOOD_PLATFORMS_MOCK = [
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
    platform: 'Ivi',
    link: 'https://www.ivi.ru/watch/423591',
    price: '3',
    rating: 3.0,
  },
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
    platform: 'Ivi',
    link: 'https://www.ivi.ru/watch/423591',
    price: '3',
    rating: 3.0
  },
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
    link: 'https://www.ivi.ru/watch/423591',
    platform: 'Ivi',
    price: '3',
    rating: 3.0
  },
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
    link: 'https://www.ivi.ru/watch/423591',
    platform: 'Ivi',
    price: '3',
    rating: 3.0
  },
];
const MY_GOOD_SEARCH_RESULTS_MOCK = [
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
  },
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
  },
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
  },
  {
    title: 'FILM_TITLE',
    description: 'FILM_DESCRIPTION',
  },
];

const actions = {
  clearFilm({commit}: {commit: any}) {
    commit('selectFilm', '')
  },
  selectingFilm({commit}: {commit: any}, filmName: string) {
    commit('selectFilm', filmName);

    axios({
      url: `${API_PATH}/get-serch-results`,
      method: "post",
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      },
      data: {
        film: filmName,
      }
    })
      .then((response) => {
        // commit('setPlatforms', response.data);
        commit('setPlatforms', MY_GOOD_PLATFORMS_MOCK);
      })
      .catch((err) => {
        // console.log('Error when loading cinema-platforms!');
        commit('setPlatforms', MY_GOOD_PLATFORMS_MOCK);
      })
  },

  searchFilm({commit}: {commit: any}, filmName: string) {
    axios.get(`${API_FILM}/search/movie?api_key=${API_KEY}&query=${filmName}`)
      .then((response) => {
        console.log(response.data.results);
        commit('setSearchResults', response.data.results);
        // commit('setSearchResults', MY_GOOD_SEARCH_RESULTS_MOCK);
      })
      .catch((err) => {
        console.log(err);
        // commit('setSearchResults', MY_GOOD_SEARCH_RESULTS_MOCK);
      })
  }
};

export default actions
